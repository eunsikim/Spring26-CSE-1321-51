import java.util.Scanner;

public class input_2 {
    public static void main(String[] args) {
        // Scanner objet will "scan" the user input
        // from the terminal, hence we use "System.in" as
        // argument for the constructor
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter your age: ");

        int age = sc.nextInt();

        System.out.println("You are " + age + " years old.");

        System.out.print("Enter your name: ");

        String name = sc.nextLine();

        System.out.println("Your name is " + name);
    }
}
