# Ryan Yonek
# Income tracking
import csv

class Income_Tracking:
    def __init__(self):
        self.income = 0

    def load_income_data(): 
        with open('income_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = ['daily', 'weekly', 'monthly']
            print(reader.fieldnames)
        for row in reader:
            print(row['daily'], row['weekly', row['monthly']])

    def save_income_data():
        with open('income_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['daily', 'weekly', 'monthly']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'daily': '50', 'weekly': '200','monthly': '3000'})
        writer.writerow({'daily': '40', 'weekly': '350','monthly': '4000'})
        writer.writerow({'daily': '60', 'weekly': '400','monthly': '2000'})
        
        return

