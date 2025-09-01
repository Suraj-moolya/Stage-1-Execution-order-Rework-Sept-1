Feature: 92674 - To Test 'New' from the editor menu in Composite editor, Facet editor, Interface editor

@TC_EPE_GT_PGSQL_92674_01
Scenario Outline: Open GT Search templates and open in view mode
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'


@select_template_and_navigate_to_view_mode_in_MOtor_UC
Examples:
  | SlNo. | Templates browser          | global template core1 | MainToolBar1     |
  | 1     | Motor_UC$$Motor_UC$$3.0.20 | View                  | Global Templates |
  
@select_template_and_navigate_to_edit_mode_in_MOtor_UC
Examples:
  | SlNo. | Templates browser          | global template core1 | 
  | 1     | Motor_UC$$Motor_UC$$3.0.20 | Edit                  | 
    
@select_template_and_navigate_to_view_mode_in_DISignal_UL
Examples:
  | SlNo. | Templates browser               | global template core1 | MainToolBar1     |
  | 1     | DISignal_UL$$DISignal_UL$$6.3.7 | View                  | Global Templates |
  
@select_template_and_navigate_to_edit_mode_in_DISignal_UL
Examples:
  | SlNo. | Templates browser               | global template core1 | 
  | 1     | DISignal_UL$$DISignal_UL$$6.3.7 | Edit                  | 
  
  
@TC_EPE_GT_PGSQL_92674_02    
Scenario Outline:click on editor menu open new,select item type,enter identifier and location
When I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on items in selevt items window in global template explorer as '<Itemname>'  
And I Enters the given identifier value in the Select Item window as '<Identifier>'
And I Open the location selection window in the 'Select Item' window
And I Expand a node in the 'Select Item' window tree structure as '<node name1>'
And I Expand a node in the 'Select Item' window tree structure as '<node name2>'
And I select a node in the 'Select Item' window tree as '<SelectNode>'
And I click modal dialog window project browser in project explorer as '<Button1>'
And I click '<button>' 'Select Item' window tree modal dialog window
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'

@open_new_from_toolbar_select_item_and_path_verify_item_created
Examples:
  | SlNo. | Toolbar          | Itemname | menu item | Identifier | node name1         | node name2  | SelectNode  | Button1 | button | Message                    |
  | 1     | Global Templates | Generic  | New...    | Test1      | Foundation Library | Application | Application | OK      | OK     | Create Generic (Completed) |
  

@TC_EPE_GT_PGSQL_92674_03    
Scenario Outline:Open GT and verify the path of the created item
When I expand '<node_name>' in Global template Window
And I Right Click on nodes System Explorer Node in system explorer as '<node1>'
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
Then I verify path of item created in Global template Window with '<Headername>'

@open_GT_verify_path_of_item_created
Examples:
  | SlNo. | node_name          | node1              | global template core1 | Headername         |
  | 1     | Foundation Library | Foundation Library | Open                  | Foundation Library |