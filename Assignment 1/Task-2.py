# Python program to print positive Numbers in given range
  
start, end = -5, 34
  
# iterating each number in list
for num in range(start, end + 1):
  
    # checking condition
    if num >= 0:
        print(num, end=" ")