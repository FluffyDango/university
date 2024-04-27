import userController from './patient.controller.js';
import userService from './patient.service.js';
import userRouter from './patient.router.js';

const patientService = new userService();
const patientController = new userController(patientService);
const patientRouter = new userRouter(patientController);

export default {
  service: patientService,
  controller: patientController,
  router: patientRouter.getRouter(),
};