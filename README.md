# Data Quality Monitoring with AI

## Overview
An AI-powered solution for monitoring data quality in cloud data warehouses with real-time anomaly detection and explainable AI visualizations.

## Setup and Deployment
### 1. Clone Repository
git clone https://github.com/ISEEYOUSTANDINGRIGHTTHERE/data-quality-monitoring-ai.git
### 2. Setup Virtual Environment and Install Dependencies
cd data-quality-monitoring-ai
pip install -r backend/requirements.txt
### 3. Train the Model
python models/train_model.py
### 4. Run backend API
uvicorn backend.app:app --reload
### 5. Launch Dashboard
streamlit run dashboard/dashboard.py
### 6. Deploy with Docker and Kubernetes
docker build -t data-quality-monitoring:latest .
kubectl apply -f deployment/deployment.yaml
kubectl expose deployment data-quality-monitoring --type=LoadB
