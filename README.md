# ml-models-comparison

Comparison of machine learning models to predict loan approval

## Dataset
The dataset relies on 13 inputs and one output: wheter a loan is approved or not

Dataset source : https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data

### Dataset Preparation
In the scripts folder, scripts can be used to 
- first, prepare the dataset: convert data into numerical values (one-hot encoding and standardize input)
- second, split main dataframe into train and test sets

Not needed, but show_raw_dataset infos can be executed to show infos about each columns

## Models Used

Each model is represented in a different jupyter notebook
Models are trained on train set, and evaluated on test set

### K-nearest neighbours

KNN classifies a data point based on the majority label of its closest neighbors in the feature space.

### Neural Network
A collection of interconnected layers of nodes that learn complex, non-linear patterns in data

### Xtreme Gradient Boosting
XGBoost is an optimized ensemble method that builds decision trees sequentially, each correcting the errors of the previous ones