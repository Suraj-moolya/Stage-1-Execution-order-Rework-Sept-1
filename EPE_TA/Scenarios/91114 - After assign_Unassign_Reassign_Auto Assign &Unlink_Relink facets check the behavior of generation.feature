Feature: 91114 - After assign/Unassign/Reassign/Auto Assign & Unlink/Relink facets check the behavior of generation, Incremental generation, Build and Build all.


#Pre-Requisites:
#Create a system in system explorer and navigate to topology explorer.
#Create ethernet network and cretae a M580 controller
#Navigate to project explorer and create a control project in system 1.


@TC_EPE_CP_PGSQL_91114_001
Scenario Outline: Right click on the Control Project and navigate to Assignment editor window 
When I RClick control project browser project browser in project explorer as '<projectBrowser1>'
And I Select context menu item EC project browser in project explorer as '<projectBrowser2>'

@Right_Click_on_ControlProject_1_and_click_ASSIGN_FACETS
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |
  | 1     | ControlProject_1 | Assign Facets   |

    
@TC_EPE_CP_PGSQL_91114_002
Scenario Outline: Assign Multiple Instance to System_1 Containers in Assignment Editor window in PE
When I Drag and Drop the Instance to in Container as '<controller>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock2>'

@DRAG_and_DROP_ValveGP_1_into_the_container_and_GENERATE
Examples:
  | SlNo. | controller | Button | assignmentsdock1   | assignmentsdock2   |
  | 1     | ValveGP_1  | OK     | System_1$$Generate | LockOn1$$Generated |
   
@DRAG_and_DROP_MotorGP_1_into_the_container_and_GENERATE  
Examples:
  | SlNo. | controller | Button | assignmentsdock1   | assignmentsdock2   |
  | 1     | MotorGP_1  | OK     | System_1$$Generate | LockOn1$$Generated | 
  
@TC_EPE_TE_PGSQL_91114_003
Scenario Outline: Right Click on the system and Create a controller
When I Right Click on nodes System Explorer Node in system explorer as '<Folder Name>'
And I Select context menu item EC project browser in project explorer as '<context menu1>'
And I Select controller in context menu as '<controller>'

@Right_Click_On_System_1_and_Create_M580_Controller
Examples:
  | SlNo. | Folder Name | context menu1     | controller |
  | 1     | System_1    | Create Controller | M580       |
     
@TC_EPE_PE_CP_0004
Scenario Outline: Open Service Mapping Editor and map to Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

@Map_Controller_1_in_ControlExecutable_1
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                 |
  | 1     | ControlProject_1 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Controller_1 | 
  
@TC_EPE_CP_PGSQL_91114_005
Scenario Outline: Modify the properties of Instances in Instance Editor window
When I double click on template Identifier in application browser as '<Identifier1>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist1>'

@Check_HYPERLINK_in_instance_editor_of_ValveGP_1
Examples:
  | SlNo. | Identifier1 | Instance editor checklist1 |
  | 1     | ValveGP_1   | Hyperlink$$1               |
  
@TC_EPE_CP_PGSQL_91114_006
Scenario Outline: Save and close the properties of instances
When I selected Instance editor save in application explorer
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

@SAVE_and_CLOSE_the_instance_property_of_ValveGP_1
Examples:
  | SlNo. | Modal dialog window1 | Instance editor close1 |
  | 1     | Yes                  | ValveGP_1              |
  

@TC_EPE_CP_PGSQL_91114_007
Scenario Outline: Perform generation for assigned facets
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock2>'

@Perform_GENERATE_on_System_1
Examples:
  | assignmentsdock1   | assignmentsdock2   | Modal dialog window1 |
  | System_1$$Generate | LockOn1$$Generated | Yes                  |

  
#Execution flow
  