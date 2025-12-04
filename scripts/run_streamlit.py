"""Script to run the Streamlit app."""

import subprocess


def main():
    """Runs the Streamlit app."""
    subprocess.run(["streamlit", "run", "src/streamlit/app.py"])


if __name__ == "__main__":
    main()
