Feature: 90990 - To Test Navigation from the Application Instance to the respective Workspace

@TC_EPE_AE_PGSQL_90990_01
Scenario Outline: Search Template in Template browser and Drag and drop from template browser to application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'

@search_templates_drag_and_drop_to_application_browser
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | MotorGP            | MotorGP$$1.0.123       |
  | 2     | ValveGP            | ValveGP$$1.0.100       |
  | 3     | HandValveGP        | HandValveGP$$1.0.58    |
  | 4     | PIDGP              | PIDGP$$1.0.153         |
  | 4     | AnalogOutputGP     | AnalogOutputGP$$1.0.93 |
  
  
@TC_EPE_AE_PGSQL_90990_02
Scenario Outline: Create and open asset workspace 
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
And I Click on Enter Press shortcut keys in system explorer
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace3>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace4>'

@create_asset_workspace_1_and_open
Examples:
  | SlNo. | Asset workspace1 | Asset workspace2 | Asset workspace3 | Asset workspace4 |
  | 1     | System_4         | Create Workspace | AssetWorkspace_1 | Edit Workspace   |

@create_asset_workspace_2_and_open  
Examples:
  | SlNo. | Asset workspace1 | Asset workspace2 | Asset workspace3 | Asset workspace4 |
  | 1     | System_4         | Create Workspace | AssetWorkspace_2 | Edit Workspace   |
  
  
@TC_EPE_AE_PGSQL_90990_03
Scenario Outline: Drag and drop instnaces to asset workspace
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>' 
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor3>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor4>'
When I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode1>'
And I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode2>'
Then Verify Link Status Node Instance in application explorer
When I Close instance editor tab Instance editor close in application explorer as '<Asset workspace name>' 

@drag_and_drop_instances_asset_workspace_and_link
Examples:
  | SlNo. | Assert Workspace Editor1 | Assert Workspace Editor2 | Assert Workspace Editor3 | Assert Workspace Editor4 | fromnode$$tonode1 | fromnode$$tonode2    | Asset workspace name |
  | 1     | AnalogOutputGP           | AnalogOutputGP           | PIDGP                    | PIDGP                    | PVRange$$AORange  | RSPRanged$$OUTRanged | AssetWorkspace_1     |
  
  
@TC_EPE_AE_PGSQL_90990_04
Scenario Outline:Check the context menu to navigate workspace from the instance
When I rclick application browser template AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I double click on the asset workspace in navigate to assetworkspace window as '<identifier>'
And I click modal dialog window project browser in project explorer as '<Button>'

@navigate_to_workspace_from_instance_contextmenu_and_close_workspace
Examples:
  | SlNo. | Application browser1 | Application browser2  | identifier       | Button |
  | 1     | PIDGP_1$$1.0.153     | Navigate to Workspace | AssetWorkspace_1 | Close  |

  
@TC_EPE_AE_PGSQL_90990_05    
Scenario Outline:  Check in case of instance is added in multiple assetworkspaces
When I rclick application browser template AE Application browser in application explorer as '<Application browser5>'
And I Select context menu item EC Application browser in application explorer as '<Application browser6>'
Then I verify instance is added in multiple workspace in context menu listing
When I click modal dialog window project browser in project explorer as '<Button>'

@checks_instance_PIDGP_is_in_one_or_more_workspace
Examples:
  | SlNo. | Application browser5 | Application browser6  | Button |
  | 1     | PIDGP_1$$1.0.153     | Navigate to Workspace | Close  |

  
@TC_EPE_AE_PGSQL_90990_06
Scenario Outline: Check the selection of multiple instance and try to navigate 
When I select multiple instances in application browser as '<instance name1>'
And I select multiple instances in application browser as '<instance name2>'
And I rclick application browser template AE Application browser in application explorer as '<Application browser7>'
And I Select context menu item EC Application browser in application explorer as '<Application browser8>'
Then verify context menu items ContextMenu in application explorer

@try_to_navigate_to_workspace_from_contextmenu_multiple_instance_selected
Examples:
  | SlNo. | instance name1     | instance name2     | Application browser7 | Application browser8  |
  | 1     | MotorGP_1$$1.0.123 | ValveGP_1$$1.0.100 | MotorGP_1$$1.0.123   | Navigate to Workspace |
  
  
@TC_EPE_AE_PGSQL_90990_07
Scenario Outline: Instantiate few instance and don't add into assetworkspace and check the context menu to navigate workspace
When I rclick application browser template AE Application browser in application explorer as '<Application browser9>'
And I Select context menu item EC Application browser in application explorer as '<Application browser10>'
Then verify context menu items ContextMenu in application explorer

@try_to_navigate_to_workspace_from_unlinked_instance
Examples:
  | SlNo. | Application browser9 | Application browser10 |
  | 1     | MotorGP_1$$1.0.123   | Navigate to Workspace |
  
  
@TC_EPE_AE_PGSQL_90990_08
Scenario Outline: Drag and drop only one instnaces to asset workspace
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>'

@drag_and_drop_only_one_instance_asset_workspace
Examples:
  | SlNo. | Assert Workspace Editor1 | Assert Workspace Editor2 |
  | 1     | PIDGP                    | PIDGP                    |

