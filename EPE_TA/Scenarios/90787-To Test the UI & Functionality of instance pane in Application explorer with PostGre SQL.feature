Feature: 90787-To Test the UI & Functionality of instance pane in Application explorer with PostGre SQL

@TC_EPE_AE_PGSQL_90787
Scenario Outline: Validate the identifiers are locked when opened
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
When I rclick application browser template AE MotorGP template in application explorer as '<Templates browser2>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC Application browser in application explorer as '<Application browser5>'
Then Verify template instance editor Instance Editor in application explorer as '<Templates browser2>'
Then Verify the instance is locked in Application browser when opened as '<Templates status>'

@verify_identifer_locked
Examples:
  | SlNo. | Templates browser1 | Templates browser2     | Application browser5 | Templates status|
  | 1     | Analog             | AnalogInputGP$$1.0.138 | Properties           | Analog$$locked|
  | 2     | ValveGP            | ValveGP$$1.0.100       | Properties           | ValveGP$$locked|
  
  
  
@TC_EPE_AE_PGSQL_90787a  
Scenario Outline: Verify the column name and mutiple windows are opened
Then Verify mutiple instances can be opened in Application browser
Then Verify the column names in Application Browser '<Column_Names>'

@verify_column_names
Examples:
  | SlNo. | Column_Names                                     |
  | 1     | Name$$Description$$Template$$Version             | 
  

@TC_EPE_AE_PGSQL_90787b  
Scenario Outline: Verify the * symbol before and after clicking on save button 
Then Verify the * symbol is reflected when istance is modified in Application Browser '<Template_Name>'

@verify_*_symbol
Examples:
  | SlNo. | Template_Name                |
  | 1     | LocalPanel$$1$$ValveGP$$No   | 
  | 2     | LocalPanel$$1$$ValveGP$$save |
  