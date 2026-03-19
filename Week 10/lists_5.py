def does_GA_exist(states):
    if "Georgia" in states:
        print("We have Georgia in our list")
    else:
        print("Georgia does not exist")

def main():
    states = ["Georgia", "Florida", "Alabama"]

    does_GA_exist(states)

    print(f"Removing {states[0]}")
    del states[0]

    does_GA_exist(states)

    print(states)

    states.clear()

    print(states)

if __name__ == "__main__":
    main()