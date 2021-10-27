public class fclass10 {
    private int number = 999;
    public int getNumber(){ return this.number; }
    public static void main(String args[]) {
        new fclass20();
    }
}


class fclass20 extends fclass10{
    fclass20() { // конструктор без параметров
        System.out.println("");
        System.out.println("Значение инкапсулированного закрытого private поля - number: "+getNumber());
        System.out.println("");
    }
}
