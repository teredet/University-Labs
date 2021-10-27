public class fclass1{
    fclass1() { // конструктор без параметров
        System.out.println("");
        System.out.println("fclass1 - это родительский класс");
    }
    public static void main(String[] args){
        new fclass2();
    }
}

class fclass3 extends fclass1 {
    fclass3() { // конструктор без параметров
        System.out.println("fclass3 - это потомок класса fclass1");
    }
}
class fclass2 extends fclass3 {
    fclass2() { // конструктор без параметров
        System.out.println("fclass2 - это потомок класса fclass3");
        System.out.println("");
    }
}