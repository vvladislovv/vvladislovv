import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.Random;

public class GameField extends JPane implements {
    private final int SIZE = 320;
    private final int DOT_SIZE = 16;
    private final int ALL_DOTS = 400;
    private Image Cactus;
    private Image Pemgvin;
    private int CactusX;
    private int CactusY;
    private int[] x = new int[ALL_DOTS];
    private int[] y = new int[ALL_DOTS];
    private int dots;
    private Timer timer;
    private boolean left = false;
    private boolean right = true;
    private boolean up = false;
    private boolean Down = false;
    private boolean inGame = true;
    
    public GameField(){
        setBackground(Color.black);
        loadImages();
    }

    public void initGame(){
        Cactus = 3;
        for (int i=0; i < Cactus; i++) {
            x[i] = 48 - i*DOT_SIZE;
        }
        timer = new Timer(250,this);
        timer.start();
        createCactus();
    }

    public void createCactus() {
    CactusX = new Random().nextInt(20)*DOT_SIZE;
    CactusY = new Random().nextInt(20)*DOT_SIZE;  
    }

    public void loadImages(){
        ImageIcon iia = new ImageIcon("Pemgvin.png");
        Pemgvin = iia.getImage();
        ImageIcon iid = new ImageIcon("Cactus.webp");
        Cactus = iid.getImage();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (inGame){
            move();
        }
        repaint();
    }

}