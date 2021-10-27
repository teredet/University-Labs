public class Encapsulate {
    public int field1 = 100;
    protected int field2 = 150;
    int field3 = 200;
    private int field4 = 250;
    public int getField4(){ return this.field4; }
    public static void main(String[] args){
        new Class2().method1();
    }
}
class Class2 extends Encapsulate{
    public void method1(){
        System.out.println("");
        System.out.println("Значение открытого public поля - field1: "+this.field1);
        System.out.println("Значение защищенного protected поля - field2: "+this.field2);
        System.out.println("Значение поля без модификатора - field3: "+this.field3);
        System.out.println("Значение инкапсулированного закрытого private поля - field4: "+getField4());
        System.out.println("");
    }
}