# app.py

def read_requirements(file_path: str = "requirements.txt") -> list[str]:
    """Read requirements.txt and return a list of lines."""
    try:
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"{file_path} not found")
        return []


def main():
    requirements = read_requirements()
    if not requirements:
        print("No requirements found.")
    else:
        print("Requirements in this project:")
        for req in requirements:
            print(f"- {req}")


if __name__ == "__main__":
    main()