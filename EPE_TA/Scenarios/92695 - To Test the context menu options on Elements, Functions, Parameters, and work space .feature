Feature: 92695 - To Test the context menu options on Elements, Functions, Parameters, Interfaces, Values, Graphical links and work space at Composite editor & Facet editor in read only mode

Scenario Outline: Search Template, View and Open Composite Editor in GT
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser1>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Close tab items EC main screen in engineering client as 'Global'
And I Click on fit to content button in global template explorer

@Search_Template_PIDGP_View_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1    | menu item |
  | 1     | PIDGP$$PIDGP$$1.0.153 | View      |
  
@Search_Template_PIDGP_UC_View_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1           | menu item |
  | 1     | $PIDGP_UC$$$PIDGP_UC$$1.0.98 | View      |
  
@Search_Template_PIDGP_CS_View_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1            | menu item |
  | 1     | $PIDGP_CS$$$PIDGP_CS$$1.0.117 | View      |
  
@Search_Template_MotorGP_View_and_Open_Composite_Editor_in_GT
Examples:
  | SlNo. | Templates browser1          | menu item |
  | 1     | $MotorGP$$$MotorGP$$1.0.123 | View      |
  
  
Scenario Outline: Right click on Element and View in Composite Editor
When I Right Click on Element in global template explorer as '<element>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on fit to content button in global template explorer

@RClick_MotorGP_Control_click_on_View
Examples:
  | SlNo. | element | menu item |
  | 1     | Control | View      |
  
@RClick_DISignal_UL_click_on_View
Examples:
  | SlNo. | element | menu item |
  | 1     | Running | View      |
  
@RClick_MotorGP_Control_click_on_Edit
Examples:
  | SlNo. | element | menu item |
  | 1     | Control | Edit      |
  
@RClick_DISignal_UL_click_on_Edit
Examples:
  | SlNo. | element | menu item |
  | 1     | Running | Edit      |

  
Scenario Outline: Verify context menu items of Elements in Composite Editor
When I Right Click on Element in global template explorer as '<element>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_context_menu_items_of_Element_in_PIDGP
Examples:
  | SlNo. | element |
  | 1     | Control |
  
@Verify_context_menu_items_of_Interface_in_PIDGP  
Examples:
  | SlNo. | element   |
  | 1     | GroupData |
  
@Verify_context_menu_items_of_Element_in_PIDGP_UC
Examples:
  | SlNo. | element |
  | 1     | PID     |
  
@Verify_context_menu_items_of_Interface_in_PIDGP_UC
Examples:
  | SlNo. | element |
  | 1     | ILCK    |
  
@Verify_context_menu_items_of_Element_in_PIDGP_CS
Examples:
  | SlNo. | element |
  | 1     | Data    |
  
@Verify_context_menu_items_of_Interface_in_PIDGP_CS
Examples:
  | SlNo. | element   |
  | 1     | PIDStatus |
  
@Verify_context_menu_items_of_Element_in_MotorGP_DISignal_UL_Facet_Editor
Examples:
  | SlNo. | element           |
  | 1     | DISignalErrorBOOL |
 

Scenario Outline: Verify context menu items of Functions in Composite Editor
When I Right Click on Function in global template explorer as '<function>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_context_menu_items_of_Function_in_PIDGP
Examples:
  | SlNo. | function     |
  | 1     | CrDocument_1 |
  
@Verify_context_menu_items_of_Function_in_PIDGP_UC
Examples:
  | SlNo. | function  |
  | 1     | Interlock |
  
@Verify_context_menu_items_of_Function_in_PIDGP_CS
Examples:
  | SlNo. | function |
  | 1     | Name     |
  
@Verify_context_menu_items_of_Function_in_MotorGP_DISignal_UL_Facet_Editor
Examples:
  | SlNo. | function |
  | 1     | If_10    |
  
 
Scenario Outline: Verify context menu items of Input Values in Composite Editor 
When I Right Click Input Value in global template explorer as '<input>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_context_menu_items_of_Input_Value_in_PIDGP
Examples:
  | SlNo. | input                                    |
  | 1     | PID Controller Control Module User Guide |
  
@Verify_context_menu_items_of_Input_Value_in_PIDGP_UC
Examples:
  | SlNo. | input |
  | 1     | - MUX |
  
@Verify_context_menu_items_of_Input_Value_in_PIDGP_CS
Examples:
  | SlNo. | input |
  | 1     | PID   |
  
  
Scenario Outline: Verify context menu items of GTE Editor workspace
When I Right Click on workspace in global template explorer
Then verify context menu items from Rclick menu items in system explorer

