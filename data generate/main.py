from numpy import random
import csv

csv_file_path = 'student.csv'

rows = []
first_row = ['cgpa', 'iq', 'profile_score', 'placed']
rows.append(first_row)


for i in range(299):
    cgpa = random.uniform(1.0, 4.0)
    iq = random.randint(115)
    profile_score = random.randint(100)
    placed = random.randint(2)
    
    one_row = [cgpa, iq, profile_score, placed]
    rows.append(one_row)

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Data generated")



