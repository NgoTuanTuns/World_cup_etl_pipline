FROM apache/airflow:3.2.2
COPY datashets /datashets
COPY requirements.txt .
RUN pip install -r requirements.txt