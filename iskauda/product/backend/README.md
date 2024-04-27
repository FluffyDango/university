# Overview
Backend for communicating between database and website. It is likely going to run on the database server rather than website server.

Made using ExpressJS

- Router: define the URLs of our backend API and call the corresponding controller functions to handle requests.
- Controller: receives incoming requests from the router and prepares necessary parameters to call the appropriate service functions.
- Service: business logic of our application. This layer is responsible for implementing the functionality required by our API endpoints, and may also handle storage-related operations
- Module: it is called dependency injection. Used to instantiate all the components, including the router, controller, and service.

Communication is done using URI such as `http://localhost:4000/users`

# Setup
## Download all packages
```bash
npm install
```

## Create .env file that has connections to mysql database, Example
```
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=1234
DB_DATABASE=database
```

# Commands



## To run
```bash
npm start
```

## To test
```bash
npm test
```

## Testing when program is on localhost running using curl:
### POST new user
```bash
curl --location 'http://localhost:4000/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "email2@example.com",
    "password": "123456"
}'
```

### GET users
```bash
curl --location 'http://localhost:4000/users'
```

### GET specific user
```bash
curl --location 'http://localhost:4000/users/a0883b24-ff13-4913-b545-0170d654b5d8'
```

### POST login
```bash
curl --location 'http://localhost:4000/patients/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "joda1234",
    "password": "password"
}'
```