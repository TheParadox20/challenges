import java.util.Scanner;
public class algA {
    public static void main(String[] args) {
        System.out.println("Welcome to the Homework Point Sum program!");
        System.out.println("How many assignments did you complete?: ");
        Scanner Assignments = new Scanner(System.in);
        int assignments = Assignments.nextInt();
        double sum=0;
        for (int i = 1; i <=
         assignments;i++) {
            Scanner Score = new Scanner(System.in);
            System.out.println("Enter score "+i+": ");
            double score = Score.nextDouble();
            sum+=score;
        }
        System.out.println("Homework point sum is "+sum);
        if ((sum/assignments)<33) {
            System.out.println("Fail");
        }
    }
}