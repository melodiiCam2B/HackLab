package jvas;
import java.awt.*;
import javax.swing.*;
import jvas.WinPan;
class test {

    public static void main(String[] args) {
        new window().setVisible(true);
        WinPan gamepanel = new WinPan();
       // window.add(gamepanel);

    }
}

class window extends JFrame{
    public window (){
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Hi!");
        ImageIcon ImageIcon = new ImageIcon("D:\\code\\HackLab\\jvas\\assets\\cathug.png");
        Image Image = ImageIcon.getImage();
        setIconImage(Image);
        setSize(768, 576);
        setLocationRelativeTo(null);

        //pack();
    }

}