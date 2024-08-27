Cardiac Prediction using Machine Learning Models
This project aims to predict cardiac health metrics such as BMI, obesity, and cholesterol levels using various machine learning models. The project compares the performance of different models, including Support Vector Machines (SVM), Decision Trees, Linear Regression, and Artificial Neural Networks (ANN).
 Table of Contents
1. Project Overview
2. Dataset
3. Prerequisites
4. Installation
5. Usage
6. Models and Evaluation
7. Results
8. Visualization

1. Project Overview
This project involves:
- Preprocessing a cardiac health dataset.
- Implementing machine learning models to predict cardiac health metrics.
- Evaluating and comparing the accuracy of each model.
- Visualizing the results for better understanding and comparison.

2.Dataset
The dataset used in this project includes various health parameters such as BMI, cholesterol, obesity, blood pressure (BP), physical activity, and age. The data is preprocessed to fill missing values, encode categorical variables, and scale features before training the models.

 3.Prerequisites
Ensure you have the following installed:
- Python 3.x
- Jupyter Notebook or Google Colab
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

4.Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/cardiac-prediction-ml.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cardiac-prediction-ml
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

5.Usage
1. Load the dataset into the project:
   - Replace the dataset path in the script with your local path.
   - Ensure the dataset includes columns: `BP`, `BMI`, `AGE`, `OBESITY`, `PHYSICAL_ACTIVITY`, and `CHOLESTROL`.
2. Run the project script:
   - You can execute the script either in a Jupyter Notebook or in Google Colab.

6. Models and Evaluation
The following models are used for prediction, and their performances are compared:
- **Support Vector Regression (SVR)**
- **Decision Tree Regressor**
- **Linear Regression**
- **Artificial Neural Network (ANN)**
The accuracy of each model is calculated and compared for predicting `BMI`, `obesity`, and `cholesterol` levels.

7. Results
The results include accuracy scores for each model, showing how well they perform in predicting the target variables. Here are some key results:
1. BMI Accuracy:
   - SVM: 99.57%
   - Decision Tree: 99.86%
   - Linear Regression: 100.0%
   - ANN: 99.80%
2. Obesity Accuracy:
   - SVM: 98.98%
   - Decision Tree: 100.0%
   - Linear Regression: 100.0%
   - ANN: 99.20%
3. Cholesterol Accuracy:
   - SVM: 69.37%
   - Decision Tree: 99.87%
   - Linear Regression: 100.0%
   - ANN: 99.81%

8.Visualization
The project includes visualizations that compare the accuracy of different models through bar charts. These visualizations help in understanding which model performs the best for each target variable.

This README provides a comprehensive overview of the "Cardiac Prediction using Machine Learning Models" project, including instructions for setup, usage, and a summary of the results. You can modify it as needed based on the specific requirements of your project.
