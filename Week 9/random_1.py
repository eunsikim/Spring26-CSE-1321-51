import random

def main():
    # Python uses your system's time as a seed
    # We can define a custom seed using the `seed()` fn.
    random.seed(100)

    for i in range(5):
        # The start and stop arguments are inclusive
        my_random_number = random.randint(5, 10)
        print(my_random_number)

if __name__ == "__main__":
    main()