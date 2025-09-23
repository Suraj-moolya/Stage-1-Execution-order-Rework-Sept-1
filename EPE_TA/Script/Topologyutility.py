####################### Milestone 3 Topology ################################

import Applicationutility 
from Topology import Topology
from ApplicationExplorerTab import ApplicationExplorerTab
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
import Actionutility
from EngineeringClient import EngineeringClient
from RefineOffline import RefineOffline
from TopologyExplorerTab import TopologyExplorerTab
from MessageBox import MessageBox
import Applicationexplorertabutility

topology_obj =  Topology()
aet_obj = ApplicationExplorerTab()
proj_obj = ProjectExplorerTab()
syse_obj = SystemExplorerScreen()
eng_obj = EngineeringClient()
refoff_obj = RefineOffline()
topo_obj = TopologyExplorerTab()
msg_obj = MessageBox()

############################################################################### 
# Function : search_template_browser_EC 
# Description : Searches for a template in the browser using the provided text. 
# Parameter : search_text (str) - Text to search for in the template browser. 
# Example : search_template_browser_EC("Modbus TCP Device") 
############################################################################### 
  
def search_template_browser_EC(search_text):
  for search_box in msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'SearchComboBoxControl', 1000):
    search_box.Click()
    break
  if search_box is not None and search_box.Exists:
    search_box.Keys(search_text)
    aqObject.CheckProperty(search_box.DataContext, "CurrentSearchText", cmpEqual, search_text)
    Log.Checkpoint(f"Search text '{search_text}' verified.")
  else:
    Applicationutility.take_screenshot()
    Log.Error("Search box not found.")

############################################################################### 
# Function : Select_template_EC 
# Description : Selects a template from the list based on the template name and version. 
# Parameter : param (str) - Template name and version separated by "$$". 
# Example : Select_template_EC("TemplateName$$1.0") 
############################################################################### 
    
def Select_template_EC(param):
  template, version = param.split('$$')
  template_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if not template_list:
    Applicationutility.take_screenshot()
    Log.Error("No templates found in the list.")
    return
  for row in template_list:
    if row.Visible and str(template) in str(row.Item.Identifier.OleValue) and str(version) == str(row.Item.ViewModel.Version.OleValue):
      aqObject.CheckProperty(row.Item.ViewModel.Version, "OleValue", cmpEqual, version)
      row.DblClick()
      Log.Checkpoint(f"Template '{template}' with version '{version}' selected.")
      return
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Template '{template}' with version '{version}' not found.")

############################################################################### 
# Function : DblClick_template_TE 
# Description : Double-clicks a template in the template explorer. 
# Parameter : temp_name (str) - Name of the template to double-click. 
# Example : DblClick_template_TE("ETesysTHW") 
############################################################################### 

def DblClick_template_TE(temp_name):
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  if not temp_list:
    Applicationutility.take_screenshot()
    Log.Error("No templates found in the grid view.")
  for temp in temp_list:
    if temp.Visible and temp_name in temp.DataContext.Identifier.OleValue:
      #aqObject.CheckProperty(temp.DataContext.Identifier, "OleValue", cmpEqual, temp_name)
      temp.DblClick()
      Log.Checkpoint(f"{temp.DataContext.Identifier.OleValue} is double clicked")
      return
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"The template '{temp_name}' is not present.")
    
############################################################################### 
# Function : Expand_communication_tab_TE 
# Description : Expands the "Communication" tab in the system explorer. 
# Parameter : val (str) - Tab name to expand (default is "Communication"). 
# Example : Expand_communication_tab_TE("Communication") 
############################################################################### 
def Expand_communication_tab_TE(val): 
#  val = "Communication" 
  sections = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "GroupHeaderRow", 1000) 
  if not sections: 
    Log.Error("No sections found.") 
    return 
  for section in sections: 
    if val in section.DataContext.Name.OleValue: 
      section.IsExpanded = True 
      Log.Message(f'{section.DataContext.Name.OleValue} is expanded') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{val} not found')

