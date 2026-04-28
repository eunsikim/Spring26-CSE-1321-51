public class for_loop {
    public static void main(String[] args) {
        // This is an array, similar (kind of) to a Python list
        int[] my_numbers = {1, 2, 3};

        // FOR EACH loop
        for(int number : my_numbers){
            System.out.println(number);
        }

        System.out.println();

        // Regular FOR loop "counting loop"
        // i++ is the same as i+=1 in python
        //
        // Parts of a FOR loop in Java
        // int i = 0 happens before the loop
        // i < 10 is the condition for the loop to keep iterating
        // i++ is what happens at the end of each iteration
        for(int i = 0; i < 10; i++){
            System.out.println(i);
        }
    }
}
