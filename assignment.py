# You can remove 'pass' if you written code in the function
# Exercise 1

def find_insert_position(data, target):

    low = 0

    high = len(data) - 1
    while low < high:
        mid = (low + high) // 2
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid
    if data[len(data)-1]<target:
        low+=1
    return data[low-1]

# Exercise 2
def integer_sqrt(n):
    # Write your code here
    pass

