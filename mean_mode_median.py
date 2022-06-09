# Enter your code here. Read input from STDIN. Print output to STDOUT

""" Input Format: The first line contains an integer, , the number of elements in the array. The second line contains  space-separated integers that describe the array's elements """

N=int(input())
X=input()
x=X.split(" ")
x = [int(i) for i in x]
x.sort()


def mean_it(a_list):
    sum = 0
    l = len(a_list)
    for i in a_list:
        sum += i
    return sum/l

def median_it(a_list):
    l = len(a_list)
    if l%2 == 0:
        return (a_list[int(l/2)] + a_list[int(l/2)-1])/2
    else:
        return a_list[int(l/2)]
    
def mode_it(a_list): #function to find the mode of a list of integers
    # initialize a frequency table to count occurance of each element
    # here we make use of a list comprehension
    frequency_table = [0 for x in range(max(a_list)+1)]
    
    # record the frequency in the virtual list
    for i in a_list:
        frequency_table[i] += 1
    
    # return the element represented by the highest frequency
    # or the first occurence of that item on the sorted list
    return frequency_table.index(max(frequency_table))
        
    # isolate the most occuring number or it's first occurrence    
    #if frequency_table.count(max(frequency_table)) > 1:
    #    return frequency_table.index(max(frequency_table))
    #else: 
    #    return max(frequency_table).index

print(mean_it(x))
print(median_it(x))
print(mode_it(x))
#print(x)
