import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


public class ExtEventHandler extends JFrame {
    ExtEventHandler(String s){
        super(s);
        setLayout(null);
        setSize(200,200);
        setVisible(true);
        this.setResizable(false);
        this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        Button b1 = new Button("Первая кнопка");
        b1.setBounds(2, 5, 96, 22);
        add(b1);
        Button b2 = new Button("Вторая кнопка");
        b2.setBounds(2, 100, 96, 22);
        add(b2);
        b1.addActionListener(new Handler(b1, b2));
        b2.addActionListener(new Handler(b1, b2));
    }
    public static void main(String[] args){
        new ExtEventHandler("");
    }
}
class Handler implements ActionListener{
    private Button ba;
    private Button bb;
    String temp;
    Handler(Button b1, Button b2){
        this.ba=b1;
        this.bb=b2;
    }
    public void actionPerformed(ActionEvent e){
        temp = ba.getLabel();
        ba.setLabel(bb.getLabel());
        bb.setLabel(temp);
    }
}
