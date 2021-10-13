class MyType { // объявляется класс
    public int myData=5; // переменная-элемент класса
    MyType() { // конструктор без параметров
        System.out.println("Constructor without parameters");
    }
    MyType(int v) { // конструктор с одним параметром
        System.out.print("Constructor with one parameter");
        System.out.println(" Setting myData="+v);
        myData=v;
    }
    public void myMethod() { // метод класса
        System.out.print("myMethod!");
        System.out.println(" myData="+myData);
    }
}

// Реализация объектов и действия с ними
public class NewClass { // первичный класс
    public static void main(String[] args) {
        // объект obj1 - реализация класса MyType
        MyType obj1=new MyType();
        obj1.myMethod(); // использование метода
        // доступ к открытой переменной
        System.out.println("---obj1.myData="+obj1.myData);
        // объект obj2 - реализация класса MyType
        MyType obj2=new MyType(100);
        // доступ к открытой переменной
        System.out.println("----obj2.myData="+obj2.myData);
    }
}
