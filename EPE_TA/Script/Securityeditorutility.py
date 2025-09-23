"""Securityeditorutility"""

# Imports
import datetime
import Applicationutility
from EngineeringClient import EngineeringClient
from ControlExpert import ControlExpert
from SecurityEditor import SecurityEditor

# Object Initialization
sed_obj = SecurityEditor()

###############################################################################
# Function   : launch_security_editor
# Description: Launches the Security Editor application and waits for it to load.
# Parameter  : None
###############################################################################
def launch_security_editor():
  TestedApps.SecEDT.Run()
  Applicationutility.wait_in_seconds(1000, 'wait')

###############################################################################
# Function : verify_the_dropdown_text_SE
# Description : Verifies if a dropdown in the Security Editor window 
#               displays or contains the given identifier text.
# Parameter : identifier (str) - Expected text to be verified in the dropdown(s).
# Example : verify_the_dropdown_text_SE("Control Expert")
###############################################################################
def verify_the_dropdown_text_SE(identifier):
  editor = sed_obj.editorwindow.object
  items = editor.FindAllChildren('WndClass','ComboBox',50)
  for item in items:
    if item.Enabled and item.wText == identifier:
      Log.Checkpoint(f'The displayed product is {identifier}')
      break
  else:
    Log.Error(f'{identifier} is not displayed')
    
def hufcef():
  verify_the_dropdown_text_SE('Control Expert')
    
###############################################################################
# Function : Click_on_a_dropdown_SE
# Description : Finds and clicks the first visible and enabled dropdown 
#               in the Security Editor window.
# Parameter : None
# Example : Click_on_a_dropdown_SE()
###############################################################################
def Click_on_a_dropdown_SE():
  editor = sed_obj.editorwindow.object
  items = editor.FindAllChildren('WndClass','ComboBox',50)
  for item in items:
    if item.Visible and item.Enabled:
        item.click()
        Log.Checkpoint('Clicked on product dropdown')
        break
  else:
    Log.Error('Product dropdown is not found')

###############################################################################
# Function : select_a_dropdown_value_policies_SE
# Description : Selects a specific value from the Product dropdown 
#               in the Security Editor -> Policies window.
# Parameter : identifier (str) - The product name to be selected from the dropdown.
# Example : select_a_dropdown_value_policies_SE("OSLoader")
###############################################################################    
def select_a_dropdown_value_policies_SE(identifier):
  Click_on_a_dropdown_SE()
  list = sed_obj.productlist.object
  list_items = list.FindAllChildren('ObjectType', 'ListItem', 50)
  for list_item in list_items:
    if list_item.Visible and list_item.Enabled:
      if list_item.Caption == identifier:
        list_item.click()
        Log.Checkpoint(f'The product {identifier} is selected')
        break
  else:
    Log.Error(f'The product {identifier} is not found')

###############################################################################
# Function   : select_a_dropdown_value_product_user_information_SE
# Description: Selects a given product from the dropdown in the 
#              User Information window of Security Editor.
# Parameter  : product_name (str) - The dropdown value to be selected.
# Example    : select_a_dropdown_value_product_user_information_SE("OSLoader")
###############################################################################    
def select_a_dropdown_value_product_user_information_SE(product_name):
  combobox = sed_obj.productdropdown.object
  if combobox.Exists:
    combobox.ClickItem(product_name)
    Log.Checkpoint(f'Clicked on {product_name}')
  else:
    Log.Error(f'{product_name} is not found')

###############################################################################
# Function   : select_a_dropdown_value_username_user_information_SE
# Description: Selects a given username from the dropdown in the 
#              User Information window of Security Editor.
# Parameter  : user_name (str) - The dropdown value to be selected.
# Example    : select_a_dropdown_value_username_user_information_SE("JohnDoe")
###############################################################################  
def select_a_dropdown_value_username_user_information_SE(user_name):
  combobox = sed_obj.usernamedropdown.object
  if combobox.Exists:
    combobox.ClickItem(user_name)
    Log.Checkpoint(f'Clicked on {user_name}')
  else:
    Log.Error(f'{user_name} is not found')

