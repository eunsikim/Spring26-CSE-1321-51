def main():
    class_size = 40
    age_sum = 0
    for i in range(class_size):
        age_sum += int(input(f"Enter the age of student {i + 1}: "))
    
    age_avg = age_sum / class_size

    print(f"The average age of this class is {age_avg}")

if __name__ == "__main__":
    main()