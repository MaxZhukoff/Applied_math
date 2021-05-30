package com.plugin.kottragu;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.plugin.kottragu.service.TimerService;
import org.jetbrains.annotations.NotNull;


// init DialogMenu
public class InitDialogMenu extends AnAction {

    @Override
    public void actionPerformed(@NotNull AnActionEvent e) {
        TimerService.getInstance().setProject(e.getProject());
        TimerService.getInstance().openDialogMenu();
    }
}
