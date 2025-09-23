Feature: 92673 - To Test 'Close' from the editor menu in composite editor, Facet editor, interface editor

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue 
#3.Create a system(System_1)

@TC_EPE_GT_PGSQL_92673_001
Scenario Outline:Open Global template and test the 'Close' option from editor menu Using templates
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
Then Verify the editor window in read only mode as '<Menu_item1>'
When I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
Then Verify header panel item is closed as '<panel>'
When I Close tab items EC main screen in engineering client as '<tab>'

@perform_view_action_from_editor_menu_using_PIDGP_template_in_Global_template
Examples:
  | SlNo. | Templates browser       | MainToolBar1     | global template core5 | Menu_item1              | Toolbar          | menu item | panel | tab              |
  | 1     | PIDGP$$PIDGP_UC$$1.0.98 | Global Templates | View                  | Composite Editor [View] | Global Templates | Close     | PIDGP | Global Templates |

@perform_edit_action_from_editor_menu_using_PIDGP_template_in_Global_template
Examples:
  | SlNo. | Templates browser       | MainToolBar1     | global template core5 | Menu_item1       | Toolbar          | menu item | panel |tab              |
  | 1     | PIDGP$$PIDGP_UC$$1.0.98 | Global Templates | Edit                  | Composite Editor | Global Templates | Close     | PIDGP |Global Templates |

@perform_view_action_from_editor_menu_using_Disignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1          | Toolbar          | menu item | panel    | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | View                  | Facet Editor [View] | Global Templates | Close     | DISignal | Global Templates |

@perform_edit_action_from_editor_menu_using_Disignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1   | Toolbar          | menu item | panel    | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | Edit                  | Facet Editor | Global Templates | Close     | DISignal | Global Templates |


@TC_EPE_GT_PGSQL_92672_002
Scenario Outline:Using Shortcut Keys to test the 'Close' option from editor menu 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
Then Verify the composite editor in read only mode as '<Menu_item1>'
When I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I perform close action using keyboard shortcut cntrlw
Then Verify header panel item is closed as '<panel>'
When I Close tab items EC main screen in engineering client as '<tab>'

@Using_shortcutkey_to_perform_View_action_use_PIDGP_template_in_Global_template
Examples:
  | SlNo. | Templates browser       | MainToolBar1     | global template core5 | Menu_item1              | Toolbar          | panel    |tab              |
  | 1     | PIDGP$$PIDGP_UC$$1.0.98 | Global Templates | View                  | Composite Editor [View] | Global Templates | DISignal |Global Templates |

@Using_shortcutkey_to_perform_edit_action_use_PIDGP_template_in_Global_template  
Examples:
  | SlNo. | Templates browser       | MainToolBar1     | global template core5 | Menu_item1       | Toolbar          | panel |tab              |
  | 1     | PIDGP$$PIDGP_UC$$1.0.98 | Global Templates | Edit                  | Composite Editor | Global Templates | PIDGP |Global Templates |

@Using_shortcutkey_to_perform_View_action_use_Disignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1          | Toolbar          | panel    | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | View                  | Facet Editor [View] | Global Templates | DISignal | Global Templates |

@Using_shortcutkey_to_perform_edit_action_use_Disignal_template_in_Global_template
Examples:
  | SlNo. | Templates browser            | MainToolBar1     | global template core5 | Menu_item1   | Toolbar          | panel    | tab              |
  | 1     | Disignal$$DISignal_UL$$6.3.7 | Global Templates | Edit                  | Facet Editor | Global Templates | DISignal | Global Templates |