"""Application Explorer Tab Utility"""

import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from ApplicationExplorerTab import ApplicationExplorerTab
from WindowsExplorer import WindowsExplorer
from MessageBox import MessageBox
import os
import csv
import xml.etree.ElementTree as ET
import datetime
import re
import Actionutility

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
aet_obj = ApplicationExplorerTab()
win_obj = WindowsExplorer()
msg_obj = MessageBox()

###############################################################################
# Function : expand_templates_browser
# Description: Expands the templates in the browser based on the provided list.
#              Iterates through the identifiers and expands the corresponding 
#              templates if they are not already expanded.
# Parameter : lst (str) - Comma-separated identifiers of templates to expand.
#             Example: "Template1,Template2,Template3"
###############################################################################   
def expand_templates_browser(lst):
    identifiers_list = lst.split(',')
    for identifier in identifiers_list:
        template = aet_obj.templatesbrowsertextbox.object.FindChild('DataContext.Identifier', identifier, 50)
        if template.Exists:
           if not template.IsExpanded:
              template.IsExpanded = True
              template.WaitProperty('IsExpanded', True, 2000)
              Log.Checkpoint(f'The folder "{identifier}" is Expanded') 
           elif template.IsExpanded:
                Log.Message(f' The Folder "{identifier}" is already Expanded')
        else:
             Log.Error(f'{identifier} Does not exist')
        
###############################################################################
# Function : collapse_templates_browser
# Description: Collapses the templates in the browser based on the provided list.
#              Iterates through the identifiers and collapses the corresponding 
#              templates if they are expanded.
# Parameter : lst (str) - Comma-separated identifiers of templates to collapse.
#             Example: "Template1,Template2,Template3"
###############################################################################
def collapse_templates_browser(lst):
    identifiers_list = lst.split(',')
    for identifier in identifiers_list:
        template = aet_obj.templatesbrowsertextbox.object.FindChild('DataContext.Identifier', identifier, 50)
        if template.Exists:
           if template.IsExpanded:
              template.IsExpanded = False
              template.WaitProperty('IsExpanded', False, 2000)
              Log.Checkpoint(f'The folder "{identifier}" is Collapsed') 
           elif template.IsExpanded:
                Log.Message(f' The Folder "{identifier}" is already Collapsed')
        else:
             Log.Error(f'{identifier} Does not exist')

###############################################################################
# Function : check_composite_templates_temp_browser
# Description: Verifies composite templates in the template browser by checking 
#              their version and description. Logs a checkpoint for each valid template.
# Parameter : None
###############################################################################
def check_composite_templates_temp_browser():
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for template in template_list:
            if template.Visible and template.Item.ViewModel.Version.OleValue != '':
                Log.Checkpoint(f"{template.Item.Identifier.OleValue} - {template.Item.ViewModel.Version.OleValue} - {template.Item.ViewModel.Description.OleValue}")
    else:
        Log.Error("No templates found in the template browser.")

###############################################################################
# Function : click_on_scroll_down_temp_browser
# Description: Scrolls down the template browser by clicking on the scroll bar.
# Parameter : count (int) - Number of times to scroll down.
#             Example: 5
###############################################################################
def click_on_scroll_down_temp_browser(count):
    temp_browser = aet_obj.templatesbrowsertextbox
    for _ in range(int(count)):
        temp_browser.click_at((temp_browser.width - 15), (temp_browser.height - 35))

###############################################################################
# Function : click_on_scroll_up_temp_browser
# Description: Scrolls up the template browser by clicking on the scroll bar.
# Parameter : count (int) - Number of times to scroll up.
#             Example: 5
###############################################################################
def click_on_scroll_up_temp_browser(count=0):
    temp_browser = aet_obj.templatesbrowsertextbox
    for _ in range(int(count)):
        temp_browser.click_at((temp_browser.width - 15), 100)

###############################################################################
# Function : check_temp_browser_list
# Description: Logs all visible templates in the template browser.
# Parameter : None
###############################################################################
def check_temp_browser_list():
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for template in template_list:
            if template.Visible:
                Log.Checkpoint(str(template.Item.Identifier.OleValue))
    else:
        Log.Error("No templates found in the template browser.")

###############################################################################
# Function : search_template_browser_AE
# Description: Searches for a template in the template browser using the search text.
# Parameter : search_text (str) - Text to search for in the template browser.
#             Example: "Motor"
###############################################################################
def search_template_browser_AE(search_text):
    temp_browser = aet_obj.templatesbrowsertextbox.object
    search = temp_browser.FindChild('ClrClassName','SearchComboBoxControl', 50)
    if search.Exists:
        search.DblClick()
        Applicationutility.wait_in_seconds(2000, 'Wait')
        search.Keys("^A")
        search.Keys("[BS]")
        search.Keys(search_text)
        Applicationutility.wait_in_seconds(1000, 'Wait')
        aet_obj.workspacebutton.object.Click()
    else:
        Log.Error("SearchComboBoxControl not found in template browser.")

###############################################################################
# Function : drag_composite_template_drop_app_browser_system1_AE
# Description: Drags a composite template from the template browser and drops it 
#              onto a system in the application browser.
# Parameter : param (str) - Template and version in the format 'template$$version'.
#             Example: "Template1$$1.0.0"
###############################################################################
def drag_composite_template_drop_app_browser_system1_AE(param):
    template, version = param.split('$$')
    Applicationutility.wait_in_seconds(2500, 'wait')
    template_ = f'${template}'
    template_item = aet_obj.templatesbrowsertextbox.object.FindChild(['Item.Identifier.OleValue'], [template_] , 1000)
    template_item1 = aet_obj.templatesbrowsertextbox.object.FindChild(['Item.Identifier.OleValue'], [template] , 1000)
    #template_item.WaitProperty('Visible', True, 5000)
    if template_item.Exists:
        #if str(version) == str(template_item.Item.ViewModel.Version.OleValue):
          fromx = template_item.ScreenLeft
          fromy = template_item.ScreenTop
          Log.Message(f"The object selected to drag is: {template_item.Item.Identifier.OleValue} with version '{template_item.Item.ViewModel.Version.OleValue}")
#        else:
#          Log.Error(f"Template '{template_item.Item.Identifier.OleValue}' with version '{template_item.Item.ViewModel.Version.OleValue}' not Visible in template browser.")
    elif template_item1.Exists:
          fromx = template_item1.ScreenLeft
          fromy = template_item1.ScreenTop
          Log.Message(f"The object selected to drag is: {template_item1.Item.Identifier.OleValue} with version '{template_item1.Item.ViewModel.Version.OleValue}")
    else:
      Log.Error(f"Template '{template}' with version '{version}' not found in template browser.")
    Applicationutility.wait_in_seconds(1000, 'Wait')
    app_item = aet_obj.applicationbrowsertextbox.object.FindChild('Item.Identifier.OleValue', 'System*', 1000)
    if app_item.Exists:
       if app_item.Visible and "System" in str(app_item.Item.Identifier.OleValue):
            tox = app_item.ScreenLeft
            toy = app_item.ScreenTop
            Log.Message(f"The object selected to drop to is: {app_item.Item.Identifier.OleValue}")
       else:
            Log.Error("No 'System' found in application browser.")
    else:
        Log.Error("Object not found in the application browser.")

    main_screen = eng_obj.mainscreenbutton
    main_screen.drag((fromx + 100), (fromy + 15), (fromx + tox + 115), -(fromy - toy))
    Applicationutility.wait_in_seconds(1000, 'wait')
    aet_obj.workspacebutton.object.Click()
  
###############################################################################
# Function : drag_composite_template_drop_app_browser_folder_AE
# Description: Drags a composite template and drops it into a folder in the app browser.
# Parameter : param (str) - Template, version, and folder name in the format 'template$$version$$folder_name'.
###############################################################################
def drag_composite_template_drop_app_browser_folder_AE(param):
    template, version, folder_name = param.split('$$')
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        for template_item in template_list:
            if template_item.Visible and str(template) in str(template_item.Item.Identifier.OleValue) and str(version) == str(template_item.Item.ViewModel.Version.OleValue):
                fromx = template_item.ScreenLeft
                fromy = template_item.ScreenTop
                Log.Message(f"The object selected to drag is: {template_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Error(f"Template '{template}' with version '{version}' not found in template browser.")
    else:
        Log.Error("No templates found in the template browser.")

    app_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if app_list:
        for app_item in app_list:
            if app_item.Visible and str(folder_name) in str(app_item.Item.Identifier.OleValue):
                tox = app_item.ScreenLeft
                toy = app_item.ScreenTop
                Log.Message(f"The object selected to drop to is: {app_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Error(f"Folder '{folder_name}' not found in application browser.")
    else:
        Log.Error("No items found in the application browser.")

    main_screen = eng_obj.mainscreenbutton
    main_screen.drag((fromx + 15), (fromy + 15), (fromx + tox), -(fromy - toy))
    Applicationutility.wait_in_seconds(1000, 'wait')
    Sys.Keys('[Enter]')

###############################################################################
# Function : run_drag_and_drop_multiple_times
# Description: Multiple Drag-Drop on a template in the application browser.
# Parameter : param (str, num) - Template identifier and version in the format 'identifier$$version', 'num'.
###############################################################################      
    
def run_drag_and_drop_multiple_times(param, count):
  for i in range(count):
    Log.Message(f"Iteration {i + 1} of {count} for param: {param}")
    try:
        drag_composite_template_drop_app_browser_folder_AE(param)
    except Exception as e:
        Log.Error(f"Error in iteration {i + 1}: {str(e)}")
    
###############################################################################
# Function : right_click_application_browser_template_AE
# Description: Right-clicks on a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def right_click_application_browser_template_AE(param):
  identifier, version = param.split('$$')
  app_list = aet_obj.applicationbrowsertextbox.find_children_for_treeviewrow()
  if app_list:
    for app_item in app_list:
      if identifier in str(getattr(app_item.Item, 'Identifier', None)) and version == str(getattr(app_item.Item.ViewModel, 'TemplateVersion', None)):
        app_item.ClickR()
        Log.Message(f"Right-clicked object is: {app_item.Item.Identifier.OleValue}")
        break
    else:
        Log.Error(f"Template '{identifier}' with version '{version}' not found.")
  else:
      Log.Error("No templates found in the application browser.")
  
###############################################################################
# Function : right_click_application_browser_folder_AE
# Description: Right-clicks on a folder in the application browser.
# Parameter : identifier (str) - Identifier of the folder to right-click.
###############################################################################
def right_click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].ClickR()
          Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
    else:
      Log.Error("InValid Identifier")
  else:
    Log.Error("No folders found in the application browser.")
  Applicationutility.wait_in_seconds(1000, 'wait')
  
###############################################################################
# Function : right_click_asset_workspace_folder_AE
# Description: Right-clicks on a folder in the asset workspace.
# Parameter : identifier (str) - Identifier of the folder to right-click.
###############################################################################
def right_click_asset_workspace_folder_AE(identifier):
  App_browser = aet_obj.assetworkspacetextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].ClickR()
          Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
  else:
    Log.Error("No folders found in the asset workspace.")
  Applicationutility.wait_in_seconds(1000, 'wait')
  
###############################################################################
# Function : verify_folder_and_template_application_browser
# Description: Verifies the presence of a folder or template in the application browser.
# Parameter : identifier (str) - Identifier of the folder or template to verify.
###############################################################################

def verify_folder_and_template_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].DataContext.Identifier.OleValue):
          Log.Checkpoint('The identifier is present : ' + str(template_list[i].DataContext.Identifier.OleValue))
          break
    else:
      Log.Error('The identifier was not found : ' + str(identifier))
  else:
    Log.Error("No folders or templates found in the application browser.")
    
###############################################################################
# Function : drag_app_browser_drop_asset_workspace_editor_AE
# Description: Drags an item from the app browser and drops it into the asset workspace editor.
# Parameter : template (str) - Identifier of the template to drag.
###############################################################################
    
def drag_app_browser_drop_asset_workspace_editor_AE(template):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  fromx, fromy = None, None
  if not template_list:
    Log.Error("No templates found in the application browser.")
    return
  for row_item in template_list:
    if row_item.Visible:
      identifier = getattr(row_item.DataContext.Identifier, 'OleValue', None)
      if identifier and template in str(identifier):
        fromx = row_item.ScreenLeft
        fromy = row_item.ScreenTop
        Log.Message(f'The object selected to drag is: {identifier}')
        break
  if fromx is None or fromy is None:
    Log.Error(f"Template '{template}' not found in the application browser.")
    return
  Workspace_editor = aet_obj.assertworkspaceeditortextbox.object
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_elements = node_element_parent.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
  n = len(node_elements)
  main_screen = eng_obj.mainscreenbutton
  base_x = Workspace_editor.ScreenLeft - 300
  base_y = Workspace_editor.ScreenTop - 300
  offset_x = 300
  offset_y = 200
  col = n % 2
  row = n // 2
  drop_x = base_x + (col * offset_x)
  drop_y = base_y + (row * offset_y)
  Log.Message(f"Dropping Instance #{n + 1} at X={drop_x}, Y={drop_y}")
  main_screen.drag(fromx + 20, fromy + 20, drop_x, drop_y)

def sdkl():
    drag_app_browser_drop_asset_workspace_editor_AE("ATV61AS")
    drag_app_browser_drop_asset_workspace_editor_AE("ATV71AS")
    drag_app_browser_drop_asset_workspace_editor_AE("MotorVSGP_1")
    drag_app_browser_drop_asset_workspace_editor_AE("MotorVSGP_2")
  

###############################################################################
# Function : verify_Template_node_Asset_Workstation_editor_AE
# Description: Verifies a template node in the asset workstation editor.
# Parameter : template (str) - Identifier of the template to verify.
###############################################################################
def verify_Template_node_Asset_Workstation_editor_AE(template):
  template_grid = aet_obj.nodeinstancebutton.object   # check if this variable is unused 
  template_grid_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'Grid', 1000)
  if template_grid_list:
    for i in template_grid_list:
      if template in str(i.ToolTip) and i.Visible:
        Log.Message(f'{i.ToolTip.OleValue} is successfully verified')
        break
    else:
      Log.Message(f'{template} no such template exists')
  else:
    Log.Error("No templates found in the asset workstation editor.")
    
