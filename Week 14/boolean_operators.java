public class boolean_operators {
    public static void main(String[] args) {
        int num1 = 4;
        int num2 = 3;

        // Comparison Operators are the same
        System.out.println(num1 > num2);
        System.out.println(num1 >= num2);
        System.out.println(num1 < num2);
        System.out.println(num1 <= num2);
        // The equality operator only
        // works when comparing primitive types
        System.out.println(num1 == num2);
        System.out.println(num1 != num2);

        // Logical Operators
        // AND => &&
        System.out.println(num1 > num2 && true);
        // OR => ||
        System.out.println(num1 > num2 || true);
        // NOT => !
        System.out.println(!(num1 > num2));
    }
}
