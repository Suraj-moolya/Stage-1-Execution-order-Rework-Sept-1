Feature: 94112 - To Test the Import with M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)

  @94112_1
  Scenario Outline: Export Controller
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I click modal dialog window Instance editor save in application explorer as 'OK'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Export_Controller
    Examples:
      | Controllers     | context menu | sub_context_menu | ExportFileName | ExportFileFormat | ExpectedExportMessage       |
      | M580_Standalone | Export       | Topology         | Controller     | .sbk             | Export Topology (Completed) |

  @94112_2
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

    @Import_Controller_Update
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

    @Import_Controller_Skip
    Examples:
      | Controllers | context menu | sub_context_menu | ImportFileName | ExpectedExportMessage       | button   | button1 | button2 |
      | System_1    | Import       | Topology         | Controller     | Import Topology (Completed) | Skip All | OK      | Resolve |

  @94112_2
  Scenario Outline: Import Controller - Create
    When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<sub_context_menu>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I click modal dialog window project browser in project explorer as '<button2>'
    And I click modal dialog window project browser in project explorer as '<button>'
    And I click modal dialog window project browser in project explorer as '<button1>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

    @Import_Controller_Create
    Examples:
      | Controllers | context menu | sub_context_menu | ImportFileName | ExpectedExportMessage       | button     | button1 | button2 |
      | System_1    | Import       | Topology         | Controller     | Import Topology (Completed) | Create All | OK      | Resolve |
    
  @94112_6
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

  @Export_Topology
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
    
  @Export_Application
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
    
  @Export_ProjectExplorer
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
  
  @Create_System_with_Password  
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
    
  @Navigate_TE_selecting_system2_and_ImportController
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
    
  @Import_Application
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
    
  @Export_Application
  Examples:
    | MainToolBar          | System   | MainToolBar1     | ControlProject | ContextMenuItem | ImportFileName  | ExpectedImportMessage      | Button |
    | Open System Explorer | System_2 | Project Explorer | System_2       | Import          | ProjectExplorer | Import Project (Completed) | OK     |
    
  @94112_5
  Scenario Outline: Add Communication Modules in PLC
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Right Click on nodes System Explorer Node in system explorer as '<ControllerNode>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem>'
    And I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowserPath>'
    And I enterkey Project Browser RO in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_Main>'
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_Child>'
    And I selected Dialog OK CE in dialog ce
    And I selected List of modified Yes button CE in dialog ce
    And I selected Dialog OK CE in dialog ce
    And I wait in seconds Refine online window in refine offline
    And I close PLC Bus window in controller configuration window
    And I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowser1>'
    And I edit IP Address in configure MDI Window in refine offline as '<MainIp>'
    And I edit IP Address in configure MDI Window in refine offline as '<Gateway>'
    And I close PLC Bus window in controller configuration window
    And I selected List of modified Yes button CE in dialog ce
    And I selected Save Refine Offline in refine offline
    And I click modal dialog window Modal dialog window in message box as '<FinalButton>'
    And I wait in seconds Refine online window in refine offline
    And I selected Close Refine Offline in refine offline
    Then Verify Action message in notification pannel container dock in project explorer as '<NotificationMessage>'
    
  @Add_Communication_Module_And_Set_IP_in_Configuration
  Examples:
    | ProjectBrowser1                                                  | MainIp                          | Gateway                | MainToolBar       | ControllerNode  | ContextMenuItem | ProjectBrowserPath                              | DialogPanel_Main | DialogPanel_Child | ConfirmationButton | NotificationMessage                | FinalButton |
    | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$3 : BME NOC 0311.4 | Main IP address$$182.233.63.105 | Gateway$$182.233.0.254 | Topology Explorer | M580_Standalone | Configure       | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$3 | Communication    | BME NOC 0311.4    | Yes                | Close Configure Editor (Completed) | OK          |
   
  @94112_5
  Scenario Outline: Add EIO Drops and Communication Modules
    When I Right Click on nodes System Explorer Node in system explorer as '<ControllerNode>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem>'
    When I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowserPath1>'
    And I Rclick Drops EIO add new device CE FBD SectionWindow in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_AddDrop>'
    And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_DeviceType>'
    And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<DialogList_Device>'
    And I selected Dialog OK CE in dialog ce
    And I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowserPath2>'
    And I enterkey Project Browser RO in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_AddDrop2>'
    And I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowserPath3>'
    And I enterkey Project Browser RO in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_Main>'
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_Module>'
    And I Navigate through project browser CE Project Browser RO in refine offline as '<ProjectBrowserPath4>'
    And I enterkey Project Browser RO in refine offline
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_DeviceType2>'
    And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<DialogPanel_Module2>'
    And I selected Save Refine Offline in refine offline
    And I click modal dialog window Modal dialog window in message box as '<FinalButton>'
    And I wait in seconds Refine online window in refine offline
    And I selected Close Refine Offline in refine offline
    Then Verify Action message in notification pannel container dock in project explorer as '<NotificationMessage>'
  
  @Add_Communication_Modules_in_EIO_Drops
  Examples:
    | ControllerNode  | ContextMenuItem | ProjectBrowserPath1        | DialogPanel_AddDrop | DialogPanel_DeviceType | DialogList_Device | ProjectBrowserPath3                                                   | DialogPanel_Main | DialogPanel_Module | ConfirmationButton | FinalButton | NotificationMessage                | ProjectBrowserPath2                                                     | DialogPanel_AddDrop2 | ProjectBrowserPath4                                                   | DialogPanel_DeviceType2 | DialogPanel_Module2 |
    | M580_Standalone | Configure       | Configuration$$2 : EIO Bus | .X80 remote drop    | BMX XBP 1200           | BME CRA 313 10    | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BMX XBP 1200$$1 | Communication    | BMX NOM 0200.4     | Yes                | OK          | Close Configure Editor (Completed) | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BMX XBP 1200$$(P) | BMX CPS 3500         | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BMX XBP 1200$$2 | Analog                  | BMX AMI 0810        |
  
  
  @94112_5A
  Scenario Outline: Generate and Build
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I RClick control project browser project browser in project explorer as '<ControlProject1>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem1>'
    And I RClick control project browser project browser in project explorer as '<ControlProject2>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenuItem2>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify notification panel message Notification Pannel in message box as '<Message>'
  
  @Generate_and_Build_After_Adding_module  
  Examples:
    | MainToolBar      | ControlProject1 | ContextMenuItem1 | ControlProject2     | ContextMenuItem2   | Message                                           | Button |
    | Project Explorer | M580_Standalone | Expand All       | ControlExecutable_1 | Generate and Build | Generate and Build Control Executable (Completed) | OK     |
   
  @94112_6
  Scenario Outline: Deploy the controller 
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

  @Deploy_the_controller__182.233.63.5__M580_Standalone
  Examples:
    | MainToolBar       | ControllerNode  | TopologyExplorerOption | ProjectDropdown                                   | ExecutablesDropdown                                       | ConfirmationDialog | TargetIPAddress | Protocol | Password    | FinalDialogButton                         | NotificationMessage              |
    | Topology Explorer | M580_Standalone | Deploy Built Project   | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                 | 182.233.63.5    | HTTPS    | Schneider0! | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |