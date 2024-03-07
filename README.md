# Chicken-Disease-Classification-DeeLearning-and-MLOps
The Chicken Disease Classification Project utilizes an end-to-end deep learning approach with MLOps practices for efficient model development, training, and deployment. The primary goal is to accurately classify chicken fecal images into two classes: Coccidiosis and Healthy.

## Workflows

1. Update Config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Updat ethe Configuration Manager in src config
6. Update the Component
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## Project Modular coding files Structure and meaning
### 1. Configuration Files:

* config.yaml: This file stores the main configuration parameters for the project, such as image size, training parameters, and paths to other resources. Updating this file adjusts the overall project settings.
* secrets.yaml (Optional): This file (if used) stores sensitive information like API keys or passwords that shouldn't be directly included in the code. Updating this file manages those credentials.
* params.yaml: This file likely defines additional hyperparameters used during the training process. Updating it allows for fine-tuning the model's learning.

### 2. Project Structure Updates:

* Update the entity: This step might involve modifying a specific entity within the project framework used for managing data or models. The nature of this update depends on the chosen framework.
* Update the Configuration Manager in src/config: This refers to updating code responsible for handling the configuration files (likely config.yaml and potentially others) within the project's source code directory (src/config).
* Update the Component: This could involve modifying a specific component within the project's codebase. The component's function depends on the project structure, but it likely relates to a specific processing step in the pipeline.
* Update the pipeline: This involves modifying code responsible for orchestrating the entire data processing and model training workflow. The pipeline likely defines the sequence of steps and their dependencies.
  
### 3. Code Updates:

* Update main.py: This is likely the main script that triggers the entire pipeline execution. Updating it might involve changing how the pipeline is called or what configurations are used.

* Update dvc.yaml: This file defines the project's DVC (Data Version Control) configuration. DVC is used for managing data dependencies and reproducibility. Here's a breakdown of the stages defined in this specific dvc.yaml file:

* data_ingestion: This stage defines a command using python src/cnnClassifier/pipeline/stage_01_data_ingestion.py to ingest the chicken fecal image data. Dependencies and outputs for this stage are also specified.
* prepare_base_model: This stage defines a command using python src/cnnClassifier/pipeline/stage_02_prepare_base_model.py to prepare a pre-trained model as the foundation for the disease classification task. Configuration parameters from config.yaml and specific hyperparameters are passed during this stage.
* training: This stage defines a command using python src/cnnClassifier/pipeline/stage_03_training.py to train the model on the prepared data. Dependencies include the data ingestion output, the prepared base model, and configuration files. Additional training hyperparameters are also passed.
* evaluation: This stage defines a command using python src/cnnClassifier/pipeline/stage_04_evaluation.py to evaluate the performance of the trained model on the data. Dependencies include the data ingestion output, the trained model, and configuration files. Additionally, evaluation metrics are specified to be stored in a "scores.json" file, with caching disabled.
