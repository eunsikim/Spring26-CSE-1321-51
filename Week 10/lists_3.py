def main():
    states = ["Georgia", "Florida", "Alabama"]
    print(states)

    if "Georgia" in states:
        print("We have Georgia in our list")
    else:
        print("Georgia does not exist")

    # Something happened to florida
    # and now we have N. Florida and S. Florida
    states[1] = "N. Florida"

    print(states)

    states.insert(2, "S. Florida")
    print(states)


if __name__ == "__main__":
    main()