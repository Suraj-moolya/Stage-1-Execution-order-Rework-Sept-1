Feature: 89914 - Multi simulator-Check the Deploy changes for the Work station having multiple control services

#Tags - @Create_Workstation_1

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
  
Scenario Outline: Create NIC in Workstation
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
#When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

@Create_NIC_in_Workstation
Examples:
  | SlNo. | context menu | project browser1       | button               |
  | 1     | Create NIC   | Create Service Handler | Workstation_1$$Close |
  
  
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
  
@Add_IP_Address_to_NIC_2
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Topology Explorer Tree4 | identifier |
  | 1     | NIC_2                   | NIC Parameters          | IPAddress$$127.0.0.1    | SubnetMask$$255.255.0.0 | NIC        |

Scenario Outline: Modify the Control Expert port in workstation
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
When I Close the Tab by Clicking on Close as '<identifier>'
  
@Add_Port_510_to_ControlExpert_1
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | identifier      |
  | 1     | ControlExpert_1         | Configuration           | Port$$510               | ControlExpert_1 |
  
@Add_Port_511_to_ControlExpert_2
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | identifier      |
  | 1     | ControlExpert_2         | Configuration           | Port$$511               | ControlExpert_2 |
  

Scenario Outline: Open Service Mapping Editor of M580_Standalone and map to Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'
@Map_Workstation_1_ControlExpert_1_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | M580_Standalone  | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_1] |
  
@Map_Workstation_1_ControlExpert_2_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | M580_Standalone2 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 [ControlExpert_2] |
  
@Map_M580_Safety_in_ControlExecutable_1
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                |
  | 1     | M580_Safety      | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Safety |
  
@Map_Workstation_1_ControlExpert_1_in_ControlExecutable_2
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | M580_Safety      | Executable       | ControlExecutable_2 | ControlExecutive_1$$Workstation_1 [ControlExpert_1] |
  
@Map_M580_Safety2_in_ControlExecutable_1
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                 |
  | 1     | M580_Safety2     | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Safety2 |
  
@Map_Workstation_1_ControlExpert_2_in_ControlExecutable_2
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                                    |
  | 1     | M580_Safety2     | Executable       | ControlExecutable_2 | ControlExecutive_1$$Workstation_1 [ControlExpert_2] |
  
  
Scenario Outline: Change safety settings of Workstation to Enable
When I Right Click on nodes System Explorer Node in system explorer as '<Workstation>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
@Change_safety_settings_of_Workstation_1_to_Enable
Examples:
  | SlNo. | context menu | options         | Workstation   |
  | 1     | Properties   | Simulator$$True | Workstation_1 |
  
  
Scenario Outline: Set Password for Simulator
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select controller in context menu as '<sub_context_menu>'
And I Select button in the modal dialoge window as 'OK'
And I Enter pssword in '<password1>' field in Controller password grid popup
And I Enter pssword in '<password2>' field in Controller password grid popup
And I click modal dialog window project browser in project explorer as '<Button>'
And I Wait for Circular Progress Bar To Complete in system explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
@Set_Password_for_Simulator
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | sub_context_menu | controlservice  | password1            | password2                    | Button | project browser2                                            |
  | 1     | Workstation_1 | Control                 | Manage Password  | ControlExpert_1 | Password$$Moolya@123 | Confirm Password$$Moolya@123 | OK     | Manage Password Workstation_1 [ControlExpert_1] (Completed) |

@Set_Password_for_Simulator_ControlExpert_2
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | sub_context_menu | controlservice  | password1            | password2                    | Button | project browser2                                            |
  | 1     | Workstation_1 | Control                 | Manage Password  | ControlExpert_2 | Password$$Moolya@123 | Confirm Password$$Moolya@123 | OK     | Manage Password Workstation_1 [ControlExpert_2] (Completed) |
   
Scenario Outline: Deploy the Simulator after enabling the password
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select controller in context menu as '<sub_context_menu>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Enter the application password that has been set for the engine'
When I Enter Controller Password deploy screen TE Confirm Password box in topology as '<Password box3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_Simulator_after_enabling_password
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     | Password box3 |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:502} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project | Moolya@123    |
 
@Deploy_Simulator2_after_enabling_password_NIC_2
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     | Password box3 |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$M580_Standalone2 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_2 {127.0.0.1:503} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project | Moolya@123    |
   
  
Scenario Outline: Do modifications in CP Refine
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'

Examples:
  | SlNo. | System Project1              | System Project2 |
  | 1     | Programs$$Tasks$$MAST$$Logic | New Section ... |
  
Scenario Outline: enter variable and select HMI option under Data Editor window when the table is blank
When I Enter Variable name and select HMI option under Data Editor window '<name>'
Examples:
  | SlNo. | name   |
  | 1     | Moolya |
  
Scenario Outline: Save and Close CE
When I wait in seconds Refine online window in refine offline
And I selected Save Refine Offline in refine offline
And I wait in seconds Refine online window in refine offline
And I selected Close Refine Offline in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'
@Save_and_Close_CP_Refine_Offline
Examples:
  | SlNo. | content                                  |
  | 1     | Close Control Project Editor (Completed) |
  
  
Scenario Outline: Deploy Changes for Simulator
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select controller in context menu as '<sub_context_menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
When I selected Rename Pop up Ok in message box
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'

