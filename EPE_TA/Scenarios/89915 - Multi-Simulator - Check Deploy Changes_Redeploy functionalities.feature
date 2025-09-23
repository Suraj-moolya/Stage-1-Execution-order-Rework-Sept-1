Feature: 89915 - Multi-Simulator - Check Deploy Changes_Redeploy functionalities

Scenario Outline: Create a Control Project for M580_Standalone
When I Right Click on nodes System Explorer Node in system explorer as '<Folder Name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

@Create_First_Controller_for_standlone
Examples:
  | SlNo. | Folder Name | context menu      | controller | project browser1  |
  | 1     | System_7    | Create Controller | M580       | Create Controller |
  
  
Scenario Outline: Create OFS,Control Service in Workstation
When I Right Click on nodes System Explorer Node in system explorer as '<Folder>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'


@Create_OFS_2Control_Service_for_Workstation_1
Examples:
  | SlNo. | context menu           | project browser1       | Folder        |
  | 1     | Create OFS             | Create Service Handler | Workstation_1 |
  | 2     | Create Control Service | Create Service Handler | Workstation_1 |
  | 3     | Create Control Service | Create Service Handler | Workstation_1 |
  | 4     | Create Supervision     | Create Service Handler | Workstation_1 |

    
Scenario Outline: Modify the IP address after mapping to workstation
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
When I Close the Tab by Clicking on Close as '<identifier>'

@Add_IP_Address_to_NIC_1
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Topology Explorer Tree4 | identifier |
  | 1     | NIC_1                   | NIC Parameters          | IPAddress$$127.0.0.1    | SubnetMask$$255.255.0.0 | NIC        |
  
  
Scenario Outline: Assign Control Executables to Control Project with respect to Control Service
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

@Map_Workstation_1_ControlExpert_1_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | ControlProject_1 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_1] |
  
@Map_Workstation_1_ControlExpert_2_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | ControlProject_2 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_2] |
  
  
Scenario Outline: Try changing Control Expert_1 with Control Expert_2 in service mapping after deployment
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser5>'
And I Expand control project browser PE project browser in project explorer as '<project browser6>'
And I Dclick Control project broswer project browser in project explorer as '<project browser7>'
And I Control executable dropdown PE project browser in project explorer as '<project browser8>'
Then Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 1>'
When I click modal dialog window project browser in project explorer as '<Button>'

@Map_Workstation_1_ControlExpert_2_to_Stanalone_580
Examples:
  | SlNo. | project browser5 | project browser6 | project browser7    | project browser8                                    | Modal Dialog Window 1 | Button |
  | 1     | ControlProject_1 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_2] | Unable to modify      | OK     |
  

Scenario Outline:Delete ControlExecutable Standalone and assign Control Expert_2 in service mapping
When I Close the Tab by Clicking on Close as '<tabname>'
And I RClick control project browser project browser in project explorer as '<project browser9>'
And I Select context menu item EC project browser in project explorer as '<project browser10>'
And I click the button '<button>' in the CE Conflict Window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser11>'

Examples:
  | SlNo. | project browser9    | project browser10 | tabname             | button | Modal dialog window1 | project browser11             |
  | 1     | ControlExecutable_1 | Delete            | ControlExecutable_1 | Yes    | Yes                  | Delete Executable (Completed) |
  
Scenario Outline:Create ControlExecutable Standalone and assign ControlExoert in service mapping 
When I RClick control project browser project browser in project explorer as '<project browser12>'
And I Select context menu item EC project browser in project explorer as '<project browser13>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser14>'
When I Dclick Control project broswer project browser in project explorer as '<project browser15>'
And I Control executable dropdown PE project browser in project explorer as '<project browser16>'
Then Verify Action message in notification pannel project browser in project explorer as '<Message1>'

Examples:
  | SlNo. | project browser12 | project browser13 | project browser14             | project browser15   | project browser16                                   | Message1                           |
  | 1     | Executables       | Create Executable | Create Executable (Completed) | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_2] | Map Service Executable (Completed) |
  
  
Scenario Outline: Build the executable after mapping
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click the button '<button>' in the CE Conflict Window
Then Verify Action message in notification pannel project browser in project explorer as '<Message1>'

Examples:
  | SlNo. | project browser1    | project browser2   | button | Message2                                          |
  | 1     | ControlExecutable_1 | Generate and Build | OK     | Generate and Build Control Executable (Completed) |
  


Scenario Outline: Modify the sections in refine offline,delete link and rebuild
When I Navigate through project browser CE Project Browser RO in refine offline as '<Navigation1>'
And I RClick on Block Refine Offline project browser in project explorer as '<project browser1>'
And I selected Unlock in refine offline
And I select '<button>' in New Device PopUp Window
And I Delete link Refine Offline Unlock in refine offline as 'ChOut'

@Unlock_for_AnalogOutPut
Examples:
  | SlNo. | Navigation1                                | project browser1 | button |
  | 1     | Programs$$Tasks$$MAST$$Logic$$FBDSection_1 | AOUTPUTGP        | Yes    |
  
  
#@create_system_without_password
#@Create_WS_and_Controller_M580_Standalone
#@Create_2Control_Service_OFS_Supervision
#@Craete_Logical_netwotrk_and_map_Workstation
#@AE_add_instnaces_and_make_them_valid
#@PE_Create_2CP_standalone_and_safety
#@Assign_instances_to_container_and_map_CS1_and_CS2_respectively_to_CP
#@Create_FBD_add_AO_and_AI
#@generate_and_build_deploy_both_Cp_with_Workstation
#@Redeploy_built_project_for_non_safety_CP
#@Open_refine_offline_for_built_project_non_safety_cp_do_modifications 
#@BUILD_Project_Configuration_window
#@save and close refine window
#@redeployProject 
#try with Safety Controller as well