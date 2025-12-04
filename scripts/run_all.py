"""Script to run all the scripts."""

from scripts.run_etl import main as run_etl
from scripts.run_streamlit import main as run_streamlit
from scripts.run_tests import main as run_tests


def main():
    """Runs all the scripts."""
    run_tests()
    run_etl()
    run_streamlit()


if __name__ == "__main__":
    main()
