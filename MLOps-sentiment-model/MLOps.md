# MLOps integration with our app
*Why MLOps*
MLOps provides reproducibility of ML pipelines, enabling more tightly-coupled collaboration across data teams, reducing conflict with devops and IT, and accelerating release velocity.

****
**The Three Main components that we will be Using for making a production ready workflow are:**

1. **Pipeline**
2. **Mlflow**
3. **Prefect**


Let's see in detail how these 3 can work together for our problem statement and how we can utilize them for modularity, reproducibility, management, deployment and maintainence of our model.

**1. Pipeline:** A sequence of data transformers with an optional final predictor. Pipeline allows you to sequentially apply a list of transformers to preprocess the data and, if desired, conclude the sequence with a final predictor for predictive modeling. i.e. the stages in which an data is moved through the various segments of the ML model building processes.

**2. MLflow:** MLflow is an open source MLOps tool that can help with the machine learning lifecycle, including training, tuning, and deploying models. some of its advantages are:

* Streamlined Experiment Tracking and Reproducibility.
* Enhanced Collaboration and Knowledge Sharing.
* Improved Model Packaging and Deployment.
* Efficient Model Lifecycle Management. 

**3. Prefect:** It is is an orchestration tool designed for managing, scheduling, running, and monitoring tasks within a workflow.we utilized it to streamline the process of sentiment analysis model building and Autoscheduling Model training in future for updated dataset.

****
### MLflow Experiment Runs
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/mlflow-experiment-view.png?raw=true">

****
### MLflow Metric-plot 1
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/mlflow-metricplot-1.png?raw=true">

****
### MLflow Metric-plot 2
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/mlflow-metricplot-2.png?raw=true">

****
### MLflow Model Registry
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/mlflow-model-registry.png?raw=true">

****
### Prefect Dashboard
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/prefect-dashboard.png?raw=true">

****
### Prefect Flow Runs view
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/prefect-flow-run.png?raw=true">

****
### Prefect Flows
<img src="https://github.com/ishaq88/flipkart-product-reviews-sentiment-analysis/blob/main/MLOps-sentiment-model/misc-pngs/prefect-flows.png?raw=true">

****
