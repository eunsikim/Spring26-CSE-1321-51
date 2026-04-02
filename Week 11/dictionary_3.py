def exists(item, dictionary):
    if item in dictionary:
        print(f"{item} exists")
    else:
        print(f"{item} does not exist")

def main():
    states = {
        "Georgia":"Atlanta", 
        "Florida":"Tallahassee", 
        "Alabama":"Montgomery"
        }
    
    # We access the keys whenever we 
    # search a dictionary
    exists("Atlanta", states)
    exists("Alabama", states)

    # We access the valus in a dictionary
    # if we access the dictionary.values()
    exists("Atlanta", states.values())
    exists("Alabama", states.values())

    exists(("Georgia", "Atlanta"), states.items())
    exists(("Georgia", "Kennesaw"), states.items())


if __name__ == "__main__":
    main()