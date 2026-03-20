# HF Pulse — AI Tool Adoption Tracking Pipeline

A fully automated data pipeline that tracks how fast AI tools 
are being adopted globally — updated weekly, displayed on a 
live public dashboard.

## Architecture
HuggingFace API → Airflow → PySpark → DuckDB → Tableau Public

## Tech Stack
- **Orchestration:** Apache Airflow 2.8.1
- **Processing:** PySpark 3.5.1
- **Analytics:** DuckDB
- **Visualization:** Tableau Public
- **Infrastructure:** Docker Compose
- **Language:** Python 3.11

## Metrics Tracked
| Metric | Description |
|--------|-------------|
| Weekly Adoption Growth Rate | How fast each AI tool is gaining users |
| Category Leaders | Which AI use case is winning right now |
| Framework Market Share | PyTorch vs TensorFlow vs JAX |
| Geographic Hotspots | Which countries are adopting fastest |
| Rising Stars | Fastest growing tools in last 90 days |
| Stickiness Score | Real adoption vs one-time curiosity |

## How to Run
1. Clone the repo
2. Install Docker Desktop
3. Run `docker compose up airflow-init`
4. Run `docker compose up airflow-webserver airflow-scheduler -d`
5. Open `http://localhost:8080` (admin/admin)

## Dashboard
Tableau Public link coming soon