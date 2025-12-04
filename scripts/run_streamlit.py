import subprocess


def main():
    subprocess.run(["streamlit", "run", "src/streamlit/app.py"])


if __name__ == "__main__":
    main()