############################################################################### 
# Function : edit_IP_Address 
# Description : Edits the IP address of a specific device in the system explorer. 
# Parameter : param (str) - Device name and new IP address separated by "$$". 
# Example : edit_IP_Address("DeviceName$$192.168.1.1") 
############################################################################### 
def edit_IP_Address(param): 
  name, IP_add = param.split('$$') 
  grid_row_obj = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "GridViewRow", 1000) 
  found = False
  if not grid_row_obj: 
    Log.Error("No grid rows found.") 
    return 
  for grid_row in grid_row_obj: 
    grid_cell_obj = grid_row.FindAllChildren("ClrClassName", "GridViewCell", 100) 
    if not grid_cell_obj: 
      Log.Error("No grid cells found.") 
      return 
    for cell_val in grid_cell_obj: 
      if name in cell_val.WPFControlText: 
        grid_row.DataContext.Expression = IP_add 
        if grid_row.DataContext.Expression == IP_add: 
          Log.Checkpoint(name + " is updated as " + IP_add) 
          found = True
          break 
  if not found: 
    Log.Error(name + " is not updated as " + IP_add) 
    Applicationutility.take_screenshot()
    
############################################################################### 
# Function : RClick_template_TE 
# Description : Right-clicks on a template in the template explorer. 
# Parameter : temp_name (str) - Name of the template to right-click. 
# Example : RClick_template_TE("ETesysTHW") 
############################################################################### 
def RClick_template_TE(temp_name): 
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row() 
  if not temp_list: 
    Log.Error("No templates found in the grid view.") 
    return 
  for temp in temp_list: 
    if temp.Visible: 
      if temp_name in temp.DataContext.Identifier.OleValue: 
        temp.ClickR() 
        Log.Checkpoint(f'{temp.DataContext.Identifier.OleValue} is right-clicked') 
        break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'The {temp_name} is not present')

############################################################################### 
# Function : select_dropdown_value_popup_TE 
# Description : Selects a value from a dropdown in a popup window. 
# Parameter : param (str) - Format: "Screen$$Property$$DropdownValue". 
# Example : select_dropdown_value_popup_TE("Screen1$$Property1$$Value1") 
############################################################################### 
def select_dropdown_value_popup_TE(param): 
  Screen, property, dropdown_value = param.split('$$') 
  para = Screen + '$$' + property 
  object_ = Actionutility.get_obj(para) 
  for i in range(object_.object.Items.Count): 
    if dropdown_value in object_.object.Items.Item[i].Identifier.OleValue: 
      object_.object.SelectedIndex = i 
      Log.Checkpoint(f'The selected value is {object_.object.Items.Item[i].Identifier.OleValue}') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'The value {dropdown_value} is not available in the dropdown')

############################################################################### 
# Function : Select_IP_from_ControlProjectDeployment 
# Description : Selects an IP address from the dropdown in the control project deployment screen. 
# Parameter : IP_address (str) - IP address to select. 
# Example : Select_IP_from_ControlProjectDeployment("192.168.1.1") 
############################################################################### 
def Select_IP_from_ControlProjectDeployment(IP_address): 
  name = topology_obj.primaryaddresslistdropdown.object 
  name.Click() 
  Dropdown_options = eng_obj.userdropdownmenuitemtextbox.object 
  Dropdown_IPList = Dropdown_options.FindAllChildren("ClrClassName", "RadComboBoxItem", 10) 
  if not Dropdown_IPList: 
    Log.Error("No IP addresses found in the dropdown.") 
    return 
  for IP in Dropdown_IPList: 
    if IP_address in IP.DataContext.FormattedAddress.OleValue: 
      IP.Click() 
      Log.Checkpoint(f'{IP.DataContext.FormattedAddress.OleValue} was selected from Dropdown option') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{IP_address} did not exist in Dropdown option')

