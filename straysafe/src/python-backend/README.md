# Business Logic of StraySafe
This is where the first REST API request will come from the frontend. Here will be AI stuff.


## Development

- Poetry build tool
- Pytest for testing

#### Poetry installation
[UNIX]
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

[WINDOWS]
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Check if installed correctly
```bash
poetry --version
```

Configure poetry to create .venv in project rather than elsewhere
```bash
poetry config virtualenvs.in-project true
```

Install dependencies regular + development
```bash
poetry install
```
To have opencv working you will need to install system-wide dependencies of opencv
```bash
sudo apt install python3-opencv
```
For windows, try
```bash
pip install python-opencv
```

##### VS code highlighting
1. Select a python file.
2. On the bottom right there should be a button for selecting python version.
3. Click and select `Enter interpreter path`
4. Go to `./src/python-backend/.venv/bin/python3.11`

#### Launching project
Launch poetry virtual environment
```bash
poetry shell
```

To launch project, write
```bash
straysafe
```

To launch tests, write
```bash
coverage run -m pytest
```

See how much of the code is tested
```bash
coverage report
```

For production use Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:8000 straysafe.run:app
```

#### Adding new dependencies
```bash
poetry add PACKAGE_NAME
```
To add it to development append `--group dev` at the end
