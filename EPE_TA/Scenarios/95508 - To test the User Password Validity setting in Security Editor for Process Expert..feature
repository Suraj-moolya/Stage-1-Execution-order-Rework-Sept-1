Feature: 95508 - To test the User Password Validity setting in Security Editor for Process Expert.

#Pre-Requisites:
#1. EPE 2025 - V4.9.0.XXXX is installed with at least System server should be installed. 
#2. Security Editor is logged in with "Security Administrator" Eg. 'SecurityAdmin'. 
#3. Create users in Security Editor with different process expert roles.

@TC_EPE_SE_95508_001
Scenario Outline: Navigate to policies page tab and check the default setting 

When I select a page tab in security editor window as '<Identifier>'
When I verify the text checkbox value as '<Identifier1>'
And I select a value from the dropdown in policies page tab as '<Identifier2>'
And I verify the login radio button as '<Identifier3>' 
And I verify the password validity button in policies tab in security editor window as '<param>'
And I select a button in policies tab in security editor window as '<Identifier4>'
And I verify the textbox value in policies tab in security editor window as '<value>'

@NAVIGATE_to_POLICIES_tab_check_default_settings_PROCESS_EXPERT
Examples:
  | SlNo. | Identifier | Identifier1    | Identifier2    | Identifier3                  | param                       | Identifier4              | value |
  | 1     | Policies   | Process Expert | Process Expert | Security on, mandatory login | Password validity period$$1 | Password validity period | 365   |
  
@TC_EPE_SE_95508_002
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
  | 1     | User information | User2     | Process Expert | Valid until the 23-11-2025 14:15:09 | Moolyase@123 | Apply       | Password successfully modified! | OK          | Valid until the 28-11-2025 02:34:20 |
