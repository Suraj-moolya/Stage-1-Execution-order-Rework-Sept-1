Feature: 94034 To Test the CCOTF changes in refine online of the M580 ePAC CyberSecurity enabled controller(FW 4.3)

  @94034_1
  Scenario Outline: Open Refine Online Window With Password
    When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I select protocol '<protocol>' in Confirm Refine Online
    And I enter password '<password>' in Controller Password Window
    And I click the button '<button>' in Controller Password Window
    And I click the button '<button>' in Confirm Refine Online
    And I Click on buttons in popup window Application browser in application explorer as '<button>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    
    @Select_Https_Protocol_in_Deploy_Window
    Examples:
      | context menu  | Controller      | protocol | password    | button | Message                               |
      | Refine Online | M580_Standalone | HTTPS    | Schneider0! | OK     | Open Refine Online Editor (Completed) |
      
      
  @94034_2
  Scenario Outline: Add IO module which supports CCOTF
    When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
    And I enterkey Project Browser RO in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
    And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
    And I selected Dialog OK CE in dialog ce
    And I selected List of modified Yes button CE in dialog ce
    And I selected Close Refine Offline in refine offline
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify Action message in notification pannel container dock in project explorer as '<message>'
    And I click modal dialog window project browser in project explorer as '<button>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify Action message in notification pannel container dock in project explorer as '<message1>'
  
  @Add_Analog_Module_in_Config_Window  
  Examples:
    | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 | button | button1 | message                              | message1                               |
    | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Analog           | BMX AMI 0810     | OK     | Yes     | Build and Deploy Changes (Completed) | Close Refine Online Editor (Completed) |
    
  @94034_3
  Scenario Outline: Update Control Project
    When I checked header cb in message box
    And I click modal dialog window Modal dialog window in message box as '<Modal dialog window2>'
    And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 3>'
    Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel4>'

  @Update_Control_Project
  Examples:
    | Modal dialog window2 | Modal Dialog Window 3                     | Notification Pannel4       | 
    | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Update Project (Completed) |
    
    
## note: Same like this for redundant M580