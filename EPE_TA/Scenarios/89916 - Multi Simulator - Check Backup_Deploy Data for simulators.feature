Feature: 89916 - Multi Simulator - Check Backup_Deploy Data for simulators


#Pre-Requisites
#Open system server and start the server
#Open Engineering client once the server is ready
#Crete control project and configure till deployment to the workstation


@TC_EPE_TE_PGSQL_89916_001
Scenario Outline: Right Click on Workstation and click on Backup Data
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<context_menu>'
And I Select controller in context menu as '<controller>'

@right_click_M580_station_node_and_click_backup_data_in_topology_explorer
Examples:
  | SlNo. | node          | context_menu | controller   |
  | 1     | Workstation_1 | Control      | Back Up Data |
  
@right_click_M580_Safety_station_node_and_click_backup_data_in_topology_explorer
Examples:
  | SlNo. | node          | context_menu | controller   |
  | 1     | Workstation_1 | Control      | Back Up Data |


@TC_EPE_TE_PGSQL_89916_002  
Scenario Outline: Select IP and Click on OK Button
When I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Enter Item in Textbox Property Window as '<item_1>'
And I click modal dialog window project browser in project explorer as '<Button>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'

@select_ip_address_M580_and_click_on_OK
Examples:
  | SlNo. | Modal dialog window5 | item_1 | Button | Modal Dialog Window 16                    |
  | 1     | 127.0.0.1:502        | 502    | OK     | MessageBox$$modaldialogwindow1textbox$$OK |
  
@select_ip_address_M580_Safety_and_click_on_OK
Examples:
  | SlNo. | Modal dialog window5 | item_1   | Button | Modal Dialog Window 16                    |
  | 1     | 127.0.0.1:505        | Sample_1 | OK     | MessageBox$$modaldialogwindow1textbox$$OK |


@TC_EPE_TE_PGSQL_89916_003
Scenario Outline:Open refine online and check the build and deploy
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>' 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I selected Dialog OK CE in dialog ce
And I selected List of modified Yes button CE in dialog ce
When I selected Build and Deploy Changes in control expert
And I selected List of modified Yes button CE in dialog ce
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel2>'
When I selected Close Refine Offline in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'

@open_refine_online_and_check_build_and_deploy_in_M580_controler
Examples:
  | SlNo. | node          | context menu | controller    | Modal dialog window5 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 | Modal dialog window1 | Notification Pannel2                 | content                                |
  | 1     | Workstation_1 | Control      | Refine Online | 127.0.0.1:502        | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 | Analog           | BMX AMI 0800     | OK                   | Build and Deploy Changes (Completed) | Close Refine Online Editor (Completed) |

@open_refine_online_and_check_build_and_deploy_in_M580_Safety_controler
Examples:
  | SlNo. | node          | context menu | controller    | Modal dialog window5 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      | Project Browser RO1                             | Dialog Panel CE3 | Dialog Panel CE4 | Modal dialog window1 | Notification Pannel2                 | content                                |
  | 1     | Workstation_1 | Control      | Refine Online | 127.0.0.1:505        | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$4 | Analog           | BMX AMI 0800     | OK                   | Build and Deploy Changes (Completed) | Close Refine Online Editor (Completed) |    


@TC_EPE_TE_PGSQL_89916_004
Scenario Outline: Right Click on Workstation and click on Deploy Data
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<context_menu>'
And I Select controller in context menu as '<controller>'

@right_click_M580_station_node_and_click_deploy_data_in_topology_explorer
Examples:
  | SlNo. | node          | context_menu | controller  |
  | 1     | Workstation_1 | Control      | Deploy Data |
  
@right_click_M580_Safety_station_node_and_click_deploy_data_in_topology_explorer
Examples:
  | SlNo. | node          | context_menu | controller  |
  | 1     | Workstation_1 | Control      | Deploy Data |  
  

@TC_EPE_TE_PGSQL_89916_005
Scenario Outline: Select IP and Click on OK Button
When I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I click modal dialog window project browser in project explorer as '<Button>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
And I click modal dialog window project browser in project explorer as '<Button1>'

@select_ip_and_click_ok_button_in_M580
Examples:
  | SlNo. | Modal dialog window5 | Button | Modal Dialog Window 16                    | Button1 |
  | 1     | 127.0.0.1:502        | OK     | MessageBox$$modaldialogwindow1textbox$$OK | Yes     |
  
@select_ip_and_click_ok_button_in_M580_Safety
Examples:
  | SlNo. | Modal dialog window5 | Button | Modal Dialog Window 16                    | Button1 |
  | 1     | 127.0.0.1:505        | OK     | MessageBox$$modaldialogwindow1textbox$$OK | Yes     | 


@TC_EPE_TE_PGSQL_89916_006  
Scenario Outline: Navigate to Project Explorer from TE to PE
When I Right Click on nodes System_1 in system_1 node as '<System_11>'
Then verify context menu items ContextMenu in system explorer
When I selected Open Project in system_1 node
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

@Navigate_to_Project_Explorer_from_te_to_pe
Examples:
  | SlNo. | System_11 | Explorer tab2    |
  | 1     | System_1  | Project Explorer |
     

@TC_EPE_TE_PGSQL_89916_007  
Scenario Outline: Create a Controller for M580_Standalone
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'

@Create_standalone_Control_Project_1
Examples:
  | SlNo. | project browser1 | context menu           | controller | 
  | 1     | System_1         | Create Control Project | M580       |
  
@Create_standalone_Control_Project_2
Examples:
  | SlNo. | project browser1 | context menu           | controller | 
  | 1     | System_1         | Create Control Project | M580       | 
  
@Create_standalone_Control_Project_3
Examples:
  | SlNo. | project browser1 | context menu           | controller | 
  | 1     | System_1         | Create Control Project | M580       | 
  
@Create_standalone_Control_Project_4_M580_Safety
Examples:
  | SlNo. | project browser1 | context menu           | controller  |
  | 1     | System_1         | Create Control Project | M580_Safety |
  
@TC_EPE_TE_PGSQL_89916_008
Scenario Outline: Right click on the Control Project and navigate to Assignment editor window in CP
When I RClick control project browser project browser in project explorer as '<projectBrowser1>'
And I Select context menu item EC project browser in project explorer as '<projectBrowser2>'
And I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'

@Right_Click_on_ControlProject_1_M580_Standalone_and_click_ASSIGN_FACETS_CP
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |container dock1            |
  | 1     | ControlProject_1 | Assign Facets   |ControlProject_1$$Generate |
  
@Right_Click_on_ControlProject_2_M580_Standalone_and_click_ASSIGN_FACETS_CP
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |container dock1            |
  | 1     | ControlProject_1 | Assign Facets   |ControlProject_1$$Generate |  

@Right_Click_on_ControlProject_3_M580_Standalone_and_click_ASSIGN_FACETS_CP
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |container dock1            |
  | 1     | ControlProject_1 | Assign Facets   |ControlProject_1$$Generate | 
  
@Right_Click_on_ControlProject_4_M580_Safety_and_click_ASSIGN_FACETS_CP
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |container dock1            |
  | 1     | ControlProject_1 | Assign Facets   |ControlProject_1$$Generate |     
  

@TC_EPE_TE_PGSQL_89916_009
Scenario Outline: Map to Controller to respective Workstation
When I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'
And I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'

@Map_controller_1_in_respective_workstation
Examples:
  | SlNo. | project browser3    | project browser4               | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Workstation_1$$ControlExpert_1 | ControlExecutable_1 | Build All        |
  
@Map_controller_2_in_respective_workstation
Examples:
  | SlNo. | project browser3    | project browser4               | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Workstation_1$$ControlExpert_2 | ControlExecutable_1 | Build All        | 
  
@Map_controller_3_in_respective_workstation
Examples:
  | SlNo. | project browser3    | project browser4               | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Workstation_1$$ControlExpert_3 | ControlExecutable_1 | Build All        | 
  
@Map_controller_4_in_respective_workstation_M580_Safety
Examples:
  | SlNo. | project browser3    | project browser4               | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Workstation_1$$ControlExpert_4 | ControlExecutable_1 | Build All        |    
  

