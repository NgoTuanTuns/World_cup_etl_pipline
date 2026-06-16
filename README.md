# World Cup ELT Pipeline

An end-to-end ELT (Extract, Load, Transform) data pipeline that processes FIFA World Cup datasets using **Pandas**, loads them into **PostgreSQL**, and orchestrates the workflow with **Apache Airflow** — all running inside **Docker**.

## Overview

This project extracts World Cup data from CSV files, transforms it using Pandas, and loads it into a PostgreSQL database. Apache Airflow manages the scheduling and orchestration of the pipeline, and the entire stack runs in Docker containers for consistent, reproducible execution.

## Architecture

```
CSV Files → Extract (Pandas) → Transform (Pandas) → Load (PostgreSQL)
                                        ↑
                              Orchestrated by Airflow
                                        ↑
                              Running on Docker
```

## Data Sources

The pipeline processes the following CSV files:

| File | Description |
|------|-------------|
| `wc_2026_fixture.csv` | Match fixtures/schedule for the 2026 World Cup |
| `wc_2026_teams.csv` | Teams participating in the 2026 World Cup |
| `wc_all_editions.csv` | Historical data on all World Cup editions/tournaments |
| `wc_all_matches.csv` | Historical match results across all World Cups |
| `wc_top_scorers.csv` | Top scorers data across World Cup history |

## Tech Stack

- **Apache Airflow** – Workflow orchestration and scheduling
- **Pandas** – Data extraction and transformation
- **PostgreSQL** – Data warehouse / storage layer
- **Docker / Docker Compose** – Containerized environment for all services
- **Python** – Core pipeline logic

## Project Structure

```
.
├── dags/
│   └── WC_dag.py    # Airflow DAG definition
├── datashets/
│   ├── wc_2026_fixture.csv
│   ├── wc_2026_teams.csv
│   ├── wc_all_editions.csv
│   ├── wc_all_matches.csv
│   └── wc_top_scorers.csv
├── include/
│   └── scripts/                     # Extract/transform/load helper scripts
├── Dockerfile
├── docker-compose.ymal
├── requirements.txt
└── README.md
```

## Pipeline Flow

1. **Extract** – Read each CSV file into a Pandas DataFrame.
2. **Transform** – Clean and reshape data (handle missing values, normalize column names/types, join/derive fields as needed).
3. **Load** – Write the transformed DataFrames into corresponding PostgreSQL tables.
4. **Orchestrate** – Airflow DAG defines task dependencies and schedules the pipeline runs.

## Prerequisites

- Docker Desktop installed and running
- Docker Compose
- (Optional) Astro CLI, if using the Astronomer Airflow setup

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd world-cup-elt-pipeline
```

### 2. Start the environment

Using Docker Compose:

```bash
docker-compose up -d
```

Or, if using Astro CLI:

```bash
astro dev start
```

### 3. Access Airflow UI

Open your browser at:

```
http://localhost:8080
```

Default credentials (if not changed): `admin` / `admin`

### 4. Trigger the DAG

Enable and trigger the `world_cup_pipeline_dag` from the Airflow UI, or via CLI:

```bash
airflow dags trigger world_cup_pipeline_dag
```

### 5. Verify data in PostgreSQL

Connect to the Postgres container:

```bash
docker exec -it <postgres-container-name> psql -U <user> -d <database>
```

Then check the loaded tables:

```sql
\dt
SELECT * FROM wc_top_scorers LIMIT 10;
```

## Environment Variables

Configure the following in your `.env` file (or Airflow connections):

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
```

## Database Schema (Tables)

| Table | Source File |
|-------|-------------|
| `wc_2026_fixture` | wc_2026_fixture.csv |
| `wc_2026_teams` | wc_2026_teams.csv |
| `wc_all_editions` | wc_all_editions.csv |
| `wc_all_matches` | wc_all_matches.csv |
| `wc_top_scorers` | wc_top_scorers.csv |

## Notes

- All file paths referenced in the Airflow tasks are relative to the container's working directory, not the host machine.
- Make sure the Postgres connection is registered in Airflow (`Admin > Connections`) before running the DAG.
- Use `conn.commit()` (or a context manager) when writing with `psycopg2` directly, since unlike `PostgresHook.run()`, manual cursor execution does not auto-commit.

## License

MIT
