def main():
    # Strings are inmutable
    text = "Hello World"
    print(text)
    # You can use the `len()` to get the number of characters
    print(len(text))

    text = "Hello CSE 1321"
    print(text)
    print(len(text))

    # Escape Sequence
    my_string = "\"\\This is a text\\\nThis is the continuation of the text\""
    print(my_string)


if __name__ == "__main__":
    main()