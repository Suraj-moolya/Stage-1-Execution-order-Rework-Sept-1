Feature: 95254 - Verify the creation and configuration of Modbus RTU Communication with Gateway

@TC_EPE_TE_PGSQL_95254_001
Scenario Outline: Drag and Drop four templates from Application Browser to Assert Workspace Editor wrt Position
When I drag template in application browser Link Editor as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>'
When I drag template in application browser Link Editor as '<Assert Workspace Editor3>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor4>'
When I drag template in application browser Link Editor as '<Assert Workspace Editor5>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor6>'
When I drag template in application browser Link Editor as '<Assert Workspace Editor7>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor8>'

@Drag_and_drop_EGtwMB_1_EMPortM_1_ATS48MBGP_1_and_MotorGP_1_templates_to_assert_workspace_editor
Examples:
  | SlNo. | Assert Workspace Editor1 | Assert Workspace Editor2 | Assert Workspace Editor3 | Assert Workspace Editor4 | Assert Workspace Editor5 | Assert Workspace Editor6 | Assert Workspace Editor7 | Assert Workspace Editor8 |
  | 1     | EGtwMB_1$$1              | EGtwMB_1                 | EMPortM_1$$2             | EMPortM_1                | ATS48MBGP_1$$3           | ATS48MBGP_1              | MotorGP_1$$4             | MotorGP_1                |

@TC_EPE_TE_PGSQL_95254_002
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

@Link_EthernetPort_and_Ethernet_Client 
Examples:
  | SlNo. | <Assert Workspace Editor1>     |
  | 1     | Ethernet Port$$Ethernet Client |
  
@TC_EPE_TE_PGSQL_95254_003 
Scenario Outline: Click on the checkbox name and modify two Instance property values and Save
When I Click on the module name in the instance editor of application explorer as '<Name>'
And I Enter Description of an instance and update the value AE instance editor as '<Instance editor value1>'
And I Enter Description of an instance and update the value AE instance editor as '<Instance editor value2>'
And I selected Instance editor save in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

@CLick_on_Logic_and_modify_the_configurations_of_ATS48MBGP_1_in_the_instance_editor
Examples:
  | SlNo. | Name  | Instance editor value1   | Instance editor value2                          | Instance editor close1 |
  | 1     | Logic | Device Modbus Address$$3 | Time Window for the Device to Execute Orders$$2 | ATS48MBGP_1            |

@TC_EPE_TE_PGSQL_95254_004  
Scenario Outline: Click on the checkbox name and modify one Instance property value and Save
When I Click on the module name in the instance editor of application explorer as '<Name>'
And I Enter Description of an instance and update the value AE instance editor as '<Instance editor value1>'
And I selected Instance editor save in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

@CLick_on_Logic_and_modify_the_configurations_of_EGtwMB_1_in_the_instance_editor
Examples:
  | SlNo. | Name  | Instance editor value1               | Instance editor close1 |
  | 1     | Logic | IP Address of gateway$$182.168.35.25 | EGtwMB_1               |

@TC_EPE_TE_PGSQL_95254_005  
Scenario Outline: Navigate to Hardware mapping Tab, check the mapping is available and map
When I Click '<tabname>' on service mapping edittor window
And I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<appfacet>'
And I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
Then I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance

@Navigate_to_Hardware_mapping_tab_and_drag_and_drop_EMPortM_1_EMPortM_in_the_hardware_mapping_editor
Examples:
  | SlNo. | tabname          | appfacet          |
  | 1     | Hardware Mapping | EMPortM_1_EMPortM |

@TC_EPE_TE_PGSQL_95254_006     
Scenario Outline: Double click on Template and open the instance property of the Template
When I double click on template Identifier in application browser as '<Identifier5>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'

@Double_Click_on_ATS48MBGP_1_in_the_Application_browser_to_open_the_instance_property
Examples:
  | SlNo. | Identifier5 | Instance Editor6 |
  | 1     | ATS48MBGP_1 | ATS48MBGP_1      |

@Double_Click_on_EGtwMB_1_in_the_Application_browser_to_open_the_instance_property  
Examples:
  | SlNo. | Identifier5 | Instance Editor6 |
  | 1     | EGtwMB_1    | EGtwMB_1         |