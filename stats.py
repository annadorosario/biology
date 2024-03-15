'''Anna doRosario 
CS152 B
09/24/2021
Lab and Project 03'''

import sys
# Write a function to compute the sum of a list of numbers 

def sum(numbers):
    total_sum = 0.0 
    for i in numbers:
        total_sum += i 

    return total_sum

# Computes the mean of the list of data
def mean(numbers):
    total_sum = sum(numbers)
    avg = total_sum/len(numbers)
   
    return(avg)

# Computes the min of the list of data 
def min(numbers):
    current_min = numbers[0]
    for i in numbers:
        if i < current_min:
            current_min = i
    
    return current_min
            

# Computes the max of the list of data 
def max(numbers):
    current_max = numbers[0]
    for i in numbers:
        if i>current_max:
            current_max = i

    return current_max
# Computes the variance of the list of data 
def variance(numbers):
    numerator_list = []
    for i in numbers:
        numerator = (((mean(numbers))-i)**2)
        numerator_list.append(numerator)
    current_variance = sum(numerator_list)/(len(numbers)-1)
    return current_variance



def test(): 
    first_list = [1, 2, 3, 4]
    sum_result = sum(first_list)
    mean_result = mean(first_list)
    min_result = min(first_list)
    max_result = max(first_list)
    variance_result = variance (first_list)
    print(sum_result)
    print(mean_result)
    print(min_result)
    print(max_result)
    print (variance_result)


if __name__ == "__main__":
    test()
