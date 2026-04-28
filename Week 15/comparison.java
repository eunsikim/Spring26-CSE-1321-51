import java.util.Scanner;

public class comparison {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s1 = "Hello";
        String s2 = "Hello";

        int num1 = 10;
        int num2 = 10;

        System.out.println(num1 == num2);

        System.out.println(s1 == s2);

        System.out.println("References for s1, s2, and user input");
        System.out.println(System.identityHashCode(s1));
        System.out.println(System.identityHashCode(s2));
        System.out.println(System.identityHashCode(sc.nextLine()));
        
        System.out.println("Comparing strings with '==' (Compare by reference)");
        System.out.println(s1 == s2);
        System.out.println(s2 == sc.nextLine());

        System.out.println("Comparing strings with '.equals' (Compare by value)");
        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(sc.nextLine()));
        
    }
}
