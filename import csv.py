import csv
import matplotlib.pyplot as plt


file_path = '/content/drive/MyDrive/Student Attitude and Behavior.csv'


willingness_good = []
willingness_bad = []


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:

        willing_percent = float(row[13].rstrip('%'))
        stress_level = row[16]

        if stress_level.lower() == "good":
            willingness_good.append(willing_percent)
        elif stress_level.lower() == "bad":
            willingness_bad.append(willing_percent)

plt.hist(willingness_good, bins=10, color='green', alpha=0.5, label='Good Stress Level')
plt.hist(willingness_bad, bins=10, color='red', alpha=0.5, label='Bad Stress Level')

plt.xlabel('Willingness Percent')
plt.ylabel('Frequency')
plt.title('Histogram of Willingness Percent by Stress Level')
plt.legend()

plt.show()