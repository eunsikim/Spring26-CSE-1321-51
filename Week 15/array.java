public class array {
    // In Java the basic type of sequence/collection
    // type is called an Array
    // Arrays are limited because you have to define a size
    // whenever you intialize one.
    // Arrays are "static" in the sense that you cannot
    // change the size in runtime.
    public static void main(String[] args) {
        // We are creating an integer array of size 10
        int[] my_int_array = new int[10];

        // To add a value in an array:
        my_int_array[0] = 10;

        // Access values by index
        System.out.println(my_int_array[0]);
        
        // To update a value by index:
        my_int_array[0] = 100;
        System.out.println(my_int_array[0]);

        // We can manually traverse each value in the array
        for(int i = 0; i < my_int_array.length; i++){
            my_int_array[i] = i;
        }

        for(int i = 0; i < my_int_array.length; i++){
            System.out.println(my_int_array[i]);
        }

        // Array sizes are fixed, cannot be changed in runtime.
        // But here are some workarounds:
        // We create a larger array and then copy each value
        // from the smaller array into the larger array
        int[] larger_int_array = new int[my_int_array.length * 2];

        for(int i = 0; i < my_int_array.length; i++){
            larger_int_array[i] = my_int_array[i];
        }

        
    }
}
