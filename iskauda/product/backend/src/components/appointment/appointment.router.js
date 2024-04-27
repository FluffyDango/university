import express from 'express';

class AppointmentRouter {
  constructor(controller) {
    this.controller = controller;
  }

  getRouter() {
    const router = express.Router();
    router.route('/:id').get(this.controller.getAppointments);
    router.route('/').post(this.controller.createAppointment);
    return router;
  }
}

export default AppointmentRouter;