############################################################################### 
# Function : select_latest_backup_data_TE 
# Description : Selects the latest backup data from the backup selection grid. 
# Parameter : None 
############################################################################### 
def select_latest_backup_data_TE():
  obj = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("RestoreDataConfirmationPanel", "", 1).WPFObject("Grid", "", 1).WPFObject("GroupBox", "Select Backup Data", 3).WPFObject("SelectionGrid")
  if obj.Items.Count == 0:
    Applicationutility.take_screenshot()
    Log.Error("No backup data available to select.")
    return
  backup_times = [int(obj.Items.Item[i].BackupTime.OleValue) for i in range(obj.Items.Count)]
  latest = max(backup_times)
  for i in range(obj.Items.Count):
    if int(obj.Items.Item[i].BackupTime.OleValue) == latest:
      obj.Items.Item[i].IsSelected = True
      Log.Checkpoint(f"The item with timestamp {latest} is selected.")
      Applicationutility.take_screenshot("Screenshot of the selected backup data")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"No item found matching the latest backup timestamp: {latest}.")
############################################################################### 
# Function : Verify_Device_Hardware_Catalog_TE 
# Description : Verifies the presence of a specific device in the hardware catalog. 
# Parameter : smp (str) - Name of the device to verify. 
# Example : Verify_Device_Hardware_Catalog_TE("DeviceName") 
############################################################################### 
def Verify_Device_Hardware_Catalog_TE(smp): 
  obj_lst = refoff_obj.fbdsectionwindowtextbox.object.FindAllChildren("Name", f"TextObject({smp})", 10) 
  if not obj_lst: 
    Log.Error("No devices found in the hardware catalog.") 
    return 
  for obj in obj_lst: 
    if obj.Text == smp: 
      Log.Checkpoint(f'{obj.Text} is verified successfully') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{smp} is not verified')

############################################################################### 
# Function : DBlClick_Properties_workstation 
# Description : Double-clicks on a specific property in the workstation. 
# Parameter : Text (str) - Name of the property to double-click. 
# Example : DBlClick_Properties_workstation("ControlExpert_1") 
############################################################################### 
def DBlClick_Properties_workstation(Text): 
  properties = proj_obj.assignmentsdocktextbox.object.FindAllChildren("ClrClassName", "GridViewRow", 100) 
  if not properties: 
    Log.Error("No properties found in the workstation.") 
    return 
  for property in properties: 
    if Text == property.DataContext.Identifier.OleValue: 
      property.DblClick() 
      Log.Message(f'{property.DataContext.Identifier.OleValue} is clicked') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{Text} property does not exist')

############################################################################### 
# Function : Expand_Properties_workstation 
# Description : Expands a specific property in the workstation. 
# Parameter : Text (str) - Name of the property to expand. 
# Example : Expand_Properties_workstation("Configuration") 
############################################################################### 
def Expand_Properties_workstation(Text): 
  properties = topology_obj.propertywindowtextbox.object.FindAllChildren("ClrClassName", "GroupHeaderRow", 100) 
  if not properties: 
    Log.Error("No properties found in the workstation.") 
    return 
  for property in properties: 
    if Text == property.DataContext.Name.OleValue: 
      property.IsExpanded = True 
      Log.Message(f'{property.DataContext.Name.OleValue} is Expanded') 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{Text} property does not exist')

############################################################################### 
# Function : change_port_number_workstation_TE 
# Description : Changes the port number for a specific heading and active port in the workstation. 
# Parameter : param (str) - Format: "Heading$$ActivePort$$PortValue". 
# Example : change_port_number_workstation_TE("Heading1$$Port1$$8080") 
############################################################################### 
def change_port_number_workstation_TE(param):
  heading, activeport, portvalue = param.split("$$")
  port = topology_obj.propertywindowtextbox.object.FindChild(["ClrClassName","Value.OleValue", "WPFControlOrdinalNo"], ["GridViewCell", activeport, "4"], 100)

  if port == None:
    Applicationutility.take_screenshot()
    Log.Error("No ports found in the property window.")
    return
  else:
    port.Click()
    Applicationutility.wait_in_seconds(1000, 'Wait')
    Sys.Keys('^A')
    Sys.Keys('[BS]')
    Sys.Keys(portvalue)
    Sys.Keys('[Enter]')
    
