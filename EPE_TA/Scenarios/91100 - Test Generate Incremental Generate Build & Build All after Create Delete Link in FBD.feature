Feature: 91100 - Test Generate Incremental Generate Build & Build All after Create Delete Link in FBD

Scenario Outline: Open the new section pop up in refine offline
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'

@Open_Mast_System_1_91100
Examples:
  | SlNo. | System Project1                        | System Project2      | 
  | 1     | Programs$$Tasks$$MAST$$Logic$$System_1 | Open                 | 
  
  
