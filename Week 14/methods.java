public class methods {
    // def is_even(number):
    //     return numer % 2 == 0

    // In java the syntax is more verbose:
    // You have to define the access modifier,
    // If it is static (we will cover this more next week)
    // We have to define the return value data type
    // We have to define the data type of each parameter
    // value.
    // Also, in Java all parameters are required
    public static boolean is_even(int number){
        return number % 2 == 0;
    }

    // If a function will not return any value
    // We can set the return type as 'void'
    public static void print_hello_world(){
        System.out.println("Hello World");
    }

    public static void test(){
        System.out.println("This print statement workds");

        return; // Return statement will also break out of the function

        System.out.println("This print statement will never work");
    }



    public static void main(String[] args) {
        System.out.println(is_even(4));
        System.out.println(is_even(5));
        print_hello_world();
        test();
    }
}