@TC_EPE_TE_PGSQL_89916_010
Scenario Outline: Navigation To Topology Explorer from PE to TE
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3      | Explorer tab4     | 
  | 1     | Topology Explorer | Topology Explorer |   
  

@TC_EPE_TE_PGSQL_89916_011  
Scenario Outline: Create multiple Control Service in Workstation folder
When I Right Click on nodes System Explorer Node in system explorer as '<Folder>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

@create_CntrolExpert_1_in_Control_Service
Examples:
  | SlNo. | context menu           | project browser1       | Folder        |
  | 1     | Create Control Service | Create Service Handler | Workstation_1 |
  
@create_CntrolExpert_2_in_Control_Service
Examples:
  | SlNo. | context menu           | project browser1       | Folder        |
  | 1     | Create Control Service | Create Service Handler | Workstation_1 | 
  
@create_CntrolExpert_3_in_Control_Service
Examples:
  | SlNo. | context menu           | project browser1       | Folder        |
  | 1     | Create Control Service | Create Service Handler | Workstation_1 |
  
@create_CntrolExpert_4_in_Control_Service_M580_Safety
Examples:
  | SlNo. | context menu           | project browser1       | Folder        |
  | 1     | Create Control Service | Create Service Handler | Workstation_1 |     
  

@TC_EPE_TE_PGSQL_89916_012
Scenario Outline:Tests with multi simulators Capabilities
When I Double Click open the '<node>' in Topology Explorer
And I Double Click open the '<ethernet network>'
And I Expand Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I Perform action on the Folder by Clicking on '<button>' in Topology Explorer

@create_control_expert1_and_assign_port_502_TE
Examples:
  | SlNo. | node          | ethernet network | Topology Explorer Tree2 | item_1 | button               |
  | 1     | Workstation_1 | ControlExpert_1  | Configuration           | 502    | Workstation_1$$Close |
  
@create_control_expert2_and_assign_port_503_TE
Examples:
  | SlNo. | node          | ethernet network | Topology Explorer Tree2 | item_1 | button               |
  | 1     | Workstation_1 | ControlExpert_2  | Configuration           | 503    | Workstation_1$$Close | 
  
@create_control_expert3_and_assign_port_504_TE
Examples:
  | SlNo. | node          | ethernet network | Topology Explorer Tree2 | item_1 | button               |
  | 1     | Workstation_1 | ControlExpert_3  | Configuration           | 504    | Workstation_1$$Close | 
  
@create_control_expert4_and_assign_port_505_TE_M580_safety
Examples:
  | SlNo. | node          | ethernet network | Topology Explorer Tree2 | item_1 | button               |
  | 1     | Workstation_1 | ControlExpert_4  | Configuration           | 505    | Workstation_1$$Close |    
  

@TC_EPE_TE_PGSQL_89916_013
Scenario Outline: Start PLC Simulator and change the port numbers
When I Run PLC Simulator
And I click on Start button on PLC Simulator 
And I change port number of simulator to 503
And I click on Start button on PLC Simulator 
And I change port number of simulator to 504
And I click on Start button on PLC Simulator
And I change port number of simulator to 505
And I click on Start button on PLC Simulator

@change_the_port_number_503
Examples:
  | SlNo. |
  | 1     |  
  
@change_the_port_number_504
Examples:
  | SlNo. |
  | 1     |  
  
@change_the_port_number_505_M580_Safety
Examples:
  | SlNo. |
  | 1     |   
  
@TC_EPE_TE_PGSQL_89916_014
Scenario Outline: Deploy the controller from workstation
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
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_the_CP1_to_Workstation_1__Slot_NIC_1{127.0.0.1:502}_Simulator
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$ControlProject_1 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:502} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |
  
@Deploy_the_CP2_to_Workstation_1__Slot_NIC_1{127.0.0.1:503}_Simulator
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$ControlProject_2 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:503} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |

@Deploy_the_CP3_to_Workstation_1__Slot_NIC_1{127.0.0.1:504}_Simulator
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$ControlProject_3 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:504} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |
  
@Deploy_the_CP4_to_Workstation_1__Slot_NIC_1{127.0.0.1:505}_Simulator_M580_Safety
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$ControlProject_4 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:505} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |        