Feature: 96838 - To Check the error while deploy of the M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)


#Note - During Deployment Remove cable
  @96838_1
  Scenario Outline: During Deploying the controller Remove the Cable
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

  @Deploy_the_controller__182.233.63.5__M580_Standalone_remove_cable
  Examples:
    | MainToolBar       | ControllerNode  | TopologyExplorerOption | ProjectDropdown                                   | ExecutablesDropdown                                       | ConfirmationDialog | TargetIPAddress | Protocol | Password    | FinalDialogButton                         | NotificationMessage                  |
    | Topology Explorer | M580_Standalone | Deploy Built Project   | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                 | 182.233.63.5    | HTTPS    | Schneider0! | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Not Completed) |