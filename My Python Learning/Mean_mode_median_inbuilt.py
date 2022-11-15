# A program to demonstrate the use of some statistics functions
import statistics
# Initialise a list of values
values = [2,3,5,2,4]
# Compute the 3 averages
arithmetic_mean = statistics.mean(values)
median_value = statistics.median(values)
modal_value = statistics.mode(values)
# Display the answers
print("The mean is ", arithmetic_mean)
print("The median and mode are %d and %d" %(median_value, modal_value))
