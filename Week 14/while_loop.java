import java.util.Scanner;

public class while_loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter -1 to stop: ");
        int input = sc.nextInt();

        while(input != -1){
            System.out.print("Enter -1 to stop: ");
            input = sc.nextInt();
        }
        
        System.out.println("Program terminated");
    }
}
