# HF Pulse — AI Tool Adoption Tracking Pipeline

An automated data pipeline that tracks which AI tools are winning 
the market — updated weekly, displayed on a live public dashboard.

## The Problem
Companies are making million-dollar AI tooling decisions based on 
hype, not data. HF Pulse delivers a data-driven, automated view of 
real AI tool adoption across 500,000+ models — refreshed every week.

## Architecture
HuggingFace API
↓
Python Ingestion (Airflow DAG)
↓
Bronze Layer — Raw Parquet (DBFS)
↓
PySpark on Databricks — Silver + Gold Delta Tables
↓
Databricks SQL — Metrics Layer
↓
Tableau Public — Live Dashboard

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.11 | API ingestion and pipeline logic |
| Apache Airflow 2.8.1 | Orchestration, scheduling, retry logic |
| PySpark 3.5.1 | Large scale data transformations |
| Databricks | Spark compute and SQL analytics |
| Delta Lake | ACID compliant table format |
| Databricks SQL | Analytical metrics queries |
| Tableau Public | Live dashboard visualization |
| Docker Compose | Airflow containerization |
| GitHub | Version control |

## Medallion Architecture
| Layer | Format | Description |
|-------|--------|-------------|
| Bronze | Parquet | Raw data exactly as received from HuggingFace API |
| Silver | Delta | Cleaned, deduplicated, enriched data |
| Gold | Delta | Aggregated metrics ready for visualization |

## Metrics Tracked
| Metric | Business Question |
|--------|------------------|
| Weekly Adoption Growth Rate | Which AI tools are gaining users fastest? |
| Category Leaders | Is NLP, computer vision or audio winning? |
| Framework Market Share | PyTorch vs TensorFlow vs JAX |
| Geographic Hotspots | Which countries are adopting AI tools fastest? |
| Rising Stars | What exploded in the last 90 days? |
| Stickiness Score | Real adoption vs one-time curiosity? |

## How to Run
1. Clone the repo
```bash
   git clone https://github.com/hodl21/hf-pulse.git
   cd hf-pulse
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Start Airflow
```bash
   docker compose up airflow-init
   docker compose up airflow-webserver airflow-scheduler -d
```
4. Open Airflow UI at `http://localhost:8080` (admin/admin)
5. Trigger the `hf_pulse_pipeline` DAG

## Project Structure
hf-pulse/
├── dags/               # Airflow DAG definitions
├── ingestion/          # HuggingFace API ingestion scripts
├── transforms/         # PySpark transformation scripts
├── analytics/          # Databricks SQL metric queries
├── data/
│   ├── bronze/         # Raw Parquet files
│   ├── silver/         # Cleaned Delta tables
│   └── gold/           # Aggregated metrics
├── docker-compose.yml  # Airflow Docker setup
├── requirements.txt    # Python dependencies
└── README.md

## Dashboard
🔗 Tableau Public link — *coming soon*

## Author
Sandeep Dumpala — [GitHub](https://github.com/hodl21)