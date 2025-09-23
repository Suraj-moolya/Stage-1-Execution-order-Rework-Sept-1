Feature: 96858 - To Test the Failure of Manage, Forgot & Clear Passwords for M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)


Scenario Outline: Check manage password failure for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
When I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'
Then I verify the controller manage password failure message as '<Fail Message>'

@Check_failure_controller_password_does_not_match
Examples:
  | SlNo. | New Password box1     | Confirm Password box2      | Modification popup3 | Btn    | Fail Message                     |
  | 1     | Password$$Schneider0! | Confirm Password$$Moolya2! | OK                  | Cancel | Confirm Password$$does not match |
  
  
Scenario Outline: Check Update manage password failure for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
When I Enter Controller Password TE New Password box in topology as '<Old Password box1>'
And I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'

@check_failure_update_controller_password_from_Schneider1!_same_new_pass,wrong_confirm_pass
Examples:
  | SlNo. | Old Password box1             | New Password box1     | Confirm Password box2       | Modification popup3 |
  | 1     | Current Password$$Schneider1! | Password$$Schneider1! | Confirm Password$$NimAjji0! | OK                  |
@check_failure_update_controller_password_by_passing_wrong_password
Examples:
  | SlNo. | Old Password box1           | New Password box1     | Confirm Password box2         | Modification popup3 |
  | 1     | Current Password$$NakkanLey | Password$$Schneider0! | Confirm Password$$Schneider0! | OK                  |

  
Scenario Outline: Clear Password failure for controller
When I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box1>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup2>' 

@Clear_controller_password_failure_Wrong_pass
Examples:
  | SlNo. | Confirm Password box1       | Modification popup2 |
  | 1     | Current Password$$Byaavarsi | OK                  |
  
  
Scenario Outline: Verify Password failure for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
Then I verify the controller manage password failure message as '<Message>'

@verify_controller_password_failure_new_and_confirm_password
Examples:
  | SlNo. | Message                          |
  | 1     | Password$$cannot be same         |
  | 2     | Confirm Password$$does not match |
@verify_controller_password_failure_for_current_password
  Examples:
    | SlNo. | Message                          |
    | 1     | Current Password$$Wrong password |
@verify_controller_password_failure_for_current_password
  Examples:
    | SlNo. | Message                          |
    | 1     | Current Password$$Wrong password |
    
        
    





