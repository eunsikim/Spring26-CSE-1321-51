public class casting {
    public static void main(String[] args) {
        double my_number = 3.14;

        // We are casting a double 3.14 value into an
        // integer. The value's decimal point will get culled
        int my_other_number = (int)3.14;

        // Casting only works between primite data types
        // If you need to convert primitive values to String
        // or the other way around, we use special functions:
        String phone_number = String.valueOf(1234567890);
        int age = Integer.parseInt("20");
    }
}
