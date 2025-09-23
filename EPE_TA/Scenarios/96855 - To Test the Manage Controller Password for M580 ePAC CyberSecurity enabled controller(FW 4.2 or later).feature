Feature: 96855 - To Test the Manage Controller Password for M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)

Scenario Outline: Select Contoller context menu option 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'

@open_manage_password_M580_Standalone_ePAC_CyberSecurity
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Manage Password         |
@open_forget_password_M580_Standalone_ePAC_CyberSecurity
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Forgot Password         |
@open_clear_password_M580_Standalone_ePAC_CyberSecurity
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Clear Password          |

  
Scenario Outline: Check manage password for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
When I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 

@set_controller_password_to_Schneider1!
Examples:
  | SlNo. | New Password box1     | Confirm Password box2         | Modification popup3 | Message     |
  | 1     | Password$$Schneider1! | Confirm Password$$Schneider1! | OK                  | (Completed) |

  
Scenario Outline: Check Update manage password for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
When I Enter Controller Password TE New Password box in topology as '<Old Password box1>'
And I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 

@update_controller_password_to_Schneider0!_from_Schneider1!
Examples:
  | SlNo. | Old Password box1             | New Password box1     | Confirm Password box2         | Modification popup3 | Message     |
  | 1     | Current Password$$Schneider1! | Password$$Schneider0! | Confirm Password$$Schneider0! | OK                  | (Completed) |

  
Scenario Outline: Clear Password for controller
When I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box1>'
And I Click on buttons in pop up message as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup2>'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 

@Clear_controller_password_Schneider0!
Examples:
  | SlNo. | Confirm Password box1         | Modification popup2 | Message     |
  | 1     | Current Password$$Schneider0! | OK                  | (Completed) |

  
Scenario Outline: Check Forgot password for controller
Then Verify forgot password Authentication Code Export popup in message box
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as '<Button>'

@Check_forgot_password_authentication_code
Examples:
  | SlNo. | Button |
  | 1     | OK     |
  
#@open_manage_password_M580_Standalone_ePAC_CyberSecurity
#@Check_failure_controller_password_does_not_match
#@set_controller_password_to_Schneider1!

#@open_manage_password_M580_Standalone_ePAC_CyberSecurity
#@check_failure_update_controller_password_from_Schneider1!_same_new_pass,wrong_confirm_pass
#@verify_controller_password_failure_new_and_confirm_password
#@check_failure_update_controller_password_by_passing_wrong_password
#@verify_controller_password_failure_for_current_password
#@update_controller_password_to_Schneider0!_from_Schneider1!

#@open_forget_password_M580_Standalone_ePAC_CyberSecurity
#@Check_forgot_password_authentication_code


############ Use clear password once all requirement TCs are executed in Order ##########
#@open_clear_password_M580_Standalone_ePAC_CyberSecurity
#@Clear_controller_password_failure_Wrong_pass
#@verify_controller_password_failure_for_current_password
#@Clear_controller_password_Schneider0!
