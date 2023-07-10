"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

from csv_manager import csv_manager
from equi_histogram import equi_histogram
import random

""""
"manual load of the csv file"
csv_manager1 = csv_manager('C:\\Users\Alekos\\Desktop\\Projects2023\\Diaxeirisi\\acs2015_census_tract_data.csv')
mylist = csv_manager1.create_mylist("Income")




"test gia random times"
a = random.randint(0, max(mylist))
b = random.randint(a, 500000)

print("a:", a)
print("b:", b)
"""
csv_file=input("Give the path of the csv file: ")
csv_manager1=csv_manager(csv_file)

mylist_column_name= input("Give the column name of the csv file: ")
mylist = csv_manager1.create_mylist(mylist_column_name)
mylist.sort(reverse=False)

a_str = input("Give the lower threshold for the income: ")
a = int(a_str)

b_str = input("Give the upper threshold for the income (must be higher than {}): ".format(int(a)))
b = int(b_str)

while(a>b):
    print("please follow instructions")
    a_str = input("Give the lower threshold for the income (must be and lower than {}): ".format(max(mylist)))
    a = int(a_str)
    b_str = input("Give the upper threshold for the income (must be higher than {}): ".format(int(a)))
    b = int(b_str)


equi_histogram1 = equi_histogram(100.0,mylist)
equi_width = equi_histogram1.create_width_histogram()
equi_depth = equi_histogram1.create_depth_histogram()
equi_histogram1.print_pleiades(a,b)

"""
"print gia na testarw ta istogrammata mou"
min_val =min(mylist)
max_val =max(mylist)
print(len(mylist),'valid income values')

print('minimum income =', min_val ,' maximum income =' , max_val)

print('equiwidth:')
for bin in equi_width:
    print("range: [{}, {}), numtuples: {}".format(bin[0], bin[1], bin[2]))

print('equidepth:')
for bin in equi_depth:
    print("range: [{}, {}), numtuples: {}".format(bin[0], bin[1], bin[2]))

"""
