Feature: 91094 - Verify Generate and Build functions after variable changes in FAST FBD Section.

@TC_EPE_CP_PGSQL_91094
Scenario Outline: Create a move block and close it
When I click on button in refine offline for move block as '<btn_value1>'
And I create a move block in refine offline for a particular section as '<query_value>' 


Examples:
  | SlNo. | btn_value1|query_value                  | 
  | 1     | Maximize|FFB$$Move$$IN$$Test1$$OK       |