package com.plugin.kottragu.service;

import java.util.Timer;
import java.util.TimerTask;

public class MyTimer {
    private static MyTimer myTimer;
    private Timer timer;
    private MyTimer() {
        timer = new Timer();
    }

    public static MyTimer getInstance() {
        if (myTimer == null)
            myTimer = new MyTimer();
        return myTimer;
    }
    public void creatTimerTask(TimerTask timerTask, int delay) {
        timerRestart();
        timer.schedule(timerTask, delay, delay);
    }
    private void timerRestart() {
        timer.cancel();
        timer = new Timer();
    }
}
