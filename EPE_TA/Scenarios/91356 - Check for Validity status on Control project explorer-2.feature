Feature: 91356 - Check for Validity status on Control project explorer-2


Scenario Outline: Create instance in Application Explorer
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'

@Navigate_to_System1_AE
Examples:
  | SlNo. | Systems Explorer | MainToolBar1                      | Explorer tab2 |
  | 1     | System_1         | Open Application Explorer (Alt+A) | Application   |

@create_instance 
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | Analog             | AnalogOutputGP$$1.0.93 |
  | 2     | Analog             | AnalogInputGP$$1.0.138 |
  | 3     | MotorGP            | MotorGP$$1.0.123       |
  | 4     | ValveGP            | ValveGP$$1.0.100       |
  | 5     | MValveGP           | MValveGP$$1.0.85       |
  

Scenario Outline:Add and Link the instance to asset workspace
When I rclick asset workspace folder AE Asset workspace in application explorer as '<AssetRoot>'
And I Select context menu item EC Asset workspace in application explorer as '<AssetAction>'
And I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor1>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor2>' 
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor3>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor4>'
When I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode1>'
And I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode2>'
Then Verify Link Status Node Instance in application explorer
When I Close instance editor tab Instance editor close in application explorer as '<Asset workspace name>'  

@Create_Asset_Workspace
Examples:
  | SlNo | AssetRoot | AssetAction      | Assert Workspace Editor1 | Assert Workspace Editor2 | Assert Workspace Editor3 | Assert Workspace Editor4 | fromnode$$tonode1 | fromnode$$tonode2    | Asset workspace name |
  | 1    | System_1  | Create Workspace | AnalogOutputGP           | AnalogOutputGP           | AnalogInputGP            | AnalogInputGP            | PVRange$$AORange  | RSPRanged$$OUTRanged | AssetWorkspace_1     |
     
 
Scenario Outline: Creating FBD section in MAST
When I Create multiple FBD Sections and Verify as '<assignmentsdock2>'

@create_5_MAST_FBD_Section
Examples:
  | SlNo. | assignmentsdock2                        |
  | 1     | ControlProject_2$$Create FBD Section$$5 |

Scenario Outline: Creating FBD section in FAST      
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<containerdock>'
And I select path of FBD in FBD creation pop up as '<path>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I verify the order of the FBD section in containerdock 

@create_FBD_select_FAST_1_to_2
Examples:
  | SlNo. | containerdock                        | Button | path |
  | 1     | ControlProject_2$$Create FBD Section | OK     | FAST |
  

Scenario Outline: Assign  Instance from system to FBD Section in PE
When I Assign Instances from instance dock to sections in containers dock as '<param>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock

@Assign_Instance_from_system_to_fbd_section_in_PE
Examples:
  | SlNo. | param                   | Button |
  | 1     | MotorGP_1$$FBDSection_1 | OK     |
  

Scenario Outline: Generate and build Control Project 
When I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'
And I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'

@Generate_and_build_CP 
Examples:
  | SlNo. | project browser3    | project browser4 | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Controller_2     |project browser1    | project browser2 |
  

Scenario Outline: Check the facet State and Validity State in control_project PE
Then I verify the section is generated successfully as '<param>'
Then Verify the validity status of control project in project browser PE as '<status1>'

Examples:
  | SlNo. | param                        | status                  |
  | 1     | MotorGP_1_MotorGP$$Generated | ControlProject_2$$Error |
  

Scenario Outline: Unassign Facets and check validity status in  Project Explorer Assignments
When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then Verify the validity status of control project in project browser PE as '<status1>'


Examples:
  | SlNo. | facet_name        | action   | status     | Message              | project browser1    | project browser2 | status1                    |
  | 1     | MotorGP_1_MotorGP | Unassign | Unassigned | Unassign (Completed) | ControlExecutable_1 | Build ALL        | ControlExecutable_1$$Error |


Scenario Outline:Re-assign Facets and check validity status Containerblock in  Project Explorer Assignments
When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then Verify the validity status of containerblock in project browser PE as '<status2>'

@Reassign_facet_M2DGP_1_Motor2GP_Assignments_Dock_PE
Examples:
  | SlNo. | facet_name        | action   | status   | Message              | project browser1    | project browser2 | status2             |
  | 1     | MotorGP_1_MotorGP | Reassign | Assigned | Reassign (Completed) | ControlExecutable_1 | Build ALL        | FBDSection_1$$Error |