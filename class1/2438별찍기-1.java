import java.util.Scanner;
class Main {
    public static void main(String[] a){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int i,j;
        for (i=1;i<=n;i++){
            for (j=1;j<=i;j++){
                System.out.print("*");
            }
            System.out.println();
        }
        s.close();
    }
}

