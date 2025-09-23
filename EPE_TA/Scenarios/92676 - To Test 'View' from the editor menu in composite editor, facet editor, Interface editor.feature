Feature: 92676 To Test 'View' from the editor menu in composite editor, facet editor, Interface editor

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue 
#3.Create a system(System_1)


@TC_EPE_GT_PGSQL_92676_001
Scenario Outline: Open Global template and test the 'View' from editor menu Using templates 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
Then Verify the editor window in read only mode as '<Menu_item1>'
When I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then Verify context submenu items are displayed
When I perform close action using keyboard shortcut cntrlw
And I Close tab items EC main screen in engineering client as '<tab>'

@test_the_View_from_editor_menu_using_Motorgp_template_in_Global_template
Examples:
  | SlNo. | Templates browser           | MainToolBar1     | global template core5 | Menu_item1              | Toolbar         | menu item | tab              |
  | 1     | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates | View                  | Composite Editor [View] | Global Template | View      | Global Templates |

@test_the_Edit_from_editor_menu_using_Motorgp_template_in_Global_template
Examples:
  | SlNo. | Templates browser           | MainToolBar1     | global template core5 | Menu_item1       | Toolbar         | menu item | tab              |
  | 1     | Motorgp$$MotorGP_UC$$1.0.98 | Global Templates | Edit                  | Composite Editor | Global Template | Edit      | Global Templates |

@Do_View_action_from_editor_menu_using_DIsignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1          | Toolbar         | menu item | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | View                  | Facet Editor [View] | Global Template | View      | Global Templates |
  
@Do_edit_action_from_editor_menu_using_DIsignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1   | Toolbar         | menu item | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | Edit                  | Facet Editor | Global Template | Edit      | Global Templates |
