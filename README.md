# Capstone Project

_ETL pipeline and Streamlit app exploring Dutch domestic rail services for the
year of 2024._

<!--toc:start-->

- [Capstone Project](#capstone-project)
  - [Usage](#usage)
    - [Prerequisites](#prerequisites)
    - [Download and install](#download-and-install)
    - [Running](#running)
  - [Data Sources](#data-sources)
  - [Planning Docs](#planning-docs)
  <!--toc:end-->

## Usage

### Prerequisites

- `python`: minimum `3.6`
  - Checked with [Vermin](https://github.com/netromdk/vermin)
- Sufficient RAM (at least 16GB)

### Download and install

Clone and navigate to directory:

```bash
git clone https://github.com/aiden1999/capstone.git && cd capstone
```

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Switch to the virtual environment:

```bash
source .venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

Install scripts:

```bash
pip install -e .
```

### Running

To run linting and tests:

```bash
run_tests
```

To run the ETL pipeline:

```bash
run_etl
```

To run the Streamlit app:

```bash
run_streamlit
```

To run everything in one command:

```bash
run_all
```

## Data Sources

All datasets sourced from [Rijden de Treinen](https://www.rijdendetreinen.nl/en/open-data).

## Planning Docs

- [Original planning doc](/docs/planning.md)
- [Future plans](/docs/future-plans.md)
