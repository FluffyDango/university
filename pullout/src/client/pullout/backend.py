"""
The SQLite backend implementation.

Database Layout
===============

tables: vcard, addressbook, users

vcard:
    fname (TEXT): formated name
    status (INT): status of this card, see below for meaning
    vcard (TEXT): the actual vcard
    vcard_metadata (TEXT)

addressbook:
    addressbook_name (TEXT): name of the addressbook
"""

OK = 0  # not touched since last sync
NEW = 1  # new card, needs to be created on the server
CHANGED = 2  # properties edited or added (news to be pushed to server)
DELETED = 3  # marked for deletion (needs to be deleted on server)

import sqlite3
import logging
import os
import platform
from .vobj import vCardObject
from typing import List, Dict, Optional

class SQLiteDb():
    def __init__(self, db_path: str=None, overwrite_db: bool=False, should_log: bool=True) -> None:
        if db_path:
            data_home = os.path.join(os.getcwd(), db_path)
        elif platform.system() == 'Windows':
            data_home = os.path.join(os.environ['APPDATA'], 'pullout-client')
        else:
            data_home = os.environ.get('XDG_DATA_HOME') or os.path.join(os.path.expanduser("~"), '.local', 'share', 'pullout-client')
        data_dir = os.path.dirname(data_home)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # LOGGING to stdout info and in file debug info
        self.logger = logging.getLogger()
        if not should_log:
            self.logger.setLevel(logging.CRITICAL)
            self.logger.disabled = True
        else:
            # Print to stdout
            ch = logging.StreamHandler()
            self.logger.setLevel(logging.INFO)
            ch.setLevel(logging.INFO)
            self.logger.addHandler(ch)


        self.db_path = data_home
        # Delete database if overwrite_db is True
        if overwrite_db and os.path.exists(self.db_path):
            os.remove(self.db_path)
        # Connect to the SQLite database (or create it if not exists)
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the SQLite database: {e}")
            return
        # Initialize the tables
        self.create_default_tables()

    def __del__(self):
        if self.conn:
            self.conn.close()

    def create_default_tables(self) -> None:
        """Creates table on init if they don't exist yet."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS addressbook (
                addressbook_id INTEGER PRIMARY KEY AUTOINCREMENT,
                addressbook_name TEXT NOT NULL,
                is_active INT DEFAULT 0,
                ctag INT DEFAULT 0,
                UNIQUE(addressbook_name)
                check(is_active IN (0, 1))
            )
        """)
        self.conn.commit()
        self.cursor.execute("""
            INSERT OR IGNORE INTO addressbook (addressbook_name, is_active)
            VALUES (?, ?)
        """, ("default", 1))
        self.conn.commit()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vcard (
                vcard_id INTEGER PRIMARY KEY AUTOINCREMENT,
                vcard_hash INTEGER NOT NULL,
                fn TEXT NOT NULL,
                org TEXT,
                title TEXT,
                adr TEXT,
                tel TEXT,
                email TEXT,
                url TEXT,
                addressbook_id_prop INT NOT NULL,
                FOREIGN KEY (addressbook_id_prop) REFERENCES addressbook(addressbook_id)
            )
        """)
        self.conn.commit()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vcard_metadata (
                href TEXT NOT NULL PRIMARY KEY,
                vcard_id INTEGER NOT NULL,
                etag TEXT NOT NULL,
                status INT NOT NULL,
                FOREIGN KEY (vcard_id) REFERENCES vcard(vcard_id),
                CHECK(status IN (0, 1, 2, 3))
            )
        """)
        self.conn.commit()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL,
                server_url TEXT NOT NULL,
                is_active INT DEFAULT 0,
                UNIQUE(username),
                CHECK(is_active IN (0, 1))
            )
        """)
        self.conn.commit()
        self.cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS delete_addressbook
            AFTER DELETE ON addressbook
            FOR EACH ROW
            BEGIN
                DELETE FROM vcard
                WHERE addressbook_id_prop = OLD.addressbook_id;
            END;
        """)
        self.conn.commit()

    # -------------------------
    # VCARD
    def add_vcard(self, vcard_obj: vCardObject, addressbook_name: str=None) -> None:
        """Adds a new vcard."""
        try:
            # Get the addressbook id
            if addressbook_name:
                addressbook_id = self.get_addressbook_id(addressbook_name)
            else:
                addressbook_id = self.get_active_addressbook()[0]

            vcard_hash = hash(vcard_obj)
            vcard_dict = vcard_obj.get_vcard_dict()
            if self.find_vcard(vcard_hash, addressbook_name):
                raise ValueError(f"Contact already exists.")
            # Add the vcard
            self.cursor.execute("""
                INSERT INTO vcard (vcard_hash, fn, org, title, adr, tel, email, url, addressbook_id_prop)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                vcard_hash,
                vcard_dict.get('FN'),
                vcard_dict.get('ORG'),
                vcard_dict.get('TITLE'),
                vcard_dict.get('ADR'),
                vcard_dict.get('TEL'),
                vcard_dict.get('EMAIL'),
                vcard_dict.get('URL'),
                addressbook_id
            ))
            self.conn.commit()
        except ValueError as e:
            self.logger.info(f"Failed to add vcard: {str(e)}")

    def delete_vcard(self, vcard_id: int) -> None:
        """Deletes the specified vcard."""
        try:
            self.cursor.execute("""
                DELETE FROM vcard
                WHERE vcard_id = ?
            """, (vcard_id,))
            self.conn.commit()
            self.logger.debug(f"BACKEND: deleted vcard with id: {vcard_id}")
            self.logger.info(f"Deleted vcard with id: {vcard_id}")
        except ValueError as e:
            self.logger.info(f"Failed to delete vcard: {str(e)}")

    def modify_vcard(self, vcard_id: int, new_vcard_dict: dict) -> None:
        """
        Modifies the specified vcard.
                Parameters:
                        vcard_id (int): The serial id of the vcard to modify
                        vcard_dict (dict): vcard with properties FN, ORG, TITLE, ADR, TEL, EMAIL, URL
        """
        self.delete_vcard(vcard_id)
        self.add_vcard(vCardObject(vcard_dict=new_vcard_dict))

    def get_vcard(self, vcard_id: int) -> dict:
        """
        Returns:
                vcard (dict): The vcard
                    id (int): The id of the vcard
                    fn (str): The formatted name
                    org (str): The organization
                    title (str): The title
                    adr (str): The address
                    tel (str): The telephone number
                    email (str): The email
                    url (str): The url
        """
        self.cursor.execute("""
            SELECT vcard_id, fn, org, title, adr, tel, email, url from vcard
            WHERE vcard_id = ?
        """, (vcard_id,))
        result = self.cursor.fetchone()
        self.logger.debug(f"BACKEND: got vcard with id: {vcard_id}")
        keys = ["VCARD_ID", "FN", "ORG", "TITLE", "ADR", "TEL", "EMAIL", "URL"]
        vcard = dict(zip(keys, result))
        return vcard

    def get_addressbook_vcards(self, addressbook_name: str) -> List[Dict]:
        """
        Returns:
                vcards (dict): A list of all vcard
                    vcard_id (int)
                    addressbook_name (str)
                    fn (str)
                    org (str)
                    title (str)
                    adr (str)
                    tel (str)
                    email (str)
                    url (str)
        """
        if addressbook_name:
            current_addressbook_id = self.get_addressbook_id(addressbook_name)
        else:
            current_addressbook_id = self.get_active_addressbook()[0]
        
        if not current_addressbook_id:
            self.logger.info("Could not find addressbook")
            return None
        self.cursor.execute("""
            SELECT vcard_id, addressbook_name, fn, org, title, adr, tel, email, url from vcard, addressbook
            WHERE addressbook_id_prop = ? AND addressbook_id = addressbook_id_prop
        """, (current_addressbook_id,))
        result = self.cursor.fetchall()
        self.logger.debug(f"BACKEND: got vcard with current addressbook: {result}")
        keys = ["VCARD_ID", "ADDRESSBOOK_NAME", "FN", "ORG", "TITLE", "ADR", "TEL", "EMAIL", "URL"]
        vcard = [dict(zip(keys, row)) for row in result]
        return vcard
    
    def get_all_vcards(self) -> dict:
        """
        Returns:
                vcard (dict): A list of all vcard
                    vcard_id (int): The id of the vcard
                    fn (str): The formatted name
                    org (str): The organization
                    title (str): The title
                    adr (str): The address
                    tel (str): The telephone number
                    email (str): The email
                    url (str): The url
        """
        self.cursor.execute("""
            SELECT vcard_id, addressbook_name, fn, org, title, adr, tel, email, url from vcard, addressbook
            WHERE addressbook_id = addressbook_id_prop
        """)
        result = self.cursor.fetchall()
        self.logger.debug(f"BACKEND: got all vcard: {result}")
        keys = ["VCARD_ID", "ADDRESSBOOK_NAME", "FN", "ORG", "TITLE", "ADR", "TEL", "EMAIL", "URL"]
        vcard = [dict(zip(keys, row)) for row in result]
        return vcard
    
    def find_vcard(self, vcard_id: int, addressbook_name: str=None) -> bool:
        """Returns True if vcard exists, False otherwise."""
        if addressbook_name:
            addressbook_id = self.get_addressbook_id(addressbook_name)
        else:
            addressbook_id = self.get_active_addressbook()[0]
        self.cursor.execute("""
            SELECT vcard_hash FROM vcard WHERE vcard_hash = ? AND addressbook_id_prop = ?
        """, (vcard_id, addressbook_id))
        result = self.cursor.fetchone()
        self.logger.debug(f"find_vcard called. Result: {result}")
        return True if result else False
    
    def get_vcard_status(self, vcard_id: int) -> int:
        """Returns the status of the specified vcard."""
        self.cursor.execute("""
            SELECT status FROM vcard_metadata WHERE vcard_id = ?
        """, (vcard_id,))
        result = self.cursor.fetchone()
        self.logger.debug(f"get_vcard_status called. Result: {result}")
        return result[0] if result else None


    # -------------------------
    # addressbook
    def create_addressbook(self, addressbook_name: str, ctag: Optional[int] = None) -> None:
        """Creates a new addressbook if it doesn't exist yet and specify that it is in use."""
        try:
            # Check if addressbook already exists
            if self.get_addressbook_id(addressbook_name):
                raise ValueError(f"addressbook '{addressbook_name}' already exists.")
            self.cursor.execute("""
                INSERT INTO addressbook (addressbook_name, is_active)
                VALUES (?, ?)
            """, (addressbook_name, 0))
            self.conn.commit()
            self.logger.info(f"Created addressbook '{addressbook_name}'")
            if ctag:
                self.update_addressbook_ctag(addressbook_name, ctag)
        except ValueError as e:
            self.logger.info(f"Failed to create addressbook: {str(e)}")

    def update_addressbook_ctag(self, addressbook_name: str, ctag: int) -> None:
        """Adds a ctag to the specified addressbook."""
        try:
            # Check if addressbook exists
            addressbook_id = self.get_addressbook_id(addressbook_name)
            if not addressbook_id:
                raise ValueError(f"addressbook '{addressbook_name}' does not exist.")
            # Add the ctag
            self.cursor.execute("""
                UPDATE addressbook SET
                ctag = ?
                WHERE addressbook_id = ?
            """, (ctag, addressbook_id))
            self.conn.commit()
            self.logger.debug(f"add_ctag_to_addressbook called")
            # self.logger.info(f"Added ctag to addressbook '{addressbook_name}'")
        except ValueError as e:
            self.logger.info(f"Failed to add ctag to addressbook: {str(e)}")

    def get_all_ctags(self) -> List[int]:
        """Returns the ctag of the specified addressbook."""
        self.cursor.execute("""
            SELECT ctag FROM addressbook
        """)
        result = self.cursor.fetchall()
        self.logger.debug(f"get_ctag_from_addressbook called. Result: {result}")
        if result:
            return [row[0] for row in result]
        else:
            return None

    def delete_addressbook(self, addressbook_name: str) -> None:
        """Deletes the specified addressbook."""
        try:
            # Check if addressbook exists
            addressbook_id = self.get_addressbook_id(addressbook_name)
            if not addressbook_id:
                raise ValueError(f"addressbook '{addressbook_name}' does not exist.")
            # default addressbook cannot be deleted
            if self.get_addressbooks().__len__() == 1:
                raise ValueError("At least one addressbook should exist.")
            elif self.get_active_addressbook()[1] == addressbook_name:
                raise ValueError(f"addressbook '{addressbook_name}' is currently in use.")
            # Delete the addressbook
            self.cursor.execute("""
                DELETE FROM addressbook WHERE addressbook_id = ?
            """, (addressbook_id,))
            self.conn.commit()
            self.logger.debug(f"delete_addressbook called")
            self.logger.info(f"Deleted addressbook '{addressbook_name}'")
        except ValueError as e:
            self.logger.info(f"Failed to delete addressbook: {str(e)}")

    def get_addressbooks(self) -> List[Dict]:
        """
        Returns:
                addressbooks (list): A list of all addressbook
                    addressbook_name (str)
                    ctag (int)
        """
        self.cursor.execute("""
            SELECT addressbook_name, ctag FROM addressbook
        """)
        result = self.cursor.fetchall()
        self.logger.debug(f"get_addressbook called. Result: {result}")
        keys = ["addressbook_name", "ctag"]
        addressbook = [dict(zip(keys, row)) for row in result]
        return addressbook

    def get_addressbook_id(self, addressbook_name: str) -> int:
        """Returns the serial id of specified addressbook name."""
        self.cursor.execute("""
            SELECT addressbook_id FROM addressbook WHERE addressbook_name = ?
        """, (addressbook_name,))
        result = self.cursor.fetchone()
        self.logger.debug(f"get_addressbook_id called. Result: {result}")
        return result[0] if result else None

    def change_addressbook(self, addressbook_name: str) -> None:
        """Changes the addressbook that is currently in use."""
        try:
            # Check if addressbook exists
            addressbook_id = self.get_addressbook_id(addressbook_name)
            if not addressbook_id:
                print(f"addressbook '{addressbook_name}' does not exist.")
                return
            current_addressbook_id = self.get_active_addressbook()[0]
            if addressbook_id == current_addressbook_id:
                print(f"addressbook '{addressbook_name}' is already in use.")
                return
            # Change the addressbook
            self.cursor.execute("""
                UPDATE addressbook SET
                is_active = ?
                WHERE addressbook_id = ?
            """, (0, current_addressbook_id))
            self.cursor.execute("""
                UPDATE addressbook SET 
                is_active = ?
                WHERE addressbook_id = ?
            """, (1, addressbook_id))
            self.conn.commit()
            self.logger.debug(f"change_addressbook called. Result: {self.cursor.fetchone()}")
            print(f"Changed addressbook to '{addressbook_name}'")
        except ValueError as e:
            self.logger.info(f"Failed to change addressbook: {str(e)}")

    def get_active_addressbook(self) -> list:
        """
        Returns:
                array with 2 elements:
                    addressbook_id (int): The id of the addressbook
                    addressbook_name (str): The name of the addressbook
        """
        self.cursor.execute("""
            SELECT addressbook_id, addressbook_name FROM addressbook
            WHERE is_active = 1
        """)
        result = self.cursor.fetchone()
        self.logger.debug(f"get_addressbook_in_use called. Result: {result}")
        return result if result else None
                
    # --
    # QUERY
    def query(self, search_options: dict, addressbook_name: str) -> dict:
        """
        Returns list of vcard, it searches with LIKE %name%

                Parameters:
                        search_options

                Returns:
                        queries (array of dicts): A list of vcard
                            VCARD_ID (int): The id of the vcard
                            addressbook_NAME (str): The name of the addressbook
                            FN (str): The formatted name
                            ORG (str): The organization
                            TITLE (str): The title
                            ADR (str): The address
                            TEL (str): The telephone number
                            EMAIL (str): The email
                            URL (str): The website
        """
        try:
            if addressbook_name:
                addressbook_id = self.get_addressbook_id(addressbook_name)
            else:
                addressbook_id = self.get_active_addressbook()[0]
            parameters = [addressbook_id]
            sql = """
                SELECT vcard_id, addressbook_name, fn, org, title, adr, tel, email, url from vcard, addressbook
                WHERE addressbook_id = ? AND addressbook_id_prop = addressbook_id
            """
            # Append search options to sql query
            for key, value in search_options.items():
                if value:
                    sql += f" AND {key} LIKE ?"
                    parameters.append(f"%{value}%")
            # if addressbook_name is specified, append it to sql query
            
            if addressbook_name:
                
                if addressbook_id:
                    sql += f" AND addressbook_id = ?"
                    parameters.append(addressbook_id)
                else:
                    ValueError(f"addressbook '{addressbook_name}' does not exist.")

            self.cursor.execute(sql, parameters)
            result = self.cursor.fetchall()
            self.logger.debug(f"BACKEND: query called. Result: {result}")
            keys = ["VCARD_ID", "ADDRESSBOOK_NAME", "FN", "ORG", "TITLE", "ADR", "TEL", "EMAIL", "URL"]
             # Map each row to a dictionary
            result_dicts = [dict(zip(keys, row)) for row in result]
            return result_dicts
        except ValueError as e:
            self.logger.info(f"Failed to query data: {str(e)}")

    # -------------------------
    # Users

    def create_user(self, server_url: str) -> None:
        """Create a user that is used in the CardDav server"""
        if self.get_user():
            self.delete_user()
            
        self.cursor.execute("""
            INSERT INTO users (username, password, server_url, is_active)
            VALUES (?, ?, ?, ?)
        """, ("all", "all", server_url, 1))
        self.conn.commit()
        self.logger.info(f"Created user for server '{server_url}'")

    def delete_user(self) -> None:
        """Delete a user that is used in the CardDav server"""
        server_url = self.get_user()['server_url']
        self.cursor.execute("""
            DELETE FROM users
            WHERE server_url = ?
        """, (server_url,))
        self.conn.commit()
        self.logger.info(f"Deleted user for server '{server_url}'")


    def get_user(self) -> Dict[str, str]:
        """
        Returns:
                (dict):
                    username (str)
                    password (str)
                    server_url (str)
        """
        self.cursor.execute("""
            SELECT username, password, server_url from users
            WHERE is_active = 1
        """)
        result = self.cursor.fetchone()
        self.logger.debug(f"get_user called. Result: {result}")
        if result:
            return {'username': result[0], 'password': result[1], 'server_url': result[2]}
        else:
            return None
        