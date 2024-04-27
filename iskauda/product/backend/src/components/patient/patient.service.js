import execute from '../../database.js';

class userService {
    getUsers = async () => {
      const [results, fields] = await execute(`
          SELECT pat_id, pat_name, pat_surname FROM patient;
          `);
      return JSON.stringify(results);
    };
  
    getUser = async (id) => {
      if (!id) return JSON.stringify({ message: 'Missing required parameter: id' });

      const [results, fields] = await execute(`
          SELECT pat_id, pat_name, pat_surname FROM patient
          WHERE pat_id = ?;
          `, [id]);
      if (results.length == 0) return JSON.stringify({ message: 'Could not find user with id: ' + id });
      return JSON.stringify(results);
    };

    loginUser = async (username, password) => {
      if (!username) return JSON.stringify({ message: 'Missing required parameter: username' });
      if (!password) return JSON.stringify({ message: 'Missing required parameter: password' });

      const [results, fields] = await execute(`
          SELECT pat_username, pat_password, pat_id FROM patient
          WHERE pat_username = ? AND pat_password = ?;
          `, [username, password]);
      if (results.length == 0) return JSON.stringify({ message: 'Invalid username or password' });
      return JSON.stringify({ success: true, id: results[0].pat_id });
    };

    addUser = async (user) => {
      const requiredProperties = ['name', 'surname', 'username', 'password'];
      for (const property of requiredProperties) {
        if (!user.hasOwnProperty(property)) {
          throw new Error(`Missing required property ${property}`);
        }
      }
      const { name, surname, username, password } = user;

      const [checkres, _] = await execute(`
          SELECT pat_username, pat_password FROM patient
          WHERE pat_username = ? AND pat_password = ?;
          `, [username, password]);
      if (checkres.length != 0) return JSON.stringify({ message: 'User already exists' });

      const [results, fields] = await execute(`
          INSERT INTO patient (pat_name, pat_surname, pat_username, pat_password)
          VALUES (?, ?, ?, ?);
          `, [name, surname, username, password]);
      if (results.length == 0) return JSON.stringify({ message: 'User not created' });
      return JSON.stringify({ success: true });
    }
  }
  
  export default userService;