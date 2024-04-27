import appointmentController from './appointment.controller.js';
import appointmentService from './appointment.service.js';
import appointmentRouter from './appointment.router.js';

const appointService = new appointmentService();
const appointController = new appointmentController(appointService);
const appointRouter = new appointmentRouter(appointController);

export default {
  service: appointService,
  controller: appointController,
  router: appointRouter.getRouter(),
};