import mysql from 'mysql2/promise';
import config from './config.js';

export default async function execute(sql, params) {
  const connection = await mysql.createConnection(config);
  const [results, fields] = await connection.execute(sql, params);
  await connection.end();

  return [results, fields];
}
