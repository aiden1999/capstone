import subprocess

from scripts.run_etl import main as run_etl


def main():
    run_etl()
    subprocess.run(["streamlit", "run", "src/streamlit/app.py"])


if __name__ == "__main__":
    main()
