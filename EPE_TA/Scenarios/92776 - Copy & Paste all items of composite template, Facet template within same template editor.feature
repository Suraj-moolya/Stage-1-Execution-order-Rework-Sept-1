Feature: 92776 - To Test Copy & Paste all items of composite template, Facet template within same template editor

Scenario Outline: Search Template, Edit and Open Composite Editor in GT

When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Close tab items EC main screen in engineering client as 'Global'
And I Click on fit to content button in global template explorer

@Search_Template_PIDGP_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1    | menu item |
  | 1     | PIDGP$$PIDGP$$1.0.153 | Edit      |
  
@Search_Template_PIDCTLGP_UL_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1              | menu item |
  | 1     | $PIDCTLGP_UL$$$PIDCTLGP$$1.0.54 | Edit      |
  
@Search_Template_PIDCTLGP_CD_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1              | menu item |
  | 1     | $PIDCTLGP_CD$$$PIDCTLGP$$1.0.37 | Edit      |
  
@Search_Template_PIDPVSPOPGP_CG_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1                | menu item |
  | 1     | $PIDPVSPOPGP$$$PIDPVSPOPGP$$1.0.0 | Edit      |
  
@Search_Template_PIDGP_UC_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1           | menu item |
  | 1     | $PIDGP_UC$$$PIDGP_UC$$1.0.98 | Edit      |
  
@Search_Template_PIDStatus_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1             | menu item |
  | 1     | PIDStatus$$PIDStatusGP$$1.0.11 | Edit      |
  
@Search_Template_MotorGP_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1          | menu item |
  | 1     | $MotorGP$$$MotorGP$$1.0.123 | Edit      |
  
@Search_Template_DigitalInputGP_UC_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1                        | menu item |
  | 1     | $DigitalInputGP_UC$$$DigitalInput$$1.0.62 | Edit      |
  
@Search_Template_DINPUTGP_UL_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1            | menu item |
  | 1     | $DINPUTGP_UL$$$DINPUT$$1.0.39 | Edit      |
  
@Search_Template_PIDGP_CS_Edit_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1            | menu item |
  | 1     | $PIDGP_CS$$$PIDGP_CS$$1.0.117 | Edit      |
  
   
   
Scenario Outline: Select All, Copy, Paste from Context Menu in GT Composite Editor  
When I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Select Submenu item from Context menu of toolbar in GT as '<submenu>'

@Select_All_from_Edit_ContextMenu_in_GT
Examples:
  | SlNo. | Toolbar          | menu item | submenu    |
  | 1     | Global Templates | Edit      | Select All |
  
@Copy_from_Edit_ContextMenu_in_GT
Examples:
  | SlNo. | Toolbar          | menu item | submenu |
  | 1     | Global Templates | Edit      | Copy    |
  
@Paste_from_Edit_ContextMenu_in_GT
Examples:
  | SlNo. | Toolbar          | menu item | submenu |
  | 1     | Global Templates | Edit      | Paste   |
  

Scenario Outline: Select All, Copy, Paste using Keys in GT Composite Editor 
When I Ctrl+A to select all in the Composite Editor window
And I Ctrl+C to copy the selected in Composite Editor window
And I Ctrl+V to paste the copied in the same Composite Editor window

@Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor 
Examples:
  | SlNo. |
  | 1     |

Scenario Outline: Verify the warning message in GT Properties pane
When I verify the warning message in the GTE pane as '<message>' 

@Verify_GT_warning_message
Examples:
  | SlNo. | message                        |
  | 1     | Please select only one object. |
  
@Verify_GT_warning_message_in_Toolbox_of_Interface_Editor
Examples:
  | SlNo. | message                              |
  | 1     | Unable to add the items in view mode |
    
  
Scenario Outline: Close GT tabs with Save pop up
When I Close tab items EC main screen in engineering client as '<tab>'
And I click modal dialog window Modal dialog window in message box as '<Button>'

@Close_PIDGP_tab_in_GT_with_save_pop_up
Examples:
  | SlNo. | Button | tab  |
  | 1     | No     | $PID |
  
@Close_Bool_tab_in_GT_with_save_pop_up
Examples:
  | SlNo. | Button | tab   |
  | 1     | No     | $Bool |
  

Scenario Outline: Close GT tabs without Save pop up
When I Close tab items EC main screen in engineering client as '<tab>'
  
@Close_PID_tab_in_GT
Examples:
  | SlNo. | tab  |
  | 1     | $PID |
  
@Close_Motor_tab_in_GT
Examples:
  | SlNo. | tab    |
  | 1     | $Motor |
  
@Close_DISignal_tab_in_GT
Examples:
  | SlNo. | tab       |
  | 1     | $DISignal |
  
@Close_Bool_tab_in_GT
Examples:
  | SlNo. | tab   |
  | 1     | $Bool |
  
@Close_DigitalInputGP_tab_in_GT
Examples:
  | SlNo. | tab      |
  | 1     | $Digital |
  
@Close_DINPUT_tab_in_GT
Examples:
  | SlNo. | tab     |
  | 1     | $DINPUT |
  
  
  
###########################################################################################
#Execution order for TC_92776
##############################################################

#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDGP_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Select_All_from_Edit_ContextMenu_in_GT
#Tags - @Copy_from_Edit_ContextMenu_in_GT
#Tags - @Paste_from_Edit_ContextMenu_in_GT
#Tags - @Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDCTLGP_UL_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor
#Tags - @Verify_GT_warning_message
#Tags - @Close_PID_tab_in_GT
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDCTLGP_CD_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor
#Tags - @Verify_GT_warning_message
#Tags - @Close_PID_tab_in_GT
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDPVSPOPGP_CG_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor
#Tags - @Verify_GT_warning_message
#Tags - @Close_PID_tab_in_GT


###############################################################################################