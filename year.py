"""
AubNet: mak109
ID: 201804131
Name: Mohamad Knio
"""
    
import sys

month=sys.argv[1] # str
days=int(sys.argv[2]) #int


year={'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}
# assume we are not in leap year feb:28 days
for i in year.keys():
    if i not in month:
        days = days + year[i] #add the days of the month and the days 
    else:
        break

print("Day of the year: ", days) 