############################################################################### 
# Function : Verify_error_messages_in_Console 
# Description : Verifies if a specific error message is displayed in the console. 
# Parameter : text (str) - Error message to verify. 
# Example : Verify_error_messages_in_Console("0 Error") 
############################################################################### 
def Verify_error_messages_in_Console(text): 
  output_msg = topology_obj.outputwindowpaneltextbox.object.FindAllChildren("WndClass", "RichEdit20W", 10) 
  if not output_msg: 
    Log.Error("No messages found in the console.") 
    return 
  for msg in output_msg: 
    if text in msg.wText and msg.Visible: 
      Log.Checkpoint(msg.wText + " error messages are displayed in Console") 
      break 
  else: 
    Applicationutility.take_screenshot()
    Log.Error(f'{text} error messages not displayed in Console')

############################################################################### 
# Function : Enter_Controller_Password_deploy_screen_TE 
# Description : Enters the controller password on the deployment screen. 
# Parameter : password (str) - Password to be entered. 
# Example : Enter_Controller_Password_deploy_screen_TE("password123") 
############################################################################### 
def Enter_Controller_Password_deploy_screen_TE(password):
  PW_box = topology_obj.PasswordControlBoxtextbox.object
  if not PW_box.Exists or not PW_box.VisibleOnScreen:
    Log.Error("Password field is not available or visible.")
    return
  else:
    PW_box.SetText("")  
    PW_box.Keys(password)
    Log.Message(f"Password entered in the field: {'*' * len(password)}")
    
###############################################################################
# Function   : select_toolbar_Menu_in_STB_Config
# Description: Finds and double-clicks the specified toolbar item in the STB 
#              Configuration window. Logs success if the item is found and 
#              clicked, otherwise logs an error.
# Parameter  : menu (str) - The ObjectIdentifier of the toolbar menu item 
#                           to be selected.
# Example    : select_toolbar_Menu_in_STB_Config("Island")
###############################################################################
    
def select_toolbar_Menu_in_STB_Config(menu):
  for item in topo_obj.stbconfigwindowtoolbar.object.FindAllChildren("ObjectType", "MenuItem", 10):
    if getattr(item, "ObjectIdentifier", "").strip() == menu:
      item.DblClick()
      Log.Checkpoint(f"Double-clicking toolbar item: {item.ObjectIdentifier}")
      break
  else:
    Log.Error(f"Toolbar item '{menu}' not found in STB Config.")
    
###############################################################################
# Function   : select_toolbar_Menu_Item_in_STB_Config
# Description: Finds and clicks the specified toolbar menu item in the STB 
#              Configuration window. Logs success if the item is found and 
#              clicked, otherwise logs an error.
# Parameter  : menu (str) - The ObjectIdentifier of the toolbar menu item 
#                           to be selected.
# Example    : select_toolbar_Menu_Item_in_STB_Config("Build")
###############################################################################
    
def select_toolbar_Menu_Item_in_STB_Config(menu):
  for item in topo_obj.stbconfigtoolbarmenuitem.object.FindAllChildren("ObjectType", "MenuItem", 10):
    if getattr(item, "ObjectIdentifier", "").strip() == menu:
      item.Click()
      Log.Checkpoint(f"Clicking toolbar menu item: {item.ObjectIdentifier}")
      break
  else:
    Log.Error(f"Toolbar item '{menu}' not found in STB Config.")
    
###############################################################################
# Function   : set_baudrate
# Description: Finds the baud rate combo box in the Baud Rate window and selects
#              the specified value. Logs a checkpoint if the selection is 
#              successful, otherwise logs an error.
# Parameter  : value (str) - The baud rate value to select in the combo box.
# Example    : set_baudrate("500 kbps")
###############################################################################
    
def set_baudrate(value):
  for item in topo_obj.baudratewindow.object.FindAllChildren("WndClass", "ThunderRT6ComboBox", 10):
    try:
      if not value.endswith(" "):
        value += " "
      item.ClickItem(value)
      Log.Checkpoint(f"Selected baud rate: {item.wText}")
    except Exception as e:
      Log.Error(f"Could not select '{value}' in combo box: {e}")
      
###############################################################################
# Function   : click_button_in_advantys
# Description: Finds the specified button in the Advantys Baud Rate window 
#              and clicks it. Logs a checkpoint if the button is clicked 
#              successfully; logs an error if the button is not found or 
#              the click fails.
# Parameter  : button (str) - The caption of the button to click.
# Example    : click_button_in_advantys("OK")
###############################################################################
      