###############################################################################
# Function : double_click_identifier_application_browser
# Description: Double-clicks an identifier in the application browser.
# Parameter : identifier (str) - Identifier to double-click.
###############################################################################
def double_click_identifier_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier == str(template_list[i].DataContext.Identifier.OleValue):
          template_list[i].DblClick()
          Applicationutility.wait_in_seconds(2000, 'wait')
          break
  else:
    Log.Error("No identifiers found in the application browser.")
    
###############################################################################
# Function : verify_inspect_instance_window_name
# Description: Verifies the name of the inspect instance window.
# Parameter : name (str) - Expected name of the inspect instance window.
###############################################################################
def verify_inspect_instance_window_name(name):
  try:
    inspect_win = aet_obj.inspectinstancewindowtextbox.object
    if str(name) in str(inspect_win.Title.OleValue):
      Log.Checkpoint('Inspect Instance window is open for : ' + str(inspect_win.Title.OleValue))
  except exception as exe:
    Log.Error('Inspect Instance window is not open')
    
###############################################################################
# Function : close_inspect_instance
# Description: Closes the inspect instance window.
# Parameter : None
###############################################################################
def close_inspect_instance():
    inspect_win = aet_obj.inspectinstancewindowtextbox
    inspect_win.click_at(inspect_win.width-30, 30)
    Applicationutility.take_screenshot()
    
###############################################################################
# Function : verify_save__changes_popup_AE
# Description: Verifies the presence of the save changes popup.
# Parameter : name (str) - Expected name of the popup.
###############################################################################
def verify_save__changes_popup_AE(name):
  window = msg_obj.exportpopupbutton.object.Visible
  if window:
    Log.Message(f'the window {msg_obj.exportpopupbutton.object.Title.OleValue} is Visible')
  else:
    Log.Error(f'the window doesnt exists in the pop up')
    
###############################################################################
# Function : Link_from_ranged_node_to_ranged_node
# Description: Links one ranged node to another in the editor.
# Parameter : param (str) - From and to node identifiers in the format 'from_node$$to_node'.
###############################################################################
def Link_from_ranged_node_to_ranged_node(param):
  from_node, to_node = param.split('$$')
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if from_node == str(node_element.DataContext.Identifier) :
            tox = node_element.ScreenLeft
            toy = node_element.ScreenTop

    for node_element in node_element_list:
      if to_node == str(node_element.DataContext.Identifier) :
        fromx = node_element.Width
        regulator1 = node_element.ScreenLeft
        regulator2 = node_element.ScreenTop
        fromy = node_element.Height
        node_element.Drag(fromx-15, fromy/2, tox-regulator1, toy-regulator2)
  else:
    Log.Error("No nodes found in the editor.")
    
def Link_instance_in_AssetWorkspaceEdittor(from_property, from_instance, to_property, to_instance):
  source, target = None, None
  for inst in aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'InstanceNode', 100):
    if getattr(inst.DataContext, 'Identifier', '') == from_instance and not source:
      source = next((p for p in inst.FindAllChildren('ClrClassName', 'TreeViewItem', 100)
                    if getattr(p.DataContext, 'Identifier', '') == from_property), None)
    if getattr(inst.DataContext, 'Identifier', '') == to_instance and not target:
      target = next((p for p in inst.FindAllChildren('ClrClassName', 'TreeViewItem', 100)
                    if getattr(p.DataContext, 'Identifier', '') == to_property), None)
  if source is None or target is None:
    return Log.Error(f"Missing: {from_instance}.{from_property} or {to_instance}.{to_property}")
  source.Drag(source.Width-1, source.Height//2,
              target.ScreenLeft-source.ScreenLeft,
              target.ScreenTop-source.ScreenTop+target.Height//2)
  Log.Message(f"Linked {from_instance}.{from_property} → {to_instance}.{to_property}")
  
###############################################################################
# Function : Verify_Link_Status
# Description: Verifies the link status of instances in the application browser.
# Parameter : None
###############################################################################
def Verify_Link_Status():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
        submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
        for i in submenuitems:
          if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
            Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has Invalid link')
            break
        else:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has valid link')
  else:
    Log.Error("No instances found in the application browser.")
    
###############################################################################
# Function : verify_application_explorer_instance_editor_tab
# Description: Verifies the presence of an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to verify.
###############################################################################
def verify_application_explorer_instance_editor_tab(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
          break
    else:
      Log.Error('The instance editor tab was not found : ' + str(identifier))
  else:
    Log.Error("No instance editor tabs found in the application explorer.")


###############################################################################
# Function : application_explorer_instance_editor_tab_close
# Description: Closes an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to close.
###############################################################################
def application_explorer_instance_editor_tab_close(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2))
  else:
    Log.Error("No instance editor tabs found in the application explorer.")
  
###############################################################################
# Function : enter_instance_description_AE_instance_editor
# Description: Enters a description for an instance in the instance editor.
# Parameter : None
###############################################################################
def enter_instance_description_AE_instance_editor():
  des = aet_obj.instancedescriptionbutton.object
  des_list = des.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  if des_list:
    for item in des_list:
      cells = item.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
      for cell in cells:
        if 'Instance Description' == str(cell.WPFControlText):
          item.Click((item.Width-25), (item.height/2) )
          Sys.Keys('Added Description !!')
          break
  else:
    Log.Error("No descriptions found in the instance editor.")
                              
###############################################################################
# Function : expand_uncheck_all_filters_temp_browser_AE
# Description: Expands and unchecks all filters in the template browser.
# Parameter : None
###############################################################################
def expand_uncheck_all_filters_temp_browser_AE():
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'Expander', 1000) 
  if template_list:
    Applicationutility.wait_in_seconds(500, 'wait')
    expander = template_list[0]
    if not expander.IsExpanded:
      expander.Click()
    list = expander.FindAllChildren('ClrClassName', 'ListBoxItem', 1000) 
    for item in list:
      if item.Visible:
        if item.DataContext.IsSelected:
          Log.Message(item.DataContext.IsSelected)
          item.DataContext.IsSelected = False    
  else:
    Log.Error("No filters found in the template browser.")

###############################################################################
# Function : extract_template_csvdata_AE
# Description: Extracts template data from a CSV file and verifies it with the application.
# Parameter : None
###############################################################################
def extract_template_csvdata_AE(file_details):
  # combines system name and file format
  #exported_csv = Project.Variables.System + ".csv"
  file_name, file_format = file_details.split('$$')
  exported_csv = Project.Variables.VariableByName[file_name]+file_format
  Applicationutility.wait_in_seconds(10000, 'wait')
  
  # collect all the template in Application Browser
  template_details = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  
  # extract csv file
  folder_name = "Test_Import_Files"
  d_path = os.path.abspath(os.path.join(os.getcwd(), folder_name, exported_csv))
  with open(d_path, mode='r') as file:
        reader = csv.reader(file)
        # all rows are stored in data list
        data = [str(row) for row in reader if len(row) >=1]
        # log Export version
        for j in data:
          if "Export Version" in str(j):
            Log.Message(str(j)) 
            break
        else:
          Log.Message("Export Version not found in excel")
        
        #checks for Template Details in data list
        for i in template_details:
          if i.WPFControlText in str(data) and i.WPFControlText not in ["Valid", "","InValid"] :
            Log.Message(f'Excel data is verified with {i.WPFControlText} in Application' ) 

###############################################################################
# Function : Enter_systemName_systemlocation_ExportWindow_AE
# Description: Enters the system name and location in the export window.
# Parameter : file_format (str) - File format for the export.
###############################################################################
def Enter_systemName_systemlocation_ExportWindow_AE(file_format):
  if not Project.Variables.VariableExists('system_1'):
        Project.Variables.AddVariable('system_1', "String")
  Project.Variables.system_1 = str('System1_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.system_1)
  Applicationutility.wait_in_seconds(2000,"Wait")
  Export_window = msg_obj.exportfilenametextbox.object
  
  if Export_window.Exists:
    filename_textbox = msg_obj.exportfilenametextbox.object
    filename_textbox.Keys(Project.Variables.system_1+file_format)
  else:
    Log.Error("Export Windows doesnt exists")
  filelocation = msg_obj.exportfilelocationtextbox
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")

###############################################################################
# Function : import_TE
# Description: Imports a file into the application.
# Parameter : None
###############################################################################
def import_TE():
  Export_window = aet_obj.comboboxtextbox.object
  
  if Export_window.Exists:
    filename_textbox = aet_obj.comboboxtextbox.object
    filename_textbox.Keys(Project.Variables.system_1+".sbk")
  else:
    Log.Error("Export Windows doesnt exists")
  filelocation = msg_obj.exportfilelocationtextbox
  tox = (filelocation.object.Height)/2
  toy = 5
  filelocation.click_at(tox,toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")

###############################################################################
# Function : Explorer_buttons_AE
# Description: Clicks a button in the explorer window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Explorer_buttons_AE(button_name):
  buttons_list = msg_obj.exportwpopupbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WndCaption) :
        button.click()
        break
    else:
      Log.Error("Button name mentioned doesnt exists")
  else:
    Log.Error("No buttons found in the explorer window.")
    
###############################################################################
# Function : Explorer_buttons_TE
# Description: Clicks a button in the explorer window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Explorer_buttons_TE(button_name):
  buttons_list = msg_obj.exportbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WndCaption) :
        button.click()
        break
    else:
      Log.Error("Button name mentioned doesnt exists")
  else:
    Log.Error("No buttons found in the explorer window.")

###############################################################################
# Function : Verify_already_exists_Popup_message_AE
# Description: Verifies the presence of a popup message indicating a file already exists.
# Parameter : None
###############################################################################
def Verify_already_exists_Popup_message_AE():
  Message_AE = msg_obj.exportwpopuptextbox.object
  Message_list_AE = Message_AE.FindAllChildren('WndClass', 'Static', 1000)
  if Message_list_AE:
    for item in Message_list_AE:
      if "Do you want to replace it?" in str(item.WndCaption) and item.WndCaption != "" :
        Log.Message(f'{item.WndCaption} sucessfully verified')
        break
    else:
      Log.Error("message:already exists.Do you want to replace it? doesnt exists")  
  else:
    Log.Error("No messages found in the popup.")
    
###############################################################################
# Function : export_System1_Export_Popup_AE
# Description: Verifies the presence of a popup message during export.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def export_System1_Export_Popup_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Error("{message} doesnt exists in the pop up")
  else:
    Log.Error("No messages found in the export popup.")
    
###############################################################################
# Function : export_System1_Export_Popup_AE_buttons
# Description: Clicks a button in the export popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def export_System1_Export_Popup_AE_buttons(button_name):
    buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                Log.Message(button.WPFControlText)
                break
        else:
            Log.Error("Button name mentioned doesn't exist.")
    else:
        Log.Error("No buttons found in the export popup.")
    
###############################################################################
# Function : extract_template_xmldata_AE
# Description: Extracts template data from an XML file and verifies it with the application.
# Parameter : None
###############################################################################
def extract_template_xmldata_AE(file_details):
    # Combines system name and file format
    #exported_xml = Project.Variables.System + ".xml"
    file_name, file_format = file_details.split('$$')
    exported_xml = Project.Variables.VariableByName[file_name]+file_format
  
    # Collect all the template details in the Application Browser
    template_details = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  
    # Extract XML file
    Log.Message(os.getcwd())
    folder_name = "Test_Import_Files"
    d_path = os.path.abspath(os.path.join(os.getcwd(), folder_name, exported_xml))
    tree = ET.parse(d_path)
    root = tree.getroot()

    # Convert XML elements to strings for easier searching
    data = [ET.tostring(element, encoding='unicode') for element in root.iter()]
    
    # Log Export Version
    export_version = root.attrib.get("Version")
    Log.Message(f"Export Version: {export_version}")
        
    # Check for Template Details in data list
    if template_details:
      for detail in template_details:
          if detail.WPFControlText in str(data) and detail.WPFControlText not in ["Valid", "","InValid"]:
              Log.Message(f'XML data is verified with {detail.WPFControlText} in Application')
    else:
      Log.Error("No template details found in the application browser.")

            
###############################################################################
# Function : verify_modification_popup
# Description: Verifies the presence of a modification popup message.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def verify_modification_popup(message):
  popupmsg = msg_obj.exportpopupbutton.object.MainText.OleValue
  if message in popupmsg:
    Log.Message(f'{popupmsg} has been verified')
  else:
    Log.Error(f'{message} does not exits in popup')
    
###############################################################################
# Function : verify_files_existance_Project_Variable_AE
# Description: Verifies the existence of a file based on a project variable.
# Parameter : filetype (str) - File type to verify.
###############################################################################
def verify_files_existance_Project_Variable_AE(filetype):
  exported_xml = Project.Variables.system_1 + filetype
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    
###############################################################################
# Function : verify_files_existance_AE
# Description: Verifies the existence of a file.
# Parameter : filename_with_extension (str) - Filename with extension to verify.
###############################################################################
def verify_files_existance_AE(filename_with_extension):
  d_path = os.path.abspath(os.path.join(os.getcwd(), filename_with_extension))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    
###############################################################################
# Function : delete_all_files_Post_Condition
# Description: Deletes all files in the post condition.
# Parameter : None
###############################################################################
def delete_all_files_Post_Condition():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == "Systems Explorer":
        pass
      else:
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        try:
          Engineeringclientutility.circularprogressbar_Wait()
        except:
          Log.Message("Progress bar was not visible")
  else:
    Log.Error("No files found in the post condition.")
      
###############################################################################
# Function : delete_created_system1_Project_Variable
# Description: Deletes the created system based on a project variable.
# Parameter : None
###############################################################################
def delete_created_system1_Project_Variable():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == Project.Variables.system_1:
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  else:
    Log.Error("No systems found in the project variable.")

###############################################################################
# Function : Verify_Notification_Message
# Description: Verifies the presence of a notification message.
# Parameter : None
###############################################################################
def Verify_Notification_Message():
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_in_seconds(5000, 'wait')  
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  if N_Message_List:
    for i in N_Message_List:
      if i.Visible and i.Panel_ZIndex == 0:
        Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        break
  else:
    Log.Error("No messages found in the notification panel.")
          
###############################################################################
# Function : Click_on_Button_Conflict_Dialog
# Description: Clicks a button in the conflict dialog.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Click_on_Button_Conflict_Dialog(button_name):##
  buttons = msg_obj.importconflictdialogtextbox.object.FindAllChildren("ClrClassName", "Button", 50)
  if buttons:
    for button in buttons:
      if button_name in button.WPFControlText:
        button.click()
        break
    else:
      Log.Error(f'Mentioned {button_name} does not exists in Conflict_Dialog' )
  else:
    Log.Error("No buttons found in the conflict dialog.")
    
