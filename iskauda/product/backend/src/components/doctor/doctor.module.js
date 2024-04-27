import userController from './doctor.controller.js';
import userService from './doctor.service.js';
import userRouter from './doctor.router.js';

const patientService = new userService();
const patientController = new userController(patientService);
const patientRouter = new userRouter(patientController);

export default {
  service: patientService,
  controller: patientController,
  router: patientRouter.getRouter(),
};