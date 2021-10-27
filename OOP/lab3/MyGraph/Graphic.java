package MyGraph;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Graphic extends JFrame{
    Graphic(String s){
        super(s);
        setLayout(null);
        setSize(120,200);
        setVisible(true);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.setResizable(true);
        Button sin = new Button("Sin");
        sin.setBounds(5, 20, 100, 25);
        add(sin);
        Button cos = new Button("Cos");
        cos.setBounds(5, 60, 100, 25);
        add(cos);
        Button x2 = new Button("Парабола");
        x2.setBounds(5, 120, 100, 25);
        add(x2);
        sin.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent event){
                new Sinus("Синус");
            }
        });
        cos.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent event){
                new Cosinus("Косинус");
            }
        });
        x2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent event){
                new X2("Парабола");
            }
        });
    }
    public static void main(String[] args){
        new Graphic("Графопостроитель");
    }
}
