Feature: 92699 - Check the keyboard shortcuts at Composite Editor, Facet Editor, Interface Editor & Link Editor

@TC_EPE_GT_PGSQL_92699_01
Scenario Outline: Open GT Perform keyboard shortcuts
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I enterkey Project Browser RO in refine offline
Then I verify the '<node>' is expanded or collapsed after Enter key

@open_GT_Try_keyboard_shortcuts
Examples:
  | SlNo. | MainToolBar1     | Systems Explorer | node             |
  | 1     | Global Templates | Global Templates | Global Templates |
  
  
@TC_EPE_GT_PGSQL_92699_02  
Scenario Outline: Search template,open it in edit mode and rename
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
And I select on '<identifier1>' module in composite ediotr window
And I use keyboard '<key1>' shortcuts to perform some actions
Then I verify the module '<module>' is in renaming state
When I use keyboard '<key7>' shortcuts to perform some actions

@search_PIDGP_edit_and_verify_renaming_state
Examples:
  | SlNo. | Templates browser1         | global template core1 | identifier1 | key1 | module      | key7    |
  | 1     | PIDGP_UC$$PIDGP_UC$$1.0.98 | Edit                  | Multiplexer | [F2] | Multiplexer | [Enter] |
  

@TC_EPE_GT_PGSQL_92699_03    
Scenario Outline: Select module,perform Copy and Paste in composite editor
When I use keyboard '<key2>' shortcuts to perform some actions
And I use keyboard '<key3>' shortcuts to perform some actions
Then I verify the module '<modulename>' is newly pasted in composite editor
When I use keyboard '<key8>' shortcuts to perform some actions

@Selects_module_Multiplexer_copy_and_paste
Examples:
  | SlNo. | identifier2 | key2 | key3 | modulename    | key8    |
  | 1     | Multiplexer | ^c   | ^v   | Multiplexer_1 | [Enter] |
  

@TC_EPE_GT_PGSQL_92699_04  
Scenario Outline: Select module and Delete
When I select on '<identifier2>' module in composite ediotr window
And I use keyboard '<key4>' shortcuts to perform some actions
And I click modal dialog window project browser in project explorer as '<Button1>'
    
@Select_module_Multiplexer_1_perform_delete
Examples:
  | SlNo. | identifier2   | key4  | Button1 |
  | 1     | Multiplexer_1 | [Del] | Yes     |
  

@TC_EPE_GT_PGSQL_92699_05
Scenario Outline: Search template,open it in edit mode and open facet editor 
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser2>'   
And I Select context menu item EC global template core in global template explorer as '<global template core2>'
And I Click on fit to content button in global template explorer
Then I verify that I have navigated to the '<tabname1>'
When I right click on '<Description1>' module in templates composite editor window
And I Select context menu item EC global template core in global template explorer as '<global template core3>'
And I Click on fit to content button in global template explorer
Then I verify that I have navigated to the '<tabname2>'
When I right click on '<Description2>' module in templates composite editor window
And I Select context menu item EC global template core in global template explorer as '<global template core4>'
And I Click on fit to content button in global template explorer
Then I verify that I have navigated to the '<tabname3>'

@search_AnalogInputGP_UC_edit_and_open_facet_editor_open_interface_editor_perform_keyboard_shortcuts
Examples:
  | SlNo. | Templates browser2                         | global template core2 | tabname1         | global template core3 | Description1 | tabname2    | Description2 | global template core4 | tabname3    |
  | 1     | AnalogInputGP_UC$$AnalogInputGP_UC$$1.0.72 | Edit                  | AnalogInputGP_UC | Edit                  | AnalogInput  | AInputGP_UC | AnalogInput  | Edit                  | AISignal_UL |

  
@TC_EPE_GT_PGSQL_92699_06  
Scenario Outline: Search the facet,select it and perform keyboard shortcuts
When I search a facet in facet editor and select as '<name$$identifier>'
And I use keyboard '<key5>' shortcuts to perform some actions
And I use keyboard '<key6>' shortcuts to perform some actions

@Search_facets_and_select_facet_editor_copy_paste
Examples:
  | SlNo. | name$$identifier           | key5 | key6 |
  | 1     | AInputSignal$$AINPUTSignal | ^c   | ^v   |
  
  
@TC_EPE_GT_PGSQL_92699_07
Scenario Outline: Select AInpputSignal and delete
When I Click on ainputsignal template header in facet editor
And I use keyboard '<key8>' shortcuts to perform some actions
And I click modal dialog window project browser in project explorer as '<Button2>'

@Select_AInputSignal_facet_editor_and_delete_using_keys
Examples:
  | SlNo. | key8  | Button2 |
  | 1     | [Del] | Yes     |

  
@TC_EPE_GT_PGSQL_92699_08    
Scenario Outline: Select AInpputSignal and open in edit mode              #Keys like enter,copy,paste and Shift+F12 is not posiible in Interface editor
When I Click on ainputsignal template header in facet editor
And I use keyboard '<key9>' shortcuts to perform some actions
Then I verify that I have navigated to the '<tabname4>'
When I Click on DO template header in interface editor
And I use keyboard '<key10>' shortcuts to perform some actions
Then I verify template '<name>' is in renaming state interface editor

@Select_AInputSignal_Nav_to_Interface_editor_check_for_keyborad_shortcuts
Examples:
  | SlNo. | key9   | tabname4     | key10 | name |
  | 1     | ![F12] | AINPUTSignal | [F2]  | DO   |
  
 
@create_project_navto_Ae_drag_n_drop_instances_to_application_pane

@TC_EPE_GT_PGSQL_92699_09
Scenario Outline: Rclick on instance and open edit links  
When I rclick application browser template AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'


Examples:
  | SlNo. | Application browser1     | Application browser2 |
  | 1     | AnalogOutputGP_1$$1.0.93 | Edit Links           |
  
  
@TC_EPE_GT_PGSQL_92699_10
Scenario Outline: Rclick on instance and open edit links  
When I drag template in application browser Link Editor as '<Assert Workspace Editor8>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'
When I Link from range node to range node AE Node Instance in application explorer as '<fromnode$$tonode1>'
Then Verify Link Status Node Instance in application explorer

Examples:
  | SlNo. | Assert Workspace Editor8 | Assert Workspace Editor9 | fromnode$$tonode1    |
  | 1     | RangeGP_1$$1             | RangeGP_1                | SPRange$$AnalogRange |
