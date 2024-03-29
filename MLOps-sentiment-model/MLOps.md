In this article we will see the benefits of Machine learning operations and how we can utilize it using various MLOps tools like MLflow and Prefect with our sentiment analysis app

***Why MLOps***:
MLOps provides reproducibility of ML pipelines, enabling more tightly-coupled collaboration across data teams, reducing conflict with devops and IT, and accelerating release velocity.

Check out this cool <a href="https://ml-ops.org/content/mlops-principles">Article</a> to understand more about Machine Learning operations.

****

### Iterative ML life cycle 
<img src="data:image/png;base64,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" alt='ML workflow'>

****

### Iterative-incremental ML operations
<img src="https://ml-ops.org/img/mlops-loop-en.jpg">

****

### ML model decay monitoring
<img src="https://ml-ops.org/img/model-decay-monitoring.jpg">

****

**The Three Main components that we will be Using for making a production ready workflow are:**

1. **Pipeline**
2. **Mlflow**
3. **Prefect**


Let's see in detail how these 3 can work together for our problem statement and how we can utilize them for modularity, reproducibility, management, deployment, maintainence and scheduling of our model.

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
