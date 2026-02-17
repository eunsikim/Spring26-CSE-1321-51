# A single iteration (repetition) of the parent loop, consists on the code
# in the loop AND the full iteration of all child loops
def main():
    restart = "Y"

    # Parent/Outer Loop
    while restart == "Y":
        print("Hello World")
        # Child/Inner Loop
        while True:
            pass
            
        while True:
            pass

        for r in restart:
            pass


        


if __name__ == "__main__":
    main()