def click_button_in_advantys(button):
  try:
    for btn in topo_obj.baudratewindow.object.FindAllChildren("WndClass", "ThunderRT6CommandButton", 10):
      if button in btn.WndCaption:
        btn.Click()
        Log.Checkpoint(f"{btn.WndCaption} clicked.")
        return
    Log.Error(f"Button '{button}' not found in Advantys window.")
  except Exception as e:
    Log.Error(f"Could not click '{button}': {e}")
    
###############################################################################
# Function   : click_button_in_advantys_popup
# Description: Finds the specified button in the Advantys Baud Rate window 
#              and clicks it. Logs a checkpoint if the button is clicked 
#              successfully; logs an error if the button is not found or 
#              the click fails.
# Parameter  : button (str) - The caption of the button to click.
# Example    : click_button_in_advantys_popup("OK")
###############################################################################    
    
def click_button_in_advantys_popup(button):
  try:
    for btn in topo_obj.stbmessageboxpopup.object.FindAllChildren("WndClass", "ThunderRT6CommandButton", 10):
      if button in btn.WndCaption:
        btn.Click()
        Log.Checkpoint(f"{button} clicked.")
        return
    Log.Error(f"Button '{button}' not found in Advantys Popup window.")
  except Exception as e:
    Log.Error(f"Could not click '{button}': {e}")
    

def select_Radio_Button_in_stb(rbutton):
  for item in topo_obj.connectionsettingwindow.object.FindAllChildren('WndClass', 'ThunderRT6OptionButton', 10):
    if item.WndCaption == rbutton:
      Log.Checkpoint(f'{item.Caption} Selected.')
      item.click()
      break
  else:
    Log.Error(f'{rbutton} Not Found')
  
def set_ip_parts(ip_address):
  ip_parts = ip_address.split('.')
  text_boxes = topo_obj.connectionsettingwindow.object.FindAllChildren('Name', 'VBObject(txtI*)', 10)
  for i, text_box in enumerate(text_boxes):
    if i < len(ip_parts):
      text_box.SetText(ip_parts[i])
      Log.Checkpoint(f"Set {text_box.Name} to {ip_parts[i]}")
  else:
    if not text_boxes:
      Log.Error(f"Failed to set IP address: {ip_address}. No matching text boxes found.")
      
def select_Button_in_stb_connection_window(button):
  for item in topo_obj.connectionsettingwindow.object.FindAllChildren('WndClass', 'ThunderRT6CommandButton', 10):
    if button in item.WndCaption:
      Log.Checkpoint(f'{item.Caption} Selected.')
      item.click()
      break
  else:
    Log.Error(f'{button} Not Found')
    
    
def Select_button_in_Data_Tranfer(button):
  try:
    for btn in topo_obj.stbmessageboxpopup.object.FindAllChildren("WndClass", "ThunderRT6CommandButton", 10):
      if button in btn.WndCaption:
        Log.Checkpoint(f"{button} clicked.")
        btn.Click()
        return
    Log.Error(f"Button '{button}' not found in Data Transfer window.")
  except Exception as e:
    Log.Error(f"Could not click '{button}': {e}")
    
import time    
def verify_notification_in_stb(expected_text, timeout=30, interval=1):
  n = topo_obj.notificantionpannelstb.object
  get_last = lambda: n.wText.strip().splitlines()[-1].split(" - ", 1)[-1] if n.wText else ""
  end = time.time() + timeout
  while time.time() < end:
    last = get_last()
    if last == expected_text:
      Log.Checkpoint(f"'{expected_text}' found in Notification Panel (last message)")
      return
    time.sleep(interval)
  Log.Error(f"'{expected_text}' not found as last message. Last Actual: {last}")
  
  
