Feature: 90980 -To Test the columns in tree view & grid view of application explorer

Scenario Outline: Create and verify multiple folders under the root node in Application Browser
When I create multiple folders under the root node in the Application Browser with value '<folder_value>'

@Create_7_folders_in_Application_Browser
Examples:
  | SlNo | folder_value      |
  | 1    | System$$Folder$$7 |
    
    
Scenario Outline: Search Template in Template browser and Drag and drop from template browser to folder structure in application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'

@Templates_to_test_tree_and_grid_view
Examples:
  | SlNo. | Templates browser1 | Templates browser2               |
  | 1     | MotorGP            | MotorGP$$1.0.123$$Folder_1       |
  | 2     | ValveGP            | ValveGP$$1.0.100$$Folder_2       |
  | 3     | HandValveGP        | HandValveGP$$1.0.58$$Folder_3    |
  | 4     | PIDGP              | PIDGP$$1.0.153$$Folder_4         |
  | 5     | AnalogInputGP      | AnalogInputGP$$1.0.138$$Folder_5 |
  
  
Scenario Outline: Shuffle default columns
When I shuffle the default columns as '<shuffle>'
Then I verify the displayed instances in Application Browser

@Shuffle_Version_and_Template_column_in_AE
Examples:
  | SlNo. | shuffle           |
  | 1     | Version$$Template |
  
  
Scenario Outline: Drag and Expand application browser
When I drag and expand the application browser in AE
Then I verify the displayed instances in Application Browser
 
@Darg_and_expand_application_browser_in_AE
Examples:
  | SlNo. |
  | 1     |