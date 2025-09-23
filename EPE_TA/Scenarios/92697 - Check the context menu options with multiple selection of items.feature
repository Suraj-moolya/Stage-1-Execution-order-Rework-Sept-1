Feature: 92697 - Check the context menu options with multiple selection of items

Scenario Outline: Select multiple items in DigitalInput_UC, right click on item and verify context menu in GTE Editor
When I select multiple items from the Editor window as '<multipleitems>'
And I Right Click on Element in global template explorer as '<element>'
Then verify context menu items from Rclick menu items in system explorer

#element$$function$$input$$interface$$sysparam

@Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_with_System_parameter
Examples:
  | SlNo. | multipleitems                            | element      |
  | 1     | DigitalInput$$Name$$_DInputGP$$PV$$$Area | DigitalInput |
  
@Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_without_System_parameter
Examples:
  | SlNo. | multipleitems                       | element      |
  | 1     | DigitalInput$$Name$$_DInputGP$$PV$$ | DigitalInput |
  
  
Scenario Outline: Select multiple items in DigitalInput_UC, right click on workspace and verify context menu in GTE Editor
When I select multiple items from the Editor window as '<multipleitems>'
And I Right Click on workspace in global template explorer
Then verify context menu items from Rclick menu items in system explorer

@Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_of_workspace
Examples:
  | SlNo. | multipleitems                       |
  | 1     | DigitalInput$$Name$$_DInputGP$$PV$$ |
  


Scenario Outline: Navigate to Area in DINPUTP_UL 
When I Select Document Outline in GTE Composite Edittor
Then I Double click element on Document Outline and verify that element in Composite Edittor as '<docoutline>'  

@Navigate_to_Area_in_DINPUTGP_UL
Examples:
  | SlNo. | element  | docoutline |
  | 1     | DINPUTGP | Area       |

    
Scenario Outline: Select multiple items in DINPUT_UL, right click on item and verify context menu in GTE Editor
And I select multiple items from the Editor window as '<multipleitems>'
And I Right Click on Element in global template explorer as '<element>'
Then verify context menu items from Rclick menu items in system explorer  

@Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_with_System_parameter
Examples:
  | SlNo. | multipleitems                     |
  | 1     | DINPUTGP$$$$$$DInputSignal$$$Area |
#DINPUTGP$$VariableName$$_PAR$$DInputSignal$$$Area

@Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_without_System_parameter
Examples:
  | SlNo. | multipleitems                |
  | 1     | DINPUTGP$$$$$$DInputSignal$$ |
  

Scenario Outline: Select multiple items in DINPUT_UL, right click on workspace and verify context menu in GTE Editor
And I select multiple items from the Editor window as '<multipleitems>'
When I Right Click on workspace in global template explorer
Then verify context menu items from Rclick menu items in system explorer

@Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_of_workspace
Examples:
  | SlNo. | multipleitems                |
  | 1     | DINPUTGP$$$$$$DInputSignal$$ |
  

  
  
  
  
#############################################################################################################
#Execution order for TC_92697
############################################################

#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_DigitalInputGP_UC_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_with_System_parameter
#Tags - @Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_without_System_parameter
#Tags - @Multiselect_items_in_Editor_of_DigitalInput_UC_and_Verify_context_menu_of_workspace
#Tags - @Close_DigitalInputGP_tab_in_GT
#Scenarios\EnginneringClient - Navigation to Global template Explorer(GTE)
#Tags - @Search_Template_DINPUTGP_UL_Edit_and_Open_Composite_Editor_in_GT
#Tags - @Navigate_to_Area_in_DINPUTGP_UL
#Tags - @Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_with_System_parameter
#Tags - @Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_without_System_parameter
#Tags - @Multiselect_items_in_Editor_of_DINPUT_UL_and_Verify_context_menu_of_workspace
#Tags - @Close_DINPUT_tab_in_GT

##############################################################################################################