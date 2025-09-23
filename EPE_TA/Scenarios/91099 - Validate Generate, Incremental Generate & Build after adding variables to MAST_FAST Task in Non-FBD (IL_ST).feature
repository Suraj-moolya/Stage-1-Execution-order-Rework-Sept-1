Feature: 91099 - Validate Generate, Incremental Generate & Build after adding variables to MAST_FAST Task in Non-FBD (IL_ST)


#@Create_standalone_Control_Project_1 
#@Open_Refine_offline_of_M580_Standalone_from_Context_Menu
#@Double_click_on_Elementary_variables_with_path_Programs-PROCESS$$Variables_&_FB_instances
#@Create_consecutivevariable_by_clicking_on_ValveGP_1_OPV_and_create_variable_Test1
#@Create_consecutivevariable_by_clicking_on_ValveGP_2_OPV_and_create_variable_Test2
#@Change_Test1_bool_value_to_INT
#@Change_Test2_bool_value_to_INT
#@create_new_section_under_mast
#@query_move_test1_test2

  
  
@TC_EPE_CP_PGSQL_91009_1
Scenario Outline: Open the new section pop up in refine offline
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'

@create_new_section_Fast
Examples:
  | SlNo. | System Project1              | System Project2      | 
  | 1     | Programs$$Tasks$$FAST$$Logic | New Section          | 
  
@create_new_section_Mast
Examples:
 | SlNo. | System Project1              | System Project2      | 
 | 1     | Programs$$Tasks$$MAST$$Logic | New Section          | 
  
@Open_Sample
Examples:
  | SlNo. | System Project1                      | System Project2      | 
  | 1     | Programs$$Tasks$$FAST$$Logic$$Sample | Open                 | 

@Open_Mast_System_1_91100
Examples:
  | SlNo. | System Project1                        | System Project2      | 
  | 1     | Programs$$Tasks$$MAST$$Logic$$System_1 | Open                 | 


@TC_EPE_CP_PGSQL_91009_1
Scenario Outline: Create new section in refine offline
Then I create a New Section under Logic in control expert as '<Section Name>'

@create_new_FBD_section
Examples:
  |SlNo.|Section Name|
  |1    |Sample$$FBD |
  
@create_new_IL_section
Examples:
  |SlNo.|Section Name|
  |1    |Sample$$IL  |
  
@create_new_ST_section
Examples:
  |SlNo.|Section Name|
  |1    |Sample_TON$$ST  |

  

  
@TC_EPE_CP_PGSQL_91009_2
Scenario Outline: Enter the query in the modal window and close it
When I enter the query in modal window for control expert as '<query_value>'
Then I close the modal window in control expert as '<btn_value>'

@query_move_test1_test2_IL
Examples:
  | SlNo. | query_value                  | btn_value      | 
  | 1     | MOVE (IN := test1)$$ST test2 | Close          | 
  
@query_move_test3_test4_IL
Examples:
  | SlNo. | query_value                  | btn_value      | 
  | 1     | MOVE (IN := test3)$$ST test4 | Close          | 
  
@query_move_MotorGP_1_CondsumGP_ST_IL
Examples:
  | SlNo. | query_value                                                    | btn_value      | 
  | 1     | MOVE (IN := MotorGP_1_CondsumGP_ST)$$ST MotorGP_2_CondsumGP_ST | Close          | 

@query_move_test1_test2_ST
Examples:
  | SlNo. | query_value                   | btn_value      | 
  | 1     | test2 := MOVE (IN := test1);  | Close          | 
  
@query_move_test3_test4_ST
Examples:
  | SlNo. | query_value                  | btn_value      | 
  | 1     | test4 := MOVE (IN := test3); | Close          | 
  
@query_move_MotorGP_1_CondsumGP_ST_ST
Examples:
  | SlNo. | query_value                                                     | btn_value      | 
  | 1     | MotorGP_2_CondsumGP_ST := MOVE (IN := MotorGP_1_CondsumGP_ST);  | Close          |   
  
  
#for saving
#@TC_EPE_PE_CP_0032a

