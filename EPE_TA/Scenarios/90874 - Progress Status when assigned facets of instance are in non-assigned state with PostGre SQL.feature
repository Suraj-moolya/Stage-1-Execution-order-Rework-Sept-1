Feature: 90874 - Progress Status when assigned facets of instance are in non-assigned state with PostGre SQL


@TC_EPE_AE_PGSQL_90874_1
Scenario Outline: Check Progress status of instances in instance browser
Then Verify the progress status of instance in Instance browser PE when opened as '<template>'
And I take photo evidence in Engineering Client

@Check_progress_status_M2DGP_1_instance_browser_at_50%
Examples:
  | SlNo. | template    |
  | 1     | M2DGP_1$$50 |
  

@TC_EPE_AE_PGSQL_90874_2
Scenario Outline: Check Progress status of instances in application browser
Then Verify the progress status of instance in Application browser when opened as '<template>'
And I take photo evidence in Engineering Client

@Check_progress_status_M2DGP_1_application_browser_at_50%
Examples:
  | SlNo. | template    |
  | 1     | M2DGP_1$$50 |
  
@Check_progress_status_GenericDeviceGP_1_application_browser_at_25%
Examples:
  | SlNo. | template              |
  | 1     | GenericDeviceGP_1$$25 |
    
    
@TC_EPE_AE_PGSQL_90874_3
Scenario Outline: Assign Facet in Project Explorer Assignments
When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Then Verify Action message in notification pannel container dock in project explorer as '<Message>'

@Unassign_facet_M2DGP_1_Motor2GP_Assignments_Dock_PE
Examples:
  | SlNo. | facet_name       | action   | status     | Message              |
  | 1     | M2DGP_1_Motor2GP | Unassign | Unassigned | Unassign (Completed) |
 
@Reassign_facet_M2DGP_1_Motor2GP_Assignments_Dock_PE
Examples:
  | SlNo. | facet_name       | action   | status   | Message              |
  | 1     | M2DGP_1_Motor2GP | Reassign | Assigned | Reassign (Completed) |
  
  
@TC_EPE_AE_PGSQL_90874_4
Scenario Outline: Expand folder in Instance Dock 
When I Expand folder in Instance Dock PE when opened as '<Folder>'
Then I take photo evidence in Engineering Client

@Expand_Folder_1_in_Instance_Dock
Examples:
  | SlNo. | Folder   |
  | 1     | Folder_1 |

  
@TC_EPE_AE_PGSQL_90874_5
Scenario Outline: Generate Containers from container dock without pop up
When I RClick on Container in Container Dock and select menu item as '<containerinstance>'
Then Verify Action message in notification pannel container dock in project explorer as '<Message>'

@Generate_TagContainer_1_Container_dock
Examples:
  | SlNo. | containerinstance        | Message                            |
  | 1     | TagContainer_1$$Generate | Generate Tag Container (Completed) |
