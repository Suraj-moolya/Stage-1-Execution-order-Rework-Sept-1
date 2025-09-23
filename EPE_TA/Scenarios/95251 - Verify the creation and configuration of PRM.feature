Feature: 95251 - Verify the creation and configuration of PRM

#Pre-Requisites:
#1.Install PRM master and its required devices.

@TC_EPE_TE_PGSQL_95251_001
Scenario Outline: Right click on the controller or workstation and select a context menu item 
When I Right Click on nodes System Explorer Node in system explorer as '<System>'
And I Select context menu item EC project browser in project explorer as '<Context menu1>'
When I Right Click on nodes System Explorer Node in system explorer as '<PRM>'
And I Select context menu item EC project browser in project explorer as '<Context menu2>'

@Right_Click_on_System_3_and_Create_PRM_Profibus_DP_and_configure
Examples:
  | SlNo. | System   | Context menu1          | PRM   | Context menu2 |
  | 1     | System_3 | Create PRM Profibus DP | PRM_1 | Configure     |
  
@TC_EPE_TE_PGSQL_95251_002  
Scenario Outline: Add devices to PRM Master
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'
And I add a device in add device modal dialog window TE configuration as '<Device>'
And I select '<button>' in DTM Browser property device window

@Add_ATV71-Profibus-DPV1-Modular_to_PRM_Master
Examples:
  | SlNo. | System Project1                | System Project2 | Device                                 | button |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Add...          | ATV71-Profibus-DPV1-Modular (from GSD) | OK     |
  
@Add_LTMR-TeSysTProfibus_v2.1_to_PRM_Master  
Examples:
  | SlNo. | System Project1                | System Project2 | Device                                  | button |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Add...          | LTMR - TeSys T Profibus v2.1 (from GSD) | OK     |
  

@TC_EPE_TE_PGSQL_95251_003 
Scenario Outline: Right click on the project and select a context menu item 
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'

@OPEN_PRM_Master
Examples:
  | SlNo. | System Project1                | System Project2 |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Open            |

@CONNECT_PRM_Master 
Examples:
  | SlNo. | System Project1                | System Project2 |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Connect         |

@DISCONNECT_PRM_Master
Examples:
  | SlNo. | System Project1                | System Project2 |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Disconnect      |

@LOAD_Data_PRM_Master      
Examples:
  | SlNo. | System Project1                | System Project2       |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Load data from device |

@STORE_Data_PRM_Master  
Examples:
  | SlNo. | System Project1                | System Project2      |
  | 1     | Host PC$$< 1 > PRM_Master_0001 | Store data to device |

@DELETE_Device_PRM_Master  
Examples:
  | SlNo. | System Project1                                                             | System Project2 |
  | 1     | Host PC$$< 1 > PRM_Master_0001$$< Profibus:126 > ATV71_Profibus_DPV1_KIBBY2 | Delete          |

  
@TC_EPE_TE_PGSQL_95251_004  
Scenario Outline: Delete the PRM from topology explorer 
When I Right Click on nodes System Explorer Node in system explorer as '<PRM>'
And I Select context menu item EC project browser in project explorer as '<Context menu2>'
And I click modal dialog window project browser in project explorer as '<Button>'

@DELETE_PRM
Examples:
  | SlNo. | PRM   | Context menu2 | Button |
  | 1     | PRM_1 | Delete        | Yes    |
 
@TC_EPE_TE_PGSQL_95251_005 
Scenario Outline: Navigate to communication mapping tab
When I Right Click on nodes System Explorer Node in system explorer as '<System>'
And I Select context menu item EC project browser in project explorer as '<Context menu1>'
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I Click '<tabname>' on service mapping edittor window

Examples:
  | SlNo. | System   | Context menu1 | project browser1    | project browser2 | tabname               |
  | 1     | System_3 | Open Project  | ControlExecutable_1 | Manage           | Communication Mapping |
  
@TC_EPE_TE_PGSQL_95251_006
Scenario Outline: Edit IP address in PRM Master
When I double click on '<settings>' in PRM Window
And I edit ip address value in PRM config as '<ip1>'
And I edit ip address value in PRM config as '<ip2>'
And I click on a button in PRM configuration window as '<button1>'

@Open_GENERAL_SETTINGS_and_Edit_IP_Address
Examples:
  | SlNo. | settings         | ip1                        | ip2                       | button1 | 
  | 1     | General Settings | IP Address:$$182.233.63.48 | Subnet Mask:$$255.255.0.0 | Apply   | 

@TC_EPE_TE_PGSQL_95251_007
Scenario Outline: Assign station address in PRM Master
When I double click on '<settings>' in PRM Window
And I click on station address value in PRM config as'<identifier>'
And I assign station address value in PRM config as'<station_address>'
And I click on a button in PRM configuration window as '<button1>'
And I click on a button in PRM configuration window as '<button2>'

@Open_PROFIBUS_DEVICES_and_Assign_Station_Address
Examples:
  | SlNo. | settings         | identifier | station_address | button1        | button2 |
  | 1     | Profibus Devices | 126        | Edit$$25        | Assign Address | Apply   |
  
@TC_EPE_TE_PGSQL_95251_007
Scenario Outline: Assign station address for devices in PRM Master
When I click on station address value in PRM config as'<identifier>'
And I assign station address value in PRM config as'<station_address>'
And I click on a button in PRM configuration window as '<button1>'
And I click on a button in PRM configuration window as '<button2>'
And I click on a button in PRM configuration window as '<button3>'

@Assign_Station_Address_for_device
Examples:
  | SlNo. | identifier | station_address | button1        | button2 | button3 |
  | 1     | 0          | Edit$$12        | Assign Address | Apply   | OK      |
  
@TC_EPE_TE_PGSQL_95251_009   
Scenario Outline: Build project from configuration window
When I click '<menu>' in Tool Bar
When I click '<menu_item>' in Tool Bar popup window

@BUILD_Project_Configuration_window
Examples:
  | SlNo. | menu  | menu_item           | 
  | 1     | Build | Rebuild All Project |
 
