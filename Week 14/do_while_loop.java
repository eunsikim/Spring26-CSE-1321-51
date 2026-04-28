import java.util.Scanner;

public class do_while_loop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int input = 0;

        do{
            
            System.out.print("Enter -1 to stop: ");
            input = sc.nextInt();
        }
        while(input != -1);
        
        System.out.println("Program terminated");
    }
}