###############################################################################
# Function : Import_File_Directory
# Description: Sets the import file directory.
# Parameter : None
###############################################################################
def Import_File_Directory():##

  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path)
  Log.Message(f"New working directory: {os.getcwd()}")
  if not Project.Variables.VariableExists("ImportTestFile_path"):
          Project.Variables.AddVariable("ImportTestFile_path", "String")
  Project.Variables.ImportTestFile_path = os.getcwd()     
      
###############################################################################
# Function : Enter_systemName_systemlocation_ImportWindow_AE
# Description: Enters the system name and location in the import window.
# Parameter : file_format (str) - File format for the import.
###############################################################################
def Enter_systemName_systemlocation_ImportWindow_AE(file_format):
#  Import_window = aet_obj.importtextbox.object
#  if Import_window.Exists:
  filelocation = aet_obj.addressbandtextbox
  tox = (filelocation.object.Height)/2
  toy = 5
  filelocation.click_at(tox,toy)
  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]") 
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(file_format)
  Applicationutility.take_screenshot('taking Screenshot')
  Sys.Keys("[Enter]")
  
###############################################################################
# Function : Import_System1_Popup_AE_buttons
# Description: Clicks a button in the import popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Import_System1_Popup_AE_buttons(button_name):
    buttons_list = aet_obj.importtextbox.object.FindAllChildren('WndClass', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            Log.Message(button.WndCaption)
            if button_name in str(button.WndCaption):
                button.click()
                break
        else:
            Log.Error("Button name mentioned doesn't exist.")
    else:
        Log.Error("No buttons found in the import popup.")
  
###############################################################################
# Function : Wait_for_Import_pop_up_AE
# Description: Waits for the import popup to appear.
# Parameter : None
###############################################################################
def Wait_for_Import_pop_up_AE():
  try:
    windows = aet_obj.importdialogbutton.object
    windows.WaitProperty("Visible", True)
  except:
    Log.Error('Wait for import popup')
  
###############################################################################
# Function : importdialog_popup_button_AE_buttons
# Description: Clicks a button in the import dialog popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def importdialog_popup_button_AE_buttons(button_name):
    buttons_list = aet_obj.importdialogbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Error(f"Button name {button_name} mentioned doesn't exist.")
    else:
        Log.Error("No buttons found in the import dialog popup.")     

###############################################################################
# Function : Verify_Warning_Popup_locked_instance_AE
# Description: Verifies the presence of a warning popup for a locked instance.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def Verify_Warning_Popup_locked_instance_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Error(f'{message} doesnt exists in the pop up')
  else:
    Log.Error("No messages found in the warning popup.")
    
###############################################################################
# Function : MessageWindow_buttons
# Description: Clicks a button in the message window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def MessageWindow_buttons(button_name):
    buttons_list = aet_obj.savechangesdialogboxtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Error(f"Button name {button_name} mentioned doesn't exist.")
    else:
        Log.Error("No buttons found in the message window.")
    
###############################################################################
# Function : Verify_DeleteMessage_content_AE
# Description: Verifies the content of a delete message popup.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def Verify_DeleteMessage_content_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Error(f'{message} doesnt exists in the pop up')
  else:
    Log.Error("No messages found in the delete message popup.")
  
###############################################################################
# Function : verify_application_browser_template_AE
# Description: Verifies the presence of a template in the application browser.
# Parameter : identifier (str) - Identifier of the template to verify.
###############################################################################
def verify_application_browser_template_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          param = str(App_list[j].Item.ViewModel.TemplateVersion)
  
    Applicationutility.modal_dialog_window_button('OK')
  
    Applicationutility.wait_in_seconds(1500, 'wait')
    App_browser = aet_obj.applicationbrowsertextbox
    App_list = App_browser.find_children_for_treeviewrow()
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          if str(param) != str(App_list[j].Item.ViewModel.TemplateVersion):
            Log.Checkpoint('The ' + str(App_list[j].Item.Identifier.OleValue) + ' template is updated to ' + str(App_list[j].Item.ViewModel.TemplateVersion))
            break
    else:
      Log.Error('The template is not updated')
    Applicationutility.take_screenshot()
  else:
    Log.Error("No templates found in the application browser.")
  
###############################################################################
# Function : delete_system_Folder
# Description: Deletes a system folder.
# Parameter : node_name (str) - Name of the node to delete.
###############################################################################
def delete_system_Folder(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == node_name :
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        try:
          ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
        except:
          Log.Message("Circular progrss bar doesnt appear for folder deletion")
  else:
    Log.Error("No folders found in the system.")
  
###############################################################################
# Function : delete_all_folder_system_ord_EC
# Description: Deletes all folders in the system in order.
# Parameter : None
###############################################################################
def delete_all_folder_system_ord_EC():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    h_level = [int(i.HierarchyLevel) for i in SE_node_list]
    n = max(h_level)
    Log.Message(n)
    for i in range(n, 0, -1):
      for ord in SE_node_list:
        if int(ord.HierarchyLevel) == 0:
          pass
        elif ord.HierarchyLevel == i:
          Log.Message(i)
          Engineeringclientutility.clickR_node_ordno_SE(ord.WPFControlOrdinalNo)
          Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
          Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
          try:
            ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
          except:
            Log.Message("Circular progress bar doesnt appear for folder deletion")
  else:
    Log.Error("No folders found in the system.")
          
###############################################################################
# Function : close_Message_Window
# Description: Closes the message window.
# Parameter : None
###############################################################################
def close_Message_Window():
    inspect_win = msg_obj.renamepopupbutton
    inspect_win.click_at(inspect_win.width-25, 25)
    Applicationutility.take_screenshot()   
 
###############################################################################
# Function : Wait_import_conflict_dialog_AE
# Description: Waits for the import conflict dialog to appear.
# Parameter : None
###############################################################################
def Wait_import_conflict_dialog_AE():
   try:
    Conflict_dialog_box = aet_obj.importconflictdialogtextbox.object
    Conflict_dialog_box.WaitProperty("Visible", True)
   except:
    Log.Message("Conflict Dialog Box did not exists") 
   
###############################################################################
# Function : ConflictWindow_buttons
# Description: Clicks a button in the conflict window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def ConflictWindow_buttons(button_name):
    buttons_list = aet_obj.importconflictdialogtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Error(f"Button name {button_name} mentioned doesn't exist.")
    else:
        Log.Error("No buttons found in the conflict window.")
    
###############################################################################
# Function : Verify_latest_template_added_Application_browser_AE
# Description: Verifies the presence of the latest template added in the application browser.
# Parameter : template_name (str) - Name of the template to verify.
###############################################################################
def Verify_latest_template_added_Application_browser_AE(template_name):
  AB_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if AB_list:
    for template in AB_list:
      if template_name == template.DataContext.Identifier.OleValue:
        Log.Message(f'{template_name} exists in Application browser')
        break
    else:
      Log.Error(f'{template_name} does not exists in Application browser')
  else:
    Log.Error("No templates found in the application browser.")
    
###############################################################################
# Function : template_checkbox
# Description: Checks or unchecks a template checkbox.
# Parameter : param (str) - Template identifier and state in the format 'identifier$$state'.
###############################################################################
def template_checkbox(param):
  identifier, state = param.split('$$')
  obj = aet_obj.instanceeditorchecklisttextbox.object
  obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if obj_list:
    for item in obj_list:
      checkbox_name = item.DataContext.ElementFullPath.OleValue 
      checkbox_ele = checkbox_name.split('|')
      Log.Message(str(checkbox_ele))
      if str(identifier) in str(checkbox_ele):
        checkbox = item.FindAllChildren('ClrClassName', 'CheckBox', 1000)
        break
    if int(state) != 0 :
      checkbox[0].wState = 1
      checkbox[0].WaitProperty('wState', 1, 100000)
      Log.Message('Checked')
    elif int(state) != 1:
      checkbox[0].wState = 0
      Log.Message('Unchecked')
  else:
    Log.Error("No checkboxes found in the template.")
    
def TC_EPE_AE_00012_and_TC_EPE_AE_00014():
  click_application_browser_template_AE('MotorGP_1$$1.0.123')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^c')
  click_application_browser_folder_AE('Folder_2')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^v')

def TC_EPE_AE_00012_and_TC_EPE_AE_00014_1():
  click_application_browser_template_AE('ValveGP_1$$1.0.100')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^c')
  click_application_browser_folder_AE('Folder_2')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^v')  
  
###############################################################################
# Function : click_application_browser_template_AE
# Description: Clicks a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def click_application_browser_template_AE(param):
  identifier,version=param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          if str(version) == str(App_list[j].Item.ViewModel.TemplateVersion):
            App_list[j].Click()
            Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
            break
    Applicationutility.wait_in_seconds(1000, 'wait')
  else:
    Log.Error("No templates found in the application browser.")
  
###############################################################################
# Function : click_application_browser_folder_AE
# Description: Clicks a folder in the application browser.
# Parameter : identifier (str) - Identifier of the folder to click.
###############################################################################
def click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].Click()
          Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
  else:
    Log.Error("No folders found in the application browser.")
       
def instance_locked_close_AE():
  msg_obj.exportpopupbutton.object.close()      
  
def Verify_file_existance():
  exported_xml = Project.Variables.system_1 + ".xml"
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Error(f"File does not exist: {d_path}")  

###############################################################################
# Function : verify_instance_validity
# Description: Verifies the validity of instances in the application browser.
# Parameter : None
###############################################################################
def verify_instance_validity():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  valid_instances = []
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
        submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
        for i in submenuitems:
          if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
            Log.Message(str(instance.DataContext.Identifier.OleValue) + ': has Invalid link')
            break
        else:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ': has valid link')
        valid_instances.append(str(instance.DataContext.Identifier.OleValue))
  else:
    Log.Error("No instances found in the application browser.")
  return valid_instances
  
###############################################################################
# Function : expand_folder_system
# Description: Expands all folders in the system.
# Parameter : None
###############################################################################
def expand_folder_system():
  ApplicationBroswer = aet_obj.applicationbrowsertextbox.object
  instances = ApplicationBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for i in instances:
      if i.IsExpandable == True:
        i.IsExpanded = True
        continue
  else:
    Log.Error("No folders found in the system.")
      
###############################################################################
# Function : verify_instance_application_browser
# Description: Verifies the presence of an instance in the application browser.
# Parameter : param (str) - Identifier of the instance to verify.
###############################################################################
def verify_instance_application_browser(param):
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
  #        Log.Message(str(instance.DataContext.Identifier.OleValue) + ' is  present in the Application browser')
        if param in str(instance.DataContext.Identifier.OleValue):
          Log.Checkpoint(f'{str(instance.DataContext.Identifier.OleValue)} is present in Application Browser')
          break
    else:
      Log.Error(f'{param} is not present in Application Browser')
  else:
    Log.Error("No instances found in the application browser.")
        
###############################################################################
# Function : verify_SameName_Errorbox_application_browser
# Description: Verifies the presence of a same name error box in the application browser.
# Parameter : None
###############################################################################
def verify_SameName_Errorbox_application_browser():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TemplatedAdorner', 1000)
  if instances:
    Log.Message(len(instances))
    for instance in instances:
      if instance.IsVisible:
        Log.Message(f'{instance.AdornedElement.ToolTip.OleValue} appeared on the screen as a ToolTip Value')
        break
    else:
      Log.Error(f'{instance.AdornedElement.ToolTip.OleValue} did not appear on the screen as a ToolTip Value')
  else:
    Log.Error("No error boxes found in the application browser.")
    
###############################################################################
# Function : rename_instance_popup_button
# Description: Clicks a button in the rename instance popup.
# Parameter : button (str) - Name of the button to click.
###############################################################################
def rename_instance_popup_button(button):
  rename_intance_object = aet_obj.renameinstancepopupmessagebutton.object
  buttons = rename_intance_object.FindAllChildren('ClrClassName', 'Button', 1000)
  if buttons:
    for i in buttons:
      if button in i.WPFControlText:
        i.Click()
        break
    else:
      Log.Error(f"No {button} button exists")
  else:
    Log.Error("No buttons found in the rename instance popup.")
    
###############################################################################
# Function : Verify_node_link_line_asset_work_AE
# Description: Verifies the presence of a node link line in the asset workspace.
# Parameter : param (str) - Identifier of the node to verify.
###############################################################################
def Verify_node_link_line_asset_work_AE(param):
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if param == str(node_element.DataContext.Identifier):
        tox = node_element.Width
        toy = node_element.Height
        node_element.ClickR(tox-5, toy/2)
        try:
          if eng_obj.rclickmenutextbox.exists:  
            Log.Message('verified two instances linked between elements')
        except:
          Log.Message('Instances are unlinked')
  else:
    Log.Error("No nodes found in the asset workspace.")
        
###############################################################################
# Function : Right_click_Assestworkspace_editor_AE
# Description: Right-clicks an instance in the asset workspace editor.
# Parameter : None
###############################################################################
def Right_click_Assestworkspace_editor_AE():
  template_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'InstanceNode', 1000)
  if template_list:
    for node in template_list:
      if 'ValveGP_1' in str(node.DataContext.Identifier.OleValue):
        Log.Message('verified instance name')
        node.ClickR((node.width/2), (25))
        Log.Message('Right clicked on instance name')
  else:
    Log.Error("No instances found in the asset workspace editor.")
      
###############################################################################
# Function : click_Abort_AE
# Description: Clicks the abort button in the notification panel.
# Parameter : None
###############################################################################
def click_Abort_AE():
  Applicationutility.wait_in_seconds(500, 'Wait')
  Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for item in Abort_list:
    if item.Panel_ZIndex == 0:
      #Log.Message(item.Panel_ZIndex)
      if item.DataContext.Status.OleValue == "Executing":
        #Log.Message(item.DataContext.Status.OleValue)
        button_list = item.FindAllChildren('ClrClassName', 'Button', 100)
        #Log.Message(len(button_list))
        button_list[0].Click()
        break
      else:
       Log.Error("No abort button is found to click for executing item.")

