Feature: 96836 - To Test the Re-deploy of the M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)

  @96836_1
  Scenario Outline: Deploy the Second controller 
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<ControllerNode>'
    And I Select context menu item EC Topology Explorer Tree in topology as '<TopologyExplorerOption>'
    And I select deploy popup dropdown value TE project dropdown in topology as '<ProjectDropdown>'
    And I select deploy popup dropdown value TE Executables dropdown in topology as '<ExecutablesDropdown>'
    And I click modal dialog window Modal dialog window in message box as '<ConfirmationDialog>'
    And I select ip adress from deploy project build TE Modal dialog window in message box as '<TargetIPAddress>'
    And I select protocol '<Protocol>' in Confirm Refine Online
    And I enter password '<Password>' in Controller Password Window
    And I click the button '<ConfirmationDialog>' in Controller Password Window
    And I Click on start engine checkobox in deploy changes refine online window
    And I click modal dialog window Modal dialog window in message box as '<ConfirmationDialog>'
    And I Click popup button object Modal Dialog Window 1 in message box as '<FinalDialogButton>'
    Then Verify Action message in notification pannel project browser in project explorer as '<NotificationMessage>'

  @Deploy_the_controller__182.233.63.5__M580_Standalone2
  Examples:
    | MainToolBar       | ControllerNode  | TopologyExplorerOption | ProjectDropdown                                    | ExecutablesDropdown                                       | ConfirmationDialog | TargetIPAddress | Protocol | Password    | FinalDialogButton                         | NotificationMessage              |
    | Topology Explorer | M580_Standalone | Deploy Built Project   | Topology$$projectdropdowntextbox$$M580_Standalone2 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                 | 182.233.63.5    | HTTPS    | Schneider0! | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
    
    
  @96836_2
  Scenario Outline: Open Refine and Do Some Modification
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I RClick control project browser project browser in project explorer as '<ControlProject>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem>'
    And I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<Section>'
    And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<ContextMenuItem2>'   
    Then I create a New Section under Logic in control expert as '<SectionName>' 
    When I selected Save Refine Offline in refine offline
    And I wait in seconds Refine online window in refine offline
    And I selected Close Refine Offline in refine offline
    Then Verify notification panel message Notification Pannel in message box as '<Content>'
    
  @OpenRefine_and_DoModification_in_M580Standalone
  Examples:
    | MainToolBar      | ControlProject  | ContextMenuItem | ExportFileName  | Section                      | ContextMenuItem2 | SectionName | Content                                  |
    | Project Explorer | M580_Standalone | Refine          | ProjectExplorer | Programs$$Tasks$$MAST$$Logic | New Section      | Sample$$FBD | Close Control Project Editor (Completed) |
    
  
  @96836_3
  Scenario Outline: Performing Increament Build
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser1>'
    And I Select context menu item EC project browser in project explorer as '<ProjectBrowser2>'
    And I click modal dialog window project browser in project explorer as '<ProjectBrowser3>'

  @IncreamentBuild_ControlEcecutable_1
  Examples:
    | project browser1    | ProjectBrowser2 | ProjectBrowser3 |
    | ControlExecutable_1 | Build           | OK              |
    
  
  @96836_4
  Scenario Outline: Deploy Changes for Controller M580 Standalone after Increament Build
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I click modal dialog window Instance editor save in application explorer as 'OK'
    And I enter password '<password>' in Controller Password Window
    And I click the button '<button>' in Controller Password Window
    When I selected Rename Pop up Ok in message box
    And I Click on OK button from Reconfirm Deploy Built Project Popup window
    Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'

  @Deploy_Changes_for__M580_Standalone_After_IncreamentBuild
  Examples:
    | MainToolBar       | context menu                         | project browser3                                 | Controller      | password    | button |
    | Topology Explorer | Deploy Changes / Undo Online Changes | Deploy Changes / Undo Online Changes (Completed) | M580_Standalone | Schneider0! | OK     |
    
    
  @94112_6
  Scenario Outline: ReDeploy the controller 
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<ControllerNode>'
    And I select ip adress from deploy project build TE Modal dialog window in message box as '<TargetIPAddress>'
    And I select protocol '<Protocol>' in Confirm Refine Online
    And I enter password '<Password>' in Controller Password Window
    And I click the button '<ConfirmationDialog>' in Controller Password Window
    And I Click on start engine checkobox in deploy changes refine online window
    And I click modal dialog window Modal dialog window in message box as '<ConfirmationDialog>'
    And I Click popup button object Modal Dialog Window 1 in message box as '<FinalDialogButton>'
    Then Verify Action message in notification pannel project browser in project explorer as '<NotificationMessage>'

  @ReDeploy_the_controller__182.233.63.5__M580_Standalone
  Examples:
    | MainToolBar       | ControllerNode  | TopologyExplorerOption | ConfirmationDialog | TargetIPAddress | Protocol | Password    | FinalDialogButton                         | NotificationMessage              |
    | Topology Explorer | M580_Standalone | Re-Deploy Last Project | OK                 | 182.233.63.5    | HTTPS    | Schneider0! | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |