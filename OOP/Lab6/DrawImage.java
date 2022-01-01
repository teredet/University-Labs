import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.io.IOException;
import javax.swing.JPanel;
import javax.swing.JFrame;


public class DrawImage extends JFrame {
    Image img = Toolkit.getDefaultToolkit().getImage("URL");
    public DrawImage() throws IOException {
        
        super.setSize(480,710);
        this.setContentPane(new JPanel() {

            public void paintComponent(Graphics g) {
                super.setLayout(null);

                super.paintComponent(g);
                g.drawImage(img, 0, 0, null);
            }
        });
        //pack();
        setVisible(true);
    }
    public static void main(String[] args) throws Exception {
        new DrawImage();

    }
}
