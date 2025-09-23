Feature: 94038 - To Test the Manage Controller Password for M580 ePAC CyberSecurity enabled controller(FW 4.2 or later)



################################################################################################################################
#Execution order for TC - 94038
###################################################################### 

#Scenario Outline: Select Contoller context menu option
#Tags-@open_manage_password_M580_Standalone_ePAC_CyberSecurity
#Tags-@pen_forget_password_M580_Standalone_ePAC_CyberSecurity
#Tags-@open_clear_password_M580_Standalone_ePAC_CyberSecurity 
#Scenario Outline: Check manage password for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
#Tags-@set_controller_password_to_Schneider1! 
#Scenario Outline: Check Update manage password for M580 ePAC CyberSecurity enabled controller FW 4.2 or later
#Tags-@update_controller_password_to_Schneider0!_from_Schneider1!
#Scenario Outline: Clear Password for controller
#Tags-@Clear_controller_password_Schneider0!
#Scenario Outline: Check Forgot password for controller
#Tags-@Check_forgot_password_authentication_code
#Tags-@open_manage_password_M580_Standalone_ePAC_CyberSecurity
#Tags-@Check_failure_controller_password_does_not_match
#Tags-@set_controller_password_to_Schneider1!

#Tags-@open_manage_password_M580_Standalone_ePAC_CyberSecurity
#Tags-@check_failure_update_controller_password_from_Schneider1!_same_new_pass,wrong_confirm_pass
#Tags-@verify_controller_password_failure_new_and_confirm_password
#Tags-@check_failure_update_controller_password_by_passing_wrong_password
#Tags-@verify_controller_password_failure_for_current_password
#Tags-@update_controller_password_to_Schneider0!_from_Schneider1!

#Tags-@open_forget_password_M580_Standalone_ePAC_CyberSecurity
#Tags-@Check_forgot_password_authentication_code


############ Use clear password once all requirement TCs are executed in Order ##########
#@open_clear_password_M580_Standalone_ePAC_CyberSecurity
#@Clear_controller_password_failure_Wrong_pass
#@verify_controller_password_failure_for_current_password
#@Clear_controller_password_Schneider0!








