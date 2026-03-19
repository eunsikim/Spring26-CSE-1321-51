import random

def main():
    random.seed(100)

    for i in range(10):
        # The arguments works exactly the same
        # as the `range()` function
        # [start, stop) and a step optional argument
        my_random_number = random.randrange(5, 10, 2)
        print(my_random_number)

if __name__ == "__main__":
    main()