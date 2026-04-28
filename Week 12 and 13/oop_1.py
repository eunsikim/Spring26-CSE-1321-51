class phone:
    # Constructor Function
    def __init__ (self, make, model, color):
        # Class Attributes/Member Attributes
        self.make = make
        self.model = model
        self.color = color
    
    # Behaviors/Member Functions
    def print_info(self):
        print(f"My phone is a {self.color} {self.make} {self.model}")

def main():
    p1 = phone("Samsung", "Galaxy S25", "Grey")
    p2 = phone("IPhone", "12 Pro", "Black")
    p3 = phone("Nokia", "2780 Flip", "Blue")

    p1.print_info()
    p2.print_info()
    p3.print_info()

    print()

    p1.model = "Galaxy S25 Ultra"

    p1.print_info()
    p2.print_info()
    p3.print_info()



if __name__ == "__main__":
    main()