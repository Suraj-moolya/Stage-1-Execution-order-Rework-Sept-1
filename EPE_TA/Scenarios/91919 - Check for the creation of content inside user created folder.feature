Feature: 91919 - Check for the creation of content inside user created folder

@TC_EPE_CR_PGSQL_91919_01
Scenario Outline: Create new folder and content in CR under any node
When I rclick folder in content repository as '<Folder Name>'
And I Select context menu item EC Application browser in application explorer as '<Context Value>'
Then I verify the created content is in editing state

@creating_folder_content_under_any_node
Examples:
  | SlNo. | Folder Name   | Context Value  |
  | 1     | User Contents | Create Folder  |
  | 2     | Folder_1      | Create Content |
    
  
@TC_EPE_CR_PGSQL_91919_02   
Scenario Outline: Enter the name for the newly created content
When I should be able to enter identifier name in content repository as '<Identifier Name>'
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'

Examples:
  | SlNo. | Identifier Name | Message                    |
  | 1     | Sample          | Update Content (Completed) |
  

@TC_EPE_CR_PGSQL_91919_03    
Scenario Outline: Naming validation for created content and verify identifier,version and date
When I Right click on created content as '<identifier>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
And I check naming validation of created content as '<Enter_name>'
Then I verify the content list of the created content

@Enter_the_name_only_with_Special_characters_and_numbers
Examples:
  | SlNo. | identifier | contextmenu_item | Enter_name |
  | 1     | Sample     | Rename           | @2323#%    |
  
@Enter_the_name_with_combination_Uppercase_and_lowercase_followed_by_numbers
Examples:
  | SlNo. | Enter_name |
  | 1     | Sample12   |
  
@Enter_the_name_with_combination_Uppercase_and_lowercase_along_with_special_charcters
Examples:
  | SlNo. | identifier | contextmenu_item | Enter_name |
  | 1     | Sample12   | Rename           | S@mple     |
  
@Enter_the_name_with_only_Uppercase
Examples:
  | SlNo. | Enter_name |
  | 1     | SAMPLE     |

  
@TC_EPE_CR_PGSQL_91919_04
Scenario Outline: Verify the sorting and filter in Columns of content
Then I verify sorting and filter of content as '<filter_name>'

Examples:
  | SlNo. | filter_name |
  | 1     | Identifier  |


  
