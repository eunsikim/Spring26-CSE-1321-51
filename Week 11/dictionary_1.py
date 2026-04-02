def main():
    # Key-Value (KV) Pair
    my_dictionary = {"World":"Hello", "pi":3.14, 3.14:"pi"}

    print(my_dictionary)

    # Adding and update are similar
    # Python will check if a key exist
    # If it exist => Update value
    # If it doesnt exist => Addition
    my_dictionary["CSE1321"] = 51

    print(my_dictionary)

    print(my_dictionary["CSE1321"])

    my_dictionary["CSE1321"] = 5
    print(my_dictionary)

    # We can delete a KV Pair by specifying
    # a key.
    # The specified key MUST exist in the dictionary
    del my_dictionary["CSE1321"]
    print(my_dictionary)

if __name__ == "__main__":
    main()