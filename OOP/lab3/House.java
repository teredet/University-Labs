import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class House extends JFrame {
    House(String s) {
        super(s);
        setLayout(null);
        setSize(500,500);
        setVisible(true);
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setResizable(false);
        this.setLocation(100,100);
    }
    public void paint(Graphics gr){
        gr.setColor(Color.BLACK);
        //прямоугольник
        gr.drawLine(150, 200, 150, 300);
        gr.drawLine(300, 200, 300, 300);
        gr.drawLine(150, 200, 300, 200);
        gr.drawLine(300, 300, 150, 300);

        //крыша
        gr.drawLine(150, 200, 225, 150);
        gr.drawLine(300, 200, 225, 150);

        //окно
        gr.drawLine(235, 250, 260, 250);
        gr.drawLine(235, 225, 260, 225);
        gr.drawLine(235, 250, 235, 225);
        gr.drawLine(260, 225, 260, 250);

        //дверь
        gr.drawLine(175, 300, 175, 250);
        gr.drawLine(200, 300, 200, 250);
        gr.drawLine(175, 250, 200, 250);

        gr.dispose();
    }
    public static void main(String[] args){
        new House("");
    }
}
