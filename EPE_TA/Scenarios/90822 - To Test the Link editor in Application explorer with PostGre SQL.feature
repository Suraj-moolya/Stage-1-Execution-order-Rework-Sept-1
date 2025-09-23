Feature: 90822 - To Test the Link editor in Application explorer with PostGre SQL


@TC_EPE_AE_PGSQL_90822_1
Scenario Outline: Verify the zoom buttons are visible the Link Editor
Then The Zoom button is visible in the bottom of Link Editor screen in Application Broswer as '<zoom_values>'

@verify_zoom_buttons
Examples:
  | SlNo. | zoom_values                     | 
  | 1     | Zoom In (+)                    |
  |2      | Zoom Out (-)| 
  |3      |Fit to content  (Ctrl + 0)|
  |4      |Zoom 100%|

  
@TC_EPE_AE_PGSQL_90822_2
Scenario Outline: Verify the options of the instance in the link editor and select a value to filter the instance
Then I verify the context options of instance of Link Editor screen in Application Browser as '<context_values>'
Then I select a value from context option to filter the values of instance of link editor screen in Application Broswer as '<drpdwn_value>'

@verify_context_value
Examples:
  | SlNo. | context_values                                                          | drpdwn_value |
  |1      |Properties, View Assignments,Hide Unbound,Hide Disabled$$AnalogOutputGP_1|AnalogOutputGP_1$$Hide Unbound|
  
  


  
#@Template_for_link_editor
#@Opening_Link_Editor_90822
#@drag_drop_link_editor



