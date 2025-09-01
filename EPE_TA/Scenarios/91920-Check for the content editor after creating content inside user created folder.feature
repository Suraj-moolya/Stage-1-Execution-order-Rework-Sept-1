Feature: 91920-Check for the content editor after creating content inside user created folder

@@TC_EPE_CR_PGSQL_91920
Scenario Outline: Opens a particular folder in CR
When I select a particular folder in content repository as '<Folder Name>'
 
@opening_system1_folder
Examples:
    | SlNo. | Folder Name |
    |1      |Systems      |
    |2      |System_1     |
    
    
@@TC_EPE_CR_PGSQL_91920a
Scenario Outline: Create new folder and content in CR
When I rclick folder in content repository as '<Folder Name>'
And I Select context menu item EC Application browser in application explorer as '<Context Value>'

@creating_folder_content
Examples:
    | SlNo. | Folder Name      | Context Value  |
    |1      |User Contents     | Create Folder  |
    |2      | Folder_1         | Create Content |
    
    
@@TC_EPE_CR_PGSQL_91920b
Scenario Outline: Enter the name for the newly created content
When I should be able to enter identifier name in content repository as '<Identifier Name>'

@creating_new_identifier
Examples:
    | SlNo. | Identifier Name  |
    |1      | Sample           | 
 

@@TC_EPE_CR_PGSQL_91920c
Scenario Outline: Open the identifier by pressin Enter button keyboard or double clicking and close the identifier as well
When Open the identifier properties either by pressing enter or double click on the selected identifier in content repository as '<Identifier Name>'
And Verify the title of the selected identifier in content repository as '<Identifier_name>'
And User closes the selected identifier by clicking on X button in content repository as '<Identifier_name>'

@opening_indentifier_enter
Examples:
    | SlNo. | Identifier Name  | Identifier_name |
    |1      | Sample$$Enter    | Sample          |
    

@opening_identifer_double_clicking   
Examples:
    | SlNo. | Identifier Name  | Identifier_name |
    |1      | Sample$$           | Sample        |
        


@@TC_EPE_CR_PGSQL_91920e
Scenario Outline: Open the identifier by right click and selectin edit content from context menu and close the identifier as well
When I rclick identifier in content repository as '<Folder Name>'
And I Select context menu item EC Application browser in application explorer as '<Context Value>'
And Verify the title of the selected identifier in content repository as '<Folder Name>'
And User closes the selected identifier by clicking on X button in content repository as '<Folder Name>'

@opening_identifier_right_click
Examples:
    | SlNo. | Folder Name      | Context Value  |
    |1      | Sample           | Edit Content   |
    
    
@@TC_EPE_CR_PGSQL_91920f
Scenario Outline: Fetch the values of identifier properties and verify them
When Open the identifier properties either by pressing enter or double click on the selected identifier in content repository as '<Identifier Name>'
And Verify the title of the selected identifier in content repository as '<Identifier_name>'
And User fetches the properties of selected identifier in content repository as '<properties_name>'

@verifying_identifier_properties_title
Examples:
    | SlNo. | Identifier Name  | Identifier_name |properties_name |
    |1      | Sample$$Enter    | Sample          |Change Description$$Description$$Author$$Date$$Type$$Version$$Identifier|