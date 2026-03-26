def main():
    students = [["John", 80.5], ["Abigail", 90], ["Dave", 70], ["Daniel", 50]]
    
    for sublist in students:
        for data in sublist:
            print(data, end=" ")
        
        print()

if __name__ == "__main__":
    main()