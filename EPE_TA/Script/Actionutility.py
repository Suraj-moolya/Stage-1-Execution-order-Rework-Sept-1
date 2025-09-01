from WindowsExplorer import WindowsExplorer
from SystemServer import SystemServer
import Applicationutility
from MessageBox import MessageBox
from EngineeringClient import EngineeringClient
from ApplicationExplorerTab import ApplicationExplorerTab
from ECWarningPopup import ECWarningPopup
from GlobalTemplatesTab import GlobalTemplatesTab
from LicenseManagement import LicenseManagement
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
from TopologyExplorerTab import TopologyExplorerTab
from Topology import Topology

import os
import datetime

Topology1 = Topology()
EngineeringClient1 = EngineeringClient()    
ApplicationExplorerTab1 = ApplicationExplorerTab()
ECWarningPopup1 = ECWarningPopup()
GlobalTemplatesTab1 = GlobalTemplatesTab()
LicenseManagement1 = LicenseManagement()
MessageBox1 = MessageBox()
ProjectExplorerTab1 = ProjectExplorerTab()
SystemExplorerScreen1 = SystemExplorerScreen()
SystemServer1 = SystemServer()
TopologyExplorerTab1 = TopologyExplorerTab()
WindowsExplorer1 = WindowsExplorer()
Screen_List = [Topology1, EngineeringClient1, ApplicationExplorerTab1, ECWarningPopup1, GlobalTemplatesTab1, LicenseManagement1, MessageBox1, ProjectExplorerTab1, SystemExplorerScreen1, SystemServer1, TopologyExplorerTab1, WindowsExplorer1]
msg_obj = MessageBox()
win_obj = WindowsExplorer()
server_obj = SystemServer()
eng_obj = EngineeringClient()
aet_obj = ApplicationExplorerTab()

###############################################################################
#Author : Preetham S R
#Function : Launches Engineering Client
#Parameter : No
###############################################################################

def launch_engineering_client():
    TestedApps.EngineeringClient.Run()
    Applicationutility.wait_for_execution(30000, 'Launching Engineering Client')

###############################################################################
#Author : Subhramanya B M
#Function : Launches Engineering Client even if one instance already running.
#Parameter : No
###############################################################################    

def launch_engineering_client_with_secondtime():
    TestedApps.EngineeringClient.Run(-1, True, -1)
    Applicationutility.wait_for_execution(30000, 'Launching Engineering Client')

###############################################################################  
# Function    : click_on_more_option
# Description : Clicks on a button within the task manager's accessible buttons 
#               matching the given element identifier.
# Parameter   : element (str) - The ObjectIdentifier of the button to be clicked.
# Example     : click_on_more_option("MoreOptionsButton")
###############################################################################

def click_on_more_option(element):
  task_obj = server_obj.consolewindow.object
  task_list = task_obj.FindAllChildren("ClassName", "accessiblebutton", 50)
  for i in range(len(task_list)):
    if task_list[i].ObjectIdentifier == element:
      task_list[i].Click()
      break
  else:
      Log.Error(f"Element with identifier '{element}' not found among accessible buttons.")

###############################################################################  
# Function    : open_select_details_tab_TM
# Description : Opens the 'Details' tab under the 'More_details' section from the 
#               task manager's by simulating keyboard shortcut and interacting with UI buttons.
# Example     : open_select_details_tab_TM()
###############################################################################

def open_select_details_tab_TM():
  Sys.Keys('^![Esc]')
  task_obj = win_obj.commandbarbutton.object
  task_list = task_obj.FindAllChildren("ClassName", "accessiblebutton", 50)
  for i in range(len(task_list)):
    if task_list[i].ObjectIdentifier == 'More_details':
      task_list[i].Click()
      break
  tab = win_obj.tabsbutton.object
  for j in range(tab.wTabCount):
    if tab.wTabCaption[j] == 'Details':
      tab.ClickTab(j)
      Log.Message('Clicked on Details tab')
      Applicationutility.wait_in_seconds(2000, 'Wait')
      break
  else:
      Log.Error("'Details' tab not found.")

