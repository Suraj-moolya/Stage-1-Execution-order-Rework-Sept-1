Feature: 95246 - Verify Creation and Configuration of M580,M340 and Quantum Controller.


@TC_EPE_TE_PGSQL_95246_001
Scenario Outline: Create a Controllers for M580 and M580_Safety.
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@create_Controller_for_M580_under_System_1
Examples:
  | SlNo. | context menu      | controller | controller_name | project browser1  | project browser2  | node     |
  | 1     | Create Controller | M580       | M580            | Create Controller | Update Controller | System_1 |

@create_Controller_for_M580_Safety_under_System_1  
Examples:
  | SlNo. | context menu      | controller  | controller_name | project browser1  | project browser2  |node     |
  | 1     | Create Controller | M580 Safety | M580_Safety     | Create Controller | Update Controller |System_1 |  
  
@create_Controller_for_M340_under_System_1  
Examples:
  | SlNo. | context menu      | controller | controller_name | project browser1  | project browser2  | node     |
  | 1     | Create Controller | M340       | M340            | Create Controller | Update Controller | System_1 |
  
@create_Controller_for_Quantum_controller_System_1  
Examples:
  | SlNo. | context menu      | controller | controller_name | project browser1  | project browser2  | node     |
  | 1     | Create Controller | Quantum    | Quantum         | Create Controller | Update Controller | System_1 |
  

@TC_EPE_TE_PGSQL_95246_002
Scenario Outline: open the Configuration window for Controllers
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<item>'

@open_configuration_window_for_M580_under_controller
Examples:
  | SlNo. | item      | node |
  | 1     | Configure | M580 |
  
@open_configuration_window_for_M580_Safety_under_controller
Examples:
  | SlNo. | item      | node        |
  | 1     | Configure | M580 Safety |
  
@open_configuration_window_for_M340_under_controller
Examples:
  | SlNo. | item      | node |
  | 1     | Configure | M340 |  
  
@open_configuration_window_for_Quantum_controller
Examples:
  | SlNo. | item      | node    |
  | 1     | Configure | Quantum |
  
  
@TC_EPE_TE_PGSQL_95246_003
Scenario Outline: Verify Default Controller Configuration for M580 Controllers
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
Then I Verify that Default Controller Configuration should be in refine offline as '<Identifier>'

@verify_default_M580_controller_configuration_under_refine
Examples:
  | SlNo. | Project Browser RO1                                | Identifier   |
  | 1     | Configuration$$PLC bus$$BME XBP 0800$$BME P58 6040 | BME P58 6040 |
  
@verify_default_M580_Safety_controller_configuration_under_refine
Examples:
  | SlNo. | Project Browser RO1                                 | Identifier    |
  | 1     | Configuration$$PLC bus$$BME XBP 0800$$BME P58 6040S | BME P58 6040S |
  
@verify_default_M340_controller_configuration_under_refine
Examples:
  | SlNo. | Project Browser RO1                                                      | Identifier |
  | 1     | Configuration$$PLC bus$$BME XBP 0800$$BMX P34 20302$$Ethernet$$Channel 3 | Channel 3  |
  

@TC_EPE_TE_PGSQL_95246_004 
Scenario Outline: Modification of M580 Configuration Parameter(Unlock Security)
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I selected unlock security EIO in control expert 

@modification_M580_configuration_in_refline_offline
Examples:
  | SlNo. | Project Browser RO1                                     |
  | 1     | Configuration$$PLC bus$$BME XBP 0800$$BME P58 6040$$EIO |
  
  
@TC_EPE_TE_PGSQL_95246_005
Scenario Outline: Verify default state of M580 Security tab in controller port
Then I verify the default state of service module in security tab window
Then I verify the engineering link mode is default state of security tab window
Then I verify the access control button in security tab window

@verify_security_tab_in_controller_port
Examples:
  | SlNo. | |
  | 1     | |

      
@TC_EPE_TE_PGSQL_95246_006
Scenario Outline: Navigate to IPConfig and set the IP address, subnetwork mask and gateway address
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I Click tabitem in EIO configaration window in control expert as '<identifiers>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window4>'

@navigate_configure_window_Set_IP_address_subnet_mask_and_validate_the_modification
Examples:
  | SlNo. | Project Browser RO1                                                     | identifiers | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4                   |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME P58 6040$$EIO | IPConfig    | Main IP address$$192.168.10.1 | Subnetwork mask$$255.255.0.0 | IP address A$$192.168.11.1 | Gateway address$$192.168.10.1 |
  

@TC_EPE_TE_PGSQL_95246_007
Scenario Outline: Navigate Build should be successful and able to save and close the window
When I Navigate through tropology Controller_1 Configuration window refline offline in  menubar as '<Item>'
And I click '<menu_item>' in Tool Bar popup window
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

