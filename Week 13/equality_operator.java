public class equality_operator {
    public static void main(String[] args) {
        // Use == operator for primitive types
        int num1 = 4;
        int num2 = 4;

        System.out.println(num1 == num2);

        // Use .equal() for complex types
        String s1 = "Hello";
        String s2 = "World";

        System.out.println(s1.equals(s2));
    }
}
