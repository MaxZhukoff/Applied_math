package com.plugin.kottragu.ui;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.ui.DialogWrapper;
import com.intellij.ui.JBColor;
import com.plugin.kottragu.service.TimerService;
import org.jdesktop.swingx.JXLabel;
import org.jdesktop.swingx.JXPanel;
import org.jdesktop.swingx.JXTextField;
import org.jetbrains.annotations.Nullable;
import javax.swing.*;

public class DialogMenu extends DialogWrapper {
    private JXTextField textField;
    private JXPanel dialogPanel;
    private JXLabel errorLabel = new JXLabel();
    private boolean isError = false;
    
    public DialogMenu(@Nullable Project project) {
        super(project);
        init();
        setSize(1000,500);
        setTitle("Timer manager");
    }

    @Override
    public void doCancelAction() {
        super.doCancelAction();
        System.out.println("Cancel clicked");
    }

    @Override
    protected void doOKAction() {
        if (textField.getText().matches("\\d+")) {
            super.doOKAction();
            TimerService.getInstance().setTime(Integer.parseInt(textField.getText())*60*1000);
            TimerService.getInstance().startTimer();
        } else {
            if (!isError) {
                errorLabel.setText("Incorrect time");
                errorLabel.setForeground(JBColor.RED);
                dialogPanel.add(errorLabel);
                isError = true;
                this.repaint();
            }
        }
    }


    @Override
    protected @Nullable JComponent createCenterPanel() {
        dialogPanel = new JXPanel();
        JXLabel label = new JXLabel("Input time in minutes");
        dialogPanel.add(label);
        textField = new JXTextField();
        textField.setSize(500,250);
        textField.setPrompt("Input time");
        dialogPanel.add(textField);
        return dialogPanel;
    }


}
