public class Polymorph {
    void method1(){
        System.out.println("Это был вызван метод суперкласса Polymorph");
    }

    public static void main(String[] args){
        new NewClass1().method1();
        new NewClass2().method1();
    }
}
class NewClass1 extends Polymorph {
    void method1(){
        System.out.println("");
        System.out.println("Это был вызван метод класса потомка NewClass1");
    }
}
class NewClass2 extends Polymorph {
    void method1(){
        System.out.println("Это был вызван метод класса потомка NewClass2");
        System.out.println("");
    }
}