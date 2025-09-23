Feature: 95416 - To Test the Failure of Manage, Forgot & Clear Passwords for M580 ePAC CyberSecurity enabled controller

################################################################################################################################
#Execution order for TC - 95416
###################################################################### 

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