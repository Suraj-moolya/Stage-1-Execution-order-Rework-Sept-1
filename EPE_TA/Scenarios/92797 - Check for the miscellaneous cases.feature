Feature: 92797 - Check for the miscellaneous cases

@TC_EPE_GT_PGSQL_92797_01
Scenario Outline: Open GT Search templates and open in edit mode
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'   
And I Select context menu item EC global template core in global template explorer as '<global template core1>'
And I Click on fit to content button in global template explorer
Then I verify that I have navigated to the '<tabname1>'

@select_template_and_navigate_to_edit_mode_in_MOtorGP
Examples:
  | SlNo. | Templates browser         | global template core1 | tabname1 |
  | 1     | MotorGP$$MotorGP$$1.0.123 | Edit                  | MotorGP  |
  
  
@TC_EPE_GT_PGSQL_92797_02
Scenario Outline: Open module from template in edit mode in Composite editor
When I right click on '<Description>' module in templates composite editor window
And I Select context menu item EC global template core in global template explorer as '<global template core2>'
And I Click on fit to content button in global template explorer
Then I verify that I have navigated to the '<tabname2>'

Examples:
  | SlNo. | Description       | global template core2 | tabname2 |
  | 1     | Control Composite | Edit                  | MotorGP  |
  
@TC_EPE_GT_PGSQL_92797_03
Scenario Outline: Verify the tooltip of the connecter with the text
When I check no of links between source and targets as '<connectorname>'
Then I check the tooltip of the connecter with controltext as '<connectortext>'

Examples:
  | SlNo. | connectortext                 | connectorname   |
  | 1     | ...tor\Logic\ILCKSignals\ILCK | Fail\$Selection |  