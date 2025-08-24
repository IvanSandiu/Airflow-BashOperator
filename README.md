# Airflow-BashOperator - Web Log Processing

## 📌 Overview
This project implements an **ETL pipeline** using **Apache Airflow**.  
The workflow processes a web log file (`accesslog.txt`) through three main stages:

1. **Extract** → Extract IP addresses from the log file.  
2. **Transform** → Filter out specific IPs (e.g., remove requests from `198.46.149.143`).  
3. **Load** → Compress the results into a `.tar` archive for storage or distribution.  

The orchestration of these tasks is defined in an Airflow DAG named `process_web_log`.

---

## ⚙️ DAG Structure
The DAG consists of three sequential tasks:

- **`extract_ip_from_log`**  
  Uses `cut` to extract IP addresses from the `accesslog.txt`.

- **`filter_ip_address`**  
  Applies `grep` to remove unwanted IPs.

- **`load_data`**  
  Compresses the final output into a `.tar` file.

Dependencies:

extract_ip_from_log → filter_ip_address → load_data

## 🔧 Airflow Configuration

The DAG uses the following default configuration (`default_args`):
- **Owner:** `owner`  
- **Notification email:** `owner@gmail.com`  
- **Retries:** 1 retry attempt if a task fails  
- **Retry delay:** 5 minutes  
- **Execution frequency:** Once per day (`timedelta(days=1)`)

## 🚀 How to Run
1. Copy `web_log_dag.py` into Airflow’s DAGs directory.  
2. Ensure the `accesslog.txt` file is available at the specified path.  
3. Start the **Airflow scheduler** and **Airflow webserver**.  
4. Enable the `process_web_log` DAG from the Airflow UI.  
5. Monitor execution from the web interface.  