@Build_successful_and_able_to_save_and_close_the_window_in_refine_offline
Examples:
  | SlNo. | Item  | menu_item       |
  | 1     | Build | Rebuild All Project |
  

@TC_EPE_TE_PGSQL_95246_008
Scenario Outline: Verify the configuration of IP address by expanding the window in topology explorer   
When I Expand topology explorer node in topology as '<Node Name>'
And I Expand topology explorer node in topology as '<Node Name1>'
When I Dclick on topology Explorer Node in topology as '<Item>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'

@Expand_System_1_window_in_topology_explorer
Examples:
  | SlNo. | Node Name | Node Name1   | Item                            | context menu | Topology Explorer Tree1                      | Topology Explorer Tree2 |
  | 1     | System_1  | Controller_1 | Controller_1 0:PriLocal 0:D 0:R | Open         | Controller_1 0:PriLocal 0:D 0:R 0:BMEP586040 | Communication           |
  
  
@TC_EPE_TE_PGSQL_95246_009
Scenario Outline: Open Physical Connection for Controller in TE 
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<item>'
And I dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree>'
When I click modal dialog window project browser in project explorer as '<Button>'

@open_physical_Connection_tab_in_controller
Examples:
  | SlNo. | item                 | node         | Topology Explorer Tree | Button |
  | 1     | Physical Connections | Controller_1 | EthernetNetwork_1      | OK     |
  
@TC_EPE_TE_PGSQL_95246_0010
Scenario Outline: Change the security settings parameters from filter to enforced 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I select a value from engineering link dropdown in security tab window as '<Value>'
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

Examples:
  | SlNo. | Project Browser RO1                                     | Value    |
  | 1     | Configuration$$PLC bus$$BME XBP 0800$$BME P58 6040$$EIO | Filtered |
  

@TC_EPE_TE_PGSQL_95246_0011
Scenario Outline:Verify Controller object gets deleted  after performing Delete action by Context Menu 
Then Verify notification panel message Notification Pannel in message box as '<content>'    

@verify_controller_object_gets_deleted_in_notification_panel_M580
Examples:
  | SlNo. | content                       |
  | 1     | Delete Controller (Completed) |
  
@check_the_notification_in_notification_panel_M340_OR_Quantum
Examples:
  | SlNo. | content                            |
  | 1     | Close Configure Editor (Completed) |  
  
 
@TC_EPE_TE_PGSQL_95246_0012
Scenario Outline:Verify warning message Controller object gets deleted after performing Delete action by Context Menu    
Then I Verify the Generation PopUp Window Message

Examples:
  | SlNo. | |
  | 1     | |
 

@TC_EPE_TE_PGSQL_95246_0013
Scenario Outline: Create a Network from communication and configure the IP
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'
And I Select_network_CE System Project in topology explorer as '<System Project3>'
And I Click tabitem in Ethernet_1 Communication window in control expert as '<identifiers>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>' 

@create_network_from_communication_and_configure_IP_address_in_M340_or_Quantum_Controller_in_refine_offline
Examples:
  | SlNo. | System Project1                  | System Project2 | System Project3 | identifiers      | MDI Window1         | MDI Window2                | MDI Window3              |
  | 1     | Project$$Communication$$Networks | New Network     | Ethernet        | IP Configuration | IP address$$0.0.0.0 | Subnetwork mask$$255.0.0.0 | Gateway address$$0.0.0.0 |


@TC_EPE_TE_PGSQL_95246_0014
Scenario Outline: Verify the default state of M340 Configuration
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>' 
Then I Verify through default configuration in Ethernet_1 Communication window in control expert as '<identifiers>'

@verify_defualt_state_in_M340_0r_Quantum_Configuration_in_refine_offline
Examples:
  | SlNo. | Project Browser RO1                        | identifiers |
  | 1     | Project$$Communication$$Networks$$Ethernet | Security    |
  

@TC_EPE_TE_PGSQL_95246_0015
Scenario Outline:Double click on the Ethernet port of the controller and assign the created network
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
When I select_item_mdi_window_CE MDI Window in refine offline as '<MDI Window1>'
And I select_item_mdi_window_CE MDI Window in refine offline as '<MDI Window2>'
When I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

@assign_the_created_network_in_ethernet_port_M340
Examples:
  | SlNo. | MDI Window1 | MDI Window2 | Project Browser RO1                                                       | identifiers |
  | 1     | ETH TCP IP  | Ethernet_2  | Configuration$$0 : PLC bus$$0 : BMX XBP 0800$$0 : BMX P34 20302$$Ethernet | Channel 3   | 