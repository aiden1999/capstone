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

- `python`
- `uv`
- Sufficient RAM (at least 16GB)

### Download

Clone and navigate to directory:

```bash
git clone https://github.com/aiden1999/capstone.git && cd capstone
```

### Running

To run linting and tests:

```bash
uv run tests
```

To run the ETL pipeline:

```bash
uv run etl
```

To run the Streamlit app:

```bash
uv run streamlit
```

To run everything in one command:

```bash
uv run all
```

## Data Sources

All datasets sourced from [Rijden de Treinen](https://www.rijdendetreinen.nl/en/open-data).
Sample data for testing from [Sample Files](https://www.getsamplefiles.com).

## Planning Docs

- [Original planning doc](/docs/planning.md)
- [Future plans](/docs/future-plans.md)
