public class array_2d {
    public static void main(String[] args){
        int[][] my_array_2d = new int[4][2];

        // Fill the 2D array
        int count = 1;
        for(int i = 0; i < my_array_2d.length; i++){
            for(int j = 0; j < my_array_2d[0].length; j++){
                my_array_2d[i][j] = count;
                count++;
            }
        }

        // Print
        for(int i = 0; i < my_array_2d.length; i++){
            for(int j = 0; j < my_array_2d[0].length; j++){
                System.out.print(my_array_2d[i][j] + " ");
            }
            System.out.println();
        }
    }
}
