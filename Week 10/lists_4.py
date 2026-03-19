def does_GA_exist(states):
    if "Georgia" in states:
        print("We have Georgia in our list")
    else:
        print("Georgia does not exist")

def main():
    states = ["Georgia", "Florida", "Alabama"]

    does_GA_exist(states)

    print(f"Removing {states.pop(0)}")

    does_GA_exist(states)

    print(states[0])
    print(states[1])


if __name__ == "__main__":
    main()