###############################################################################
# Function : replace_template_combo_AE
# Description: Replaces a template in the combo box.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def replace_template_combo_AE(param):
    identifier, version = param.split('$$')
    comb = aet_obj.replacetemplatecombotextbox.object
    if comb.Items.Count:
      for i in range(comb.Items.Count):
        if identifier in comb.Items.Item[i].TemplateName.OleValue:
          if version in comb.Items.Item[i].TemplateName.OleValue:
            comb.SelectedIndex = i
            Log.Message('The Selected template is ' + str(comb.Items.Item[i].TemplateName.OleValue))
            Applicationutility.wait_in_seconds(1500, 'wait')
            aet_obj.replacetemplatetextbox.click()
            break
      else:
        Log.Error('No template with ' + str(identifier) + ' and ' + str(version))
    else:
      Log.Error("No templates found in the combo box.")
      
###############################################################################
# Function : capture_template_application_browser_AE
# Description: Captures a template in the application browser.
# Parameter : identifier (str) - Identifier of the template to capture.
###############################################################################
def capture_template_application_browser_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        return identifier + str('$$')+ str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue)
  else:
    Log.Error("No templates found in the application browser.")

###############################################################################
# Function : verify_template_replaced_AE
# Description: Verifies that a template has been replaced in the application browser.
# Parameter : param (str) - Template identifier and new template in the format 'identifier$$template'.
###############################################################################
def verify_template_replaced_AE(param):
  identifier, template = param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        if str(template) != str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue):
          Log.Checkpoint('The Template ' + str(template) + ' is changed to ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue))
          break
        else:
          Log.Error('The Template ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue) + ' is not changed.' )  
  else:
    Log.Error("No templates found in the application browser.")
        
###############################################################################
# Function : verify_button_enabled_disabled_modaldialogue_window
# Description: Verifies whether a button is enabled or disabled in a modal dialogue window.
# Parameter : button_name (str) - Name of the button to verify.
###############################################################################
def verify_button_enabled_disabled_modaldialogue_window(button_name):
  buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WPFControlText):
        if  not button.Enabled:
          Log.Warning( str(button.WPFControlText) + ' button is disabled')
          Applicationutility.take_screenshot()
          break
        else:
             Log.Message(str(button.WPFControlText) +" button is Enabled")
  else:
    Log.Error("No buttons found in the modal dialogue window.")
           
###############################################################################
# Function : verify_template_application_browser
# Description: Verifies the presence of a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'template$$version'.
###############################################################################
def verify_template_application_browser(param):
  template, version = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible:
        if template_list[i].DataContext.ViewModel.DisplayTypeName.OleValue != 'Folder':
          if template in template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue:
            if version in str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue):
              Log.Checkpoint(str(template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue) +' '+  str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue))
              break
    else:
      Log.Error(f'Template {template} - {version} not in Application Browser')     
  else:
    Log.Error("No templates found in the application browser.")
      
###############################################################################
# Function : wait_import_dialogue_window_appear
# Description: Waits for the import dialogue window to appear.
# Parameter : None
###############################################################################
def wait_import_dialogue_window_appear():
  try:
    Import_window = aet_obj.importtextbox.object
    Import_window.WaitProperty('Visible',True, 1000)
    Log.Message("Import window  appeared")   
  except:
    Log.Error("Import window did not appear")

###############################################################################
# Function : Verify_Notification_pannel_Message
# Description: Verifies the presence of a notification panel message.
# Parameter : Message (str) - Expected message in the notification panel.
###############################################################################
def Verify_Notification_pannel_Message(Message):
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_for_execution()
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  if N_Message_List:
    for i in N_Message_List:
      if i.Visible and i.Panel_ZIndex == 0:
        if Message in i.DataContext.Message.OleValue:
          Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
          Applicationutility.wait_in_seconds(1000, 'Wait')
          break
        else:
          Log.Error(f'{i.DataContext.Message.OleValue} in Notification Pannel')
  else:
    Log.Error("No messages found in the notification panel.")
        
## this method can be used for drag and drop intances in assetworkspace or linkeditor based on position 
## only 3 position can be defined based on the screen width
###############################################################################
# Function : drag_app_browser_drop_asset_workspace_editor_with_POS_AE
# Description: Drags an item from the app browser and drops it into the asset workspace editor at a specified position.
# Parameter : param (str) - Template identifier and position in the format 'template$$pos'.
###############################################################################
def drag_app_browser_drop_asset_workspace_editor_with_POS_AE(param):
  Log.Message(param)
  template, pos = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if template in str(template_list[i].DataContext.Identifier.OleValue):
          fromx = template_list[i].ScreenLeft
          fromy = template_list[i].ScreenTop
          Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
          break
  else:
    Log.Warning("No templates found in the application browser.")
  
  Workspace_editor = aet_obj.assertworkspaceeditortextbox.object
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_presence = node_element_parent.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
  n = len(node_element_presence)
  
  if pos == '1':
    tox = node_element_presence[n-1].ScreenLeft
    tox = tox/2
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
  elif pos == '2':
    tox = Workspace_editor.ScreenLeft
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
  else:
    tox = node_element_presence[n-1].ScreenLeft
    tox = tox*1.25
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
    
###############################################################################
# Function : verify_application_explorer_instance_editor_tab1
# Description: Verifies the presence of an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to verify.
###############################################################################
def verify_application_explorer_instance_editor_tab1(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
          break
    else:
      Log.Error('The instance editor tab was not found : ' + str(identifier))
  else:
    Log.Error("No instance editor tabs found in the application explorer.")

###############################################################################
# Function : remove_PV_ranged_link_AE
# Description: Removes the PV ranged link in the asset workspace.
# Parameter : None
###############################################################################
def remove_PV_ranged_link_AE():
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if 'PVRanged' == str(node_element.DataContext.Identifier):
        tox = node_element.Width
        toy = node_element.Height
        node_element.ClickR(tox-5, toy/2)
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Engineeringclientutility.select_ContextMenu_Items_EC('Delete')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        break
    else:
      Log.Error('PVRanged not found.')
  else:
    Log.Error("No nodes found in the asset workspace.")
    
###############################################################################
# Function : EmptyPages_ImportWindow_PE
# Description: Enters the system name and location in the import window for empty pages.
# Parameter : file_format (str) - File format for the import.
###############################################################################
def EmptyPages_ImportWindow_PE(file_format):
  filelocation = aet_obj.addressbandtextbox
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  base_path = os.getcwd()
  folder_name =  "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(file_format)


  
###############################################################################
# Function   : handle_import_conflicts
# Parameters : target_instance (str) - MotorGP_1.
# Description: Handles import conflict resolution by clicking "Update" for 
#              a specific instance (e.g., 'MotorGP_1') and skipping all others..
###############################################################################
def handle_import_conflict(target_instance):
  try:
    buttons = aet_obj.importconflictdialogtextbox.object.FindAllChildren('ClrClassName', 'RadioButton', 1000)

    [btn.Click() for btn in buttons if (
      (getattr(getattr(getattr(btn, "DataContext", None), "OldInstanceIdentifier", None), "OleValue", None) == target_instance and "Update" in str(getattr(btn, "ToolTip", ""))) or
      (getattr(getattr(getattr(btn, "DataContext", None), "OldInstanceIdentifier", None), "OleValue", None) != target_instance and "Skip" in str(getattr(btn, "ToolTip", "")))
    )]

  except Exception as e:
    Log.Error(f"Import conflict handler failed: {e}")
    
###############################################################################  
# Function : verify_progress_indicator_AE
# Description: Verifies the progress of instances in the application browser.
# Parameter : identifier (str) - Identifier of the instance to verify the progress
###############################################################################
def verify_progress_indicator_AE(param):
  lst = {
    0: 'Instance still has default values/no links exist/no facet has been assigned',
    25: 'No facet has been assigned',
    50: "Facets have not been assigned to both types of projects/the status of some assigned facets is not 'Assigned'",
    75: "Some facets are not assigned yet",
    "locked": "The instance is being updated",
    100 : ''
  }
 
  identifier, progress_value = param.split('$$')
 
  # Convert progress_value to int if it's a digit
  if progress_value.isdigit():
    progress_value = int(progress_value)
 
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
 
  if template_list:
    for item in template_list:
      if item.Visible:
        if identifier in str(item.DataContext.Identifier.OleValue):
          if item.DataContext.IsProgressStateVisible:
            tooltip = item.DataContext.ProgressStateToolTip.OleValue
            Log.Message(tooltip)
            expected_tooltip = lst.get(progress_value)
            if expected_tooltip in tooltip:
              Log.Checkpoint(f"The {item.DataContext.Identifier.OleValue} progress when {str(progress_value)}% is: " + str(item.DataContext.ProgressStateToolTip.OleValue))
            else:
              Log.Error("Progress tooltip did not match the expected value.")
            break
          elif not item.DataContext.IsProgressStateVisible:
               if progress_value == 100:
                  Log.Checkpoint(f"The {item.DataContext.Identifier.OleValue} progress is at 100%.")
                  break
          else:
            Log.Error(f"{item.DataContext.Identifier.OleValue}'s Progress State is not visible.")
    else:
      Log.Error("Instance not found in the list.")
  else:
    Log.Error("No templates found.")

###############################################################################  
# Function : verify_progress_status_of_all_templates
# Description: Verifies the progress of all instances in the application browser.
# Parameter : None
###############################################################################    
    
def verify_progress_status_of_all_templates():
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for item in template_list:
      if item.Visible:
        if item.DataContext.Identifier.OleValue:
          if item.DataContext.ProgressStateToolTip.OleValue:
              Log.Checkpoint(f"The instance progress when {str(progress_value)}% is: " + str(item.DataContext.ProgressStateToolTip.OleValue))
          else:
              Log.Error("There is No Progress tooltip Value.")
    else:  
      Log.Error("Instance not found in the list.")
  else:
    Log.Error("No templates found.")
   
###############################################################################
# Function : click_on_scroll_down_app_browser
# Description: Scrolls down the application browser textbox a specified number 
#              of times by simulating scroll or click actions.
# Parameter : count (int) - The number of times to scroll down.
# Example : click_on_scroll_down_app_browser(5)
###############################################################################
def click_on_scroll_down_app_browser(count):
    temp_browser = aet_obj.applicationbrowsertextbox
    for _ in range(int(count)):
        temp_browser.click_at((temp_browser.width - 15), (temp_browser.height - 35))

###############################################################################  
# Function : Search_ApplicationBrowser_textbox
# Description: Searches the Application Browser in AE
# Parameter : 
# Example :  
###############################################################################
def Search_ApplicationBrowser_textbox(param):  
  AppBrowser = aet_obj.applicationbrowsertextbox.object
  App_list = AppBrowser.FindAllChildren("ClrClassName", "SearchComboBoxControl", 100)
  for i in App_list:
    if i.WPFControlName == "PART_SearchTextBox":
      i.Keys(param)
      i.WaitProperty('Text.OleValue', param, 3000)
      if i.Text.OleValue == param:
         Log.Checkpoint(f'The value : {i.Text.OleValue} is entered in the searchbox')
      else:
           Log.Error(f'The value : {param} is not entered in the searchbox')
      aet_obj.workspacebutton.object.Click()
      break
  else:
    Log.Error("Search textbox not found in application browser.")

###############################################################################  
# Function   : Select_Filter_in_ApplicationBrowser  
# Description: Applies a filter to a specific column in the Application Browser  
#              using the column name provided.  
# Parameter  :  *Filter â€“ A string in the format "FilterName"  
#Identifier
#ViewModel.LinkValid
#ViewModel.DataValid
#ViewModel.TemplateVersion
#ViewModel.TemplateIdentifier
# Example    :  Select_Filter_in_ApplicationBrowser("Identifier")  
###############################################################################
def Select_Filter_in_ApplicationBrowser(filter_name):
  Filtericon = aet_obj.applicationbrowsertextbox.object.FindAllChildren("ClrClassName", "FilteringDropDown", 1000)
  Log.Message(len(Filtericon))
  for i in Filtericon:
    Log.Message(i.Column.UniqueName.OleValue)
    if filter_name == i.Column.UniqueName.OleValue:
      i.Click()
      Log.Checkpoint(f"{i.Column.UniqueName.OleValue} filter is clicked")
      break
  else:
        Log.Error(f"{filter_name} not found")

###############################################################################
# Function   : Verify_Notification_Message_Details  
# Description: Verifies if a specific message is present in the Notification Panel,  
#              expands the message, and scrolls through to log all visible messages.  
# Parameter  :  
#   message – The exact message text to verify in the Notification Panel  
#   scrolls – Number of times to scroll through the panel to capture messages  
# Example    :  
#   Verify_Notification_Message_Details("Export (Completed)", "5")  
###############################################################################

def Verify_Notification_Message_Details(message, scrolls):
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_in_seconds(5000, 'wait')  
  list = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "GridViewToggleButton", 50)
  notificationpanel = msg_obj.notificationpanneltextbox
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  if N_Message_List:
    for i in N_Message_List:
      if i.Visible and i.Panel_ZIndex == 0 and i.DataContext.Message.OleValue == message:
        Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        expand_btns = i.FindAllChildren("WPFControlName", "PART_ExpandButton", 5)
        for btn in expand_btns:
              if btn.WPFControlName == "PART_ExpandButton":
                btn.Click()
                Log.Checkpoint("Notification Panel message is expanded")
                break

    scrolls = int(scrolls)
    seen_messages = set()
    for scroll_count in range(scrolls):
        notificationpanel.click_at((notificationpanel.width - 15), (notificationpanel.height - 35))
        aqUtils.Delay(700) 
        for index, j in enumerate(N_Message_List, start=1):
            if j.Visible and j.DataContext.Message.OleValue not in seen_messages:
                seen_messages.add(j.DataContext.Message.OleValue)
                Log.Checkpoint(f"{j.DataContext.Message.OleValue} in Notification Panel")

    Log.Message(f"Finished scrolling {scrolls} times.")

    for _ in range(scrolls):
            notificationpanel.click_at((notificationpanel.width - 15), 10)  

  else:
    Log.Error("No messages found in the notification panel.")


###############################################################################  
# Function   : faulty_modification_csvdata_AE  
# Description: Replaces the TemplateIdentifier value in a CSV file with a new  
#              identifier while keeping the version unchanged.  
# Parameter  :  
#   file_details   – A string in the format "System$$.csv" to locate the file  
#   new_identifier – The new TemplateIdentifier to replace the existing one  
# Example    :  
#   faulty_modification_csvdata_AE("System$$.csv", "$MyCustomTemplate")  
###############################################################################