###############################################################################
# Function : verify_the_login_radiobutton_SE
# Description : Verifies if the specified radio button is selected in the 
#               Security Editor window.
# Parameter : identifier (str) - The caption of the radio button to verify.
# Example : verify_the_login_radiobutton_SE("Security on, avoidable login")
###############################################################################
def verify_the_login_radiobutton_SE(identifier):
  editor = sed_obj.securityeditorwindow.object
  items = editor.FindAllChildren('WndClass','Button',50)
  for item in items:
    if item.Exists and item.Visible:
      if item.wChecked == True and item.WndCaption == identifier:  
        Log.Checkpoint(f'{identifier} is checked')
        break
  else:
    Log.Error(f'{identifier} is not selected')

###############################################################################
# Function : select_a_button_security_editor_window
# Description : Clicks a button in the Security Editor window based on its caption.
# Parameter : identifier (str) - The caption of the button to be clicked.
# Example : select_a_button_security_editor_window("OK")
###############################################################################  
def select_a_button_security_editor_window(identifier):
  editor = sed_obj.editorwindow.object
  items = editor.FindAllChildren('WndClass','Button',50)
  for item in items:
    if item.Enabled and item.WndCaption == identifier:
      item.click()
      Log.Checkpoint(f'{identifier} is selected')
      break
  else:
    Log.Error(f'{identifier} is not selected')

###############################################################################
# Function : select_a_button_policies_security_editor_window
# Description : Clicks a button in the Security Editor -> Policies window 
#               based on its caption.
# Parameter : identifier (str) - The caption of the button to be clicked.
# Example : select_a_button_policies_security_editor_window("Apply")
###############################################################################  
def select_a_button_policies_security_editor_window(identifier):
  editor = sed_obj.policiestab.object
  items = editor.FindAllChildren('WndClass','Button',50)
  for item in items:
    if item.Enabled and item.Visible:
      if item.WndCaption == identifier:
       item.click()
       Log.Checkpoint(f'{identifier} is selected')
       break
  else:
    Log.Error(f'{identifier} is not selected')

###############################################################################
# Function : select_a_button_user_information_security_editor_window
# Description : Clicks a button in the Security Editor -> User Information window 
#               based on its caption.
# Parameter : identifier (str) - The caption of the button to be clicked.
# Example : select_a_button_user_information_security_editor_window("OK")
###############################################################################  
def select_a_button_user_information_security_editor_window(identifier):
  editor = sed_obj.userinformationtab.object
  items = editor.FindAllChildren('WndClass','Button',50)
  for item in items:
    if item.Enabled and item.Visible:
      if item.WndCaption == identifier:
       item.click()
       Log.Checkpoint(f'{identifier} is selected')
       break
  else:
    Log.Error(f'{identifier} is not selected')

###############################################################################
# Function : Edit_textbox_value_policies_SE
# Description : Updates the value of the first enabled textbox in the 
#               Security Editor -> Policies window.
# Parameter : value (str) - The new value to be entered in the textbox.
# Example : Edit_textbox_value_policies_SE("60")
###############################################################################  
def Edit_textbox_value_policies_SE(value):
  editor = sed_obj.policiestab.object
  items = editor.FindAllChildren('WndClass','Edit',50)
  for item in items:
    if item.Enabled and item.WndClass == 'Edit':
      item.wText = value
      Log.Checkpoint(f'The updated value is {value}')
      break
  else:
    Log.Error(f'{value} is not updated')

