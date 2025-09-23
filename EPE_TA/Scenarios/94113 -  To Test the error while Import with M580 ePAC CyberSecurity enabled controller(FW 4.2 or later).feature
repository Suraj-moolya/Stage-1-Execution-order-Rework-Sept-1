Feature: 94113 -  To Test the error while Import with M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)

  @94113_1
  Scenario Outline: Export Controller
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I click modal dialog window Instance editor save in application explorer as 'OK'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Export_Controller_94113
    Examples:
      | Controllers     | context menu | sub_context_menu | ExportFileName | ExportFileFormat | ExpectedExportMessage       |
      | M580_Standalone | Export       | Topology         | Controller     | .sbk             | Export Topology (Completed) |

  @94113_2
  Scenario Outline: Import Controller - Update
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button2>'
    And I click modal dialog window project browser in project explorer as '<button>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    And I click modal dialog window Instance editor save in application explorer as '<button1>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Import_Controller_Update_94113
    Examples:
      | Controllers | context menu | sub_context_menu | ImportFileName | ExpectedExportMessage       | button     | button1 | button2 |
      | System_1    | Import       | Topology         | Controller     | Import Topology (Completed) | Update All | OK      | Resolve |

  @94112_2
  Scenario Outline: Import Controller - Skip
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button2>'
    And I click modal dialog window project browser in project explorer as '<button>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Import_Controller_Skip_94113
    Examples:
      | Controllers | context menu | sub_context_menu | ImportFileName | ExpectedExportMessage       | button   | button1 | button2 |
      | System_1    | Import       | Topology         | Controller     | Import Topology (Completed) | Skip All | OK      | Resolve |

  @94113_3
  Scenario Outline: Import Controller - Create
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button2>'
    And I click modal dialog window project browser in project explorer as '<button>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Import_Controller_Create_94113
    Examples:
      | Controllers | context menu | sub_context_menu | ImportFileName | ExpectedExportMessage       | button     | button1 | button2 |
      | System_1    | Import       | Topology         | Controller     | Import Topology (Completed) | Create All | OK      | Resolve |
    
  @94113_4
  Scenario Outline: Export Topology
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Click on Nodes System Explorer Node in system explorer as '<System>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I click modal dialog window Instance editor save in application explorer as 'OK'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

  @Export_Topology_94113
  Examples:
    | Controllers | context menu | sub_context_menu | ExportFileName   | ExportFileFormat | ExpectedExportMessage       | MainToolBar          | System   | MainToolBar1      |
    | System_1    | Export       | Topology         | TopologyExplorer | .sbk             | Export Topology (Completed) | Open System Explorer | System_1 | Topology Explorer |
    
      
  @94112_6
  Scenario Outline: Export Application Explorer
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Click on Nodes System Explorer Node in system explorer as '<System>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuItem>'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'
    
  @Export_Application_94113
  Examples:
    | MainToolBar          | System   | MainToolBar1         | ApplicationBrowser | ContextMenuItem | ExportFileName      | ExportFileFormat | ExpectedExportMessage |
    | Open System Explorer | System_1 | Application Explorer | System_1           | Export          | ApplicationExplorer | .csv             | Export (Completed)    |
    
      
  @94112_6
  Scenario Outline: Export Project Explorer
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Click on Nodes System Explorer Node in system explorer as '<System>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I RClick control project browser project browser in project explorer as '<ControlProject>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'
    
  @Export_Application_94113
  Examples:
    | MainToolBar          | System   | MainToolBar1     | ControlProject | ContextMenuItem | ExportFileName  | ExportFileFormat | ExpectedExportMessage      | Button |
    | Open System Explorer | System_1 | Project Explorer | System_1       | Export          | ProjectExplorer | .sbk             | Export Project (Completed) | OK     |
      
  @94112_3
  Scenario Outline: Set and enable System Access Password while creating System
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<Folder>'
    And I selected Create System in context menu with password
    And I Enter Controller Password TE New Password box in topology as '<New Password box1>'
    And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
    And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
    Then Verify Action message in notification pannel project browser in project explorer as '<project browser>'
   
  @Create_System_with_Password_94113 
  Examples:
    | MainToolBar          | project browser           | New Password box1   | Confirm Password box2       | Folder   |
    | Open System Explorer | Create System (Completed) | Password$$Mooly@123 | Confirm Password$$Mooly@123 | Folder_1 |
    
  @94112_4
  Scenario Outline: Navigation To Topology Explorer and Import Controller
    When I Click on Nodes System Explorer Node in system explorer as '<SystemsExplorer>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<SystemsExplorer>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'
    
  @Navigate_TE_selecting_system2_and_ImportController_94113
  Examples:
    | SystemsExplorer | MainToolBar            | context menu | sub_context_menu | ImportFileName   | ExpectedExportMessage       | button     | button1 | button2 |
    | System_2        | Open Topology Explorer | Import       | Topology         | TopologyExplorer | Import Topology (Completed) | Create All | OK      | Resolve |
    
  @94112_6
  Scenario Outline: Import Application Explorer
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Click on Nodes System Explorer Node in system explorer as '<System>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuItem>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'
    
  @Import_Application_94113
  Examples:
    | MainToolBar          | System   | MainToolBar1         | ApplicationBrowser | ContextMenuItem | ImportFileName      | ExpectedImportMessage | button |
    | Open System Explorer | System_2 | Application Explorer | System_2           | Import          | ApplicationExplorer | Export (Completed)    | OK     |
    
      
  @94112_6
  Scenario Outline: Import Project Explorer
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Click on Nodes System Explorer Node in system explorer as '<System>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I RClick control project browser project browser in project explorer as '<ControlProject>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'
    
  @Export_Application_94113
  Examples:
    | MainToolBar          | System   | MainToolBar1     | ControlProject | ContextMenuItem | ImportFileName  | ExpectedImportMessage      | Button |
    | Open System Explorer | System_2 | Project Explorer | System_2       | Import          | ProjectExplorer | Import Project (Completed) | OK     |