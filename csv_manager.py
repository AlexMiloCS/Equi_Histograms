"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

import csv

class csv_manager:    
    def __init__(self, csv_path):
        self.csv_path= csv_path

    def create_mylist(self,column_name):
        income_list = []
        with open(self.csv_path) as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            column_index = headers.index(column_name)
            for row in reader:
                column_value = row[column_index]
                if(column_value != ""):
                    income_list.append(float(column_value))    
        return income_list
    
    