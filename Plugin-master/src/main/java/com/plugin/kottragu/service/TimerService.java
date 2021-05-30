package com.plugin.kottragu.service;

import com.intellij.notification.Notification;
import com.intellij.notification.NotificationGroup;
import com.intellij.notification.NotificationType;
import com.intellij.openapi.project.Project;
import com.plugin.kottragu.ui.DialogMenu;
import lombok.Setter;
import lombok.SneakyThrows;
import java.util.TimerTask;

public class TimerService {
    private static TimerService timerService;
    @Setter
    private Project project;
    private NotificationGroup notificationGroup;
    @Setter
    private int time = 3600000; // 1 hour

    private TimerService() {
    }

    public static TimerService getInstance() {
        if (timerService == null)
            timerService = new TimerService();
        return timerService;
    }

    public void openDialogMenu() {
        DialogMenu dialogMenu = new DialogMenu(project);
        dialogMenu.show();
    }

    public void startTimer() {
        MyTimer.getInstance().creatTimerTask(createTimerTask(), time);
    }

    public void startTimer(NotificationGroup notificationGroup) { // start with initialize project
        this.notificationGroup = notificationGroup;
        System.out.println("timer started");
        startTimer();
    }

    private TimerTask createTimerTask() {
        return new TimerTask() {
            @SneakyThrows
            @Override
            public void run() {
                createNotification(project, notificationGroup);
            }
        };
    }

    private void createNotification(Project project, NotificationGroup STICKY_GROUP) {

        Notification msg = STICKY_GROUP.createNotification("Napominanie", "You arbeite uze" + time/(1000*60) + "minutes", "Take a rest for 5 min", NotificationType.INFORMATION);
        msg.notify(project);
    }




}
