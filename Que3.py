""""Biggest and smallest number in an array
 Write a program to print the biggest and smallest number in the array."""""

'function'
def find_max_min(numbers):
    if not numbers:
        return None, None
    max_num = min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

'array1 = [1,2,3,4,5]'
array2=[5, 3, 7, 4, 2]
max_value, min_value = find_max_min(array2)

if max_value is not None and min_value is not None:
    print(f"The largest number in the array is: {max_value}")
    print(f"The smallest number in the array is: {min_value}")
else:
    print("The array is empty.")
