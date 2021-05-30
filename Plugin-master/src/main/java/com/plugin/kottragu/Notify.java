package com.plugin.kottragu;

import com.intellij.notification.NotificationDisplayType;
import com.intellij.notification.NotificationGroup;
import com.intellij.openapi.project.Project;
import com.intellij.openapi.startup.StartupActivity;
import com.plugin.kottragu.service.TimerService;
import org.jetbrains.annotations.NotNull;

public class Notify implements StartupActivity {
    public static final NotificationGroup STICKY_GROUP =
            new NotificationGroup("demo.notifications.balloon",
                    NotificationDisplayType.STICKY_BALLOON, true);


    public void runActivity(@NotNull Project project) {

        TimerService.getInstance().setProject(project);
        TimerService.getInstance().startTimer(STICKY_GROUP);
    }
}