def faulty_modification_csvdata_AE(file_details, new_identifier):
  # combines system name and file format
  file_name, file_format = file_details.split('$$')
  exported_csv = Project.Variables.VariableByName[file_name]+file_format
  Applicationutility.wait_in_seconds(10000, 'wait')

  # collect all the template in Application Browser
  template_details = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)

  # extract csv file
  folder_name = "Test_Import_Files"
  d_path = os.path.abspath(os.path.join(os.getcwd(), folder_name, exported_csv))

  #read from csv    
  with open(d_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #to get a specific row data and modify it
    for i, line in enumerate(lines):
          if line.startswith(":TemplateIdentifier="):
              match = re.match(r"(:TemplateIdentifier=)(\S+)(\s+Version=.*)", line)
              if match:
                prefix = match.group(1)          # ":TemplateIdentifier="
                old_identifier = match.group(2)  # "$INTERLOCK8OFFGP_UC"
                version_part = match.group(3)    # " Version=1.0.5"

                # Build new line with new_identifier but same version part
                lines[i] = f"{prefix}{new_identifier}{version_part}\n"
                break

  #write to csv    
  with open(d_path, 'w', encoding='utf-8') as f:
          f.writelines(lines)
          Log.Checkpoint(f"File saved and TemplateIdentifier changed to: {new_identifier}")



###############################################################################  
# Function   : Apply_Filter_AssetWorkspace  
# Description: Applies a filter in the Asset Workspace grid by selecting a column  
#              and entering the filter value.  
# Parameter  :  
#   Filter – A string in the format "Filtername$$Value"  
#            Example: "Identifier$$AnalogInputGP_1"  
# Example    :  
#   Apply_Filter_AssertWorkspace("Identifier$$AnalogInputGP_1")  
###############################################################################

def Select_Filter_AssetWorkspace(filter_name):
  AssetFilter = aet_obj.AssetWorkspaceFilter.object.FindAllChildren("ClrClassName", "FilteringDropDown", 50)
  for i in AssetFilter:
          if i.Column.UniqueName.OleValue == filter_name:
            i.Click()
            Log.Checkpoint(f"{i.Column.UniqueName.OleValue} filter is clicked")
            break
  else:
        Log.Checkpoint(f"{filter_name} not found")


############################################################################################
# Function   : enter_text_filter_textboxs_in_Assetworkspace
# Description: Enters text into one of two known text boxes in the filter panel.
# Parameter  : param (str) - TextBoxName$$ValueToEnter
# Example    : enter_text_filter_textboxs_in_Assetworkspace("textbox1$$AssertWorkspace_1")
#############################################################################################

def enter_text_filter_textboxs_in_Assetworkspace(param):
    txtbx, Txt = param.split('$$')  
    stackpanels = eng_obj.filterstackpannel.object.FindAllChildren('ClrClassName', 'StringFilterEditor', 100)

    if txtbx == 'textbox1':
        stackpanels[1].Text = Txt
        if stackpanels[1].DataContext.Value.OleValue == Txt:
          Log.Checkpoint(f'The value set in textbox1 is: {stackpanels[1].Text.OleValue}')
    elif txtbx == 'textbox2':
        stackpanels[0].Text = Txt
        if stackpanels[0].DataContext.Value.OleValue == Txt:
          Log.Checkpoint(f'The value set in textbox2 is: {stackpanels[0].Text.OleValue}')
    else:
        Log.Warning(f'Unknown or missing textbox identifier: {txtbx}')
        
###############################################################################
# Function   : verify_all_folders_expanded_or_Collapsed
# Description: Verifies if all folders in the Application Browser are expanded or Collapsed.
#              Logs a warning for each folder that is expandable but not expanded.
#              If all folders are expanded, logs a success message.
# Parameters : None
###############################################################################  
   
def verify_all_folders_expanded_or_Collapsed():
  instances = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  not_expanded = [i for i in instances if i.IsExpandable and not i.IsExpanded]
  [Log.Message(f"Folder Collapsed: {i.DataContext.Identifier}") for i in not_expanded]
  if not not_expanded:
    Log.Message("All folders are expanded")
    
###############################################################################
# Function   : navigate_identifier_application_browser
# Description: Navigates to a specific identifier in the Application Browser,
#              selects it, and performs a directional key press (Left or Right).
#              Used for expanding or collapsing nodes using keyboard navigation.
# Parameters : 
#   identifier - The unique name (string) of the instance or folder to focus on.
#   direction  - The direction of keyboard action to perform ("left" or "right" or up, down).
# Notes      :
#   - Presses LEFT to collapse and RIGHT to expand the target node.
#   - Skips hidden items and only interacts with visible ones.
###############################################################################    
    
def navigate_identifier_application_browser(identifier, direction):
  rows = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if not rows: return Log.Warning("No identifiers found.")
  direction = direction.lower()
  key_map = {"left": "[Left]", "right": "[Right]", "up": "[Up]", "down": "[Down]"}
  key = key_map.get(direction)
  if not key: return Log.Warning(f"Invalid direction '{direction}'")
  for r in rows:
    if r.Visible and str(r.DataContext.Identifier.OleValue) == identifier:
      r.Click()
      if direction in ["up", "down"]:
        for _ in range(len(rows)): r.Keys(key)
        Log.Message(f"Scrolled {direction.upper()} to {'top' if direction == 'up' else 'bottom'} on '{identifier}'")
      else:
        r.Keys(key)
        Log.Message(f"Pressed {direction.upper()} on '{identifier}'")
      Applicationutility.wait_in_seconds(2000, 'wait')
      break
      
###############################################################################
# Function   : double_click_instance_in_instance_editor
# Description: Searches for the given instance name in the Instance Editor.
#              If found, performs a double-click on the corresponding row and
#              logs whether it is expanded or not.
#              Logs a warning if the instance is not found or an error occurs.
# Parameters : name (str) – The name of the instance to double-click.
###############################################################################
      
def double_click_instance_in_instance_editor(name):
  for row in aet_obj.instanceeditorchecklisttextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000):
    try:
      if any(tb.WPFControlText == name for tb in row.FindAllChildren('ClrClassName', 'TextBlock', 100)):
        row.DblClick(); Log.Checkpoint(f"{name} | IsExpanded: {row.IsExpanded}"); return
    except Exception as e: Log.Error(f"Row error: {e}")
  Log.Error(f"Instance '{name}' not found.")
  
###############################################################################
# Function   : double_click_asset_workspace_folder
# Description: Searches for the given identifier in the Asset Workspace TreeView.
#              If a matching and visible folder is found, performs a double-click
#              on the folder and logs the action.
#              Waits for a second after the click to allow UI updates.
# Parameters : identifier (str) – The identifier of the folder to double-click.
###############################################################################
  
def double_click_asset_workspace_folder(identifier):
  for row in aet_obj.assetworkspacetextbox.find_children_for_treeviewrow():
    if row.Visible and identifier in str(row.Item.Identifier.OleValue):
      row.DblClick()
      Log.Message(f"Double-clicked on {row.Item.Identifier.OleValue}")
      Applicationutility.wait_in_seconds(1000, 'wait')
      return
  Log.Error("No matching folder found in asset workspace.")

###############################################################################
# Function   : key_action_asset_workspace_folder
# Description: Navigates within the Asset Workspace TreeView using keyboard arrows.
#              Finds the row matching the identifier, brings it into focus, and 
#              presses the specified arrow key (left, right, up, down).
#              If scrolling (up/down), key press is repeated for full scroll.
#              Logs appropriate messages or warnings for invalid directions or 
#              missing identifiers.
# Parameters : identifier (str) – The identifier to locate in the TreeView.
#              direction  (str) – The direction key to press (left/right/up/down).
###############################################################################  
    
def key_action_asset_workspace_folder(identifier, direction):
  rows = aet_obj.assetworkspacetextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if not rows: return Log.Warning("No identifiers found.")
  direction = direction.lower()
  key_map = {"left": "[Left]", "right": "[Right]", "up": "[Up]", "down": "[Down]"}
  key = key_map.get(direction)
  if not key: return Log.Warning(f"Invalid direction '{direction}'")
  for r in rows:
    if r.Visible and str(r.DataContext.Identifier.OleValue) == identifier:
      r.Click()
      if direction in ["up", "down"]:
        for _ in range(len(rows)): r.Keys(key)
        Log.Message(f"Scrolled {direction.upper()} to {'top' if direction == 'up' else 'bottom'} on '{identifier}'")
      else:
        r.Keys(key)
        Log.Message(f"Pressed {direction.upper()} on '{identifier}'")
      Applicationutility.wait_in_seconds(2000, 'wait')
      break
      
def double_click_templatebrowser_folder(identifier):
  for row in aet_obj.templatesbrowsertextbox.find_children_for_treeviewrow():
    try:
      if row.Visible and identifier in str(row.Item.Identifier.OleValue):
        row.DblClick(); Log.Message(f"{identifier} | IsExpanded: {row.IsExpanded}"); return
    except Exception as e: Log.Warning(f"Row error: {e}")
  Log.Warning("No matching folder found in asset workspace.")
 
  
   
def key_action_template_browser_folder(identifier, direction):
  rows = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if not rows: return Log.Warning("No identifiers found.")
  direction = direction.lower()
  key_map = {"left": "[Left]", "right": "[Right]", "up": "[Up]", "down": "[Down]"}
  key = key_map.get(direction)
  if not key: return Log.Warning(f"Invalid direction '{direction}'")
  for r in rows:
    if r.Visible and str(r.DataContext.Identifier.OleValue) == identifier:
      r.Click()
      if direction in ["up", "down"]:
        for _ in range(len(rows)): r.Keys(key)
        Log.Message(f"Scrolled {direction.upper()} to {'top' if direction == 'up' else 'bottom'} on '{identifier}'")
      else:
        r.Keys(key)
        Log.Message(f"Pressed {direction.upper()} on '{identifier}'")
      Applicationutility.wait_in_seconds(2000, 'wait')
      break
      
def extend_right_panel():
    # get the panel object
    panel = aet_obj.applicationbrowsertextbox.object
    delta_px=150
    extra_right=5

    # start point: middle height, a little to the right of the edge
    start_x = panel.Width + extra_right
    start_y = panel.Height // 2

    # drag horizontally
    panel.Drag(start_x, start_y, start_x + delta_px, start_y)

    aqUtils.Delay(200)
    Log.Message(f"Extended panel by {delta_px}px (start {extra_right}px outside to the right)")

###############################################################################
# Function    : verify_status_instance_editor
# Description : Verifies that the status of an instance in the Application 
#               Browser matches the status displayed in the Instance Editor.
# Parameters  : None
# Returns     : None
###############################################################################
def verify_status_instance_editor():
    instnaceBroswer = aet_obj.applicationbrowsertextbox.object
    instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)

    AE_Status_value = None
    Instance_editor_status = None

    if instances:
        for instance in instances:
            if instance.Panel_ZIndex != 0 and instance.DataContext is not None:
                submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
                AE_Status_value = submenuitems[1].Value
                break
          
    obj = aet_obj.workspacebutton.object
    obj_lst = obj.FindAllChildren('ClrClassName', 'DockPanel', 1000)    
    if obj_lst:
        for x in obj_lst:
            x_lst = x.FindAllChildren('ClrClassName', 'TextBlock', 1000)
            Instance_editor_status = x_lst[0].WPFControlText
            break
          
    if AE_Status_value == Instance_editor_status:
        Log.Checkpoint(f"PASS: AE Status '{AE_Status_value}' matches Instance Editor status '{Instance_editor_status}'.")
    else:
        Log.Error(f"FAIL: AE Status '{AE_Status_value}' does not match Instance Editor status '{Instance_editor_status}'.")
        
###############################################################################
# Function    : verify_invalid_details
# Description : Verifies the validation messages shown in the 'Instance Invalid'
#               popup based on the provided instance identifier value.
#               Checks for specific validation errors such as:
#               - Invalid characters present
#               - Identifier containing only digits
#               - Identifier length exceeding limits
# Parameters  : None
# Returns     : None
###############################################################################
    def has_special_char(s):
      for ch in s:
        if not ch.isalnum():  # checks if char is NOT A-Z, a-z, or 0-9
            return True
    return False   
    
def verify_invalid_details():
    indtifiervalue = verify_instance_validity()
    obj=aet_obj.workspacebutton.object
    obj_lst=obj.FindAllChildren('ClrClassName', 'UCVectorButton', 1000)    
    if obj_lst:
      obj_lst[0].click()
      
    pop_up=aet_obj.instanceinvalid_popup.object
    pop_up_lst=pop_up.FindAllChildren('ClrClassName', 'InstanceInvalidDialogView', 1000)
    if str(indtifiervalue[0]) in str(pop_up_lst[0].Title):
        Log.Checkpoint("Pass")
    
      
    pop_up_values=pop_up.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
    if pop_up_values:
        for i in pop_up_values:
            if str(indtifiervalue[0]) in i.WPFControlText:                
                Invalid_Details= (pop_up_values[len(pop_up_values)-2].WPFControlText)
                break
                
    value = str(indtifiervalue[0])          
    if len(value) < 17:
      if has_special_char(value):
        if "invalid character" in str(Invalid_Details):
            Log.Checkpoint("Validation Passed: 'invalid character' found in Invalid_Details.")
        else:
            Log.Error("Validation Failed: Expected 'invalid character' not found in Invalid_Details.")
      elif value.isdigit():
        if "contain at least one character" in str(Invalid_Details):
            Log.Checkpoint("Validation Passed: 'contain at least one character' found in Invalid_Details.")
        else:
            Log.Error("Validation Failed: Expected 'contain at least one character' not found in Invalid_Details.")
    elif len(value) > 18:
      if "exceeded limit" in str(Invalid_Details):
        Log.Checkpoint("Validation Passed: 'exceeded limit' found in Invalid_Details.")
      else:
        Log.Error("Validation Failed: Expected 'exceeded limit' not found in Invalid_Details.")   
    Sys.Keys("[Esc]")
    
###############################################################################
#Function :multiclick_application_browser_template_AE
# Description : Clicks on multiple templates in application browser of AE using 
#               identifier and version of the template
# Parameter :(str) - Identifier and version of the template
# Example : multiclick_application_browser_template_AE("Identifier$$Version")
############################################################################### 
def multiclick_application_browser_template_AE(param):
  identifier,version = param.split("$$")
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for item in App_list:
      if identifier in item.DataContext.Identifier.OleValue:
        if version in item.DataContext.ViewModel.TemplateVersion.OleValue:
          item.Click(10,10,skCtrl)
          Log.Message(f"{item.DataContext.Identifier.OleValue} with version {item.DataContext.ViewModel.TemplateVersion.OleValue} is clicked")
          break
        else:
          Log.Error(f"{item.DataContext.Identifier.OleValue} with version {item.DataContext.ViewModel.TemplateVersion.OleValue} is not clicked")
          
