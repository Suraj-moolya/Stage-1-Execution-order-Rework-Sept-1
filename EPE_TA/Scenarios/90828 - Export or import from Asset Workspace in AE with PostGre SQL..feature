Feature: 90828 To Test the export or import from Asset Workspace in Application explorer with PostGre SQL.

@TC_EPE_AE_PGSQL_90828_1
Scenario Outline: Export Asset Workspace from Root Node - Export as XML, verify XML file
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Export Window as '<File detail>'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify Extracted Template XML Data and Template Details Export in ec windows explorer '<File detail>'
Then I Expand '<Message>' and verify the notification message contents '<Scroll count>'

@Export_AssetWorkspace_RootNode_as_xml
Examples:
  | SlNo. | Asset workspace4 | Application browser2 | File detail         | Message            | Scroll count |
  | 1     | System_1         | Export               | AssetRootNode$$.xml | Export (Completed) | 3            |
 
   
  
@TC_EPE_AE_PGSQL_90828_2
Scenario Outline: Export Asset Workspace from Root Node - Export as CSV, verify CSV file
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Export Window as '<File detail>'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify Extracted Template CSV Data and Template Details Export in ec windows explorer '<File detail>'

@Export_AssetWorkspace_RootNode_as_csv
Examples:
  | SlNo. | Asset workspace4 | Application browser2 | File detail         |
  | 1     | System_1         | Export               | AssetRootNode$$.csv |
  
@Export_AssetWorkspace_as_csv
Examples:
  | SlNo. | Asset workspace4 | Application browser2 | File detail |
  | 1     | AssetWorkspace_1 | Export               | Asset$$.csv |
  
@Export_Empty_AssetWorkspace_as_csv
Examples:
  | SlNo. | Asset workspace4 | Application browser2 | File detail |
  | 1     | AssetWorkspace_2 | Export               | Asset$$.csv |
  
  
  
@TC_EPE_AE_PGSQL_90828_3A 
Scenario Outline: Assert Workspace pane - Apply Filter
When I select the filter in AE Asset Workspace pane as '<Filter>'
And I select the filter combobox item as '<Comboitem>'
And I enter text to filter in the filter textbox of Asset Workspace as '<Text>'
And I click on filter button in the filter window of Asset Workspace
And I click on close button in the filter window of Asset Workspace
Then I verify if the specific filter action in the AE application browser pane

@Apply_Filter_in_Asset_Workspace
Examples:
  | SlNo. | Filter     | Comboitem     | Text                       |
  | 2     | Identifier | combobox2$$Or | textbox1$$AssetWorkspace_1 |
  
  
@TC_EPE_AE_PGSQL_90828_3B
Scenario Outline: Assert Workspace pane - Clear Filter
When I select the filter in AE Asset Workspace pane as '<Filter>'
And I clear the applied filter in Assert Workspace pane
And I click on close button in the filter window of Asset Workspace
Then I verify if the specific filter action in the AE application browser pane

@Clear_Filter_in_Asset_Workspace
Examples:
  | SlNo. | Filter     |
  | 1     | Identifier |
  
  
  
@TC_EPE_AE_PGSQL_90828_4 
Scenario Outline: Import Asset Workspace - RightClick on the Root Node and select Import from the context menu
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Import Window as '<File detail>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

@Import_Asset_Workspace_to_System
Examples:
  | SlNo. | Asset workspace4 | Application browser2 | File detail         |
  | 1     | System           | Import               | AssetRootNode$$.csv |


  
@TC_EPE_AE_PGSQL_90828_5
Scenario Outline: Import - Click on Create all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
And Verify the instances in Application Browser '<scroll count>'
Then Verify Message from notification panel AE Notification Pannel in message box

@Import_Assert_Workspace_Create 
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 | scroll count |
  | 1     | Create All              | OK                      | 5            |
  

    
@TC_EPE_AE_PGSQL_90828_6
Scenario Outline: Import - Click on Update all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify Message from notification panel AE Notification Pannel in message box

@Import_Assert_Workspace_Update 
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Update All              | OK                      |
   
@Import_Assert_Workspace_Skip
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Skip All                | OK                      |

 
@TC_EPE_AE_PGSQL_90828_7
Scenario Outline: Create empty Asset workspace
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace5>'
And I Click on Enter Press shortcut keys in system explorer

@Create_empty_Asset_workspace
Examples:
  | SlNo. | Asset workspace4 | Asset workspace5 |
  | 1     | System_1         | Create Workspace |
  
  
  
#######################################################################################################
#Execution order for TC_90828 and TC_90829
##############################################################
  
#Tags - @Navigate_to_System1_AE
#Tags - @Templates_for_builds_before_6334
#Scenarios\ApplicationExplorer - Expand Asset workspace
#Tags - @Create_empty_Asset_workspace
#Tags - @Export_AssetWorkspace_RootNode_as_xml
#Tags - @Export_Empty_AssetWorkspace_as_csv
#Tags - @Apply_Filter_in_Asset_Workspace
#Tags - @Export_AssetWorkspace_as_csv
#Tags - @Clear_Filter_in_Asset_Workspace
#Tags - @Export_AssetWorkspace_RootNode_as_csv
#Tags - @Import_Asset_Workspace_to_System
#Tags - @Import_Assert_Workspace_Skip
#Tags - @Import_Asset_Workspace_to_System
#Tags - @Import_Assert_Workspace_Update
#Tags - @Import_Asset_Workspace_to_System
#Tags - @Import_Assert_Workspace_Create
#Scenarios\EnginneringClient - Navigate to System Explorer ( SE )
#Scenarios\EnginneringClient - Creation of System - By Right clicking on System Explorer
#Tags - @Navigate_to_System2_AE
#Tags - @Import_Asset_Workspace_to_System
#Tags - @Edit_exportedcsv_with_Invalid_template_name_and_Import
#Tags - @Import_Assert_Workspace_Create

###########################################################################################################