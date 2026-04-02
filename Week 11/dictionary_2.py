def main():
    states = {
        "Georgia":"Atlanta", 
        "Florida":"Tallahassee", 
        "Alabama":"Montgomery"
        }
    
    # This FOR loop just prints
    # the KEY values
    for item in states:
        print(item)
    
    for item in states.values():
        print(item)

    for item in states.items():
        print(item)
    
    for item in states.items():
        print(f"State: {item[0]}, Capital: {item[1]}")


if __name__ == "__main__":
    main()