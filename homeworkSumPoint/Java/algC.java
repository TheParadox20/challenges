import java.util.Scanner;
public class algC {
    public static void main(String[] args) {
        System.out.println("Welcome to the Homework Point Sum program!");
        double sum=0;
        int itterations = 0;
        while (true) {
            System.out.println("Do you want to enter a homework score? ('yes' or 'no')");
            Scanner Input = new Scanner(System.in);
            String input = Input.nextLine();
            if (input=="yes") {
                Scanner Score = new Scanner(System.in);
                double score = Score.nextDouble();
                sum+=score;
                itterations++;
            } else if(input=="no") {
                break;
            } else{
                System.out.println("Unrecognized entry! Please try again.");
            }
        }
        if ((sum/itterations)<33) {
            System.out.println("Fail");
        }
    }
}
