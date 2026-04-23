public class math_operators {
    public static void main(String[] args) {
        // In java, any arithmetical operator
        // will result a value of type int
        // if both operands are int
        // And double if one or both operands
        // are double.
        int int_num_1 = 4;
        int int_num_2 = 3;

        double db_num_1 = 4.0;
        double db_num_2 = 3.0;

        System.out.println(int_num_1 + int_num_2);
        System.out.println(int_num_1 - int_num_2);
        System.out.println(int_num_1 * int_num_2);
        System.out.println(int_num_1 / int_num_2);
        System.out.println(int_num_1 % int_num_2);

        System.out.println(db_num_1 + db_num_2);
        System.out.println(db_num_1 - db_num_2);
        System.out.println(db_num_1 * db_num_2);
        System.out.println(db_num_1 / db_num_2);
        System.out.println(db_num_1 % db_num_2);

        System.out.println(int_num_1 + db_num_2);
        System.out.println(int_num_1 - db_num_2);
        System.out.println(int_num_1 * db_num_2);
        System.out.println(int_num_1 / db_num_2);
        System.out.println(int_num_1 % db_num_2);
    }
}
