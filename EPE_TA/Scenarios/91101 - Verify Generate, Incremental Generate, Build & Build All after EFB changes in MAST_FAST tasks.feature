Feature: 91101 - Verify Generate, Incremental Generate, Build & Build All after EFB changes in MAST_FAST tasks

@TC_EPE_CP_PGSQL_91009_1
Scenario Outline: Open the new section pop up in refine offline
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'

@create_new_section_Mast
Examples:
 | SlNo. | System Project1              | System Project2      | 
 | 1     | Programs$$Tasks$$MAST$$Logic | New Section          | 
 
 
@TC_EPE_CP_PGSQL_91101_1
Scenario Outline: Enter the query in the modal window and close it
When I enter the query in modal window for control expert as '<query_value>'

@Query_TON_ST
Examples:
  | SlNo. | query_value                  | 
  | 1     | TON_1 (IN := test1,       PT := T#20s,       Q => test2,       ET => et);$$ |
  
@Query_Move_ST
Examples:
  | SlNo. | query_value                     | 
  | 1     | test2 := MOVE (IN := test1); $$ |
  
@Modified_Preset_Time_Ton_ST
Examples:
  | SlNo. | query_value                  | 
  | 1     | TON_1 (IN := test1,       PT := T#15s,       Q => test2,       ET => et);$$ |
  
@remove_query_ST
Examples:
  | SlNo. | query_value | 
  | 1     | $$          |
  

  
#@Open_ST_section