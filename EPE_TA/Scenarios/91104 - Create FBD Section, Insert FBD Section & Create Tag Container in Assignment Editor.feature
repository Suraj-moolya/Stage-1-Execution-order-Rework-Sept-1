Feature: 91104 - Create FBD Section, Insert FBD Section & Create Tag Container in Assignment Editor

# Pre-Requisites : Create a control project in PE tab open conatiners

@TC_EPE_CP_PGSQL_91104_01
Scenario Outline: Create FBD Section and verify the order
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<containerdock>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I verify the order of the FBD section in containerdock

@Create_FBD_and_verify_FBD_order
Examples:
  | SlNo. | containerdock                        | Button |
  | 1     | ControlProject_1$$Create FBD Section | OK     |

@Cancel_create_FBD_Section
Examples:
  | SlNo. | containerdock                        | Button |
  | 1     | ControlProject_1$$Create FBD Section | Cancel |
  
  
@TC_EPE_CP_PGSQL_91104_02
Scenario Outline:Select the path of FBD in create FBD pop up
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<containerdock>'
And I select path of FBD in FBD creation pop up as '<path>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I verify the order of the FBD section in containerdock

@create_FBD_select_FAST
Examples:
  | SlNo. | containerdock                        | Button | path |
  | 1     | ControlProject_1$$Create FBD Section | OK     | FAST |

  
@TC_EPE_CP_PGSQL_91104_03
Scenario Outline: Create FBD Section,rename and check for naming validation
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<containerdock>'
And I rename FBD Section in create FBD Section popup as '<rename>'
Then I Verify the new fbd section created

@Rename_FBD_as_Section_1_valid
Examples:
  | SlNo. | containerdock                        | rename    | 
  | 1     | ControlProject_1$$Create FBD Section | Section_1 | 
  
@Enter_32_character_name_for_FBD_Section_invalid
Examples:
  | SlNo. | containerdock                        | rename                            |
  | 1     | ControlProject_1$$Create FBD Section | abcdefghijklmnopqrstuvwxyzabcdefg |
  
@Enter_invalid_character_like_@,#,,%_in_name_for_FBD_Section_invalid
Examples:
  | SlNo. | containerdock                        | rename     |
  | 1     | ControlProject_1$$Create FBD Section | Section@#1 | 
   
@Enter_name_with_underscore_at_the_end_of_name_for_FBD_Section_invalid
Examples:
  | SlNo. | containerdock                        | rename     | 
  | 1     | ControlProject_1$$Create FBD Section | Section_1_ | 

@Enter_name_"DO"_as_name_for_FBD_Section_invalid
Examples:
  | SlNo. | containerdock                        | rename | 
  | 1     | ControlProject_1$$Create FBD Section | DO     | 
  
@Enter_name_with_underscores_and_numeric_in_between_characters_as_name_for_FBD_Section
Examples:
  | SlNo. | containerdock                        | rename      | 
  | 1     | ControlProject_1$$Create FBD Section | FBD_1_new_2 | 
  
  
@TC_EPE_CP_PGSQL_91104_04
Scenario Outline: Insert new FBD section in container dock and verify order
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<containerdock>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then Verify notification panel message Notification Pannel in message box as '<Message>'
Then I verify the order of the FBD section in containerdock

@Rclick_FBDSection_2_Insert_FBD_Section
Examples:
  | SlNo. | containerdock                    | Button | Message                        |
  | 1     | FBDSection_2$$Insert FBD Section | OK     | Insert FBD Section (Completed) |
  