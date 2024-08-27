# -*- coding: utf-8 -*-
"""Minor Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MdhefMBdwOMt2tX_5Q9T4lVC1F__PiU7

#** BEFORE PREPROCESSING**
"""

#IMPORTING LIBRARIES
from sklearn import svm
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("/content/medical_dataset.xlsx")

##CHOLESTROL
le = LabelEncoder()
data["OBESITY"] = le.fit_transform(data["OBESITY"])
data["PHYSICAL_ACTIVITY"] = le.fit_transform(data["PHYSICAL_ACTIVITY"])

# Feature Scaling
scaler = StandardScaler()
X = data.drop(["BP","BMI","AGE","OBESITY","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)
y = data["CHOLESTROL"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# SVM
svm_model = svm.SVR()  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
svm_accuracy1 = svm_model.score(X_test, y_test)

# Decision Tree
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_accuracy1 = dt_model.score(X_test, y_test)

#LINEAR REGRESSION
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_accuracy1 = lr_model.score(X_test, y_test)

# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
ann_model.fit(X_train, y_train)
ann_accuracy1 = ann_model.score(X_test, y_test)
# Compare accuracies
print("Cholestrol Accuracy:")
print("SVM Accuracy:", svm_accuracy1 * 100)
print("Decision Tree Accuracy:", dt_accuracy1 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy1*100)
print("ANN Accuracy:", ann_accuracy1 * 100)
print("\n")
#Cholestrol Model Graph

models = ["SVM", "Decision Tree", "LINEAR REGRESSION", "ANN"]
accuracies = [svm_accuracy1*100,dt_accuracy1*100, lr_accuracy1*100,ann_accuracy1*100]

plt.figure(figsize=(8, 5))
bar_width = 0.6
bars = plt.bar(models, accuracies, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparison Targeting Cholesterol')
plt.ylim(0, 110)  # Set the y-axis range to match accuracy values
# Add accuracy values on top of bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

##OBESITY


# Feature Scaling
scaler = StandardScaler()
X = data.drop(["BP","BMI","AGE","CHOLESTROL","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)

# Split Data
y = data["OBESITY"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


# Train and Evaluate Models
# SVM
svm_model = svm.SVR()  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
svm_accuracy2 = svm_model.score(X_test, y_test)


# Decision Tree
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_accuracy2 = dt_model.score(X_test, y_test)


#LINEAR REGRESSION
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_accuracy2 = lr_model.score(X_test, y_test)


# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
ann_model.fit(X_train, y_train)
ann_accuracy2 = ann_model.score(X_test, y_test)

# Compare accuracies
print("obesity Accuracy:")
print("SVM Accuracy:", svm_accuracy2 * 100)
print("Decision Tree Accuracy:", dt_accuracy2 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy2*100)
print("ANN Accuracy:", ann_accuracy2 * 100)
print("\n")

#CHOLESTROL MODEL GRAPH

models = ["SVM", "Decision Tree", "LINEAR REGRESSION", "ANN"]
accuracies = [svm_accuracy2*100,dt_accuracy2*100,lr_accuracy2*100,ann_accuracy2*100]

plt.figure(figsize=(8, 5))
bar_width = 0.6
bars = plt.bar(models, accuracies, color=['blue', 'green', 'orange', 'red'])

plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparison Targeting Obesity')
plt.ylim(0, 110)  # Set the y-axis range to match accuracy values

# Add accuracy values on top of bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

##BMI
le = LabelEncoder()
data["OBESITY"] = le.fit_transform(data["OBESITY"])
data["PHYSICAL_ACTIVITY"] = le.fit_transform(data["PHYSICAL_ACTIVITY"])

# Feature Scaling
scaler = StandardScaler()
X = data.drop(["BP","CHOLESTROL","AGE","OBESITY","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)

# Split Data
y = data["BMI"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


# Train and Evaluate Models
# SVM
svm_model = svm.SVR()  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
svm_accuracy1 = svm_model.score(X_test, y_test)


# Decision Tree
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_accuracy1 = dt_model.score(X_test, y_test)


#LINEAR REGRESSION
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_accuracy1 = lr_model.score(X_test, y_test)


# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
ann_model.fit(X_train, y_train)
ann_accuracy1 = ann_model.score(X_test, y_test)

# Compare accuracies
print("BMI Accuracy:")
print("SVM Accuracy:", svm_accuracy1 * 100)
print("Decision Tree Accuracy:", dt_accuracy1 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy1*100)
print("ANN Accuracy:", ann_accuracy1 * 100)
print("\n")

#BMI MODEL GRAPH
models = ["SVM", "Decision Tree", "LINEAR REGRESSION", "ANN"]
accuracies = [svm_accuracy1*100,dt_accuracy1*100,lr_accuracy1*100,ann_accuracy1*100]

plt.figure(figsize=(8, 5))
bar_width = 0.6
bars = plt.bar(models, accuracies, color=['blue', 'green', 'orange', 'red'])

plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparison Targeting BMI')
plt.ylim(0, 110)  # Set the y-axis range to match accuracy values

# Add accuracy values on top of bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

"""1  **Cholestrol Accuracy**:
*   SVM Accuracy: 69.3668887070704
*   Decision Tree Accuracy: 99.8728127649734
*   LINEAR REGRESSION ACCURACY: 100.0
*   ANN Accuracy: 99.81036167470063

2   **OBESITY ACCURACY:**
*   SVM Accuracy: 98.97650375914573
*   Decision Tree Accuracy: 100.0
*   LINEAR REGRESSION ACCURACY: 100.0
*   ANN Accuracy: 99.1961687621517

3  **BMI ACCURACY:**
*   SVM Accuracy: 99.57049686434667
*   Decision Tree Accuracy: 99.86249939692718
*   LINEAR REGRESSION ACCURACY: 100.0
*   ANN Accuracy: 99.7954479325297

#PREPROCESSING THE DATA
"""

#PRE PROCESSING
data1=pd.read_excel("/content/medical_dataset.xlsx")
df1 = pd.DataFrame(data1)

df1['PHYSICAL_ACTIVITY'] = df1['PHYSICAL_ACTIVITY'].astype(str)
df1['OBESITY'] = df1['OBESITY'].astype(str)
# Encode categorical variables using LabelEncoder
label_encoder = LabelEncoder()
df1['OBESITY'] = label_encoder.fit_transform(df1['OBESITY'])
df1['PHYSICAL_ACTIVITY'] = label_encoder.fit_transform(df1['PHYSICAL_ACTIVITY'])

# Fill missing values with 0
df1.fillna(0, inplace=True)

# Display the preprocessed DataFrame
print(df1)

#FINDING THE CORELATION BETWEEN ALL THE PARAMETERS WITH AGE
# Calculate correlation matrix
correlation_matrix = df1.corr()

# Get correlation of 'AGE' with other parameters
correlation_with_age = correlation_matrix['AGE']

# Print correlation results
print(correlation_with_age)

#correlation data
correlation_data = {
    'BMI': 0.464740,
    'OBESITY': 0.440392,
    'PHYSICAL_ACTIVITY': -0.194424,
    'CHOLESTROL': 0.218171,
    'BP': 0.063532
}
# Create a DataFrame from the correlation data
correlation_df = pd.DataFrame.from_dict(correlation_data, orient='index', columns=['Correlation'])
# Create a scatter plot with all data points
plt.figure(figsize=(10, 6))
plt.scatter(correlation_df.index, correlation_df['Correlation'], color='blue', marker='o', s=100)
plt.title('Scatter Plot of Parameters Correlation with AGE')
plt.xlabel('Parameters')
plt.ylabel('Correlation with AGE')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

"""# **AFTER PREPROCESSING**"""

#1  BMI
le = LabelEncoder()
data1["OBESITY"] = le.fit_transform(data1["OBESITY"])
data1["PHYSICAL_ACTIVITY"] = le.fit_transform(data1["PHYSICAL_ACTIVITY"])

# Feature Scaling
scaler = StandardScaler()
X = data1.drop(["BP","CHOLESTROL","AGE","OBESITY","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)

# Split Data
y = data1["BMI"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

## Train and Evaluate Models


# SVM
svm_model = svm.SVR()
X_train=X_train.astype(float)  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
X_test=X_test.astype(float)
svm_accuracy_1 = svm_model.score(X_test, y_test)

# Decision Tree
dt_model = DecisionTreeRegressor()
X_train=X_train.astype(float)
X_test=X_test.astype(float)
dt_model.fit(X_train, y_train)
dt_accuracy_1 = dt_model.score(X_test, y_test)

#LINEAR REGRESSION
lr_model = LinearRegression()
X_train=X_train.astype(float)
lr_model.fit(X_train, y_train)
X_test=X_test.astype(float)
lr_accuracy_1 = lr_model.score(X_test, y_test)


# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
X_train=X_train.astype(float)
ann_model.fit(X_train, y_train)
X_test=X_test.astype(float)
ann_accuracy_1 = ann_model.score(X_test, y_test)


# Compare accuracies
print("BMI Accuracy Comparison:")
print("SVM Accuracy:", svm_accuracy_1 * 100)
print("Decision Tree Accuracy:", dt_accuracy_1 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy_1*100)
print("ANN Accuracy:", ann_accuracy_1 * 100)
print("\n")


#BMI MODEL GRAPH
models = ["SVM", "Decision Tree","LINEAR REGRESSION" ,"ANN"]
accuracies = [svm_accuracy_1*100, dt_accuracy_1*100,lr_accuracy_1*100,ann_accuracy_1*100]


plt.figure(figsize=(8, 5))
bar_width=0.6
plt.bar(models, accuracies, color=['blue', 'green', 'orange','purple'],width=bar_width)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparision Targeting BMI')
plt.ylim(0,110)  # Set the y-axis range to match accuracy values


for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

#2 OBESITY
le = LabelEncoder()
data1["OBESITY"] = le.fit_transform(data1["OBESITY"])
data1["PHYSICAL_ACTIVITY"] = le.fit_transform(data1["PHYSICAL_ACTIVITY"])

# Feature Scaling
scaler = StandardScaler()
X = data1.drop(["BMI","CHOLESTROL","AGE","BP","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)

# Split Data
y = data1["OBESITY"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train and Evaluate Models
# SVM
svm_model = svm.SVR()  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
svm_accuracy2 = svm_model.score(X_test, y_test)


# Decision Tree
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_accuracy2 = dt_model.score(X_test, y_test)


#LINEAR REGRESSION
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_accuracy2 = lr_model.score(X_test, y_test)


# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
ann_model.fit(X_train, y_train)
ann_accuracy2 = ann_model.score(X_test, y_test)


# Compare accuracies
print("OBESITY Accuracy Comparison:")
print("SVM Accuracy:", svm_accuracy2 * 100)
print("Decision Tree Accuracy:", dt_accuracy2 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy2*100)
print("ANN Accuracy:", ann_accuracy2 * 100)
print("\n")


# OBESITY MODEL GRAPH
models = ["SVM", "Decision Tree", "LINEAR REGRESSION", "ANN"]
accuracies = [svm_accuracy2 * 100, dt_accuracy2 * 100, lr_accuracy2 * 100, ann_accuracy2 * 100]

plt.figure(figsize=(8, 5))
bar_width = 0.6
bars = plt.bar(models, accuracies, color=['blue', 'green', 'purple', 'orange'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparison Targeting OBESITY')
plt.ylim(0, 115)  # Set the y-axis range to match accuracy values

# Add accuracy values on top of bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

#3 CHOLESTROL
le = LabelEncoder()
data1["OBESITY"] = le.fit_transform(data1["OBESITY"])
data1["PHYSICAL_ACTIVITY"] = le.fit_transform(data1["PHYSICAL_ACTIVITY"])

# Feature Scaling
scaler = StandardScaler()
X = data1.drop(["BP","BMI","AGE","OBESITY","PHYSICAL_ACTIVITY" ], axis=1)
X_scaled = scaler.fit_transform(X)

# Split Data
y = data1["CHOLESTROL"]
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train and Evaluate Models
# SVM
svm_model = svm.SVR()  # Use Support Vector Regression for regression tasks
svm_model.fit(X_train, y_train)
svm_accuracy1 = svm_model.score(X_test, y_test)

# Decision Tree
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)
dt_accuracy1 = dt_model.score(X_test, y_test)


#LINEAR REGRESSION
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_accuracy1 = lr_model.score(X_test, y_test)


# Artificial Neural Network (ANN) model
ann_model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=10000, random_state=42)
ann_model.fit(X_train, y_train)
ann_accuracy1 = ann_model.score(X_test, y_test)


# Compare accuracies
print("CHOLESTROL Accuracy Comparison:")
print("SVM Accuracy:", svm_accuracy1 * 100)
print("Decision Tree Accuracy:", dt_accuracy1 * 100)
print("LINEAR REGRESSION ACCURACY:",lr_accuracy1*100)
print("ANN Accuracy:", ann_accuracy1 * 100)
print("\n")

#CHOLESTROL MODEL GRAPH
models = ["SVM", "Decision Tree", "LINEAR REGRESSION", "ANN"]
accuracies = [svm_accuracy1*100, dt_accuracy1*100, lr_accuracy1*100, ann_accuracy1*100]

plt.figure(figsize=(8, 5))
bar_width = 0.6
bars = plt.bar(models, accuracies, color=['blue', 'green', 'orange', 'purple'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Comparison Targeting CHOLESTROL')
plt.ylim(0, 110)  # Set the y-axis range to match accuracy values

# Add accuracy values on top of bars
for bar, accuracy in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, f'{accuracy:.2f}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

"""**BMI Accuracy Comparison:**
* SVM Accuracy: 83.39943686941257
* Decision Tree Accuracy: 99.99346589833706
* LINEAR REGRESSION ACCURACY: 100.0
* ANN Accuracy: 99.99641245958716

**OBESITY Accuracy Comparison:**
* SVM Accuracy: 99.29469767113102
* Decision Tree Accuracy: 100.0
* LINEAR REGRESSION ACCURACY: 100.0
* ANN Accuracy: 98.82795813071431

**CHOLESTROL Accuracy Comparison:**
* SVM Accuracy: 6.10586915523773
* Decision Tree Accuracy: 99.9155395798023
* LINEAR REGRESSION ACCURACY: 100.0
* ANN Accuracy: 99.999664135684

# COMPARISION
"""

# CHOLESTROL  COMPARISION

methods = ['SVM', 'Decision Tree', 'Linear Regression', 'ANN']
original_accuracies = [69.3668887070704, 99.8728127649734, 100.0, 99.81036167470063]
comparison_accuracies = [6.10586915523773,99.9155395798023,100.0,99.999664135684]
bar_width = 0.4
bar_positions = list(range(len(methods)))
comparison_bar_positions = [pos + bar_width for pos in bar_positions]

plt.figure(figsize=(10, 6))

plt.bar(bar_positions, original_accuracies, width=bar_width, label='BEFORE PREPROCESSING')
plt.bar(comparison_bar_positions, comparison_accuracies, width=bar_width, label='AFTER PREPROCESSING')

plt.xlabel('Methods')
plt.ylabel('Accuracy')
plt.title('Cholesterol Accuracy Comparison')
plt.xticks([pos + bar_width/2 for pos in bar_positions], methods)
plt.legend()

# Adding value labels on top of the bars
for i, value in enumerate(original_accuracies):
    plt.text(bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

for i, value in enumerate(comparison_accuracies):
    plt.text(comparison_bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

methods = ['SVM', 'Decision Tree', 'Linear Regression', 'ANN']
obesity_accuracies = [98.97650375914573, 100.0, 100.0, 99.1961687621517]
obesity_comparison_accuracies = [99.29469767113102, 100.0, 100.0, 98.82795813071431]

bar_width = 0.4
bar_positions = list(range(len(methods)))
comparison_bar_positions = [pos + bar_width for pos in bar_positions]

plt.figure(figsize=(10, 6))

plt.bar(bar_positions, obesity_accuracies, width=bar_width)
plt.bar(comparison_bar_positions, obesity_comparison_accuracies, width=bar_width)

plt.xlabel('Methods')
plt.ylabel('Accuracy')
plt.title('Obesity Accuracy Comparison')
plt.xticks([pos + bar_width/2 for pos in bar_positions], methods)


# Adding value labels on top of the bars
for i, value in enumerate(obesity_accuracies):
    plt.text(bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

for i, value in enumerate(obesity_comparison_accuracies):
    plt.text(comparison_bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

methods = ['SVM', 'Decision Tree', 'Linear Regression', 'ANN']
bmi_accuracies = [99.57049686434667, 99.86249939692718, 100.0, 99.7954479325297]
bmi_comparison_accuracies = [83.39943686941257, 99.99346589833706, 100.0, 99.99641245958716]

bar_width = 0.4
bar_positions = list(range(len(methods)))
comparison_bar_positions = [pos + bar_width for pos in bar_positions]

plt.figure(figsize=(10, 6))

plt.bar(bar_positions, bmi_accuracies, width=bar_width)
plt.bar(comparison_bar_positions, bmi_comparison_accuracies, width=bar_width)

plt.xlabel('Methods')
plt.ylabel('Accuracy')
plt.title('BMI Accuracy Comparison')
plt.xticks([pos + bar_width/2 for pos in bar_positions], methods)

# Adding value labels on top of the bars
for i, value in enumerate(bmi_accuracies):
    plt.text(bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

for i, value in enumerate(bmi_comparison_accuracies):
    plt.text(comparison_bar_positions[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()

# Adjust the space for the x-axis labels
plt.subplots_adjust(bottom=0.15)

plt.show()

"""# **ACCURACY ANALYSIS**

"""

# COMPARISION OF ACCURACIES OF AFTER AND BEFORE PREPROCESSING DATA

# Model names
models = ['SVM', 'Decision Tree', 'LR', 'ANN']

# Accuracy values for each dataset - Before Processing
cholesterol_accuracy_before = [69.3668887070704, 99.8728127649734, 100.0, 99.81036167470063]
obesity_accuracy_before = [98.97650375914573, 100.0, 100.0, 99.1961687621517]
bmi_accuracy_before = [99.57049686434667, 99.86249939692718, 100.0, 99.7954479325297]

# Accuracy values for each dataset - After Preprocessing
cholesterol_accuracy_after = [6.10586915523773, 99.9155395798023, 100.0, 99.999664135684]
obesity_accuracy_after = [99.29469767113102, 100.0, 100.0, 98.82795813071431]
bmi_accuracy_after = [83.39943686941257, 99.99346589833706, 100.0, 99.99641245958716]

# Calculate average accuracy for each model - Before Processing
average_accuracy_before = [(cholesterol_accuracy_before[i] + obesity_accuracy_before[i] + bmi_accuracy_before[i]) / 3 for i in range(len(models))]

# Calculate average accuracy for each model - After Preprocessing
average_accuracy_after = [(cholesterol_accuracy_after[i] + obesity_accuracy_after[i] + bmi_accuracy_after[i]) / 3 for i in range(len(models))]

# Create pie charts
plt.figure(figsize=(12, 5))

# Before Processing
plt.subplot(1, 2, 1)
plt.pie(average_accuracy_before, labels=models, autopct='%1.2f%%', startangle=140)
plt.title('Before Processing Average Model Accuracy')

# After Preprocessing
plt.subplot(1, 2, 2)
plt.pie(average_accuracy_after, labels=models, autopct='%1.2f%%', startangle=140)
plt.title('After Preprocessing Average Model Accuracy')

plt.tight_layout()

plt.show()

# Model names
models = ['SVM', 'Decision Tree', 'LR', 'ANN']

# Accuracy values for each dataset - Before Processing
cholesterol_accuracy_before = [69.3668887070704, 99.8728127649734, 100.0,99.81036167470063]
obesity_accuracy_before = [ 98.97650375914573, 100.0, 100.0, 99.1961687621517 ]
bmi_accuracy_before = [99.57049686434667, 99.86249939692718, 100.0,99.7954479325297]

# Accuracy values for each dataset - After Preprocessing
cholesterol_accuracy_after = [6.10586915523773,99.9155395798023, 100.0,99.99974245219737]
obesity_accuracy_after = [99.29469767113102, 100.0, 100.0, 98.82795813071431]
bmi_accuracy_after = [83.39943686941257, 99.99346589833706, 100.0, 99.99641245958716]

# Calculate average accuracy for each model - Before Processing
average_accuracy_before = [(cholesterol_accuracy_before[i] + obesity_accuracy_before[i] + bmi_accuracy_before[i]) / 3 for i in range(len(models))]

# Calculate average accuracy for each model - After Preprocessing
average_accuracy_after = [(cholesterol_accuracy_after[i] + obesity_accuracy_after[i] + bmi_accuracy_after[i]) / 3 for i in range(len(models))]

accuracy_difference = [after - before for before, after in zip(average_accuracy_before, average_accuracy_after)]

# Print the accuracy difference for each model
for i in range(len(models)):
    print(f"{models[i]}: {accuracy_difference[i]:.3f}")