"""Script to run the Streamlit app."""

import subprocess
import sys


def main():
    """Runs the Streamlit app."""
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "src/streamlit/app.py"], check=True
    )


if __name__ == "__main__":
    main()
