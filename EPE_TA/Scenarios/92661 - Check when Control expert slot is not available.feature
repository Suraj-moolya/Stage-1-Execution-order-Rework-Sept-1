Feature: 92661 - Check when Control expert slot is not available

@TC_EPE_GT_PGSQL_92661_01
Scenario Outline: Occupy all Control Expert slots form TE and PE
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then verify displayed Project Browser RO in refine offline

@open_refine_offline_control_project_1
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | ControlProject_1 | Refine           |
  

@open_refine_offline_control_project_2
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | ControlProject_2 | Refine           |
  
@open_refine_offline_control_project_3
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | ControlProject_3 | Refine           |
  
@open_refine_offline_control_project_4
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | ControlProject_4 | Refine           |
  

@TC_EPE_GT_PGSQL_92661_02
Scenario Outline: Open GT and search template and view it in edit mode
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
And I Click on Edit menu item in global template explorer as '<Tab1>'
Then Verify Modal Dialog Window Text in message box as '<Message>'
When I click modal dialog window project browser in project explorer as '<Button1>'

@select_template_and_navigate_to_edit_mode_in_MOtorGP_UL_and_Templatizer
Examples:
  | SlNo. | Templates browser1              | global template core1 | MainToolBar1     | Tab1        | Button1 | Message                         |
  | 1     | motorgp_ul$$$MOTORGP_UL$$1.0.56 | Edit                  | Global Templates | Templatizer | OK      | There is no free slot available |
  

@TC_EPE_GT_PGSQL_92661_03
Scenario Outline: Close all occupied Control Expert slots opened 
When I selected Close Refine Offline in refine offline
And I Select button in the modal dialoge window as '<button name1>'
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'

@close_control_expert_slots_occupied
Examples:
  | SlNo. | button name1 | Message                                  |
  | 1     | No           | Close Control Project Editor (Completed) |
  
 
@TC_EPE_GT_PGSQL_92661_04
Scenario Outline: Close all tabs in Enginnering Client
When I click toolbar item in select variables window as '<Button Name>'
And I close all tabs except system explorer in Engineering Client


Examples:
  | SlNo. | Button Name |
  | 1     | Close       |


@TC_EPE_GT_PGSQL_92661_05
Scenario Outline: Occupy all Control Expert slots from Global Templates
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar2>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser3>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
And I Click on Edit menu item in global template explorer as '<Tab2>'
And I Click on open control participant button in global template explorer

@select_template_and_navigate_to_edit_mode_in_MOtorGP_UL_templatizer_and_open_participant_window
Examples:
  | SlNo. | Templates browser3             | global template core1 | Tab2        | MainToolBar2     |
  | 1     | Motorgp_ul$$MOTORGP_UL$$1.0.56 | Edit                  | Templatizer | Global Templates |
  

@select_template_and_navigate_to_edit_mode_in_Byte_UL_templatizer_and_open_participant_window
Examples:
  | SlNo. | Templates browser3      | global template core1 | Tab2        | MainToolBar2     |
  | 1     | Byte_ul$$Byte_UL$$1.0.8 | Edit                  | Templatizer | Global Templates |
  

@select_template_and_navigate_to_edit_mode_in_Bool_UL_templatizer_and_open_participant_window
Examples:
  | SlNo. | Templates browser3       | global template core1 | Tab2        | MainToolBar2     |
  | 1     | Bool_ul$$Bool_UL$$1.0.13 | Edit                  | Templatizer | Global Templates |
  

@select_template_and_navigate_to_edit_mode_in_VALVEGP_UL_templatizer_and_open_participant_window
Examples:
  | SlNo. | Templates browser3             | global template core1 | Tab2        | MainToolBar2     |
  | 1     | valvegp_ul$$VALVEGP_UL$$1.0.50 | Edit                  | Templatizer | Global Templates |
  

Scenario Outline: Open CE tab when all slots are occupied and verify dialog
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar2>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser3>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
And I Click on Edit menu item in global template explorer as '<Tab2>'
Then Verify Modal Dialog Window Text in message box as '<Message>'
When I click modal dialog window project browser in project explorer as '<Button2>'

@open_CE_from_GT_when_slots_are_occupied_and_verify_pop_up_message
Examples:
  | SlNo. | Templates browser3                 | global template core1 | Tab2        | MainToolBar2     | Message                         | Button2 |
  | 1     | AoutputGP_UL$$AOUTPUTGP_UL$$1.0.40 | Edit                  | Templatizer | Global Templates | There is no free slot available | OK      |
  

@TC_EPE_GT_PGSQL_92661_06
Scenario Outline: Close all Participant displays opened from GT 
When I selected Close Refine Offline in refine offline
And I Click popup button object project browser in project explorer as '<project browser>'
And I Select button in the modal dialoge window as '<button name3>'

@close_control_expert_slots_occupied_from_GT
Examples:
  | SlNo. | project browser                           | button name3 |
  | 1     | MessageBox$$modaldialogwindow1textbox$$OK | Yes          |
  

@TC_EPE_GT_PGSQL_92661_07
Scenario Outline: Close all participant windows in GT
When I click on the tab in Header Panel as '<Headername>'
And I click toolbar item in select variables window as '<Button Name>'

@click_on_MOTORGP_UL_tab_and_close_select_variale_window
Examples:
  | SlNo. | Headername | Button Name |
  | 1     | MOTORGP_UL | Close       |
  
@click_on_Byte_UL_tab_and_close_select_variale_window
Examples:
  | SlNo. | Headername | Button Name |
  | 1     | Byte_UL    | Close       |
  
@click_on_Bool_UL_tab_and_close_select_variale_window
Examples:
  | SlNo. | Headername | Button Name |
  | 1     | Bool_UL    | Close       |
   
@click_on_VALVEGP_UL_tab_and_close_select_variale_window
Examples:
  | SlNo. | Headername | Button Name |
  | 1     | VALVEGP_UL | Close       |
  
  
@TC_EPE_GT_PGSQL_92661_08
Scenario Outline: Close all tabs in Enginnering Client
When I close all tabs except system explorer in Engineering Client
  
Examples:
  | SlNo. | 
  | 1     |