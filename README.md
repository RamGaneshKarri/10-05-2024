📊 ScoreSigma
ScoreSigma is a machine learning project designed to predict a student's math score based on various factors such as gender, parental education, test preparation, and reading/writing scores. This project utilizes linear regression on the popular "Student Performance" dataset.

🧠 Objective
To build a predictive model that estimates math scores using student-related attributes, helping educators identify patterns in student performance.

🔍 Dataset
Source: Kaggle — "Students Score in Math Exam"

Format: CSV file with 1000 records

Features used:

Gender

Race/Ethnicity

Parental Level of Education

Lunch

Test Preparation Course

Reading Score

Writing Score

⚙️ Technologies Used
Python

pandas, NumPy

scikit-learn

matplotlib / seaborn (for visualization)

Jupyter Notebook

Google Colab

📈 Model Used
Linear Regression

Evaluation Metrics:

Mean Squared Error (MSE)

R² Score (coefficient of determination)

🔄 Workflow
Import and explore dataset

Preprocess and encode categorical data

Split into training and testing sets

Train using Linear Regression

Evaluate model performance

Visualize prediction results

Predict new student math scores

📌 Sample Prediction
A sample prediction is made using a row from the test set:

python
Copy
Edit
example = X_test.iloc[1:2]
prediction = model.predict(example)
print("Predicted math score:", prediction[0])
📊 Visualization
The project includes:

Bar charts for average scores by gender

Regression plots comparing actual vs predicted scores