########################################################################################
# Function : Click_module_name_instance_editor
# Description : Clicks on the specific module name in instance editor.
# Parameter : identifier (str) - Name of the module.
#             Example: "Logic"
########################################################################################
def Click_module_name_instance_editor(identifier):
    obj = aet_obj.instanceeditorchecklisttextbox.object
    obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if not obj_list:
        Log.Warning("No checkboxes found in the template.")
        return
    Log.Message(f'Total items found: {len(obj_list)}')
    clicked = False
    for item in obj_list:
        full_path = item.DataContext.ElementFullPath.OleValue
        element_parts = full_path.split('|')
        if str(identifier) in element_parts[-1]:
            Log.Message(f"Matched Element: {full_path}")
            item.Click()
            Log.Message(f"Clicked on checkbox label/value: {element_parts[-1]}")
            clicked = True
            break
    if not clicked:
      Log.Warning(f"No matching checkbox label found for identifier '{identifier}'")
          
#######################################################################################
#test case 90979
# Function    : mutiple_folder_creation
# Description : Creates multiple folders under "root_folder" depending on the count given.
#               Each folder is named using the provided base name followed by an underscore and a sequence number.
# Parameter   : param (str) - A string containing the base folder name and the number of folders to create,
#                             separated by '$$'. Example: "Folder$$5"
# Returns     : list - A list containing the names of the folders created.
##########################################################################################
def mutiple_folder_creation(param):
    root_folder, base_name, count = param.split('$$')
    count = int(count)  # Ensure count is an integer
    
    actual_folders = [f"{base_name}_{i}" for i in range(1, count + 1)]
    created_folders = []

    # Create folders
    for folder_name in actual_folders:
        right_click_application_browser_folder_AE(root_folder)
        Engineeringclientutility.select_ContextMenu_Items_EC("Create Folder")
        Sys.Keys(folder_name)
        Sys.Keys("[Enter]")

    # Fetch created folders from UI
    instanceBrowser = aet_obj.applicationbrowsertextbox.object
    instances = instanceBrowser.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if instances:
        for item in instances:
            if item.Panel_ZIndex != 0 and hasattr(item.DataContext, 'Identifier'):
                created_folders.append(item.DataContext.Identifier.OleValue)

    # Compare
    if actual_folders == created_folders:
        Log.Checkpoint(f"[PASS] Folders created successfully: {created_folders}")
    else:
        Log.Error(f"[FAIL] Folder mismatch.\nExpected: {actual_folders}\nFound: {created_folders}")

    return actual_folders, created_folders

#######################################################################################
# Function    : add_instance_under_folders
# Description : Fetches all created folders from the Application Browser, sorts them in ascending order,
#               and adds instances (templates) under each folder.
#               The template names and versions are taken from the predefined 'lt' list.
#               For each folder, the corresponding template is searched, dragged, and verified.
# Parameters  : template_list_str (str) - Comma-separated template name-version pairs
# Returns     : None
#######################################################################################   
def drag_composite_template_drop_app_browser_AE(param):
    # Split template, version, and optional drop target
    parts = param.split('$$')
    template = parts[0]
    version = parts[1]
    drop_target = parts[2] if len(parts) > 2 and parts[2].strip() else "System"

    Applicationutility.wait_in_seconds(2500, 'wait')

    # Find the template to drag
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren(
        'ClrClassName', 'TreeListViewRow', 1000
    )
    if template_list:
        for template_item in template_list:
            if (template_item.Visible 
                and str(template) in str(template_item.Item.Identifier.OleValue) 
                and str(version) == str(template_item.Item.ViewModel.Version.OleValue)):
                fromx = template_item.ScreenLeft
                fromy = template_item.ScreenTop
                Log.Message(f"The object selected to drag is: {template_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Error(f"Template '{template}' with version '{version}' not found in template browser.")
            return
    else:
        Log.Error("No templates found in the template browser.")
        return

    # Find the drop target in application browser
    app_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren(
        'ClrClassName', 'TreeListViewRow', 1000
    )
    if app_list:
        for app_item in app_list:
            if app_item.Visible and drop_target in str(app_item.Item.Identifier.OleValue):
                tox = app_item.ScreenLeft
                toy = app_item.ScreenTop
                Log.Message(f"The object selected to drop to is: {app_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Error(f"No '{drop_target}' found in application browser.")
            return
    else:
        Log.Error("No items found in the application browser.")
        return

    # Perform the drag and drop
    main_screen = eng_obj.mainscreenbutton
    main_screen.drag((fromx + 100), (fromy + 15), (fromx + tox + 115), -(fromy - toy))
    Applicationutility.wait_in_seconds(1000, 'wait')
    
def add_instance_under_each_folders(template_list_str):
    try:        
        # Convert comma-separated string to list
        lt = [t.strip() for t in template_list_str.split(",")]
        Log.Checkpoint(f"Parsed template list: {lt}")
        
        instanceBrowser = aet_obj.applicationbrowsertextbox.object
        instances = instanceBrowser.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
        
        if not instances:
            Log.Error("No instances found in the Application Browser.")
            return
        
        Log.Checkpoint(f"Found {len(instances)} instances in Application Browser.")
        
        created_folders = []
        for item in instances:
            if item.Panel_ZIndex != 0 and hasattr(item.DataContext, 'Identifier'):
                created_folders.append(item.DataContext.Identifier.OleValue)
        
        if not created_folders:
            Log.Error("No valid folders found to add instances.")
            return
        
        created_folders = sorted(created_folders)
        Log.Checkpoint(f"Created folders list: {created_folders}")
        
        # Validate list lengths
        if len(created_folders) < len(lt):
            Log.Error(f"Mismatch: Templates count ({len(lt)}) is greater than folders count ({len(created_folders)}).")
            return
        
        for i, item in enumerate(created_folders):
            try:
                template_name = lt[i].split('$$')[0]  # Take value before $$
                Log.Checkpoint(f"Processing template '{template_name}' for folder '{item}'.")
                
                search_template_browser_AE(template_name)
                Log.Checkpoint(f"Searched template '{template_name}'.")
                
                drag_composite_template_drop_app_browser_AE(f"{lt[i]}$${item}")
                Log.Checkpoint(f"Dragged and dropped template '{template_name}' under folder '{item}'.")
                
                verify_instance_application_browser(template_name)
                Log.Checkpoint(f"Verified instance for template '{template_name}'.")
            
            except Exception as e:
                Log.Error(f"Error while processing template '{lt[i]}' for folder '{item}': {str(e)}")
    
    except Exception as main_e:
        Log.Error(f"Unexpected error in add_instance_under_each_folders: {str(main_e)}")

#######################################################################################
# Function    : verify_contextMenu_MultipleSelection
# Description : Performs multiple selection of items in the Application Browser based 
#               on the given parameter and verifies the displayed context menu options.
#     param (str) - Selection type. 
#######################################################################################
def verify_contextMenu_MultipleSelection(param):
    instanceBrowser = aet_obj.applicationbrowsertextbox.object
    instances = instanceBrowser.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)

    created_folders = []
    if instances:
        for item in instances:
            if hasattr(item.DataContext, 'Identifier'):
                created_folders.append(item.DataContext.Identifier.OleValue)
                if 'System' in str(item.DataContext.Identifier.OleValue):
                    item.click()
        created_folders = sorted(created_folders)

    Log.Message("Created folders: " + str(created_folders))

    # Select multiple items
    for item in created_folders:
        if param == 'Folder' and 'Folder' in item:
            multiclick_application_browser_template_AE(item)
        elif 'Folder' not in item and param == 'ValveGP':
            multiclick_application_browser_template_AE(item)

    # Right-click on the specified param item
    right_click_application_browser_folder_AE(param)

    # Get actual context menu values
    actual_context_value = Engineeringclientutility.Verify_ContextMenu_Items()
    Log.Message("Actual context menu: " + str(actual_context_value))

    # Expected values based on param type
    if param == 'Folder':
        expected_context_value = ['Clean Up', 'Delete', 'Export', 'Paste', 'Replace Template', 'Update Template']
    else:
        expected_context_value = ['Delete', 'Export', 'Replace Template', 'Update Template']

    # Compare
    if actual_context_value == expected_context_value:
        Log.Checkpoint("Context menu items match expected.")
    else:
        Log.Error("Mismatch in context menu items.\nExpected: {}\nActual: {}".format(
            expected_context_value, actual_context_value
        ))

###############################################################################
# Function : verify_asterik_visibility
# Description: Verifies the * symbol is present when any modification is done to a instance
# Parameter : param (str) - to verify the * symbol for the selected param                        
##############################################################################      
      
def verify_asterik_visibility(param):
    identifier,state,inst_value,save_value=param.split('$$')
    template_checkbox(identifier + '$$' + state)
    instance_value = verify_application_explorer_instance_editor_tab(inst_value)    
    if '*' in instance_value:
        Log.Checkpoint("The instance value contains '*': " + instance_value)
    else:
        Log.Error("The instance value does NOT contain '*'. Actual value: " + instance_value)
    if save_value=='save':
      save_instance(inst_value)
    
def save_instance(inst_value):
  save_obj=aet_obj.instanceeditorsavebutton.click()
  instance_value = verify_application_explorer_instance_editor_tab(inst_value)
  if '*' not in instance_value:
        Log.Checkpoint("The instance value does NOT contains '*': " + instance_value)
  else:
        Log.Error("The instance value does contain '*'. Actual value: " + instance_value)
		
###############################################################################
# Function : instance_column_names
# Description: Verifies column names 
# Parameter : None
##############################################################################
def instance_column_names(values):
  expected_col_names= values.split('$$')
  actual_col_names=[]
  instance_header_list = aet_obj.instanceeditorchecklisttextbox.object.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 1000)
  instance_template_list= aet_obj.instanceeditorchecklisttextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  
  for item in instance_template_list:
    if item.Visible:
      item.click()
      break  
      
  if instance_header_list:    
    for _ in range(len(expected_col_names)):
      Sys.Keys("[Tab]")         
      Applicationutility.wait_in_seconds(5000,'wait')
      for values in instance_header_list:        
        if values.Visible:
          if values.WPFControlText not in actual_col_names:        
            actual_col_names.append(values.WPFControlText)
          Applicationutility.wait_in_seconds(5000,'wait')       
      
  if sorted(actual_col_names) == sorted(expected_col_names):
    Log.Checkpoint("Column names match: " + str(actual_col_names))
  else:
    Log.Error("Column names do not match.\nExpected: " + str(expected_col_names) + "\nActual: " + str(actual_col_names)) 
	
	
###############################################################################
# Function : verify_mutiple_instance_window
# Description: Verifies the mutiple windows can be opened for selected instances
# Parameter : identifier (str) - to verify the selected instance window is opened
##############################################################################
def locked_instance_count():
  instance_value=[]
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible:
        if 'System' not in (str(template_list[i].DataContext.Identifier.OleValue)):          
          if template_list[i].DataContext.IsProgressStateVisible:
            tooltip = template_list[i].DataContext.ProgressStateToolTip.OleValue
            if tooltip=='The instance is being updated':
              instance_value.append(str(template_list[i].DataContext.Identifier.OleValue))

  return instance_value
  
def open_tab_instance(identifier):
  identifier_value=locked_instance_count()
  template = eng_obj.mainscreenbutton.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    for j in range(len(identifier_value)):
      if template_list[i].Visible: 
        if identifier_value[j] in str(template_list[i].Header.OleValue):
          Log.Checkpoint("Tab values are matching with the isntances locked")         
      else:
        Log.Warning("Tab Item mentioned is not Valid")
          
def verify_mutiple_instance_window():
     identifier_value=locked_instance_count()
     open_tab_instance(identifier_value)
     
     
######################################################################################### 
# Function   : modify_csv_asset_workspace  
# Description: Reads a CSV file representing asset workspace data, searches for 
#              rows within specified template or interface sections matching a 
#              given instance name, and removes those rows from the file. The CSV 
#              is assumed to be comma-separated.  
# Parameter  :  
#   file_details - String with format "VariableName$$.csv" indicating the file to process  
#   modification - String with format "TemplateName$$InstanceName" specifying which 
#                  template section and instance to target for deletion  
# Example    :  
#   modify_csv_asset_workspace("AssetRootNode$$.csv", "AnalogInputGP$$AnalogInputGP_1")  
#########################################################################################