###############################################################################
#Author : Suraj R
#Function : Engineering Client Shortcut Key options
#Parameter :R, T, A, P 
###############################################################################

def explorer_shortcut_key(Shortcut):
  Explorer_shortcut = {"Alt+R":"R","Alt+T":"T","Alt+A":"A","Alt+P":"P"}
  if Shortcut in Explorer_shortcut:
    shortcut_key = "~"+ str(Explorer_shortcut[Shortcut])
    Sys.Keys(shortcut_key)
  else:
    Log.Error("No shortcut key assigned for the explorer")
    
###############################################################################
#Author : Suraj R
#Function : Escape keyboard action
#Parameter : No
###############################################################################

def escape_key_action():
    Sys.Keys('[Esc]')
    Applicationutility.take_screenshot()

###############################################################################
#Author : Preetham S R
#Function : Takes screenshot of the screen
#Parameter : Message
###############################################################################   
 
def take_screenshot(msg="taking screenshot of current screen"):
    """take screenshot"""
    element = Sys.Desktop.Picture()
    Log.Picture(element, msg)

###############################################################################
#Author : Suraj R
#Function : Performs Delete Keboard action
#Parameter : No
############################################################################### 
   
def delete_key_AE():
  Sys.Keys('[Del]')
  Applicationutility.take_screenshot()
  
###############################################################################  
# Function    : check_CE_instances_TM
# Description : Verifies the number of running ControlExpert.exe instances in the 
#               Task Manager detail list and compares it to the expected count.
# Parameters  : instances (int) - Expected number of ControlExpert.exe instances.
# Example     : check_CE_instances_TM(2)
###############################################################################

 
def check_CE_instances_TM(instances):
  Applicationutility.wait_in_seconds(2000, 'wait')
  details_list = win_obj.detaillisttextbox.object
  count = 0
  Log.Enabled = False
  for i in range(details_list.wItemCount-2):
    if details_list.wItem[i] == 'ControlExpert.exe':
      #count += 1
#      Log.Message(str(details_list.wItem[i]) + ' - ' +str(count))
      details_list.FocusItem(i)
      Applicationutility.wait_in_seconds(1000, 'wait')
  Log.Enabled = True
  for i in range(details_list.wItemCount-2):
    if details_list.wItem[i] == 'ControlExpert.exe':
      count += 1  
      if count == instances:
        break    
  if str(count) == str(instances):
    Log.Checkpoint(str(count) + ' instances of CE is running in Task Manager')
    Applicationutility.take_screenshot()
  else:
    Log.Error(str(count) + ' instances of CE is running in Task Manager')
    Applicationutility.take_screenshot()
  
###############################################################################
#Author : Preetham S R
#Function : Waits for execution completion WRT Engineering Client Notification Panel
#Parameter : No
###############################################################################    

def wait_for_execution():
  Applicationutility.wait_in_seconds(500, 'Wait')
  Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for item in Abort_list:
    if item.Panel_ZIndex == 0:
      for _ in range(100):
        if item.DataContext.Status.OleValue != "Executing":
          break
        else:
          Applicationutility.wait_in_seconds(1000, 'Loading !!!')
  Applicationutility.wait_in_seconds(1500, 'Wait')
  
###############################################################################
#Author : Preetham S R
#Function : Performs click action on Engineering client pop up window
#Parameter : Button Name
###############################################################################

def modal_dialog_window_button(button_name):
  try:
    buttons_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    take_screenshot('Taking Screenshot of the Message Window.')
    for button in buttons_list:
      if button_name in str(button.WPFControlText) :
        button.click()
        Log.Checkpoint('Clicked ' + str(button.WPFControlText) + ' button.')
        break
    else:
      Log.Error("Button name mentioned doesnt exists")
  except:
    Log.Error('Expected Pop up not present')  
    
###############################################################################
#Author : Preetham S R
#Function : To get the object from the object repository
#Parameter : Screen Name & Object Name
###############################################################################  

def get_obj(param):
  Screen, property = param.split('$$')
  for Screen_item in Screen_List:
    if str(Screen) in str(Screen_item):
        obj = getattr(Screen_item, property)
        return obj
  else:
    Log.Error(f'The object {property} at {Screen} not found !')

