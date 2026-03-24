# Create a function where you take a single list of float numbers
# ranging from [0, 100] as parameter and then figure out the 
# smalles element in the list and then return that value.
#
# Example:
#   [4, 3, 10, 1], the function should return 1
def lowest(nums):
    lowest_number = nums[0]

    for number in nums:
        if number < lowest_number:
            lowest_number = number
    
    return lowest_number

# Create a function that takes in a list of floats ranging 
# from [0, 100] containing just 2 numbers and a second parameter
# which is going to be another float.
#
# The function finds out the lowest value in the list, if the lowest
# value is less than the second parameter, replace the lowest value
# in the list with the second parameter.
#
# The function returns the list.
#
# Example:
#   ([80, 60], 100) the function returs => [100, 80]
def replace(nums, third_number):
    lowest_number_index = 0

    if nums[lowest_number_index] > nums[1]:
        lowest_number_index = 1
    
    if nums[lowest_number_index] < third_number:
        nums[lowest_number_index] = third_number
    
    return nums


def main():
    quizzes = [80, 70, 90, 100, 60, 76, 81, 100, 80, 85]
    tests = [70, 80]
    final_exam = 95
    print(lowest(quizzes))
    print(replace(tests, final_exam))

    # Assuming Quizzes are 25%, and each test also 25%, and the final exam 25%
    # Calculate the final grade for the student.
    # Hint: You can use the len() function to figure out the number of items in a sequence
    # Example: print(len(quizzes)) => prints `10`

if __name__ == "__main__":
    main()