class video_game{
    // Member Attributes are defined
    // in the class body, not in the constructor
    private String name;
    private int id;
    static int nextID = 1;
    private String rate; // E, PG-13, R, etc...
    private String genre; 
    private String modality; // Single Player, Co-op, Multiplaer, etc..
    private Double price;
    public int example = 10;

    // Constructor
    // - Default Constructor
    public video_game(){
        id = nextID;
        nextID++;
    }
    // - Overloaded Constructor
    public video_game(String name, String rate, String genre, String modality, Double price){
        // `this` will always refer to the object
        // `this.name` is referencing the Member attribute name, not the parameter.
        this.name = name;
        this.rate = rate;
        this.genre = genre;
        this.modality = modality;
        this.price = price;
        id = nextID;
        nextID++;
    }

    // Setter and Getter Functions
    // Setter
    public void setName(String name, String role){
        if(role.equals("dev")){
            System.out.println("Changing the game name to " + name);
            this.name = name;
        }
        else{
            System.out.println("You do not have permission to do this.");
        }
    }
    // Getter function
    public String getName(){
        return name;
    }

    public int getID(){
        return id;
    }
}

public class oop_1 {
    public static void print_hello_world(){
        System.out.println("Hello World");
    }
    public static void main(String[] args) {
        System.out.println("vide_game class nextID: " + video_game.nextID);
        video_game game1 = new video_game("OwlMon", "E", "fighting", "Single Player", 3.99);
        System.out.println("Game 1 id: " + game1.getID());
        
        System.out.println("vide_game class nextID: " + video_game.nextID);
        video_game game2 = new video_game();
        System.out.println("Game 2 id: " + game2.getID());
        
        System.out.println("vide_game class nextID: " + video_game.nextID);
        video_game game3 = new video_game();
        System.out.println("Game 3 id: " + game3.getID());
        
        System.out.println("vide_game class nextID: " + video_game.nextID);
        video_game game4 = new video_game();
        System.out.println("Game 4 id: " + game4.getID());
    }
}
