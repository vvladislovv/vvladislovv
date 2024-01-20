import java.util.Scanner;

public class MainApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Веддите первое число");
        float a = sc.nextFloat();
        System.out.println("Веддите Второе число");
        float b = sc.nextFloat();
        System.out.println("Веддите оперецию (+, -, *, /)");
        char opetayion = sc.next().charAt(0);

        

        if (opetayion == '+') {
            float resual = a + b;
            System.out.println("Сумма чисел "+ a + " и " + b + " равна " + resual);
            System.out.println(+ a + " и " + b + " = " + resual);
        } else if (opetayion == '-') {
            float resual = a - b;
            System.out.println("Разность чисел "+ a + " и " + b + " равна " + resual);
            System.out.println(+ a + " и " + b + " = " + resual);
        } else if (opetayion == '*') {
            float resual = a * b;
            System.out.println("Разность чисел "+ a + " и " + b + " равна " + resual);
            System.out.println(+ a + " и " + b + " = " + resual);
        } else if (opetayion == '/') {
            float resual = a / b;
            System.out.println("Разность чисел "+ a + " и " + b + " равна " + resual);
            System.out.println(+ a + " и " + b + " = " + resual);
        } else {
            System.out.println("Указаная операция не поддерживаеться калькулятором");
        }
    }
}