###############################################################################
#Author : Preetham S R
#Function : To click on pop ups
#Parameter : window_class, parent_object, Button Name
###############################################################################  

def Click_popup_button(param):
  window_class, parent_object, button_name = param.split('$$') 
  parm = window_class + '$$' + parent_object
  obj = get_obj(parm)
  buttons_list = obj.object.FindAllChildren('ClrClassName', 'Button', 1000)
  Applicationutility.wait_in_seconds(500, 'Wait')
  if buttons_list:
    take_screenshot('Taking Screenshot of the Popup Window.')
    for button in buttons_list:
      Applicationutility.wait_in_seconds(1000, 'Wait')
      if button_name in str(button.WPFControlText) and button.Enabled == True:
        button.click()
        Log.Message('Clicked ' + str(button.WPFControlText) + ' button.')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        break
    else:
        Log.Error(f"No enabled button with text containing '{button_name}' found.")
  else:
    Log.Error("Button name mentioned doesnt exists")

###############################################################################
#Author : Preetham S R
#Function : Close tab in Engineering Client 
#Parameter : tab Name
###############################################################################   
 
def close_tab_items_EC(identifier):
  template = eng_obj.mainscreenbutton.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2)) 
        break
  else:
     Log.Error("Tab Item mentioned is not Valid")

###############################################################################
#Author : Gunachanthiran k
#Function : Checking Instance Loding Timing is Within 2 seconds or Not.
#Parameter : 
###############################################################################     
    
def reload_application_explorer_and_measure_time():
  try:
    app_browser = aet_obj.applicationbrowsertextbox.object
    if not app_browser.Exists:
      Log.Error("Application browser not found.")
      return

    start = aqDateTime.Now()
    for _ in range(20):
      if app_browser.FindAllChildren("ClrClassName", "TreeListViewRow", 1000):
        duration = aqDateTime.TimeInterval(start, aqDateTime.Now())
        Log.Checkpoint(f"Tree loaded in {aqConvert.TimeIntervalToStr(duration)}")
        return
      aqUtils.Delay(100)

    Log.Warning("Tree did not load within timeout.")
  except Exception as e:
    Log.Error(f"Error: {e}")

 
###############################################################################
#Author : 
#Function :
#Parameter :
###############################################################################    

def ProjectSample():   # Check for Redundant method
    # Obtains the path to the folder that stores the project configuration files
    ConfigPath = Project.ConfigPath
    # Searches for the .tcLS files in the folder
    ConfigFiles = aqFileSystem.FindFiles(ConfigPath, "*.tcLS")
    if ConfigFiles.Count > 0:
      while ConfigFiles.HasNext():
        aFile = ConfigFiles.Next();
        Log.Message(aFile.Name + " file is located in " + ConfigPath)
    else:
      Log.Message("No .tcLS files were found")

###############################################################################
#Author : Preetham S R
#Function : Verify Dialog Window Text 
#Parameter : Text
###############################################################################

def modal_dialog_window_dialog(param):
  obj = msg_obj.modaldialogwindowtextbox
  headder_list = obj.object.FindAllChildren('WPFControlName', 'HeaderGrid', 1000)
  dialog = headder_list[0].FindAllChildren('ClrClassName', 'TextBlock', 25)
  if dialog:
    for text in dialog:
      if param in str(text.WPFControlText):
        Log.Checkpoint('Dialog box message : ' + str(text.WPFControlText))
        take_screenshot('Taking Screenshot of the Message Window.')
        break
    else:
        Log.Error(f'{param} : not found!')
        take_screenshot('Taking Screenshot of the Message Window.')
  else:
    Log.Error('Dialog Window not found!')
      
def afvds(): #Template update operation not started. Unable to find a template of a later version for selected instances.	10:58:51	Normal			0.00
  modal_dialog_window_dialog('Unable to find a template of a later version')
###############################################################################
#Author : Preetham S R
#Function : To select dropdown value in PopUp Dialog Window
#Parameter : Dependant Dropdown text, Dropdown Value
###############################################################################  

