Feature: 92672 - To Test 'Show Changes log' from Editor menu in composite editor, Facet editor, Interface editor

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue 
#3.Create a system(System_1)

@TC_EPE_GT_PGSQL_92672_001
Scenario Outline: Open GLobal template and Find the template in search ( ex. MotorGP, DISignal_ul)
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'

@open_GT_and_find_template_in_search_box_EX.motorgp_uc
Examples:
  | SlNo. | Templates browser           | MainToolBar1     |
  | 1     | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates |
  
@open_GT_and_find_template_in_search_box_EX.DISignal_ul
Examples:
  | SlNo. | Templates browser            | MainToolBar1     |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates |
  

@TC_EPE_GT_PGSQL_92672_002
Scenario Outline: Select the template and double click on it and navigate through view mode
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'   
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
Then Verify the composite editor in read only mode as '<Menu_item1>'

@select_template_and_navigate_to_view_mode_in_motorgp_uc
Examples:
  | SlNo. | Templates browser           | global template core5 | Menu_item1          |
  | 1     | Motorgp$$MotorGP_UC$$1.0.98 | View                  | Switch to edit mode |
  
@select_template_and_navigate_to_view_mode_in_DISignal_ul
Examples:
  | SlNo. | Templates browser            | global template core5 | Menu_item1          |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | View                  | Switch to edit mode |


@TC_EPE_GT_PGSQL_92672_003
Scenario Outline: Click on the editor menu and select the show log changes option.
When I perform right click on editor window in GT
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then Verify changeslog window is displayed

@click_on_editor_menu_and_open_changes_Log
Examples:
  | SlNo. | menu item        |
  | 1     | Show Changes Log | 
  
  
@TC_EPE_GT_PGSQL_92672_004
Scenario Outline: Check the changes log displayed in edit mode
When I Click on Edit menu item in global template explorer as '<global template core5>'
Then Verify changeslog window is displayed

@check_changes_log_in_edit_mode
Examples:
  | SlNo. | global template core5 |
  | 1     | Switch to edit mode   |
