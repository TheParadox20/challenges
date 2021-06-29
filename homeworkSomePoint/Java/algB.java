import java.util.Scanner;
public class algB {
    public static void main(String[] args) {
        System.out.println("Welcome to Homework Point Sum program!");
        double sum =0;
        int itterations=0;
        while(true){
            System.out.println("Enter a homework score, or -1 to quit:");
            Scanner Score = new Scanner(System.in);
            double score = Score.nextDouble();
            if (score<0) {
                break;
            }
            sum+=score;
            itterations++;
        }
        System.out.println("Homework point sum is "+sum);
        if ((sum/itterations)<33) {
            System.out.println("Fail");
        }
    }
}