def modal_dialog_windo_selectItem(param): 
  controller, val = param.split("$$")
  network_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'ComboBox', 1000)
  if network_list:
    for network in network_list:
      if controller in network.DataContext.DeviceIdentifier.OleValue:
        Log.Message(network.DataContext.DeviceIdentifier.OleValue)
        network.SelectedItem = val
        Log.Message(str(network.SelectedItem) + " is selected")
        take_screenshot('Taking Screenshot')
        break
    else:
      Log.Error(f'{val} does not exist in the drop down')
  else:
    Log.Error(f'{controller}, {val} : not found !')
      
###############################################################################
# Function : Enter_filename_fileformat_Export_Window
# Description: Enters the file name and location in the export window.
# Parameter : file_name, file_format (str) - File format for the export.
###############################################################################

def Enter_filename_fileformat_Export_Window(file_details):
  file_name, file_format = file_details.split('$$')
  if not Project.Variables.VariableExists(file_name):
        Project.Variables.AddVariable(file_name, "String")     
  Project.Variables.VariableByName[file_name] = str(file_name + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.VariableByName[file_name])
  Applicationutility.wait_in_seconds(2000,"Wait")
  try:
      Export_window = msg_obj.exportfilenametextbox.object
      if Export_window.Exists:
        filename_textbox = msg_obj.exportfilenametextbox.object
        filename_textbox.Keys(Project.Variables.VariableByName[file_name]+file_format)
      filelocation = msg_obj.exportfilelocationtextbox
      tox = (filelocation.object.Height)/2
      toy = 10
      filelocation.click_at(tox,toy)
      base_path = os.getcwd()
      folder_name = "Test_Import_Files"
      full_path = os.path.join(base_path, folder_name) 
      Sys.Keys(full_path)
      Applicationutility.take_screenshot('taking Screenshot')
      Sys.Keys("[Enter]")    
  except:
         Log.Error("Export Windows doesnt exists")  

###############################################################################
# Function : Enter_fileName_fileformat_Import_Window
# Description: Enters the system name and location in the import window.
# Parameter : file_format (str) - File format for the import.
###############################################################################
 
def Enter_fileName_fileformat_Import_Window(file_details):
  filename, fileformat = file_details.split('$$')
  filelocation = aet_obj.addressbandtextbox
  tox = ((filelocation.object.Height)/2) + 5
  toy = 5+5
  filelocation.click_at(toy,tox)
  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]") 
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(Project.Variables.VariableByName[filename] + fileformat)
  Applicationutility.take_screenshot('taking Screenshot')
  Applicationutility.wait_in_seconds(1500,"Wait")
  Sys.Keys("[Enter]")   

###############################################################################
# Function   : Export_File
# Description: Handles the export operation by assigning the export filename 
#              to a TestComplete variable, setting the export location, and 
#              confirming the file path without direct user interaction.
# Parameters : 
#   file_name   - The base name of the file to export (string)
#   file_format - The file extension (e.g., ".txt", ".xml") (string)
###############################################################################  

def get_default_file_path():
  path = os.path.join(os.getcwd(), "Test_Import_Files")
  if not os.path.exists(path):
    os.makedirs(path)
  return path
 
def Export_File(file_name, file_format):
  folder = get_default_file_path()
  full_name, dup_name = file_name + file_format, f"{file_name}(1){file_format}"
  full_path, dup_path = os.path.join(folder, full_name), os.path.join(folder, dup_name)

  if not Project.Variables.VariableExists(file_name):
    Project.Variables.AddVariable(file_name, "String")
  Project.Variables.VariableByName[file_name] = full_name

  if not msg_obj.exportfilenametextbox.object.Exists:
    Log.Error("Export Window does not exist"); return

  msg_obj.exportfilelocationtextbox.click_at(msg_obj.exportfilelocationtextbox.object.Height / 2, 10)
  Sys.Keys(folder); Sys.Keys("[Enter]")
  msg_obj.exportfilenametextbox.object.Keys(full_name)
  Applicationexplorertabutility.Explorer_buttons_AE("Save")
  Delay(1000); Sys.Keys("[Enter]")

  if os.path.exists(dup_path): os.remove(dup_path)
