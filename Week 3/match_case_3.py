def main():
    x = 10

    if x < 11:
        print("x is less than 11")
    else:
        print("x is greater than or equal to 11")

    # How can I do this using just one `MATCH-CASE` statement
    # Without using the `IF` keyword.
    # Assume `X` can be any value [-inf, inf]
    match x < 11:
        case True:
            print("x is less than 11")
        case False:
            print("x is greater than or equal to 11")
    
    # Practice, what if we add an `ELIF` statement.
        


if __name__ == "__main__":
    main()