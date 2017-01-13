#
 # Task:
 # Write a program to find the row with the **maximum** spread
 # in the weather.dat file,
 # where spread is defined as the difference between MxT and MnT.
 # @author John Kiragu Mutua
 # Author email : mutuakiragu@gmail.com
#
import operator
import re
#This function reads data from file
##And returns the data in form of a list
##Skips the day that the header and values
def read_data_from_file(file_to_read):
    list_of_data = []
    try:
        with open(file_to_read) as f:
            next(f)
            next(f)
            for line in f:
                list_of_data.append(line.split())
        return list_of_data
    except IOError:
        raise IOError('The provided input is not a dictionary')

#Cleans  values obtained from file ensuring
#Numerical operations can be perfomed on them minus errors
def clean_mnt_or_mxt_value(value):
    value = re.sub("[^0-9.]", "", value)
    return float(value)

##Takes data read from file and calculaes the spread
##Returns dictionary with day as key and spread as value
def calculate_spreads(data_from_file):
    #Remove last row(containing aggregation data)
    data_from_file.pop()
    spreads = {}
    for row_of_data in data_from_file:
        day = row_of_data[0];
        mxt = clean_mnt_or_mxt_value(row_of_data[1])
        mnt = clean_mnt_or_mxt_value(row_of_data[2])
        spread = mxt - mnt
        spreads[day] = spread
    return spreads

#Gets maximum spread value
def get_max_spread_value(differences_in_mxt_and_mnt):
    maximum_key = max(differences_in_mxt_and_mnt.items(),
                     key=operator.itemgetter(1))[0]
    ##Perform an 0(1) operation to get the value
    maximum_value = differences_in_mxt_and_mnt[maximum_key]
    result = "Day : "+str(maximum_key)+" Spread: "+str(maximum_value)
    return result

##Calculation and spread display
data = read_data_from_file('weather.dat');
spreads = calculate_spreads(data)
print(get_max_spread_value(spreads))