def modify_csv_asset_workspace(file_details, modification):

    # Parse file details
    file_name, file_format = file_details.split('$$')
    Template, Instance = modification.split('$$')
    exported_csv = Project.Variables.VariableByName[file_name] + file_format

    Applicationutility.wait_in_seconds(5, 'Waiting for file to be ready')

    # Build file path
    folder_name = "Test_Import_Files"
    d_path = os.path.abspath(os.path.join(os.getcwd(), folder_name, exported_csv))

    if not os.path.exists(d_path):
        Log.Error(f"File not found: {d_path}")
        return

    Log.Message(f"Processing file: {exported_csv}")

    # Read file
    with open(d_path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    output_lines = []
    inside_instance = False
    inside_interfacelinks = False
    headers = []
    col_indices = {}

    for line in lines:
        stripped_line = line.strip()

        # Section markers
        if stripped_line.startswith(':TemplateIdentifier='):
            inside_instance = Template in stripped_line
            inside_interfacelinks = False
            headers = []
            col_indices = {}
            output_lines.append(line)
            continue

        elif stripped_line.startswith(':InterfaceLinks'):
            inside_instance = False
            inside_interfacelinks = True
            headers = []
            col_indices = {}
            output_lines.append(line)
            continue

        # Capture headers
        if stripped_line.startswith(':$Action') or stripped_line.startswith('$Action'):
            headers = [h.strip().replace('\u200b', '') for h in line.split(',')]
            col_indices = {name: idx for idx, name in enumerate(headers)}
            output_lines.append(line)
            continue

        # Process Create rows
        if stripped_line.startswith('Create'):
            parts = [p.strip() for p in line.split(',')]

            if len(parts) < len(headers):
                output_lines.append(line)
                continue

            if inside_instance:
                idx = col_indices.get('$InstanceName')
                if idx is not None and parts[idx] == Instance:
                    continue 

            elif inside_interfacelinks:
                idx = col_indices.get('$SourceInstanceName')
                if idx is not None and parts[idx] == Instance:
                    continue 

            output_lines.append(','.join(parts))
        else:
            output_lines.append(line)

    # Write updated file
    with open(d_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')

    Log.Message("File modified successfully.")
    
    
###############################################################################
# Function   : click_on_status_filter_arrow_in_application_browser
# Description: Finds and clicks on the "Arrow" control in the Application 
#              Browser filter section, which is used to expand or collapse 
#              the status filter options.
# Parameter  : None
# Example    : click_on_status_filter_arrow_in_application_browser()
###############################################################################

def click_on_status_filter_arrow_in_application_browser():
    template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'Path', 1000)
    for i in template_list:
            if i.WPFControlName == "Arrow":
                i.click()
                Log.Checkpoint("Status filter arrow is clicked")
                break
    else:
      Log.Error("Status filter arrow not found")
      
      
      
###############################################################################
# Function   : verify_the_checkboxes_in_status_filter_AE
# Description: Checks and logs all checkboxes under the status filter section 
#              in the Application Explorer (AE). If checkboxes are found, their 
#              names are logged. If none are found, an error is logged.
# Parameter  : None
# Example    : verify_the_checkboxes_in_status_filter_AE()
###############################################################################
     
def verify_the_checkboxes_in_status_filter_AE():
  app_browser = aet_obj.applicationbrowsertextbox.object
  statusfilter = app_browser.FindAllChildren("ClrClassName", "CheckBox", 100)
  if statusfilter:
      for item in statusfilter:
        Log.Message(f"{item.WPFControlText} checkbox is displayed")
  else:
        Log.Error("Checkboxes not found")
  
      

###############################################################################
# Function   : select_application_browser_status_filter_checkboxes
# Description: Selects or deselects specific checkboxes in the Application 
#              Browser filter panel based on the provided input string.
#              For example: "Needs Attention$$1" / "Needs Attention$$0"
#                           "Data Invalid$$1" / "Data Invalid$$0" 
#                           "Link Invalid$$1" / "Link Invalid$$0"
#                           "Progress$$1" / "Progress$$0"
# Parameter  : checkboxes (str) - A comma-separated string of checkbox label and 
#              state pairs, where state is `1` (checked) or `0` (unchecked).
# Example    : select_application_browser_status_filter_checkboxes("Link Invalid$$1")
###############################################################################


def select_application_browser_status_filter_checkboxes(checkboxes):
  param = checkboxes.split(',')
  for checkbox in param:
    text, val = checkbox.split('$$') 
    val = int(val)
    app_browser = aet_obj.applicationbrowsertextbox.object
    statusfilter = app_browser.FindAllChildren("ClrClassName", "CheckBox", 50)
    if statusfilter:
      for item in statusfilter:
        if item.WPFControlText == text:
          item.wState = val
          if item.wState == val:
            Applicationutility.wait_in_seconds(5000, 'wait')
            Log.Checkpoint(f'the checkbox :{item.WPFControlText} is set to {item.wState}')
            break
          else:
            Log.Error(f'the checkbox :{item.WPFControlText} is not set to {item.wState}')
    else:
      Log.Error("checkbox not found")  
      
def hdy():
  select_application_browser_status_filter_checkboxes("Link Invalid$$1")

  
  
###############################################################################
# Function   : verify_instances_in_application_browser
# Description: Verifies and logs the presence of unique application instances 
#              in the Application Browser. It filters out any instances whose 
#              identifiers start with the word "System" and ensures duplicates 
#              are not logged. Adds a short wait between logs for visibility.
# Parameter  : None
# Example    : verify_instances_in_application_browser()
###############################################################################
              
def verify_instances_in_application_browser():
    App_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    found = False
    skip = "System"
    seen = set()

    if not App_list:
        Log.Error("No instance found in application browser.")
        return

    for i in App_list:
        if i.Visible:
            try:
                identifier = i.Item.Identifier.OleValue
                if identifier.startswith(skip):
                    continue
                if identifier not in seen:
                    Log.Checkpoint(f"{identifier} is displayed")
                    Applicationutility.wait_in_seconds(2000, 'wait')
                    found = True
                    seen.add(identifier)
            except AttributeError:
                Log.Message("No more instance found in application browser.")
                break
    
      
##############################################################################################
# Function   : click_on_grid_view_icon_in_application_browser
# Description: Finds and clicks on the Grid/Tree view toggle icon in the Application Browser. 
#              This icon is used to switch between different views of the application 
#              instances (e.g., grid view or tree view).
# Parameter  : None
# Example    : click_on_grid_view_icon_in_application_browser()
##############################################################################################

def click_on_grid_view_icon_in_application_browser():
   list1 = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'Path', 1000)
   for i in list1:
        if i.WPFControlName == "PathIcon":
          i.click()
          Log.Checkpoint("Grid/Tree view icon is clicked")
          break
   else:
      Log.Error("Grid/Tree view icon not found")
            
   
###########################################################################################
# Function: verify_values_instance_win_AE
# Description: Verifies whether the specified value exists among the text blocks 
#              in the Instance Window of the Application Explorer. Logs a 
#              checkpoint if a match is found.
# Parameters: value (str) – The text value to verify in the Instance Window.
###############################################################################
def verify_values_instance_win_AE(value):
    try:
        value_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'TextBlock', 1000)
        
        if value_lst:
            found = False
            for item in value_lst:
                if value == str(item.WPFControlText):
                    Log.Checkpoint(f"Value '{value}' found in Instance Window.")
                    found = True
                    break
            if not found:
                Log.Error(f"Value '{value}' not found in Instance Window.")
        else:
            Log.Error("No TextBlocks found in Instance Window.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while verifying value '{value}': {str(e)}")

###########################################################################################
# Function: enter_alias_name
# Description: Finds the property field in the Instance Window of the Application Explorer
#              that matches the specified value, enters the provided alias into its
#              associated text box, and verifies that the entry was successful by logging
#              a checkpoint. Reports errors if the field or text box is not found, or if
#              the entered value does not match the expected alias.
# Parameters: param (str) – A string in the format "value$$alias_value", where 'value' is
#                         the name of the property field to search for, and 'alias_value'
#                         is the value to enter into the corresponding text box.
###########################################################################################
        
def enter_alias_name(param):
  value,alias_value=param.split('$$')
  property_lst=aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'PropertyGridField', 1000)
  if not property_lst:
        Log.Error("No PropertyGridField elements found.")
        return
  for item in property_lst:
        field_value = getattr(item.DataContext.DisplayName, 'OleValue', '')
        
        if value in str(field_value):
            field_lst = item.FindAllChildren('ClrClassName', 'TextBox', 1000)
            
            if not field_lst:
                Log.Error(f"No TextBox found for field '{value}'")
                return
            
            field_lst[0].Click()
            Sys.Keys(alias_value)
            
            # Checkpoint to verify the alias value is entered
            entered_value = field_lst[0].wText
            if alias_value == entered_value:
                Log.Checkpoint(f"Alias '{alias_value}' successfully entered for field '{value}'.")
            else:
                Log.error(f"Alias entry mismatch: expected '{alias_value}', but found '{entered_value}'.")

            return alias_value
    
  Log.Error(f"Field with name containing '{value}' not found.")

###########################################################################################
# Function: uncheck_instance_editor_values
# Description: Searches for a checkbox in the Instance Editor of the Application Explorer
#              whose label matches the specified value, and clicks it to uncheck it.
#              Logs a checkpoint if the checkbox is successfully found and unchecked,
#              or logs an error if the checkbox is not found.
# Parameters: value (str) – The text value of the checkbox to be unchecked.
###########################################################################################
       
def uncheck_instance_editor_values(value):
    value_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'CheckBox', 1000)
    
    if not value_lst:
        Log.Error("No checkboxes found in the instance editor.")
        return
    
    found = False

    for item in value_lst:
        if value in str(item.WPFControlText):
            item.Click()
            Log.Checkpoint(f"Checkbox with value '{value}' was successfully checked.")
            found = True
        break
    
    if not found:
        Log.Error(f"Checkbox with value '{value}' not found.")

###########################################################################################
# Function: verify_folder_alias_value
# Description: Checks whether a specified alias value is present among the items in the
#              Instance Browser of the Application Explorer. It searches through all
#              available entries for an alias identifier that contains the given value,
#              and logs a checkpoint if found or an error if not found.
# Parameters: value (str) – The alias name or substring to search for in the instance browser.
###########################################################################################
def verify_folder_alias_value(value):          
    instanceBrowser = aet_obj.applicationbrowsertextbox.object
    instances = instanceBrowser.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)

    if not instances:
        Log.Error("No items found in the instance browser.")
        return    

    found = False

    for item in instances:
        if hasattr(item.DataContext, 'AliasIdentifier'):
            alias_name = str(item.DataContext.AliasIdentifier.OleValue)
            if value in alias_name:
                found = True
                break

    if found:
        Log.Checkpoint(f"Alias '{value}' is present in the instance browser.")
    else:
        Log.Error(f"Alias '{value}' was not found in the instance browser.")

###########################################################################################
# Function: drag_instance_folder_folder
# Description: Drags an instance folder from a source location to a target folder within
#              the Instance Browser of the Application Explorer.
#              encountered during the process.
# Parameters: param (str) – A string in the format "template$$folder_name$$move", where:
#                         template (str) – The identifier substring of the source instance.
#                         folder_name (str) – The name of the target folder to drop into.
#                         move (str) – Direction of the move: "UP" to drop above, or any other
#                                      value to drop below the target folder.
###########################################################################################
        
def drag_instance_folder_folder(param):
    template, folder_name, move  = param.split('$$')
    # Find all instance items in the application browser
    instance_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    
    if not instance_list:
        Log.Error("No items found in the instance browser.")
        return
    
    fromx = fromy = tox = toy = None

    # Find the instance to drag from
    for item in instance_list:
        if item.Panel_ZIndex != 0 and hasattr(item.Item, 'Identifier'):
          identifier = str(item.Item.Identifier.OleValue)
          if template in identifier:
              fromx = item.ScreenLeft
              fromy = item.ScreenTop
              Log.Message(f"Found source object: {identifier}")
              break
    
    if fromx is None or fromy is None:
        Log.Error("Source object '{template}' not found.")
        return

    # Find the target folder to drop into
    for app_item in instance_list:
      if app_item.Panel_ZIndex != 0 and hasattr(app_item.Item, 'Identifier'):
        identifier = str(app_item.Item.Identifier.OleValue)
        if app_item.Visible and folder_name in identifier:
 
            tox = app_item.ScreenLeft
            toy = app_item.ScreenTop
            Log.Message(f"Target object found: {identifier}")
            break

    if tox is None or toy is None:
        Log.Error(f"Target folder '{folder_name}' not found.")
        return

    # Perform drag and drop action
    main_screen = eng_obj.mainscreenbutton
    delta_x = tox - fromx
    delta_y = toy - fromy
    
    if move =='Up':
      main_screen.drag(fromx+10, fromy+10, 0, delta_y-10)
    else:
      main_screen.drag(fromx+10, fromy+10, 0, delta_y+10)

    Applicationutility.wait_in_seconds(1000, 'Waiting after drag')  # Changed to 1 second for practical usage
    Log.Checkpoint(f"Drag-and-drop operation from '{template}' to '{folder_name}' completed successfully.")

###########################################################################################
# Function: check_instance_description_and_add_Value_AE_instance_editor
# Description: Searches for a specified description within the Instance Editor of the
#              Application Explorer and sets its value based on the parameter type.
#              The function supports different parameter types including String, Short,
#              Duration, Integer, and Boolean, and applies the given value accordingly.#              
# Parameters: param (str) – A string in the format "Description$$Value_to_be_passed", where:
#                         Description (str) – The description text to search for.
#                         Value_to_be_passed (str) – The value to set for the matching description.
###########################################################################################
    
def check_instance_description_and_add_Value_AE_instance_editor(param):
    parameter_value, Description, Value_to_be_passed = param.split('$$')
    parameter_expand_instance_Editor(parameter_value)
    des = aet_obj.instancedescriptionbutton.object
    des_list = des.FindAllChildren('ClrClassName', 'GridViewRow', 1000)

    if not des_list:
        Log.Warning("No descriptions found in the instance editor.")
        return

    found = False

    for item in des_list:
        cells = item.FindAllChildren('ClrClassName', 'GridViewCell', 1000)

        for cell in cells:
            if Description in str(cell.WPFControlText):
                found = True
                Log.Message(f"Found description: '{Description}'")
                cell.Click()
                Sys.Keys('[Tab]')
                Sys.Keys('[Tab]')
                item.Click((item.Width - 25), (item.Height / 2))

                param_type = item.DataContext.ParameterType
                try:
                    if param_type == 'String' or param_type == 'Short':
                        Sys.Keys(Value_to_be_passed)
                        Sys.Keys('[Enter]')
                        Applicationutility.wait_in_seconds(2, 'Wait')
                        Log.Checkpoint(f"The {param_type} value is set to {item.DataContext.Expression.OleValue}")
                    
                    elif param_type == 'Duration' or param_type == 'Integer':
                        Sys.Keys(int(Value_to_be_passed))
                        Sys.Keys('[Enter]')
                        Applicationutility.wait_in_seconds(2, 'Wait')
                        Log.Checkpoint(f"The {param_type} value is set to {item.DataContext.Expression.OleValue}")

                    elif param_type == 'Boolean':
                        checkbox = item.FindAllChildren('ClrClassName', 'CheckBox', 1000)
                        if not checkbox:
                            Log.Error("Checkbox not found for Boolean parameter.")
                            return
                        if checkbox[0].wState != int(Value_to_be_passed):
                            checkbox[0].ClickButton(int(Value_to_be_passed))
                            Applicationutility.wait_in_seconds(2, 'Wait')
                        Log.Checkpoint(f"The checkbox value is set to {checkbox[0].wState}")

                    else:
                        Log.Error(f"Unsupported parameter type: {param_type}")
                
                except Exception as e:
                    Log.Error(f"Error while setting value: {str(e)}")

                return  # Exit after processing the first matching description
    if not found:
        Log.Error(f"Description '{Description}' not found in the instance editor.")