@Verify_context_menu_items_of_GTE_Editor_workspace
Examples:
  | SlNo. |
  | 1     |
  
  
Scenario Outline: Verify the context menu options on deferred parameters(grey hexagons)
When I Right Click on Grey Hexagon in global template explorer as '<hexa>'
Then verify context menu items from Rclick menu items in system explorer
  
@Verify_context_menu_items_of_grey_hexagon_in_PIDGP_UC
Examples:
  | SlNo. | hexa                  |
  | 1     | Force Remote Setpoint |
  
@Verify_context_menu_items_of_grey_hexagon_in_PIDGP_CS
Examples:
  | SlNo. | hexa        |
  | 1     | Normal Mode |
  
  
Scenario Outline: Verify the context menu options on deferred interfaces(orange hexagons)
When I Right Click on Orange Hexagon in global template explorer as '<hexa1>'
Then verify context menu items from Rclick menu items in system explorer

@Verify_context_menu_items_of_orange_hexagon_in_PIDGP
Examples:
  | SlNo. | hexa1                                |
  | 1     | c19cd02e-9848-4829-9525-4693115aaa9b |
  
@Verify_context_menu_items_of_orange_hexagon_in_PIDGP_UC
Examples:
  | SlNo. | hexa1                                |
  | 1     | aaa096b7-0ab0-4748-89bb-b602166735f6 |
  

Scenario Outline: Verify the context menu of Graphical link in Composite Editor
When I RClick on graphical link in Composite Editor as '<identifier>'
Then verify context menu items from Rclick menu items in system explorer

@RClick_and_verify_context_menu_of_link_in_composite_editor_PIDGP
Examples:
  | SlNo. | identifier |
  | 1     | PIDStatus  |


  
  
  
####################################################################################################################
#Execution order for TC_92695
##############################################################

#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDGP_View_and_Open_Composite_Editor_in_GT
#Tags - @Verify_context_menu_items_of_Element_in_PIDGP
#Tags - @Verify_context_menu_items_of_Function_in_PIDGP
#Tags - @RClick_and_verify_context_menu_of_link_in_composite_editor_PIDGP
#Tags - @Verify_context_menu_items_of_Interface_in_PIDGP
#Tags - @Verify_Copy_unavailable_for_System_Parameter_in_Editor_window
#Tags - @Verify_context_menu_items_of_Input_Value_in_PIDGP
#Tags - @Verify_context_menu_items_of_GTE_Editor_workspace
#Tags - @Verify_context_menu_items_of_orange_hexagon_in_PIDGP
#Tags - @Close_PID_tab_in_GT
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDGP_UC_View_and_Open_Composite_Editor_in_GT
#Tags - @Verify_context_menu_items_of_Element_in_PIDGP_UC
#Tags - @Verify_context_menu_items_of_Interface_in_PIDGP_UC
#Tags - @Verify_context_menu_items_of_Function_in_PIDGP_UC
#Tags - @Verify_context_menu_items_of_Input_Value_in_PIDGP_UC
#Tags - @Verify_context_menu_items_of_GTE_Editor_workspace
#Tags - @Verify_context_menu_items_of_grey_hexagon_in_PIDGP_UC
#Tags - @Verify_context_menu_items_of_orange_hexagon_in_PIDGP_UC
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_PIDGP_CS_View_and_Open_Composite_Editor_in_GT
#Tags - @Verify_context_menu_items_of_Element_in_PIDGP_CS
#Tags - @Verify_context_menu_items_of_Interface_in_PIDGP_CS
#Tags - @Verify_context_menu_items_of_grey_hexagon_in_PIDGP_CS
#Tags - @Verify_context_menu_items_of_Input_Value_in_PIDGP_CS
#Tags - @Verify_context_menu_items_of_Function_in_PIDGP_CS
#Tags - @Close_PIDGP_tab_in_GT_with_save_pop_up
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_MotorGP_View_and_Open_Composite_Editor_in_GT
#Tags - @RClick_MotorGP_Control_click_on_View
#Tags - @RClick_DISignal_UL_click_on_View
#Tags - @Verify_context_menu_items_of_Element_in_MotorGP_DISignal_UL_Facet_Editor
#Tags - @Verify_context_menu_items_of_Function_in_MotorGP_DISignal_UL_Facet_Editor
#Tags - @Verify_context_menu_items_of_GTE_Editor_workspace
#Tags - @Close_DISignal_tab_in_GT
#Tags - @Close_Motor_tab_in_GT
#Tags - @Close_Motor_tab_in_GT


######################################################################################################################