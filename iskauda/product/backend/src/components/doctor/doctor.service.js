import execute from '../../database.js';

class userService {
    addUser = async (user) => {
      const requiredProperties = ['name', 'surname', 'username', 'password', 'level'];
      for (const property of requiredProperties) {
        if (!user.hasOwnProperty(property)) {
          throw new Error(`Missing required property ${property}`);
        }
      }
      const { name, surname, username, password, level } = user;

      const [checkres, _] = await execute(`
          SELECT pat_username, pat_password FROM doctor
          WHERE doc_username = ? AND doc_password = ?;
          `, [username, password]);
      if (checkres.length != 0) return JSON.stringify({ message: 'User already exists' });

      const [results, fields] = await execute(`
          INSERT INTO doctor (doc_name, doc_surname, doc_username, doc_password, level)
          VALUES (?, ?, ?, ?, ?);
          `, [name, surname, username, password, level]);
      if (results.length == 0) return JSON.stringify({ message: 'User not created' });
      return JSON.stringify({ success: true });
    }
  
    getUsers = async () => {
      const [results, fields] = await execute(`
          SELECT doc_name, doc_surname, level FROM doctor;
          `);
      return JSON.stringify(results);
    };
  
    getUser = async (id) => {
      if (!id) throw new Error('Missing required parameter: id');

      const [results, fields] = await execute(`
          SELECT doc_name, doc_surname, level FROM doctor
          WHERE doc_id = ?;
          `, [id]);
      return JSON.stringify(results);
    };

    loginUser = async (username, password) => {
      if (!username) return JSON.stringify({ message: 'Missing required parameter: username' });
      if (!password) return JSON.stringify({ message: 'Missing required parameter: password' });

      const [results, fields] = await execute(`
          SELECT doc_username, doc_password, doc_id FROM doctor
          WHERE doc_username = ? AND doc_password = ?;
          `, [username, password]);
      if (results.length == 0) return JSON.stringify({ message: 'Invalid username or password' });
      return JSON.stringify({ success: true, id: results[0].doc_id });
    };
  }
  
  export default userService;