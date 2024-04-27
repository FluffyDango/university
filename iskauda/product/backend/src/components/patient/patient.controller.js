
class userController {
  constructor(userService) {
    this.userService = userService;
  }

  createUser = async (req, res) => {
    const user_body = req.body;
    try {
      const user = await this.userService.addUser(user_body);
      res.status(200).send(JSON.parse(user));
    } catch (err) {
      res.status(500).send({ message: err.message });
    }
    return res.status(201).send();
  };

  getUsers = async (_, res) => {
    try {
      const users = await this.userService.getUsers();
      res.status(200).send(JSON.parse(users));
    } catch (err) {
      res.status(500).send({ message: err.message });
    }
  };

  getUser = async (req, res) => {
    const { id } = req.params;
    try {
      const user = await this.userService.getUser(id);
      res.status(200).send(JSON.parse(user));
    } catch (err) {
      res.status(500).send({ message: err.message });
    }
  };

  loginUser = async (req, res) => {
    const { username, password } = req.body;
    try {
      const result = await this.userService.loginUser(username, password);
      res.status(200).send(JSON.parse(result));
    } catch (err) {
      res.status(500).send({ message: err.message });
    }
  };
}

export default userController;