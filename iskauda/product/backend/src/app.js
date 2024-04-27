import express from 'express';
import loadRoutes from './loaders/routes.js';
import errorMiddleware from './middlewares/error.js';
import cors from 'cors';

const app = express();

app.use(cors());
app.use(express.json());
loadRoutes(app);
app.use(errorMiddleware);

export default app;