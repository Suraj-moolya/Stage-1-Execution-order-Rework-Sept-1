Feature: 95507 - To test the User Password Validity setting in Security Editor for Control Expert.

#Pre-Requisites:
#1. EPE 2025 - V4.9.0.XXXX is installed with at least System server should be installed. 
#2. Security Editor is logged in with "Security Administrator" Eg. 'SecurityAdmin'. 
#3. Create users in Security Editor with different process expert roles.

@TC_EPE_SE_95507_001
Scenario Outline: Navigate to policies page tab and check the default setting 

When I select a page tab in security editor window as '<Identifier>'
When I verify the text checkbox value as '<Identifier1>'
And I verify the login radio button as '<Identifier2>' 
And I verify the password validity button in policies tab in security editor window as '<param>'
And I select a button in policies tab in security editor window as '<Identifier3>'
And I verify the textbox value in policies tab in security editor window as '<value>'

@NAVIGATE_to_POLICIES_tab_check_default_settings_CONTROL_EXPERT
Examples:
  | SlNo. | Identifier | Identifier1    | Identifier2                  | param                       | Identifier3              | value |
  | 1     | Policies   | Control Expert | Security on, mandatory login | Password validity period$$0 | Password validity period | 365   |

@TC_EPE_SE_95507_002
Scenario Outline: Modify the default setting value and provide a invalid setting value

When I edit a textbox value in policies tab in security editor window as '<value>' 
And I select a button in policies tab in security editor window as '<Identifier>'
And I verify the static message in security editor window as '<Identifier1>'
And I select a button in security editor window as '<Identifier2>'
And I verify the textbox value in policies tab in security editor window as '<value1>'

@MODIFY_the_password_validity_period_setting_as_366_days
Examples:
  | SlNo. | value | Identifier | Identifier1                                                            | Identifier2 | value1 |
  | 1     | 366   | Apply      | Password validity period duration shall be in the range 90 to 365 days | OK          | 365    |

@MODIFY_the_password_validity_period_setting_as_89_days  
Examples:
  | SlNo. | value | Identifier | Identifier1                                                            | Identifier2 | value1 |
  | 1     | 89    | Apply      | Password validity period duration shall be in the range 90 to 365 days | OK          | 365    |


@TC_EPE_SE_95507_003
Scenario Outline: Modify the default setting value and check the setting value without clicking apply

When I verify the textbox value in policies tab in security editor window as '<value>'
And I edit a textbox value in policies tab in security editor window as '<value1>'
And I select a page tab in security editor window as '<Identifier>'
And I select a page tab in security editor window as '<Identifier1>'
And I verify the textbox value in policies tab in security editor window as '<value>'

@MODIFY_the_value_without_clicking_apply
Examples:
  | SlNo. | value | value 1 | Identifier       | Identifier1 |
  | 1     | 365   | 200     | User information | Policies    |
  
@TC_EPE_SE_95507_004
Scenario Outline: Modify the default setting value and provide a valid setting value

When I edit a textbox value in policies tab in security editor window as '<value>'
And I select a button in policies tab in security editor window as '<Identifier>'
And I verify the textbox value in policies tab in security editor window as '<value>'

@MODIFY_the_password_validity_period_setting_as_90_days
Examples:
  | SlNo. | value | Identifier |
  | 1     | 90    | Apply      |
  
@MODIFY_the_password_validity_period_setting_as_180_days
Examples:
  | SlNo. | value | Identifier |
  | 1     | 180   | Apply      |
  
@MODIFY_the_password_validity_period_setting_as_360_days
Examples:
  | SlNo. | value | Identifier |
  | 1     | 360   | Apply      |

@TC_EPE_SE_95507_005

Scenario Outline: Navigate to user information page tab and modify the setting 
When I select a page tab in security editor window as '<Identifier>'
And I select a value from the username dropdown in user information page tab as '<user_name>'
And I select a value from the product dropdown in user information page tab as '<product_name>'
And I verify the static message in security editor window as '<Identifier3>'
When I edit the textbox1 value in user information tab in security editor window as '<value>'
And I edit the textbox2 value in user information tab in security editor window as '<value>'
And I select a button in user information tab in security editor window as '<Identifier4>'
And I verify the static message in security editor window as '<Identifier5>'
And I select a button in security editor window as '<Identifier6>'
And I verify the static message in security editor window as '<Identifier7>'

@NAVIGATE_to_USER_INFORMATION_tab_MODIFY_default_settings
Examples:
  | SlNo. | Identifier       | user_name | product_name   | Identifier3                         | value        | Identifier4 | Identifier5                     | Identifier6 | Identifier7                         |
  | 1     | User information | User1     | Control Expert | Valid until the 23-11-2025 14:15:09 | Moolyase@123 | Apply       | Password successfully modified! | OK          | Valid until the 28-11-2025 02:34:20 |


@TC_EPE_SE_95507_006
Scenario Outline: Login using valid credentials in security editor
When I edit the textbox1 value in user information tab in security editor window as '<username>'
And I edit the textbox2 value in user information tab in security editor window as '<password>'
And I select a button in security editor window as '<button>'

@Logging_in_to_Security_Editor
Examples:
  | SlNo. | username      | password     | button |
  | 1     | SecurityAdmin | Moolyase@123 | Login  |