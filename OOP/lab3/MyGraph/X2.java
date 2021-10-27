package MyGraph;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class X2 extends JFrame{
    X2(String s){
        super(s);
        setLayout(null);
        setSize(600,300);
        setVisible(true);
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        this.setResizable(false);
        this.setLocation(300,300);
    }
    public void paint(Graphics gr){
        int y; int j=0; int k=0;
        gr.setColor(Color.WHITE);
        gr.fillRect(0,0,600,300);
        gr.setColor(Color.lightGray);
        while(j<600){
            gr.drawLine(j, 0, j, 300);
            j+=50;
        }
        while(k<300){
            gr.drawLine(0, k, 600, k);
            k+=50;
        }
        gr.setColor(Color.BLACK);
        gr.drawLine(300, 0, 300, 300);
        gr.drawLine(0, 150, 600, 150);
        gr.drawString("0", 305, 165);
        gr.setColor(Color.RED);
        for(double i=0; i<1000;i++){
            y=-(int)(i*i/300)+150;
            gr.drawLine((int)i+300, y, (int)i+300, y);
            gr.drawLine(-(int)i+300, y, -(int)i+300, y);
        }
        gr.dispose();
    }
}
