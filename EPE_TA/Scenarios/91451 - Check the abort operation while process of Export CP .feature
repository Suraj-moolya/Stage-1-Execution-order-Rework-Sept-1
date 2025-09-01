Feature: 91451 - Check the abort operation while process of Export Control Project
 
 
@TC_EPE_CP_PGSQL_91451_001  
Scenario Outline: Check the abort operation while process of Export control project
When I Click on Abort button in Notification Panel
Then Verify notification panel message Notification Pannel in message box as '<content>'

@check_the_abort_message_displayed_in_notification_panel
Examples:
  | SlNo. | content                               |
  | 1     | Generate FBD Section (Not Successful) |
 