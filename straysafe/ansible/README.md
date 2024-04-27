# ANSIBLE SETUP

Make sure you have at least 3GB disk for using the normal setup and 5GB or more for building locally without artifacts

To launch initial setup, launch `ansible_vm_setup.sh`. It will show ip and port on which the frontend lives.
```bash
./ansible_vm_setup.sh
```
There is website setup with no gitlab artifacts, meaning it will build everything and use from local host.

### Modifying existing VM's
Database can be modified by connecting to the database and doing queries. Some useful commands:
```sql
DROP DATABASE straysafe;
CREATE DATABASE straysafe;

-- Rename
ALTER DATABASE straysafe RENAME TO straysafe_old;

-- DROP ALL TABLES
DO $$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;
```

To input all sql files from directory:
```bash
for file in ./sql_scripts/*.sql
do
  psql -d straysafe -U straysafe -h public_ip -p port -f "$file"
done
```

For updating everything else make sure you have at least 5GB!
```bash
git pull origin your-branch
ansible-playbook website-setup-no-gitlab.yaml -i hosts --ask-vault-pass
```
This will build everything locally and send it to the server.
It will take a while, especially if you did not give a lot of cpu power.