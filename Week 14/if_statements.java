import java.util.Scanner;

public class if_statements {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your age: ");

        int age = sc.nextInt();

        if(age >= 21){
            System.out.println("You are eligible to vote and drink");
        }
        else if(age >= 18){
            System.out.println("You are eligible to vote but not drink");
        }
        else{
            System.out.println("You are not eligible to vote and drink");
        }
    }
}
