# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:49:19 2024

@author: Fpeng_97
"""

# Step 1: initiaize a variable counting 100000 to 999999
num_count = 100000

# Step 2: create a while loop looking for the target number
while (num_count <= 999999):
    num_string = str(num_count)
    if num_string[-1] == num_string[-4] and num_string[-2] == num_string[-3]:
        more_mile_string = str(num_count + 1)
        if more_mile_string[-1] == more_mile_string[-5] and more_mile_string[-2] == more_mile_string[-4]:
            more_mile_string = str(int(more_mile_string) + 1)
            if more_mile_string[-2] == more_mile_string[-5] and more_mile_string[-3] == more_mile_string[-4]:
                more_mile_string = str(int(more_mile_string) + 1)
                if more_mile_string[-1] == more_mile_string[-6] and more_mile_string[-2] == more_mile_string[-5] and more_mile_string[-3] == more_mile_string[-4]:
                    correct_num = num_count 
                    break
    num_count += 1

print("the number is ", correct_num)