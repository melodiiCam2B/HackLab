package jvas;

import javax.swing.*;
import java.awt.*;

public class WinPan extends JPanel {
    final int swidth  = 768;
    final int sheight = 576;
    public WinPan() {
        this.setPreferredSize(new Dimension(swidth, sheight));
        this.setBackground(Color.BLACK);
        this.setDoubleBuffered(true);
    }


}
