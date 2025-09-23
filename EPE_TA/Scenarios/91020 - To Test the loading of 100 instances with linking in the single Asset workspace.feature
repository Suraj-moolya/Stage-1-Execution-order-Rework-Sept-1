Feature: 91020 - To Test the loading of 100 instances with linking in the single Asset workspace

@TC_EPE_AE_PGSQL_91020_01
Scenario Outline: Search templates Drag and drop to Application pane
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'

@search_templates_drag_and_drop_to_application_browser
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | PIDGP              | PIDGP$$1.0.153         |
  |       |                    | PIDGP$$1.0.153         |
  |       |                    | PIDGP$$1.0.153         |
  |       |                    | PIDGP$$1.0.153         |
  | 2     | AnalogOutputGP     | AnalogOutputGP$$1.0.93 |
  |       |                    | AnalogOutputGP$$1.0.93 |
  |       |                    | AnalogOutputGP$$1.0.93 |
  |       |                    | AnalogOutputGP$$1.0.93 |

  
@TC_EPE_AE_PGSQL_91020_02
Scenario Outline: Create Asset Workspace,open Workspace   
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
And I Click on Enter Press shortcut keys in system explorer
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace3>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace4>'
Then Verify Message from notification panel AE Notification Pannel in message box

@create_asset_workspace_1_and_open
Examples:
  | SlNo. | Asset workspace1 | Asset workspace2 | Asset workspace3 | Asset workspace4 |
  | 1     | System_4         | Create Workspace | AssetWorkspace_1 | Edit Workspace   |
  
  
@TC_EPE_AE_PGSQL_91020_03
Scenario Outline: Drag and drop instnaces to asset workspace and link the instances
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>' 
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor3>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor4>'
When I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode1>'
And I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode2>'
And I Click on fit to content button in global template explorer
Then Verify Link Status Node Instance in application explorer

@drag_and_drop_instances_asset_workspace_and_link
Examples:
  | SlNo. | Assert Workspace Editor1 | Assert Workspace Editor2 | Assert Workspace Editor3 | Assert Workspace Editor4 | fromnode$$tonode1 | fromnode$$tonode2    |
  | 1     | AnalogOutputGP_1         | AnalogOutputGP_1         | PIDGP_1                  | PIDGP_1                  | PVRange$$AORange  | RSPRanged$$OUTRanged |
  | 2     | AnalogOutputGP_2         | AnalogOutputGP_2         | PIDGP_2                  | PIDGP_2                  | PVRange$$AORange  | RSPRanged$$OUTRanged |
  | 3     | AnalogOutputGP_3         | AnalogOutputGP_3         | PIDGP_3                  | PIDGP_3                  | PVRange$$AORange  | RSPRanged$$OUTRanged |
  | 4     | AnalogOutputGP_4         | AnalogOutputGP_4         | PIDGP_4                  | PIDGP_4                  | PVRange$$AORange  | RSPRanged$$OUTRanged |

  
@TC_EPE_AE_PGSQL_91020_04
Scenario Outline: Open AE and Import Assetworkspace having 100 instances
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import1>'
And I Select button in the modal dialoge window as '<Button name>'
Then Verify Message from notification panel AE Notification Pannel in message box

@open_AE_import_assetworkspace
Examples:
  | SlNo. | MainToolBar1              | Asset workspace1 | Asset workspace2 | Import1          | Button name |
  | 1     | Open Application Explorer | System_3         | Import           | Assetworkspace_1 | OK          |
  
  
@TC_EPE_AE_PGSQL_91020_05  
Scenario Outline: Open, close and open assetworkspace and check the instances available
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
And I Close instance editor tab Instance editor close in application explorer as '<Asset workspace name1>' 
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor1>'

@open_and_assetwprkspace_after_loading_100_instances
Examples:
  | SlNo. | Asset workspace1 | Asset workspace2 | Instance Editor1 |
  | 1     | AssetWorkspace_1 | Edit Workspace   | AssetWorkspace_1 |
  
  
@TC_EPE_AE_PGSQL_91020_06
Scenario Outline: Close and open assetworkspace and check the instances available
When I Close instance editor tab Instance editor close in application explorer as '<Asset workspace name1>'
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor3>'
 
@close_and_open_assetworkspace_after_open
Examples:
  | SlNo. | Asset workspace name1 | Asset workspace1 | Asset workspace2 | Instance Editor3 |
  | 1     | AssetWorkspace_1      | AssetWorkspace_1 | Edit Workspace   | AssetWorkspace_1 |
  
  
@TC_EPE_AE_PGSQL_91020_07  
Scenario Outline: copy assetworkspace, paste it in system and open the pasted workspace
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace1>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace2>'
And I Close instance editor tab Instance editor close in application explorer as '<Asset workspace name>' 
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace3>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace4>'
Then Verify Message from notification panel AE Notification Pannel in message box
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace5>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace6>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor2>'

@Copy_the_assetworkspace_and_paste
Examples:
  | SlNo. | Asset workspace1 | Asset workspace2 | Asset workspace name1 | Asset workspace3 | Asset workspace4 | Asset workspace5   | Asset workspace6 | Instance Editor2   |
  | 1     | AssetWorkspace_1 | Copy             | AssetWorkspace_1      | System_4         | Paste            | AssetWorkspace_1_1 | Edit Workspace   | AssetWorkspace_1_1 |
  
  
@TC_EPE_AE_PGSQL_91020_08
Scenario Outline: Perform any action while import is loading
When I double click on template Identifier in application browser as '<Identifier1>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'

Examples:
  | SlNo. | Identifier1      | Instance Editor6 |
  | 1     | AnalogOutputGP_1 | AnalogOutputGP_1 |