public class poorboy{
    String name;
    String nationality;
    String message;

public poorboy(String name, String nationality, String message){
    this.name = name;
    this.nationality = nationality;
    this.message = message;
}
public void displayinfo(){
    System.out.println("-------");
    System.out.println("Name : " +name);
    System.out.println("Nationality : " +nationality);
    System.out.println("Message : " +message);
}
public static void main(String[] args) {
    poorboy tony = new poorboy("Tony Montana", "Cuban", "The World Is Yours, Chico");
    poorboy henry = new poorboy("Henry Hill", "Italian", "As Far Back As I Can Remember I Always Wanted to be a Gangster");

    tony.displayinfo();
    henry.displayinfo();
}
}