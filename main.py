import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = np.genfromtxt('lung_cancer.csv', delimiter=',', dtype=None, names=True)

# Extract the features and labels
age = data['age']
gender = data['gender']
race = data['race']
smoker = data['smoker']
days_to_cancer = data['days_to_cancer']
stage_of_cancer = data['stage_of_cancer']

#Compute the mean and standard deviation of age
age_mean = np.mean(age)
age_std = np.std(age)


 #Create a histogram to show the distribution of age
plt.hist(age)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')
plt.show()
#np.seterr(invalid='ignore')

# Compute the number of males and females in the data
num_males = np.count_nonzero(gender == b'Male')
num_females = np.count_nonzero(gender == b'Female')

# Create a pie chart to show the gender distribution
labels = ['Male', 'Female']
sizes = [num_males, num_females]

colors = ['lightblue', 'pink']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Gender Distribution')
plt.show()

# Compute the mean and standard deviation of days_to_cancer
days_mean = np.mean(days_to_cancer)
days_std = np.std(days_to_cancer)

# Create a scatter plot to show the relationship between age and days_to_cancer
plt.scatter(age, days_to_cancer)
plt.xlabel('Age')
plt.ylabel('Days to Cancer Diagnosis')#plt.title('Age vs. Days to Cancer Diagnosis')
plt.show()
