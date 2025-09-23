Feature: 92696 - To Test the context menu options of Ref or Def, toolbox items, graphical links and workspace at Interface editor in read only mode & edit mode

Scenario Outline: Right click on Element and select menuitem in Facet Editor
When I Right Click on Element in global template explorer as '<element>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'

@RClick_DISignal_UL_TSDISignalVar_click_on_View
Examples:
  | SlNo. | element       | menu item |
  | 1     | TSDISignalVar | View      |
  
@RClick_DISignal_UL_TSDISignalVar_click_on_Edit
Examples:
  | SlNo. | element       | menu item |
  | 1     | TSDISignalVar | Edit      |
  
Scenario Outline: Drag and drop toolbox transformation item and verify its context menu in Interface Editor
When I drag and drop toolbox item in Interface Editor as '<toolboxitem>'
And I RClick on toolbox transformation item in Interface Editor as '<toolboxitem>'
Then verify context menu items from Rclick menu items in system explorer

@Drag_drop_Interface_Editor_Toolbox_item_verify_context_menu 
Examples:
  | SlNo. | toolboxitem |
  | 1     | Concat      |
  
Scenario Outline: Verify the context menu of Graphical link in Interface Editor
When I RClick on graphical link in Interface Editor
Then verify context menu items from Rclick menu items in system explorer

@RClick_and_verify_context_menu_of_link_in_interface_editor
Examples:
  | SlNo. |
  | 1     |

  
  

###############################################################################################################################
#Execution order for TC_92696
########################################################################################

#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_MotorGP_View_and_Open_Composite_Editor_in_GT
#Tags - @RClick_MotorGP_Control_click_on_View
#Tags - @RClick_DISignal_UL_click_on_View
#Tags - @Find_and_Navigate_to_TSDISignalVar_in_GTE_Editor_of_Motor_UC
#Tags - @RClick_DISignal_UL_TSDISignalVar_click_on_View
#Tags - @Verify_Copy_unavailable_for_Interface_Editor_window
#Tags - @Verify_GT_warning_message_in_Toolbox_of_Interface_Editor
#Tags - @Verify_context_menu_items_of_GTE_Editor_workspace
#Tags - @RClick_and_verify_context_menu_of_link_in_interface_editor
#Tags - @Close_Bool_tab_in_GT
#Tags - @Close_DISignal_tab_in_GT
#Tags - @Close_Motor_tab_in_GT
#Tags - @Close_Motor_tab_in_GT
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_MotorGP_Edit_and_Open_Composite_Editor_in_GT
#Tags - @RClick_MotorGP_Control_click_on_Edit
#Tags - @RClick_DISignal_UL_click_on_Edit
#Tags - @Find_and_Navigate_to_TSDISignalVar_in_GTE_Editor_of_Motor_UC
#Tags - @RClick_DISignal_UL_TSDISignalVar_click_on_Edit
#Tags - @Verify_Copy_unavailable_for_Interface_Editor_window
#Tags - @Drag_drop_Interface_Editor_Toolbox_item_verify_context_menu
#Tags - @Verify_context_menu_items_of_GTE_Editor_workspace
#Tags - @RClick_and_verify_context_menu_of_link_in_interface_editor
#Tags - @Close_Bool_tab_in_GT_with_save_pop_up
#Tags - @Close_DISignal_tab_in_GT
#Tags - @Close_Motor_tab_in_GT
#Tags - @Close_Motor_tab_in_GT

##############################################################################################