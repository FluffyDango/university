import dotenv from 'dotenv';

dotenv.config();

const BACKEND_URL = 'http://' + process.env.NEXT_PUBLIC_DB_IP + ':' + process.env.NEXT_PUBLIC_DB_PORT;

export async function getData(URI: string) {
  try {
    const response = await fetch(BACKEND_URL + URI);

    console.log(response);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Network error:', error);
    return null;
  }
}

export async function postData(URI: string, body: any) {
  try {
    const response = await fetch(BACKEND_URL + URI, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });
    console.log(response);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Network error:', error);
    return null;
  }
}