###############################################################################
# Function : Verify_textbox_value_policies_SE
# Description : Verifies that at least one enabled textbox in the 
#               Security Editor -> Policies window contains the expected value.
# Parameter : value (str) - The expected value of the textbox.
# Example : Verify_textbox_value_policies_SE("60")
###############################################################################  
def Verify_textbox_value_policies_SE(value):
  editor = sed_obj.policiestab.object
  for item in editor.FindAllChildren('WndClass', 'Edit', 50):
      if item.Enabled and item.WndClass == 'Edit':
        if item.wText == value:
          Log.Checkpoint(f'Verified: Textbox value is correctly set to "{value}"')
          break
  else:
    Log.Error(f'Verification failed: Expected value "{value}", but found "{item.wText}"')

###############################################################################
# Function : verify_static_message_security_editor_window
# Description : Verifies that a static message (label/text) is displayed 
#               in the Security Editor window.
# Parameter : identifier (str) - The expected static message text.
# Example : verify_static_message_security_editor_window("Password validity period duration shall be in the range 90 to 365 days")
###############################################################################
def verify_static_message_security_editor_window(identifier):
  editor = sed_obj.editorwindow.object
  items = editor.FindAllChildren('WndClass','Static',50)
  for item in items:
    if item.Enabled and item.WndCaption == identifier:
      Log.Checkpoint(f'The message {identifier} is verified')
      break
  else:
    Log.Error(f'Expected message {identifier} is disabled')
  
###############################################################################
# Function : select_a_page_tab_security_editor_window
# Description : Selects a specific page tab in the Security Editor window 
#               based on its identifier.
# Parameter : identifier (str) - The name/identifier of the tab to be selected.
# Example : select_a_page_tab_security_editor_window("Policies")
###############################################################################  
def select_a_page_tab_security_editor_window(identifier):
  editor = sed_obj.pagetab.object
  items = editor.FindAllChildren('ObjectType','PageTab',50)
  for item in items:
    if item.Enabled and item.ObjectIdentifier == identifier:
      item.click()
      Log.Checkpoint(f'{identifier} is selected')
      break
  else:
    Log.Error(f'{identifier} is not selected')
  
###############################################################################
# Function : verify_the_password_button_policies_SE
# Description : Verifies if a specific password-related button in the 
#               Security Editor -> Policies window has the expected state.
# Parameter : param (str) - Input in the format "ButtonName$$State"
#             where ButtonName is the button caption and State is the expected state.
# Example : verify_the_password_button_policies_SE("Password required$$1")
############################################################################### 
def verify_the_password_button_policies_SE(param):
  identifier, value = param.split('$$')
  editor = sed_obj.securityeditorwindow.object
  items = editor.FindAllChildren('WndClass', 'Button', 50)
  for item in items:
      if item.Exists and item.Visible:
          if item.WndCaption == identifier and str(item.wState) == value:
              Log.Checkpoint(f'Button "{identifier}" found with state "{value}"')
              break
  else:
      Log.Error(f'Button "{identifier}" with expected state "{value}" not found.')

###############################################################################
# Function   : Edit_textbox1_value_user_information_SE
# Description: Updates the value of the first enabled Edit box 
#              in the User Information window of Security Editor.
# Parameter  : value (str) - The new text to be entered.
# Example    : Edit_textbox1_value_user_information_SE("Admin123")
############################################################################### 
def Edit_textbox1_value_user_information_SE(value):
  editor = sed_obj.Editbox1SE.object
  if editor.Enabled and editor.WndClass == 'Edit':
    editor.wText = value
    Log.Checkpoint(f'The updated value is {value}')
  else:
    Log.Error(f'{value} is not updated')
    
###############################################################################
# Function   : Edit_textbox2_value_user_information_SE
# Description: Updates the value of the second Edit box 
#              in the User Information window of Security Editor.
# Parameter  : value (str) - The new text to be entered.
# Example    : Edit_textbox2_value_user_information_SE("Admin123")
###############################################################################   
def Edit_textbox2_value_user_information_SE(value):
  editor = sed_obj.Editbox2SE.object
  if editor.Enabled and editor.WndClass == 'Edit':
    editor.wText = value
    Log.Checkpoint(f'The updated value is {value}')
  else:
    Log.Error(f'{value} is not updated')
    
    
  

   


  
  
  