###############################################################################
# Function   : Import_File
# Description: Automates the file import process by navigating to the desired 
#              file path and selecting the target file stored in a TestComplete 
#              variable.
# Parameters :
#   file_name - The name of the variable that holds the full file name
###############################################################################
 
def Import_File(file_name):
  if Project.Variables.VariableExists(file_name):
    file_name = Project.Variables.VariableByName[file_name]
  folder = get_default_file_path()
  loc_box = aet_obj.addressbandtextbox
  loc_box.click_at(30, loc_box.object.Height / 2)
  Sys.Keys(folder)
  Sys.Keys("[Enter]")
  name_box = aet_obj.comboboxtextbox.object
  name_box.Click()
  Sys.Keys(file_name)
  Sys.Keys("[Enter]")
  
###############################################################################
# Function   : select_filter_list_box_items
# Description: Selects one or more items from a filter list box based on the 
#              provided string of item values, separated by '$$'.
# Parameter  : param (str) - List of values to select (e.g., "Item1$$Item2").
# Example    : select_filter_list_box_items("GenD_1$$MotorGP_1") or ('GenD_1')
###############################################################################

def select_filter_list_box_items(param):
    items = param.split('$$')
    scroll_height = eng_obj.filterscrollviewer.object.ScrollableHeight
    for i in range(50):
        if i != scroll_height:
          eng_obj.filterlistbox.click_at(eng_obj.filterlistbox.width-15, eng_obj.filterlistbox.height-15)
        else:
             break
    count = 0
    list_box = eng_obj.filterlistbox.object.FindAllChildren('ClrClassName', 'ListBoxItem', 100)
    Applicationutility.wait_in_seconds(1000, 'Wait')
    if list_box:
      for item in list_box:
        if item.DataContext.Value.OleValue in items:
           item.DataContext.IsSelected = True 
           Applicationutility.wait_in_seconds(1500, 'Wait')
           if item.DataContext.IsSelected:
              Log.Checkpoint(f'{item.DataContext.Value.OleValue} : Checkbox value is set to : {item.DataContext.IsSelected}')
              count += 1
              if count == len(items):
                 break
           else:
                Log.Error(f"Item '{item_value}' not selected.")
      else:
           if count == 0:
                Log.Error("None of the specified items were found in the listbox.")
    else:
        Log.Error('No list box items detected.')
           
###############################################################################
# Function   : select_filter_combobox_item
# Description: Selects a value from a specific combo box based on the combo box
#              name and value passed as param.
# Parameter  : param (str) - ComboBoxName$$ValueToSelect
# Example    : select_filter_combobox_item("combobox1$$StartsWith")
###############################################################################    
def select_filter_combobox_item(param):
     obj_dict = {
         "combobox1": 1,
         "combobox2": 2,
         "combobox3": 3
     }

     ComboBox, Combo_value = param.split('$$')
     Combos = eng_obj.filterstackpannel.object.FindAllChildren('ClrClassName', 'RadComboBox', 100)
     combo_found = False
     for combo in Combos:
         if combo.WPFControlOrdinalNo == obj_dict.get(ComboBox):
             combo_found = True
             for i in range(combo.wItemCount):
                 if Combo_value in combo.wItem[i]:
                     combo.SelectedIndex = i
                     if combo.wItem[i] == Combo_value:
                         Log.Checkpoint(f'{combo.wItem[i]} is selected in the combo box')
                         break
                     else:
                         Log.Error('Item matched but was not selected.')
                         break
             else:
                 Log.Error(f'No Combo box item matches: {Combo_value}')
             break
     if not combo_found:
         Log.Error(f'No combo box found for key: {ComboBox}') 
###############################################################################
# Function   : enter_text_filter_textboxs
# Description: Enters text into one of two known text boxes in the filter panel.
# Parameter  : param (str) - TextBoxName$$ValueToEnter
# Example    : enter_text_filter_textboxs("textbox1$$GenD_1")
###############################################################################

