Feature: 92782 - Check the copy and paste action with combination of shortcut key and context menu options

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue
#3.Open Global Templates Explorer

@TC_EPE_GT_PGSQL_92782_001
Scenario Outline: Search the template and edit in Global Templates Explorer
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on fit to content button in global template explorer
And I Right Click on control template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item1>'
And I perform right click on editor window in GT
And I Select context menu item EC global template core in global template explorer as '<menu item2>'
And I Right Click on supervision template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item1>'
And I perform right click on editor window in GT
And I Select context menu item EC global template core in global template explorer as '<menu item2>'

@SEARCH_and_EDIT_AnalogInputGP_and_perform_COPY_and_PASTE_action
Examples:
  | SlNo. | Templates browser                   | menu item | menu item1 | menu item2 | 
  | 1     | Analoginput$$AnalogInputGP$$1.0.138 | Edit      | Copy       | Paste      | 

@TC_EPE_GT_PGSQL_92782_002
Scenario Outline: Copy & paste control template using keyboard actions  
When I Click on control template header in global template explorer
And I perform copy using keyboard actions
And I perform paste using keyboard actions

Examples:
  | SlNo. | content |
  | 1     | NA      |

@TC_EPE_GT_PGSQL_92782_003
Scenario Outline: Copy & paste supervision template using keyboard actions 
When I Click on supervision template header in global template explorer
And I perform copy using keyboard actions
And I perform paste using keyboard actions

Examples:
  | SlNo. | content |
  | 1     | NA      |
