public class overloaded_methods {
    // Overloaded Method Rules:
    // 1. The name/identifier must be the same
    // 2. The signature must be unique on each Ov. Method
    //      Signature == Data types in the parameter
    public static int add(int num1, int num2){
        System.out.println("add(int,int)");
        return num1 + num2;
    }
    
    public static double add(double num1, double num2){
        System.out.println("add(double,double)");
        return num1 + num2;
    }
    
    public static int add(int num1, double num2){
        System.out.println("add(int,double)");
        return num1 + (int)num2;
    }
    
    public static double add(double num1, int num2){
        System.out.println("add(double,int)");
        return num1 + num2;
    }
    
    public static int add(int num1){
        System.out.println("add(int)");

        // return num1 + 10;
        // This is the same as the code above
        return add(num1, 10);
    }
    
    public static void main(String[] args) {
        System.out.println(add(4, 3));
        System.out.println(add(4));
        System.out.println(add(4.0, 3.0));
        System.out.println(add(4, 3.0));
        System.out.println(add(4.0, 3));
    }
}
