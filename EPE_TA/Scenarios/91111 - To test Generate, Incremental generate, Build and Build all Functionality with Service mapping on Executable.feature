Feature: 91111 - To test Generate, Incremental generate, Build and Build all Functionality with Service mapping on Executable


#Pre-Requisites:
#Open project explorer and create a control project in system 1.

@TC_EPE_CP_PGSQL_91111_001
Scenario Outline: Open Manage of Control Executeable and verify service mapping state
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then I verify the service mapping to the controller as '<project browser3>'

@Open_Manage_ControlExecutable_1_verify_NOT_ASSIGNED_service_mapping
Examples:
  | SlNo. | project browser1    | project browser2 | project browser3                 |
  | 1     | ControlExecutable_1 | Manage           | ControlExecutive_1$$Not Assigned |
  
@Open_Manage_ControlExecutable_1_verify_WORKSTATION_1_service_mapping
Examples:
  | SlNo. | project browser1    | project browser2 | project browser3                  |
  | 1     | ControlExecutable_1 | Manage           | ControlExecutive_1$$Workstation_1 |
  
  
@TC_EPE_CP_PGSQL_91111_002
Scenario Outline: Check Build, Build All, Generate and Build option state from control executeable context menu
When I RClick control project browser project browser in project explorer as '<project browser1>'
Then I verify the context menu item enabled state as '<project browser2>'

@check_context_menu_BUILD_option_state_DISABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Build$$Disabled  |

@check_context_menu_BUILD_ALL_option_state_DISABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2   |
  | 1     | ControlExecutable_1 | Build All$$Disabled |
  
@check_context_menu_GENERATE_AND_BUILD_option_state_DISABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2             |
  | 1     | ControlExecutable_1 | Generate and Build$$Disabled |
  
@check_context_menu_BUILD_ALL_option_state_ENABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2  |
  | 1     | ControlExecutable_1 | Build All$$Enabled |
  
@check_context_menu_GENERATE_AND_BUILD_option_state_ENABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2            |
  | 1     | ControlExecutable_1 | Generate and Build$$Enabled |
   
@check_context_menu_BUILD_option_state_ENABLED_ControlExecutable_1
Examples:
  | SlNo. | project browser1    | project browser2 |
  | 1     | ControlExecutable_1 | Build$$Enabled   |
        

@TC_EPE_CP_PGSQL_91111_003
Scenario Outline: Selecting context menu item from control executable context menu
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'

@Select_BUILD_ALL_from_ControlExecutable_1_context_menu
Examples:
  | SlNo. | project browser1    | project browser2 | project browser3 |
  | 1     | ControlExecutable_1 | Build All        | OK               |
  
  
@TC_EPE_CP_PGSQL_91111_004
Scenario Outline: To verify built state of the control project
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
Then Verify build state of control executable PE project browser in project explorer as '<project browser3>'

@verify_Built_state_of_controlProject_1_BUILT
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                             | content |
  | 1     | ControlProject_1 | Executables      | ControlProject_1$$ControlExecutable_1$$Built | NA      |

@verify_Built_state_of_controlProject_1_OUTOFDATE
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                                 |
  | 1     | ControlProject_1 | Executables      | ControlProject_1$$ControlExecutable_1$$OutOfDate |

