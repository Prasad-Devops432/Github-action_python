from typing import List
from flask import Flask

app = Flask(__name__)


def read_requirements(file_path: str = "requirements.txt") -> List[str]:
    """Read and return a list of package requirements from a file."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]


@app.route("/")
def home():
    return "Hello, this is a CI/CD pipeline demo app!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)