def enter_text_filter_textboxs(param):
  txtbx, Text = param.split('$$')  
  stackpanel = eng_obj.filterstackpannel.object.DataContext
  
  if txtbx in 'textbox1':
     stackpanel.Filter1 = str(Text)
     Applicationutility.wait_in_seconds(1500, 'Wait')
     if stackpanel.Filter1.OleValue == Text:
        Log.Checkpoint(f'The Text box value set is : {stackpanel.Filter1.OleValue}')
     else:
          Log.Error(f'The text box value is not {Text}')
          
  elif txtbx in 'textbox2':
     stackpanel.Filter2 = Text     
     Applicationutility.wait_in_seconds(1500, 'Wait')
     if stackpanel.Filter2.OleValue == Text:
        Log.Checkpoint(f'The Text box value set is : {stackpanel.Filter2.OleValue}')
     else:
          Log.Error(f'Failed to set textbox2 value to {Text}')
  else:
        Log.Error(f'Unknown textbox identifier: {txtbx}')
        
###############################################################################
# Function   : changing_values_in_csv
# Description: Toggles the boolean values (TRUE/FALSE) of multiple headings 
#              in a CSV file for a specific instance name. The function reads 
#              the CSV, finds the target instance, and flips the boolean values 
#              for the specified headings.
# Parameters : 
#   file_name     - The CSV file name to be updated (stored under default path)
#   instance_name - The target instance name whose values need to be toggled
#   headings      - A string or list of headings to be toggled, separated by $$
###############################################################################
  
def changing_values_in_csv(file_name, instance_name, headings):
  if isinstance(headings, str):
    headings = [h.strip() for h in headings.split("$$") if h.strip()]
  file_path = os.path.join(get_default_file_path(), file_name)
  with open(file_path, newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
    header_row_index = instance_col_index = None
    for i, row in enumerate(rows):
      if "$InstanceName" in row:
        header_row_index = i
        instance_col_index = row.index("$InstanceName")
        break
    if header_row_index is None:
      Log.Error("Header '$InstanceName' not found.")
      return
    heading_col_indices = {h: rows[header_row_index].index(h) for h in headings if h in rows[header_row_index]}
    if not heading_col_indices:
      Log.Error("No valid headings provided.")
      return
    updated = False
    for row in rows[header_row_index + 1:]:
      if len(row) > instance_col_index and row[instance_col_index].strip() == instance_name:
        for h, idx in heading_col_indices.items():
          if len(row) > idx:
            curr = row[idx].strip().upper()
            row[idx] = "FALSE" if curr == "TRUE" else "TRUE"
            Log.Checkpoint(f"Updated '{h}' for '{instance_name}' from '{curr}' to '{row[idx]}'")
          else:
            Log.Error(f"Column index {idx} out of range for heading '{h}'")
        updated = True
        break
    if not updated:
      Log.Error(f"Instance '{instance_name}' not found.")
      return
  with open(file_path, 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(rows)
  Log.Checkpoint("CSV file updated successfully.")
  
###############################################################################
# Function   : modal_dialog_window_navigate_asset_worskspace
# Description: Navigates through a modal dialog window to find and open 
#              an asset workspace based on the given identifier.
# Parameter  : identifier (str) - The unique identifier of the asset workspace 
#              to locate and open.
###############################################################################
def modal_dialog_window_navigate_asset_worskspace(identifier):
  Workspace_name = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for item in Workspace_name:
    if item.DataContext.Identifier.OleValue == identifier:
      item.DblClick()
      Log.Message(f"Double clicked on {item.DataContext.Identifier.OleValue}")
      break
    else:
      Log.Error(f"{item.DataContext.Identifier.OleValue} not found")  

###############################################################################
# Function   : verify_modal_dialog_window_navigate_asset_worskspace
# Description: Verifies the presence of instances in the modal dialog window 
#              by checking if each workspace item has a valid identifier.
# Parameter  : None
###############################################################################      
def verify_modal_dialog_window_navigate_asset_worskspace():
  Workspace_name = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for item in Workspace_name:
    if item.DataContext.Identifier.OleValue:
      Log.Message(f"The current instance is available in {item.DataContext.Identifier.OleValue}")
    else:
      Log.Warning(f"{item.DataContext.Identifier.OleValue} not found")