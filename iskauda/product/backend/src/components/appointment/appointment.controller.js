
class appointmentController {
    constructor(service) {
      this.service = service;
    }
  
    createAppointment = async (req, res) => {
      const appointment_body = req.body;
      try {
        const user = await this.service.createAppoint(user_body);
        res.status(200).send(JSON.parse(user));
      } catch (err) {
        res.status(500).send({ message: err.message });
      }
      return res.status(201).send();
    };
  
    getAppointments = async (req, res) => {
      const { id } = req.params;
      try {
          const appointments = await this.service.getAppointments(id);
          res.status(200).send(JSON.parse(appointments));
      } catch (err) {
          res.status(500).send({ message: err.message });
      }
    }
  }
  
  export default appointmentController;