@Deploy_Changes_for_Simulator
Examples:
  | SlNo. | sub_context_menu                     | project browser3                                 | Controller    | Topology Explorer Tree1 |
  | 1     | Deploy Changes / Undo Online Changes | Deploy Changes / Undo Online Changes (Completed) | Workstation_1 | Control                 |
  
  
Scenario Outline: Open refine online of Simulator
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Open_refine_online_of_Simulator_M580Standalone2_NIC_2
Examples:
  | SlNo. | Controller    | context menu | sub_context_menu | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window5       | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      |
  | 1     | Workstation_1 | Control      | Refine Online    | Topology$$projectdropdowntextbox$$M580_Standalone2 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | Slot NIC_2 {127.0.0.1:503} | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) |
  
@Open_refine_online_of_Simulator_M580Safety_NIC_1
Examples:
  | SlNo. | Controller    | context menu | sub_context_menu | project dropdown2                             | Executables dropdown3                                     | Modal dialog window5       | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      |
  | 1     | Workstation_1 | Control      | Refine Online    | Topology$$projectdropdowntextbox$$M580_Safety | Topology$$executablesdropdowntextbox$$ControlExecutable_2 | Slot NIC_1 {127.0.0.1:510} | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) |
  
@Open_refine_online_of_Simulator_M580Safety2_NIC_1
Examples:
  | SlNo. | Controller    | context menu | sub_context_menu | project dropdown2                              | Executables dropdown3                                     | Modal dialog window5       | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      |
  | 1     | Workstation_1 | Control      | Refine Online    | Topology$$projectdropdowntextbox$$M580_Safety2 | Topology$$executablesdropdowntextbox$$ControlExecutable_2 | Slot NIC_1 {127.0.0.1:511} | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) |
  

  
  
  
#######################################################################################################################################
#Execution order for TC_89914
##############################################################################

#Tags - @Create_Workstation_1
#Tags - @Create_OFS_2Control_Service_for_Workstation_1
#Tags - @Create_NIC_in_Workstation
#Tags - @Add_IP_Address_to_NIC_1
#Tags - @Add_IP_Address_to_NIC_2
#Tags - @Close_Workstation_1_in_Topology_Explorer
#Scenarios\55 Map the EPE devices to controller - Map Workstion to Ethernet Network
#Tags - @Change_safety_settings_of_Workstation_1_to_Disable
#Tags - @Close_Workstation_1_in_Topology_Explorer
#Scenarios\EnginneringClient - Navigation To Application Explorer(AE) - Main Tool Bar
#Tags - @Templates_for_builds_before_6334
#Scenarios\EnginneringClient - Navigation To Project Explorer(PE) - Main Tool Bar
#Tags - @Create_standalone_Control_Project_1
#Tags - @Double_Click_Containers
#Tags - @Assign_Instance_from_system_to_different_Containers_in_PE
#Tags - @Map_Workstation_1_ControlExpert_1_in_ControlExecutable
#Scenarios\146 Build_Build all the existing executable(if any errors found, clear and build) - Generate and Build from  executeable r-click
#Tags - @Right_Click_M580_Standalone_Collapse_All
#Tags - @Create_standalone_Control_Project_2
#Tags - @Double_Click_Containers
#Tags - @Assign_Instance_from_system_to_M580_Standalone2_Containers_in_PE
#Tags - @Map_Workstation_1_ControlExpert_2_in_ControlExecutable
#Scenarios\146 Build_Build all the existing executable(if any errors found, clear and build) - Generate and Build from  executeable r-click
#Tags - @Right_Click_M580_Standalone2_Collapse_All
#Tags - @Right_Click_M580_Standalone_ExpandAll
#Scenarios\EnginneringClient - Navigation To Topology Explorer(TE) - Main Tool Bar
#Scenarios\XX PLCSimulator - Start PLC Simulator
#Tags - @Deploy_the_Workstation_1_after_disabling_the_password__Slot_NIC_1{127.0.0.1:502}_Simulator
#Tags - @Change_safety_settings_of_Workstation_1_to_Enable
#Tags - @Close_Workstation_1_in_Topology_Explorer
#Tags - @Set_Password_for_Simulator
#Tags - @Deploy_Simulator_after_enabling_password
#Scenarios\EnginneringClient - Navigation To Project Explorer(PE) - Main Tool Bar
#Tags - @Open_Refine_offline_of_M580_Standalone_from_Context_Menu
#Tags - @Double_click_on_Elementary_variables_with_path_Variables_&_FB_instances
#Tags - @Create_consecutivevariable_as_Moolya   
#Tags - @Save_and_Close_CP_Refine_Offline
#Scenarios\146 Build_Build all the existing executable(if any errors found, clear and build) - Generate and Build from  executeable r-click
#Scenarios\EnginneringClient - Navigation To Topology Explorer(TE) - Main Tool Bar
#Tags - @Deploy_Changes_for_Simulator
#Scenarios\XX PLCSimulator - Change port number of simulator to 503
#Tags - @Set_Password_for_Simulator_ControlExpert_2
#Tags - @Deploy_Simulator2_after_enabling_password_NIC_2
#Tags - @close_Project_explorer
#Tags - @Open_refine_online_of_Simulator_M580Standalone2_NIC_2
#Tags - @Double_click_on_Elementary_variables_with_path_Variables_&_FB_instances   