def verify_instance(instance_name, expected_status):
  refoff_obj.mdiwindowtextbox.object.Maximize()
  diagram_window = refoff_obj.fbdsectionwindowtextbox.object
  diagram_window.Click()
  seen = set()
  text_objects = []
  def check_texts(texts):
    found_instance = False
    for text in texts:
      if instance_name in text:
        found_instance = True
        continue
      if found_instance:
        if text == expected_status:
          Log.Checkpoint(f"{instance_name} → {expected_status}")
          return True, None
        return False, text
    return False, None
  children = diagram_window.FindAllChildren("Name", "TextObject*", 100)
  for child in children:
    text = getattr(child, "Text", "")
    if not text or text in seen:
      continue
    seen.add(text)
    text_objects.append(text)
  found, status = check_texts(text_objects)
  if found:
    return True
  prev_count = len(seen)
  for _ in range(49):
    diagram_window.MouseWheel(-5)
    aqUtils.Delay(200)
    children = diagram_window.FindAllChildren("Name", "TextObject*", 100)
    for child in children:
      text = getattr(child, "Text", "")
      if not text or text in seen:
        continue
      seen.add(text)
      text_objects.append(text)
    found, status = check_texts(text_objects[prev_count:])
    if found:
      return True
    if len(seen) == prev_count:
      break
    prev_count = len(seen)
  if status:
    Log.Error(f"{instance_name} did not reach status {expected_status}. Actual status: {status}")
  else:
    Log.Error(f"{instance_name} did not reach status {expected_status}. No status found.")
  return False
  
def Verify_manage_password_failure_controller(param):
    Applicationutility.wait_in_seconds(1000, 'Wait')
    field, Tooltip_Message = param.split("$$")
    if "Password" == field:
      obj = topo_obj.newpasswordboxtextbox.object
      if Tooltip_Message in obj.ToolTip.OleValue:
        Log.Checkpoint(f'The Message "{obj.ToolTip.OleValue}" is visible')
      else:
        Log.Error(f'The Message "{Tooltip_Message}" is not visible')
    elif "Confirm Password" == field:
      obj = topo_obj.ConfirmPasswordboxtextbox.object
      if Tooltip_Message in obj.ToolTip.OleValue:
        Log.Checkpoint(f'The Message "{obj.ToolTip.OleValue}" is visible')
      else:
        Log.Error(f'The Message "{Tooltip_Message}" is not visible')
    elif "Current Password" == field:
      obj = topo_obj.oldpasswordboxboxtextbox.object
      if Tooltip_Message in obj.ToolTip.OleValue:
        Log.Checkpoint(f'The Message "{obj.ToolTip.OleValue}" is visible')
      else:
        Log.Error(f'The Message "{Tooltip_Message}" is not visible')
    else:
      Applicationutility.take_screenshot()
      Log.Error(f"Unknown field '{field}' provided for password entry")
      
      @when("I Click on export System1 Export Popup AE buttons Export in ec windows explorer as {arg}")
      @when("I Click on buttons in pop up message as {arg}")
      def step_impl(ok):
          """I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'"""
          obj.buttonexportclickonexportsystem1exportpopupaebuttons(ok)

def select_protocol_in_confirm_refine_online(item_text):
  for combo in topology_obj.confirmationrefineonline.object.FindAllChildren("ClrClassName", "RadComboBox", 100):
    combo.ClickItem(item_text)
    Log.Checkpoint(f"Selected {combo.Wtext}")
    break
  else:
    Log.Error(f"Item '{item_text}' not found")
    
def enter_password(password):
  for item in topology_obj.controllerpasswordwindow.object.FindAllChildren("ClrClassName", "PasswordBox", 100):
    item.wText = password
    Log.Checkpoint("Password Entered in controller Password TextBox")
    break
  else:
    Log.Error(f'Password text box not found')
  
def click_button_in_controller_password(button):
  for btn in topology_obj.controllerpasswordwindow.object.FindAllChildren("ClrClassName", "Button", 100):
    if btn.WPFControlText == button:
      btn.Click()
      Log.Checkpoint(f'{btn.WPFControlText} clicked in Controller Password Window')
      break
  else:
    Log.Error(f'{button} not found')
    
def click_button_in_confirm_refine_online(button):
  for btn in topology_obj.confirmationrefineonline.object.FindAllChildren("ClrClassName", "Button", 100):
    if btn.WPFControlText == button:
      btn.WaitProperty("Enabled", True, 5000); btn.Click()
      Log.Checkpoint(f"{btn.WPFControlText} clicked")
      return
  Log.Error(f"{button} not found")