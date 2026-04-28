public class overloaded_methods {
    // A method's signature refers to its parameter(s) and their data type
    // Also, in Java we can have functions with the same name/identifier
    // This is called overloaded methods and each method must have
    // a UNIQUE signature.

    public static int add(int num1, int num2){
        return num1 + num2;
    }

    public static int add(int num1){
        return num1 + 10;
    }
    
    public static void main(String[] args) {
        System.out.println(add(4, 3));
        System.out.println(add(4));
    }
}