###############################################################################
# Function: parameter_expand_instance_Editor
# Description: Searches for a description in the instance editor by matching the 
#              provided value with the names of description headers. If the header 
#              is found and is not already expanded, it clicks to expand it.
# Parameters:
#   value (str) - The name or part of the name of the description header to search for.
###############################################################################
def parameter_expand_instance_Editor(value):    
    des = aet_obj.instancedescriptionbutton.object
    des_list = des.FindAllChildren('ClrClassName', 'GroupHeaderRow', 1000)

    if not des_list:
        Log.Error("No descriptions found in the instance editor.")
        return
    
    found = False
    for item in des_list:
        if value in str(item.DataContext.Name.OleValue):
            found = True
            if str(item.IsExpanded) == 'False':
                item.Click()
                Log.Checkpoint(f"Expanded the description '{value}'.")
            else:
                Log.Checkpoint(f"The description '{value}' is already expanded.")
            break
    
    if not found:
        Log.Error(f"Description with value '{value}' not found in the instance editor.")

###########################################################################################
# Function: select_template_instance_ediotr
# Description: Searches for a specific template in the Instance Editor's checklist and
#              selects it by clicking the corresponding item. The function looks for
#              items whose element path contains both provided identifiers.
# Parameters: param (str) – A string in the format "identifier$$identifier1", where:
#                         identifier (str) – A substring to match within the element path.
#                         identifier1 (str) – Another substring to match within the element path.
###########################################################################################       
def select_template_instance_ediotr(param):
    identifier, identifier1 = param.split('$$')
    obj = aet_obj.instanceeditorchecklisttextbox.object
    obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if not obj_list:
        Log.Error("No items found in the instance editor checklist.")
        return

    found = False

    for item in obj_list:
        checkbox_name = item.DataContext.ElementFullPath.OleValue
        checkbox_ele = checkbox_name.split('|')

        if str(identifier) in str(checkbox_ele) and str(identifier1) in str(checkbox_ele):
            item.Click()
            Log.Checkpoint(f"Template with identifiers '{identifier}' and '{identifier1}' selected.")
            found = True
            break

    if not found:
        Log.Error(f"Template with identifiers '{identifier}' and '{identifier1}' not found in the checklist.")

# Function   : verify_validity_indicator_status_of_instances_in_AE
# Description: Iterates through all visible application instances in the 
#              Application Browser (AE) based on their hierarchy level and 
#              verifies their validity status.
# Parameter  : None
# Example    : verify_validity_indicator_status_of_instances_in_AE()
#########################################################################################
    
def verify_validity_indicator_status_of_instances_in_AE():
    level = 1
    App_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 1000)
    if not App_list:
        Log.Error("No items found in the application browser.")
        return
    while True:
        found = False
        for item in App_list:
            if item.Visible and item.Level == level:
                found = True
                identifier = str(item.Item.Identifier.OleValue)
                if item.DataContext.HasValidationError == False:
                    Log.Checkpoint(f"Status of {identifier} at level {item.Level} is Valid")
                elif item.DataContext.HasValidationError == True:
                    Log.Checkpoint(f"Status of {identifier} at level {item.Level} is Invalid")
                else:
                    Log.Error(f"Unknown validation state for {identifier}")
        if not found:
            break
        level += 1
        Applicationutility.wait_in_seconds(1000, "wait") 

###############################################################################################
# Function   : drag_instance_from_folder_to_folder_in_AE
# Description: Drags an instance (like a folder or item) from one location to another 
#              within the Application Explorer. It finds both the source and target by name 
#              and performs the drag-and-drop action between them.
# Parameter  : param (str) - A string with the source and target names, separated by '$$'. 
# Format     : "SourceName$$TargetName"
# Example    : drag_instance_from_folder_to_folder_in_AE("MotorGP_1$$Folder_3")
# This will drag 'MotorGP_1' and drop it into 'Folder_3' in the Application Explorer.
###############################################################################################
def drag_instance_from_folder_to_folder_in_AE(param):
  source_name, target_name = param.split('$$')
  rows = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  source = next((r for r in rows if getattr(r.Item, "Identifier", None) and str(r.Item.Identifier.OleValue) == source_name), None)
  target = next((r for r in rows if getattr(r.Item, "Identifier", None) and str(r.Item.Identifier.OleValue) == target_name), None)
  if source is not None and target is not None:
    dx, dy = target.ScreenLeft - source.ScreenLeft, target.ScreenTop - source.ScreenTop
    source.Drag(-1, -1, dx, dy, 500)
    Log.Checkpoint(f"Successfully dragged '{source_name}' to '{target_name}'.")
  else:
    Log.Error(f"Source '{source_name}' or Target '{target_name}' not found in Application Browser.")

    
##########################################################################################  
# Function   : shuffle_instance_coulmn_headers
# Description: Drags and rearranges column headers in the Application Explorer. It finds 
#              the source and target headers by name and performs the drag-and-drop 
#              operation to reorder them.
# Parameter  : param (str) - A string with the source and target header names, separated by '$$'.  
# Format     : "SourceHeader$$TargetHeader"
# Example    : shuffle_instance_column_headers("Version$$Template")
# Headers    : Template, Version ,Data, Link, Assigned State, Description, Area, Path
# This will drag the 'Version' column header and drop it onto the 'Template' column header.
##########################################################################################    

def shuffle_instance_column_headers(param):
  source_name, target_name = param.split('$$')
  rows = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 1000)
  source = next((r for r in rows if getattr(r, "WPFControlText", None) and str(r.WPFControlText) == source_name), None)
  target = next((r for r in rows if getattr(r, "WPFControlText", None) and str(r.WPFControlText) == target_name), None)
  if source is not None and target is not None:
    dx, dy = target.ScreenLeft - source.ScreenLeft, target.ScreenTop - source.ScreenTop
    source.Drag(-1, -1, dx, dy, 500)
    Log.Checkpoint(f"Successfully dragged '{source_name}' to '{target_name}'.")
  else:
    Log.Error(f"Source '{source_name}' or Target '{target_name}' not found in Application Browser.")
    
    
    
############################################################################################### 
# Function   : Drag_and_expand_application_browser
# Description: Drags the right edge of the Application Browser window to expand it horizontally.
# Parameter  : None
# Example    : Drag_and_expand_application_browser()
################################################################################################   
  
def Drag_and_expand_application_browser():
    appbrowserwindow = aet_obj.AppBrowserWindowExpand.object
    width = appbrowserwindow.Width
    height = appbrowserwindow.Height
    dx = width - 1 
    dy = height // 2
#    appbrowserwindow.HoverMouse(dx, dy)
#    Applicationutility.wait_in_seconds(500, 'wait')
    appbrowserwindow.Drag(dx, dy, 400, 0, 500)
    Log.Checkpoint(f"Application Browser is expanded")



##############################################################################################
# Function   : enter_field_name_in_AE
# Description: Enters a specified value into a designated text field within 
#              the Folder Properties section of the AE interface.
# Parameter  : param (str) - A string in the format "AutomationID$$Value", 
#              where:
#              - AutomationID: WPF Automation ID of the target text field
#              - Value       : The text to be entered into the field
# Example    : enter_field_name_in_AE("Field_Name$$MyValue")
#              "Alias_FieldEditor$$textinput"
#              "Description_FieldEditor$$textinput"
#              "Area_FieldEditor$$textinput"
##############################################################################################

def enter_field_name_in_AE(param):
  field, name = param.split('$$')
  properties = aet_obj.FolderProperties.object.FindAllChildren("ClrClassName", "TextBox", 1000) 
  for i in properties:
    if i.WPFControlAutomationId == field:
      i.Keys(name)
      Log.Checkpoint(f"{i.WPFControlAutomationId} entered as {name}")
      break
  else:
    Log.Error("Field Editor not found")
    
def shg():
  enter_alias_name_in_AE("Alias_FieldEditor$$Test")

 
############################################################################################### 
# Function   : verify_zoom_buttons
# Description: Verifies if a zoom button with the specified tooltip text is present within the
#              workspace toolbar of the application under test.
# Parameter  : param (str) - The tooltip text of the zoom button to verify.
# Example    : verify_zoom_buttons("Zoom In (+)")
###############################################################################################

def verify_zoom_buttons(param):
    zoom_values = []
    
    obj_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'ToolBar', 1000)
    if obj_lst:
        for item in obj_lst:
            zoom_lst = item.FindAllChildren('ClrClassName', 'ContentPresenter', 1000)
            Log.Message(f"Found {len(zoom_lst)} zoom elements.")
            
            if zoom_lst:
                for zoom in zoom_lst:
                    if hasattr(zoom, 'ToolTip') and zoom.ToolTip is not None:
                        tooltip = str(zoom.ToolTip.OleValue).strip()  # Remove extra spaces
                        zoom_values.append(tooltip)
                    else:
                        Log.Message("Zoom element missing ToolTip.")
    
    Log.Message(f"Collected zoom tooltips: {zoom_values}")
    
    if param in zoom_values:
        Log.Checkpoint(f"Zoom button '{param}' is present.")
    else:
        Log.Error(f"Zoom button '{param}' not found.")


    
############################################################################################### 
# Function   : verify_link_instance_options
# Description: Finds a specific link node instance by name, right-clicks on it to open the context
#              menu, verifies the menu items, and checks if the expected list matches the actual list.
# Parameter  : param (str) - A string containing the expected list and the instance name separated
#                           by '$$', e.g. "Option1,Option2$$AnalogOutputGP_1".
# Example    : verify_link_instance_options("Option1,Option2$$AnalogOutputGP_1")
###############################################################################################
def verify_link_instance_options(param):
    expected_list_str, instance_value = param.split('$$')
    expected_list = [item.strip() for item in expected_list_str.split(',')]
    
    # Perform right-click on the instance
    if not right_click_instance_link(instance_value):
        Log.Error(f"Could not right-click on instance '{instance_value}'")
        return
    
    # Verify context menu items
    actual_context_value = Engineeringclientutility.Verify_ContextMenu_Items()
    Log.Message(f"Actual context menu items: {actual_context_value}")

    # Compare expected and actual lists
    if set(expected_list) == set(actual_context_value):
        Log.Checkpoint("Expected context menu items match the actual items.")
    else:
        Log.Error(f"Expected items {expected_list} do not match actual items {actual_context_value}")

        
def ttt():
  verify_link_instance_options("Properties, View Assignments,Hide Unbound,Hide Disabled$$AnalogOutputGP_1")
  
  
############################################################################################### 
# Function   : right_click_instance_link
# Description: Finds a link node instance by its name and performs a right-click on it.
# Parameter  : instance_value (str) - The name of the link node instance to right-click.
# Example    : right_click_instance_link("AnalogOutputGP_1")
###############################################################################################

def right_click_instance_link(instance_value):
    obj_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
    
    if not obj_lst:
        Log.Error("No LinkNodeControl items found")
        return False
    
    for item in obj_lst:
        value_lst = item.FindAllChildren('ClrClassName', 'TextBlock', 1000)
        
        if value_lst:
            for value in value_lst:
                text_value = str(value.Text.OleValue).strip()
                if text_value == instance_value:
                    value.ClickR()
                    Log.Message(f"Right-clicked on instance: {instance_value}")
                    return True
    
    Log.Error(f"Instance '{instance_value}' not found")
    return False

############################################################################################### 
# Function   : fetch_instance_sub_values
# Description: Retrieves all visible text values from 'TextBlock' elements within 'TreeView' controls
#              in the workspace. These represent the sub-values or details of an instance.
# Returns    : list - A list of strings containing the text of visible 'TextBlock' elements.
# Example    : values = fetch_instance_sub_values()
###############################################################################################
def fetch_instance_sub_values():
    sub_values = []
    obj_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'TreeView', 1000)
    
    if not obj_lst:
        Log.Warning("No TreeView controls found in the workspace.")
        return sub_values
    
    for item in obj_lst:
        value_lst = item.FindAllChildren('ClrClassName', 'TextBlock', 1000)
        Log.Message(f"Found {len(value_lst)} TextBlock items in a TreeView.")
        
        for text_block in value_lst:
            if text_block.IsVisible:
                sub_values.append(text_block.WPFControlText)
                Log.Message(f"Visible TextBlock added: '{text_block.WPFControlText}'")
    
    Log.Message(f"Total visible sub-values found: {len(sub_values)}")
    return sub_values

    
############################################################################################### 
# Function   : verify_filtered_symbol
# Description: Checks if the filtered symbol (with 'PartFiltered') is visible within the workspace.
#              It searches through all 'LinkNodeControl' items and verifies if the filtered part is active.
# Parameter  : value (str) - The name or description of the symbol being verified (used in log messages).
# Returns    : bool - True if the filter is visible at least once, False otherwise.
# Example    : verify_filtered_symbol("AnalogOutputGP_1")
###############################################################################################
def verify_filtered_symbol(value):
    obj_lst = aet_obj.workspacebutton.object.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
    
    if not obj_lst:
        Log.Error("No LinkNodeControl items found")
        return False
    
    found = False
    
    for item in obj_lst:
        value_lst = item.FindAllChildren('WPFControlName', 'PartFiltered', 1000)
        
        if value_lst:  # Ensure the list is not empty
            if value_lst[0].IsVisible:
                Log.Checkpoint(f"{value} is selected")
                found = True
            else:
                Log.Checkpoint("No filter is added")
    
    return found
############################################################################################### 
# Function   : click_instance_option_link
# Description: Finds an instance link by name, right-clicks it, selects an option from the context menu,
#              and verifies whether the instance values have changed (e.g., some items are hidden).
# Parameter  : param (str) - A string containing the instance name and dropdown option separated by '$$'.
#              Format: "instance_value$$drp_dwn_value"
# Example    : click_instance_option_link("AnalogOutputGP_1$$Hide Disabled")
###############################################################################################
def click_instance_option_link(param):
    instance_value, drp_dwn_value = param.split('$$')
    
    actual_values = fetch_instance_sub_values()
    right_click_instance_link(instance_value)
    Engineeringclientutility.select_ContextMenu_Items_EC(drp_dwn_value)
    expected_values = fetch_instance_sub_values()
    verify_filtered_symbol(drp_dwn_value)
    
    if len(actual_values) != len(expected_values):
        if drp_dwn_value == "Hide Disabled":
            Log.Checkpoint(f"Filter applied: '{drp_dwn_value}'. Some values are now hidden.")
        else:
            Log.Checkpoint(f"Option '{drp_dwn_value}' selected. Instance values have been updated.")
    else:
        Log.Checkpoint(f"Option '{drp_dwn_value}' selected, but no changes were detected in instance values.")
