import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Read the dataset


df = pd.read_csv(r"C:/Users/hp/PycharmProjects/Chatbot/dataset.csv", names=['English', 'Sesotho', 'Business studies', 'Agriculture', 'Physical Science', 'Accounting', 'Biology', 'Design and Technology', 'Religious Knowledge', 'ICT', 'Development Studies', 'French', 'Mathematics', 'Geography', 'Intergrated Home Economics', 'Fashion and Textile', 'Literature', 'History', 'Tourism', 'Role'])

# Map grades to their corresponding values
grade_map = {'A*': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 2, 'U': 1, 'X': 0}

# Get input from the user
print('Please enter your results for each subject:')
user_input = {}
for i in range(1, 20):
    subject_name = input(f'Subject {i}: ')
    if subject_name:
        grade = input('Grade: ')
        user_input[subject_name] = grade

# Create a list of grades based on the user input
user_grades = []
for subject in df.columns[:-1]:
    if subject in user_input:
        user_grades.append(grade_map[user_input[subject]])
    else:
        user_grades.append(0)  # Set the grade to 0 if the subject is not in user input

# Fit a KNN model with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(df.iloc[:, :-1], df.iloc[:, -1])

# Predict the course based on the user grades
prediction = knn.predict([user_grades])[0]

# Print the recommended course
print(f'Based on your results, we recommend the {prediction} course.')
