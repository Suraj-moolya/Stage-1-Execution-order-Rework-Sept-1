Feature: 89912 - Multi simulator-Check the safety and maintenance mode switching in refine online for workstation incase safety password is disabled

Scenario Outline: Create a Control Project for M580_Safety
When I Right Click on nodes System Explorer Node in system explorer as 'Controllers'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
@Create_M580_Safety2_Controller
Examples:
  | SlNo. | context menu      | controller  | controller_name | project browser1  | project browser2  |
  | 1     | Create Controller | M580 Safety | M580_Safety2    | Create Controller | Update Controller |
  
  
Scenario Outline: Change safety settings of controller to Disable
When I Right Click on nodes System Explorer Node in system explorer as '<Controller name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Select button in the modal dialoge window as '<Button name>'

@Change_safety_settings_of_M580_Safety_controller_to_Disable
Examples:
  | SlNo. | context menu | options       | Button name | Controller name |
  | 1     | Properties   | Safety$$False | Yes         | M580_Safety     |
 
@Change_safety_settings_of_M580_Safety2_controller_to_Disable 
Examples:
  | SlNo. | context menu | options       | Button name | Controller name |
  | 1     | Properties   | Safety$$False | Yes         | M580_Safety2    |
  
@Change_controller_password_settings_of_M580_Safety_to_Disable
Examples:

  | SlNo. | context menu | options           | Button name | Controller name |
  | 1     | Properties   | Controller$$False | Yes         | M580_Safety     |
 
@Change_controller_password_settings_of_M580_Safety2_to_Disable 
Examples:
  | SlNo. | context menu | options           | Button name | Controller name |
  | 1     | Properties   | Controller$$False | Yes         | M580_Safety2    |
  
  
Scenario Outline: Map EtherNet Network to Controller
When I Right Click on nodes System Explorer Node in system explorer as '<Topology Explorer Tree1>'
And I Select context menu item EC project browser in project explorer as '<Topology Explorer Tree2>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
When I click modal dialog window project browser in project explorer as '<Button>'

@Map_EtherNet_Network_to_M580_Safety
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3   | Topology Explorer Tree4   | Button |
  | 1     | M580_Safety             | Physical Connections    | M580_Safety 0$$SE_Network | M580_Safety 2$$SE_Network | OK     |
  
@Map_EtherNet_Network_to_M580_Safety2
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3    | Topology Explorer Tree4     | Button |
  | 1     | M580_Safety2            | Physical Connections    | M580_Safety2 0$Lab_Network | M580_Safety2 2$$Lab_Network | OK     |
  
  
Scenario Outline: Close Controllers  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
@Close_Controllers_in_Topology_Explorer__M580_Safety2
Examples:
  | SlNo. | button              | FolderName  |
  | 1     | M580_Safety2$$Close | Controllers |
  
  
Scenario Outline: Open Configuration window of Controller
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<Notification>'

@open_Configuration_window_of_Controller_M580_Safety2
Examples:
  | SlNo. | Controller   | context menu | Notification          |
  | 1     | M580_Safety2 | Configure    | Open Configure Editor |
  

Scenario Outline: Create control executeable
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I enterkey Project Browser RO in refine offline
Then Verify Action message in notification pannel project browser in project explorer as '<Notification>'

@Create_control_executeable
Examples:
  | SlNo. | project browser1 | project browser2  | Notification                  |
  | 1     | Executables      | Create Executable | Create Executable (Completed) |
  
  
Scenario Outline: Generate and Build from  executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'

@Generate_and_Build_ControlExecutable_2
Examples:
  | SlNo. | project browser1    | project browser2   | project browser3 |
  | 1     | ControlExecutable_2 | Generate and Build | OK               |


Scenario Outline: Switch to Maintenance mode in Refine Online
When I click on the Switch to Maintenance Mode button in Refine Online window
@Click_on_Maintenance_mode_button_in_Refine_Online
Examples:
  | SlNo. |
  | 1     |
  
Scenario Outline: Switch to Safety mode in Refine Online
When I click on the Switch to Safety Mode button in Refine Online window
@Click_on_Safety_mode_button_in_Refine_Online
Examples:
  | SlNo. |
  | 1     |
  
Scenario Outline: Verify Maintenance mode in Refine Online
Then I verify the Maintenance Mode button in Refine Online window
@Verify_Maintenance_mode_status_in_Refine_Online
Examples:
  | SlNo. |
  | 1     |
  
Scenario Outline: Verify Safety mode in Refine Online
Then I verify the Safety Mode button in Refine Online window
@Verify_Safety_mode_status_in_Refine_Online
Examples:
  | SlNo. |
  | 1     |
  
  
  
  
  
#######################################################################################################################################
#Execution order for TC_89912
##############################################################################

