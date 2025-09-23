Feature: 92675 - To Test 'Edit' from the editor menu in Composite editor, Facet editor

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue

@TC_EPE_GT_PGSQL_92675_001
Scenario Outline: Open Global template and Find the template in search ( ex. MotorGP, DISignal_ul)
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then Verify the composite editor in read only mode as '<Menu_item1>'

@Open_GT_and_search_MotorGP_UC_and_view
Examples:
  | SlNo. | Templates browser           | MainToolBar1     | menu item | Menu_item1          |
  | 1     | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates | View      | Switch to edit mode |
  
@Open_GT_and_search_DISignal_UL_and_view
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | menu item | Menu_item1          |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | View      | Switch to edit mode |

@TC_EPE_GT_PGSQL_92675_002  
Scenario Outline: Verify the sub menu items in edit menu   
When I click on the menu item bar in the composite editor in GT '<title>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then I verify the context submenu items
When I Click on Edit menu item in global template explorer as '<menu_item>'
And I click on the menu item bar in the composite editor in GT '<title>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then I verify the context submenu items

@VERIFY_Edit_submenuitems_in_VIEW_and_EDIT_mode
Examples:
  | SlNo. | title            | menu item | menu_item           |
  | 1     | Global Templates | Edit      | Switch to edit mode |
  
  @92675
  Scenario Outline:  Verify 'Edit' functionality for Composite Editor in GTE
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplatesBrowser>'
    And I Select context menu item EC global template core in global template explorer as '<ContextMenu>'
    Then Verify the composite editor in read only mode as '<TitleBar>'
    When I Click on Editor toolbar in global template explorer as '<Toolbar>'
    And I Select context menu item EC global template core in global template explorer as '<MenuItem>'
    Then Verify context submenu items are displayed
    
  @Verify_View_Motorgp_UC_in_GTE
  Examples:
    | TemplatesBrowser            | MainToolBar      | ContextMenu | TitleBar                | Toolbar          | MenuItem |
    | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates | View        | Composite Editor [View] | Global Templates | View     |
 
  @Verify_Edit_Motorgp_UC_in_GTE
  Examples:
    | TemplatesBrowser            | MainToolBar      | ContextMenu | TitleBar         | Toolbar          | MenuItem |
    | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates | Edit        | Composite Editor | Global Templates | Edit     |
    
  @Verify_View_DISignal_UL_in_GTE
  Examples:
    | TemplatesBrowser             | MainToolBar      | ContextMenu | TitleBar                | Toolbar          | MenuItem |
    | Disignal$$DISignal_UL$$6.3.7 | Global Templates | View        | Composite Editor [View] | Global Templates | View     |
    
  @Verify_Edit_DISignal_UL_in_GTE
  Examples:
    | TemplatesBrowser             | MainToolBar      | ContextMenu | TitleBar         | Toolbar          | MenuItem |
    | Disignal$$DISignal_UL$$6.3.7 | Global Templates | Edit        | Composite Editor | Global Templates | Edit     |
