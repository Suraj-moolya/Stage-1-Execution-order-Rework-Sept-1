Feature: 90820-To Test the Instance Data Status in Application explorer with PostGre SQL

@@TC_EPE_AE_PGSQL_90820
Scenario Outline: Validate the instance window when the identifier is renamed with special characters
When I double click on template Identifier in application browser as '<Templates browser3>'
Then Verify the status of Identifier in application browser with instance editor window
When I Close instance editor tab Instance editor close in application explorer as '<Templates browser3>'
When I rclick application browser template AE Application browser in application explorer as '<Templates browser2>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I clicked Enter in keyboard shortcut
When I double click on template Identifier in application browser as '<Name1>'
Then Verify the status of Identifier in application browser with instance editor window
And Verify the details of invalid status in isntance editor window in Application Browser
When I Close instance editor tab Instance editor close in application explorer as '<Name1>'


@validate_special_chars
Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser5 | Name1      | Templates browser3 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | Rename               | MotorGP_@# | MotorGP_1          |
  
  
@@TC_EPE_AE_PGSQL_90820a
Scenario Outline: Validate the instance window when the identifier is renamed with either just numeric value or long value
When I rclick application browser template AE Application browser in application explorer as '<Templates browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser>' 
And I Rename the Insatnce to the requirement '<ReName>'
And I clicked Enter in keyboard shortcut
When I double click on template Identifier in application browser as '<ReName>'
Then Verify the status of Identifier in application browser with instance editor window
When I Close instance editor tab Instance editor close in application explorer as '<ReName>'
When I rclick application browser template AE Application browser in application explorer as '<Templates browser2>'
And I Select context menu item EC Application browser in application explorer as '<Application browser>' 
And I Rename the Insatnce to the requirement '<ReName1>'
And I clicked Enter in keyboard shortcut
When I double click on template Identifier in application browser as '<ReName1>'
Then Verify the status of Identifier in application browser with instance editor window
And Verify the details of invalid status in isntance editor window in Application Browser
When I Close instance editor tab Instance editor close in application explorer as '<ReName1>'

@validate_numeric_long_value
Examples:
  | SlNo. | Templates browser            | Application browser | ReName    | ReName1             | Templates browser2 |
  | 1     | MotorGP_@#$$1.0.123          | Rename              | MotorGP_1 | MotorGP_1qwertyuiop | MotorGP$$1.0.123   |
  | 2     | MotorGP_1qwertyuiop$$1.0.123 | Rename              | MotorGP_1 | 123456              | MotorGP$$1.0.123   |