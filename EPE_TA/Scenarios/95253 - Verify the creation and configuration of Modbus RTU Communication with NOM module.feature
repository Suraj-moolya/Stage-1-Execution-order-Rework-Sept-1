Feature: 95253 - Verify the creation and configuration of Modbus RTU Communication with NOM module

@TC_EPE_TE_PGSQL_95253_001
Scenario Outline: Right click on the controller or workstation and select a context menu item 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<Context menu>'

@Right_Click_on_Controller_1_and_Configure
Examples:
  | SlNo. | Controller   | Context menu |
  | 1     | Controller_1 | Configure    |
  
@TC_EPE_TE_PGSQL_95253_002
Scenario Outline: Add modules in the configuration window of the controller
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'
And I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'
And I selected Dialog OK CE in dialog ce
 
@Add_BMX_NOM_0200.2_module
Examples:
  | SlNo. | Project Browser RO1                                              | Dialog Panel CE3 | Dialog Panel CE4 |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$2 : BMX NOM 0200.2 | Communication    | BMX NOM 0200.2   |
   
@TC_EPE_TE_PGSQL_95253_003
Scenario Outline: Drag and Drop three templates from Application Browser to Assert Workspace Editor wrt Position
When I drag template in application browser Link Editor as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>'
When I drag template in application browser Link Editor as '<Assert Workspace Editor3>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor4>'
When I drag template in application browser Link Editor as '<Assert Workspace Editor5>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor6>'

@Drag_and_drop_MBPortM_1_ATS22MBGP_1_and_MotorGP_1_templates_to_assert_workspace_editor
Examples:
  | SlNo. | Assert Workspace Editor1 | Assert Workspace Editor2 | Assert Workspace Editor3 | Assert Workspace Editor4 | Assert Workspace Editor5 | Assert Workspace Editor6 |
  | 1     | MBPortM_1$$1             | MBPortM_1                | ATS22MBGP_1$$2           | ATS22MBGP_1              | MotorGP_1$$3             | MotorGP_1                |


@TC_EPE_TE_PGSQL_95253_004
Scenario Outline: Link between facet nodes of respective instances in assert workspace editor
When I Link from range node to range node AE Node Instance in application explorer as '<Assert Workspace Editor1>'
Then Verify Link Status Node Instance in application explorer

@Link_ModbusPort_and_ModbusClient
Examples:
  | SlNo. | <Assert Workspace Editor1> |    
  | 1     | ModbusPort$$Modbus Client|            

@Link_DEV1S1D_and_Dev1S1D  
Examples:
  | SlNo. | <Assert Workspace Editor1> |
  | 1     | DEV1S1D$$Dev1S1D           |
  
    
@TC_EPE_TE_PGSQL_95253_005
Scenario Outline: Double click on Template and open the instance property of the Template
When I double click on template Identifier in application browser as '<Identifier5>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'

@Double_Click_on_ATS22MBGP_1_in_the_Application_browser_to_open_the_instance_property
Examples:
  | SlNo. | Identifier5 | Instance Editor6 |
  | 1     | ATS22MBGP_1 | ATS22MBGP_1      |
  
@TC_EPE_TE_PGSQL_95253_006
Scenario Outline: Save and Close the instance property in the instance editor window 
When I selected Instance editor save in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'

@Save_the_instance_property_of_MotorGP_1_and_close
Examples:
  | SlNo. | Instance editor close8 |
  | 1     | MotorGP_1              |
  
@TC_EPE_TE_PGSQL_95253_007
Scenario Outline: Navigate to Hardware mapping Tab, check the mapping is available and map
When I Click '<tabname>' on service mapping edittor window
And I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<appfacet>'
And I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
Then I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance

@Navigate_to_Hardware_mapping_tab_and_drag_and_drop_MBPortM_1_MBPortM_in_the_hardware_mapping_editor
Examples:
  | SlNo. | tabname          | appfacet          |
  | 1     | Hardware Mapping | MBPortM_1_MBPortM |
  

@TC_EPE_TE_PGSQL_95253_008  
Scenario Outline: Click on the checkbox name and modify the Instance property value and Save
When I Click on the module name in the instance editor of application explorer as '<Name>'
And I Enter Description of an instance and update the value AE instance editor as '<Instance editor value1>'
And I Enter Description of an instance and update the value AE instance editor as '<Instance editor value2>'
And I selected Instance editor save in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

@CLick_on_Logic_and_modify_the_configurations_of_ATS22MBGP_1_in_the_instance_editor
Examples:
  | SlNo. | Name  | Instance editor value1   | Instance editor value2                          | Instance editor close1 |
  | 1     | Logic | Device Modbus Address$$2 | Time Window for the Device to Execute Orders$$2 | ATS22MBGP_1            |

  
@TC_EPE_TE_PGSQL_95253_009  
Scenario Outline: Modify the configuration in topology configuration window
When I select a value from text object block in refine offline as '<Identifier>'
And I click on a button mdi configuration window in topology explorer as '<ButtonName1>' 
And I click on a button mdi configuration window in topology explorer as '<ButtonName2>'
And I click on a button mdi configuration window in topology explorer as '<ButtonName3>'

@Modify_the_configuration_for_channel0
Examples:
  | SlNo. | Identifier | ButtonName1 | ButtonName2 | ButtonName3 |
  | 1     | Channel 0  | 8 bits      | RS485       | Even        |

@TC_EPE_TE_PGSQL_95253_010  
Scenario Outline: Modify the configurations in topology configuration window
When I select a value from text object block in refine offline as '<Identifier>'
And I select_item_mdi_window_CE MDI Window in refine offline as '<MDIwindow>'

@Modify_the_configuration_for_channel1
Examples:
  | SlNo. | Identifier | MDIwindow | 
  | 1     | Channel 1  | Master    | 