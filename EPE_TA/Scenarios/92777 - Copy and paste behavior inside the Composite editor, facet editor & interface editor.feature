Feature: 92777 - Copy and paste behavior inside the Composite editor, facet editor & interface editor

# @Search_Template_PIDGP_UC_Edit_and_Open_Composite_Editor_in_GT

Scenario Outline: Copy Paste block in same Composite Editor window
When I Right Click on Element in global template explorer as '<element>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item1>'
And I Select Submenu item from Context menu of toolbar in GT as '<submenu>'

@Copy_Paste_PID_block_in_same_level_Composite_Editor
Examples:
  | SlNo. | menu item | Toolbar          | menu item1 | submenu | element |
  | 1     | Copy      | Global Templates | Edit       | Paste   | PID     |
  

Scenario Outline: Copy Paste block in different Composite Editor window
When I Right Click on Element in global template explorer as '<element>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
When I Right Click on Element in global template explorer as '<element1>'
And I Select context menu item EC global template core in global template explorer as '<menu item1>'
And I Click on fit to content button in global template explorer
And I Click on Editor toolbar in global template explorer as '<Toolbar>'
And I Select context menu item EC global template core in global template explorer as '<menu item1>'
And I Select Submenu item from Context menu of toolbar in GT as '<submenu>'

@Copy_Paste_Interlocks_block_in_different_level_Composite_Editor
Examples:
  | SlNo. | menu item | menu item1 | Toolbar          | submenu | element    | element1 |
  | 1     | Copy      | Edit       | Global Templates | Paste   | Interlocks | PID      |
  
# @Search_Template_PIDCTLGP_UL_Edit_and_Open_Composite_Editor_in_GT
  
Scenario Outline: Verify Copy disabled for Element in Facet Editor window    
When I Right Click on Element in global template explorer as '<element>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_Copy_disabled_for_Element_in_Facet_Editor_window
Examples:
  | SlNo. | element   |
  | 1     | PIDCTL_ST |
  
Scenario Outline: Verify Copy paste of Function in Facet Editor window
When I Right Click on Function in global template explorer as '<function>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Ctrl+V to paste the copied in the same Composite Editor window

@Verify_Copy_Paste_of_Function_in_Facet_Editor_window
Examples:
  | SlNo. | menu item | function    |
  | 1     | Copy      | FormatValue |
  
  
Scenario Outline: Find, Search and Navigate to block in GTE editor window  
When I Ctrl+F to search for the block in GTE Editor and enter search text as '<block>'
And I Right-Click on the searched block in Editor window as '<block>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'

@Find_and_Navigate_to_PVRanged_Interface_in_GTE_Editor
Examples:
  | SlNo. | block    | menu item |
  | 1     | PVRanged | Navigate  |
  
@Find_and_Navigate_to_Configuration_Data_Input_Value_in_GTE_Editor
Examples:
  | SlNo. | block                | menu item |
  | 1     | - Configuration Data | Navigate  |
  
@Find_and_Navigate_to_$Area_System_Parameter_in_GTE_Editor
Examples:
  | SlNo. | block | menu item |
  | 1     | $Area | Navigate  |
  
@Find_and_Navigate_to_TSDISignalVar_in_GTE_Editor_of_Motor_UC
Examples:
  | SlNo. | block         | menu item |
  | 1     | TSDISignalVar | Navigate  |
  
  
Scenario Outline: Verify Copy paste of Interface in Facet Editor window
When I Right Click on Element in global template explorer as '<element>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Ctrl+V to paste the copied in the same Composite Editor window

@Verify_Copy_Paste_of_interface_in_Facet_Editor_window
Examples:
  | SlNo. | menu item | element  |
  | 1     | Copy      | PVRanged |
  

Scenario Outline: Verify Copy paste of Input value in Facet Editor window
When I Right Click Input Value in global template explorer as '<input>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Ctrl+V to paste the copied in the same Composite Editor window

@Verify_Copy_Paste_of_Input_Value_in_Facet_Editor_window
Examples:
  | SlNo. | menu item | input                |
  | 1     | Copy      | - Configuration Data |
  
Scenario Outline: Verify Copy unavailable for System Parameter in Facet Editor window
When I Right Click System Parameter in global template explorer as '<param>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_Copy_unavailable_for_System_Parameter_in_Editor_window
Examples:
  | SlNo. | param |
  | 1     | $Area |
  
Scenario Outline: Verify Copy unavailable for Interface Editor window 
When I Right Click on block in Interface Editor in global template explorer as '<block>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_Copy_unavailable_for_Interface_Editor_window
Examples:
  | SlNo. | block |
  | 1     | Def   |
  
  
  
  
  
###########################################################################################
#Execution order for TC_92777
##############################################################

#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDGP_UC_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Copy_Paste_PID_block_in_same_level_Composite_Editor
#Tags - @Copy_Paste_Interlocks_block_in_different_level_Composite_Editor
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDCTLGP_UL_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Verify_Copy_disabled_for_Element_in_Facet_Editor_window
#Tags - @Verify_Copy_Paste_of_Function_in_Facet_Editor_window
#Tags - @Find_and_Navigate_to_PVRanged_Interface_in_GTE_Editor
#Tags - @Verify_Copy_Paste_of_interface_in_Facet_Editor_window
#Tags - @Find_and_Navigate_to_Configuration_Data_Input_Value_in_GTE_Editor
#Tags - @Verify_Copy_Paste_of_Input_Value_in_Facet_Editor_window
#Tags - @Find_and_Navigate_to_$Area_System_Parameter_in_GTE_Editor
#Tags - @Verify_Copy_unavailable_for_System_Parameter_in_Editor_window
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDStatus_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Select_All_Copy_Paste_using_Keys_in_GT_Composite_Editor
#Tags - @Verify_Copy_unavailable_for_Interface_Editor_window
#Tags - @Close_PID_tab_in_GT


#################################################################################################