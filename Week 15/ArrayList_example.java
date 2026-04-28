import java.util.ArrayList;

public class ArrayList_example {
    // ArrayList are very much like Lists in Ptyhon
    // Dynamic Size, "Inifinite" size, and lots of useful functions
    public static void main(String[] args) {
        // We cannot use primitive types on arraylist,
        // instead we use "Wrapper" class for primitive types:
        // - Integer for int
        // - Double for double
        // - Character for char
        // etc...
        ArrayList<Integer> my_int_list = new ArrayList();

        my_int_list.add(100);
        my_int_list.add(101);
        my_int_list.add(102);

        System.out.println("Iterating with a FOR EACH loop");
        for(int num : my_int_list){
            System.out.println(num);
        }
        System.out.println("Iterating with a FOR loop");
        for(int i = 0; i < my_int_list.size(); i++){
            System.out.println(my_int_list.get(i));
        }

        // Remove by index
        System.out.println("Removing the first index");
        my_int_list.remove(0);

        for(int num : my_int_list){
            System.out.println(num);
        }
    }
}