#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Create a Control Project for M580_Safety
#Tags - @Change_safety_settings_of_M580_Safety_controller_to_Disable
#Tags - @Close_Controllers_in_Topology_Explorer__M580_Safety
#Tags - @open_Configuration_window_of_Controller_M580_Safety
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Unlock Security of 4th gen M580 controller
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Double click on PLC Bus
#Tags - @Change_CPU_Version_of_controller__BME_P58_4040S_03.30
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Close PLC Bus Window in TM
#Scenarios\66 Do some modification in configure and deploy the project to controller - Save and Close configuration without configuration pop up
#Tags - @Change_controller_password_settings_of_M580_Safety_to_Disable
#Tags - @Close_Controllers_in_Topology_Explorer__M580_Safety
#Tags - @Map_EtherNet_Network_to_M580_Safety
#Tags - @Create_M580_Safety2_Controller
#Tags - @Change_safety_settings_of_M580_Safety2_controller_to_Disable
#Tags - @Close_Controllers_in_Topology_Explorer__M580_Safety2
#Tags - @open_Configuration_window_of_Controller_M580_Safety2
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Unlock Security of 4th gen M580 controller
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Double click on PLC Bus
#Tags - @Change_CPU_Version_of_controller__BME_P58_4040S_03.30
#Scenarios\50 Configure controllers like standalone & HSBY M580_M580 safety_M340_Quantum - Close PLC Bus Window in TM
#Scenarios\66 Do some modification in configure and deploy the project to controller - Save and Close configuration without configuration pop up
#Tags - @Change_controller_password_settings_of_M580_Safety2_to_Disable
#Tags - @Close_Controllers_in_Topology_Explorer__M580_Safety2
#Tags - @Map_EtherNet_Network_to_M580_Safety2
#Tags - @Create_Workstation_1
#Tags - @Create_OFS_2Control_Service_for_Workstation_1
#Tags - @Add_Port_510_to_ControlExpert_1
#Tags - @Add_Port_511_to_ControlExpert_2
#Tags - @Close_Workstation_1_in_Topology_Explorer
#Scenarios\55 Map the EPE devices to controller - Map Workstion to Ethernet Network
#Tags - @Change_safety_settings_of_Workstation_1_to_Disable
#Tags - @Close_Workstation_1_in_Topology_Explorer
#Scenarios\EnginneringClient - Navigation To Application Explorer(AE) - Main Tool Bar
#Tags - @Templates_for_builds_before_6334
#Scenarios\EnginneringClient - Navigation To Project Explorer(PE) - Main Tool Bar
#Tags - @Rename_controller_M580_Safety
#Tags - @Right_Click_M580_Safety_ExpandAll
#Tags - @Double_Click_Containers
#Tags - @Assign_Instance_from_system_to_M580_Safety_Containers_in_PE
#Tags - @Create_control_executeable
#Tags - @Map_M580_Safety_in_ControlExecutable_1
#Tags - @Map_Workstation_1_ControlExpert_1_in_ControlExecutable_2
#Scenarios\146 Build_Build all the existing executable(if any errors found, clear and build) - Generate and Build from  executeable r-click
#Tags - @Generate_and_Build_ControlExecutable_2
#Tags - @Right_Click_M580_Safety_Collapse_All
#Tags - @Rename_controller_M580_Safety2
#Tags - @Right_Click_M580_Safety2_ExpandAll
#Tags - @Double_Click_Containers
#Tags - @Assign_Instance_from_system_to_M580_Safety2_Containers_in_PE
#Tags - @Create_control_executeable
#Tags - @Map_M580_Safety2_in_ControlExecutable_1
#Tags - @Map_Workstation_1_ControlExpert_2_in_ControlExecutable_2
#Scenarios\146 Build_Build all the existing executable(if any errors found, clear and build) - Generate and Build from  executeable r-click
#Tags - @Generate_and_Build_ControlExecutable_2
#Scenarios\EnginneringClient - Navigation To Topology Explorer(TE) - Main Tool Bar
#Scenarios\XX PLCSimulator - Open PLC Simulator
#Tags - @Change_the_Simulator_port_to_510
#Tags - @Change_the_Simulator_port_to_511
#Tags - @Deploy_the_Workstation_1_after_disabling_the_password__Slot_NIC_1{127.0.0.1:510}_Simulator
#Tags - @Deploy_the_Workstation_1_after_disabling_the_password__NIC_1{127.0.0.1:511}_Simulator
#Tags - @close_Project_explorer
#Tags - @Open_refine_online_of_Simulator_M580Safety_NIC_1
#Tags - @Click_on_Maintenance_mode_button_in_Refine_Online
#Tags - @Verify_Maintenance_mode_status_in_Refine_Online
#Tags - @Click_on_Safety_mode_button_in_Refine_Online
#Tags - @Verify_Safety_mode_status_in_Refine_Online
#Scenarios\78 Open refine online and check the build and deploy functionality - Close Refine online window and yes on popup
#Tags - @Open_refine_online_of_Simulator_M580Safety2_NIC_1
#Tags - @Click_on_Maintenance_mode_button_in_Refine_Online
#Tags - @Verify_Maintenance_mode_status_in_Refine_Online
#Tags - @Click_on_Safety_mode_button_in_Refine_Online
#Tags - @Verify_Safety_mode_status_in_Refine_Online
#Scenarios\78 Open refine online and check the build and deploy functionality - Close Refine online window and yes on popup


##########################################################################################################################################################
  
