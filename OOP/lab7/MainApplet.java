import javax.swing.*;
import java.awt.*;

// Потік для розрахунку координат лінії
class ComputeLines implements Runnable  {
    boolean going = true;
    public ComputeLines(MainApplet parentObj)    {
        parent = parentObj;
    }
    public void compute()    {
        int w = parent.getSize().width-1, h = parent.getSize().height-1;
        parent.LineCoordinates
                ((int)(Math.random()*w),(int)(Math.random()*h),
                        (int)(Math.random()*w), (int)(Math.random()*h));
    }
    MainApplet parent; 	// посилання на творця об'єкта
    public void run()     {
        while(going) { compute(); }
    }
}

class ComputeRects extends Thread {
    boolean going = true;
    // конструктор одержує посилання на творця об`єкта - аплет
    public ComputeRects(MainApplet parentObj) {
        parent = parentObj;
    }
    public void run() {
        while(going) {
            int w = parent.getSize().width-1, h = parent.getSize().height-1;
            parent.RectCoordinates
                    ((int)(Math.random()*w),(int)(Math.random()*h));
        }
    }
    MainApplet parent; // посилання на творця об`єкта
}

// Потік для розрахунку координат овалу
class ComputeOvals extends Thread {
    boolean going = true;
    public ComputeOvals(MainApplet parentObj) {
        parent = parentObj;
    }
    public void run() {
        while(going) {
            int w = parent.getSize().width-1, h = parent.getSize().height-1;
            parent.OvalCoordinates((int)(Math.random()*w),(int)(Math.random()*h));
        }
    }
    MainApplet parent; // посилання на творця об`єкта
}

public class MainApplet extends JApplet {
    // скопіюйте з попереднього приклада
    ComputeRects m_rects = null;
    ComputeOvals m_ovals = null;
    int m_rectX = 0; int m_rectY = 0;
    int m_ovalX = 0; int m_ovalY = 0;
    // скопіюйте з попереднього приклада
    ComputeLines m_lines = null;
    int m_lineX1 = 0, m_lineX2 = 0, m_lineY1 = 0, m_lineY2 = 0;
    // Синхронний метод для установки координат
    // прямокутника з іншого потоку
    public synchronized void RectCoordinates(int x, int y)    {
        m_rectX = x; m_rectY = y;
        this.repaint();
    }

    // Синхронний метод для установки координат овалу
    // з іншого потоку
    public synchronized void OvalCoordinates(int x, int y)    {
        m_ovalX = x; m_ovalY = y;
        this.repaint();
    }
// Синхронний метод для установки координат лінії
// из другого потока

    public synchronized void LineCoordinates(int x1, int y1, int x2, int y2)  {
        m_lineX1 = x1; m_lineX2 = x2; m_lineY1 = y1; m_lineY2 = y2;
        this.repaint();
    }
    @Override
    public void start()     {
        super.start();
        // Запускаємо потоки
        // скопіюйте з попереднього приклада
        if (m_rects == null) {
            m_rects = new ComputeRects(this); m_rects.start();
        }
        if (m_ovals == null) {
            m_ovals = new ComputeOvals(this); m_ovals.start();
        }
        // скопіюйте з попереднього приклада
        if (m_lines == null) {
            m_lines = new ComputeLines(this);
            new Thread(m_lines).start();
        }
    }
    @Override
    public void stop()     {
        super.stop();
        // Зупиняємо потоки
        // скопіюйте з попереднього приклада
        if(m_rects != null) m_rects.going = false;
        if(m_ovals != null) m_ovals.going = false;
        // скопіюйте з попереднього приклада
        if(m_lines != null) m_lines.going = false;
    }
    public void paint(Graphics g)     {
        // скопіюйте з попереднього приклада
        int w = this.getWidth(), h = this.getHeight();
        g.clearRect(0, 0, w, h);
        g.setColor(Color.red);
        g.fillRect(m_rectX, m_rectY, 20, 20);
        g.setColor(Color.blue);
        g.fillOval(m_ovalX, m_ovalY, 20, 20);
        // скопіюйте з попереднього приклада
        g.setColor(Color.green);
        g.drawLine(m_lineX1, m_lineX2, m_lineY1, m_lineY2);
    }
    public static void main(String[] args)     {    }
}


