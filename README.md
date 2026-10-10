# Python CI Pipeline Demo

A small Flask application with unit tests and a GitHub Actions pipeline that
runs those tests on every push and pull request. The project also includes a
Dockerfile so the same app can run in a container.

## What it does

- `app.py` is a Flask app with one route (`/`) and a helper function that reads a
  requirements file.
- `test_app.py` contains pytest tests for the route and the helper.
- `.github/workflows/main.yml` installs the dependencies and runs the tests
  on Ubuntu with Python 3.10 whenever code is pushed to `main` or a pull request is opened.

## Project layout

```
.
├── app.py                  # Flask application
├── test_app.py             # pytest tests
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image (gunicorn server, non-root user)
├── .dockerignore
└── .github/workflows/main.yml   # CI pipeline
```

## Run the tests locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Run the app locally

```bash
python app.py
# then open http://localhost:5000
```

## Run the app in Docker

```bash
docker build -t python-ci-demo .
docker run --rm -p 5000:5000 python-ci-demo
```

## Pipeline

| Step | What happens |
|------|--------------|
| Checkout | Pulls the repository code |
| Set up Python | Installs Python 3.10 and caches pip packages |
| Install dependencies | Installs everything in `requirements.txt` |
| Run tests | Runs `pytest -v` and fails the build if any test fails |

The workflow can also be started manually from the Actions tab (`workflow_dispatch`).

## What I learned

- Writing tests that run automatically in CI.
- Using a Dockerfile that installs dependencies in a separate, cached layer and runs as a non-root user.

## Next steps

- Add a build-and-push job so the container image is published after tests pass.
- Add a linter such as `flake8` as a pipeline step.
