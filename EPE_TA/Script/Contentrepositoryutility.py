import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from SystemExplorerScreen import SystemExplorerScreen
from ContentRepository import ContentRepository

eng_obj = EngineeringClient()
ses_obj = SystemExplorerScreen()
con_obj = ContentRepository()


###############################################################################################################################
# Function:expand_content_repository
# Description:Expand the Content Repository in System explorer. 
# Parameter:None
################################################################################################################################
def Expand_nodes_ContentRepository(identifier):
  node = ses_obj.systemexplorernodebutton.object
  nodes = node.FindAllChildren('ClrClassName', 'ExplorerNode', 1000)
  Log.Message(len(nodes))
  for item in nodes:
    if identifier in item.DataContext.Identifier.OleValue:
      item.IsExpanded = True
      Log.Message('Content Repository is Expanding')
  
###########################################################################################################
# Function:Create_multiple_folders
# Description:Create multiple folders under the User Content. 
# Parameter:The name of the folder under which the system is created.
############################################################################################################
def Select_multiple_folders_1(): # Redundant method ? fix method
  Select = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("Grid", "", 2).WPFObject("Grid", "", 1).WPFObject("WorkspaceControl").WPFObject("FrameHostContainer", "", 1).WPFObject("FrameHostControl", "", 1).WPFObject("Grid", "", 1).WPFObject("ContentPanel").WPFObject("PART_SelectedContentHost").WPFObject("UserControl", "", 1).WPFObject("ContentControl", "", 1).WPFObject("ContentPresenter", "", 1).WPFObject("WorkFrameControl", "", 1).WPFObject("Grid", "", 1).WPFObject("SystemsTree").WPFObject("CoreGraph", "", 1).WPFObject("ExplorerNode", "", 17).WPFObject("PART_PortContainer")
  nodes = Select.FindAllChildren('WPFControlName', 'PART_PortContainer')
  Log.Message(len(nodes))
  for item in nodes:
      if identifier in item.DataContext.Identifier.OleValue:
        item.IsSelect = True
        Log.Message('Folder is Selecting')
  Select.Click()
  Select.Sys.Keys("[Hold]^")
##########################################################################################################  
# Function:Select_multiple_folders
# Description:Select multiple folders under the User Content. 
# Parameter:The name of the folder under which the system is created
#########################################################################################################  
def Select_multiple_folders(param): # Redundant method ? fix method
#  param = 'Folder_1$$Folder_2$$Folder_3$$Folder_4$$Folder_5'
  lst = param.split('$$')
  node = ses_obj.systemexplorernodebutton.object
  nodes = node.FindAllChildren('ClrClassName', 'ExplorerNode', 1000)
  for folder in lst:
    for item in nodes:
      if folder in item.DataContext.Identifier.OleValue:
        item.Click(5,5,skCtrl)
        break
    else:
      Log.Error(f'Folders selected {item.DataContext.Identifier.OleValue}')
  
####################################################################
# Function:expand_content_repository
# Description:Expand the Content Repository in System explorer. 
# Parameter:None
#######################################################################
  node = ses_obj.systemexplorernodebutton.object
  nodes = node.FindAllChildren('ClrClassName', 'ExplorerNode', 1000)
  Log.Message(len(nodes))
  for item in nodes:
    if identifier in item.DataContext.Identifier.OleValue:
      item.IsExpanded = True
      Log.Message(f'{item.DataContext.Identifier.OleValue} is Expanding')
      break
  else:
      Log.Message(f'{identifier} Node is not Expanding')
      
#######################################################################################################     
# Function:Verify_multiple_folders
# Description:Verifying the multiple folders are selecting and unselecting under the User Content. 
# Parameter:None
#######################################################################################################
def verify_Select_multiple_folders_EC(Param):
  param = 'Folder_1$$Folder_2$$Folder_3$$Folder_4$$Folder_5'
  lst = param.split('$$')
  node = ses_obj.systemexplorernodebutton.object
  nodes = node.FindAllChildren('ClrClassName', 'ExplorerNode', 1000)
  for folder in lst:
    for item in nodes:
      if folder in item.DataContext.Identifier.OleValue:
        if item.DataContext.IsSelected:
          Log.Checkpoint(f'{item.DataContext.Identifier.OleValue} is Selected.')
          break
        elif not item.DataContext.IsSelected: 
          Log.Error(f'{item.DataContext.Identifier.OleValue} is Not Selected.')
          break
    else:
      Log.Error(f'Folders selected {item.DataContext.Identifier.OleValue}')
      
#########################################################################################      
# Function:Property_window
# Description:Enter the values inside textbox Property Window 
# Parameter:Values_ Pass the values under folders
#########################################################################################
def Property_Window(): 
  Applicationutility.wait_in_seconds(2000, 'Wait')
  topology_obj.backupdatadescriptiontextbox.enter_text("Content")

###############################################################################
# Function    : select_folder_in_content_repository
# Description : Selects a folder from the Content Repository in the workspace.
#               Searches through available folders and double-clicks the
#               matching one based on the provided folder name or identifier.
# Parameters  : folder_name (str) - The name or identifier of the folder to select.
###############################################################################           
def select_folder_in_content_repository(folder_name):
    try:
        obj = eng_obj.workspacetextbox.object
        obj_lst = obj.FindAllChildren("ClrClassName", "ExplorerNode", 1000)
        Log.Message(f"Total folders found: {len(obj_lst)}")

        if not obj_lst:
            Log.Error("No folders found in the Content Repository.")
            return

        for item in obj_lst:
            if folder_name == 'Systems':
                if folder_name in str(item.DataContext.Name.OleValue):
                    item.DblClick()
                    Log.Checkpoint(f"Successfully selected folder: {folder_name}")
                    return
            elif folder_name in str(item.DataContext.Identifier.OleValue):
                item.DblClick()
                Log.Checkpoint(f"Successfully selected folder: {folder_name}")
                return

        Log.Error(f"Folder '{folder_name}' not found in the Content Repository.")

    except Exception as e:
        Log.Error(f"Error while selecting folder '{folder_name}': {str(e)}")
            
###############################################################################
# Function    : right_click_folder_in_content_repository
# Description : Right-clicks a folder in the Content Repository based on the 
#               provided folder identifier. Validates visibility before clicking.
#               Logs success or error accordingly.
# Parameters  : folder_identifier (str) - Identifier of the folder to right-click.
###############################################################################
def right_click_folder_in_content_repository(folder_identifier):
    try:
        cr_folders = eng_obj.workspacetextbox.object
        cr_folders_lst = cr_folders.FindAllChildren("ClrClassName", "ExplorerNode", 1000)

        if not cr_folders_lst:
            Log.Error("No folders found in the Content Repository.")
            return

        for item in cr_folders_lst:
            if item.Visible and folder_identifier in str(item.DataContext.Identifier.OleValue):
                item.ClickR()
                Log.Checkpoint(f"Successfully right-clicked on folder: {item.DataContext.Identifier.OleValue}")
                Applicationutility.wait_in_seconds(1000, 'Wait after right-click')
                return

        Log.Error(f"Folder with identifier '{folder_identifier}' not found or not visible.")

    except Exception as e:
        Log.Error(f"Error while right-clicking folder '{folder_identifier}': {str(e)}")

###############################################################################
# Function    : right_click_identifier_in_content_repository
# Description : Right-clicks an item in the Content Repository grid based on the 
#               provided identifier. Validates visibility before clicking.
#               Logs success or error accordingly.
# Parameters  : identifier_value (str) - Identifier of the grid cell to right-click.
###############################################################################
def right_click_identifier_in_content_repository(identifier_value):
    try:
        cr_folders = eng_obj.workspacetextbox.object
        cr_folders_lst = cr_folders.FindAllChildren("ClrClassName", "GridViewCell", 1000)
        Log.Message(f"Total grid cells found: {len(cr_folders_lst)}")

        if not cr_folders_lst:
            Log.Error("No items found in the Content Repository grid.")
            return

        for item in cr_folders_lst:
            if item.Visible and identifier_value in str(item.DataContext.Identifier.OleValue):
                item.ClickR()
                Log.Checkpoint(f"Successfully right-clicked on item: {item.DataContext.Identifier.OleValue}")
                Applicationutility.wait_in_seconds(1000, 'Wait after right-click')
                return

        Log.Error(f"Identifier '{identifier_value}' not found or not visible in the grid.")

    except Exception as e:
        Log.Error(f"Error while right-clicking identifier '{identifier_value}': {str(e)}")        


def select_ContextMenu_Items_EC(menu_item):
  menu = eng_obj.rclickmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "*MenuItem", 50)
  for item in menu_items:
    if item.Visible and item.Enabled:
      if item.Header != None and str(item.Header.OleValue) == str(menu_item):
        item.Click()
        Log.Checkpoint('The Context Menu Item clicked is : ' + str(menu_item))
        #Sys.Keys('[Tab]')
        break
  else:
    Log.Warning(f'The Context menu item {menu_item} not found !')
  Applicationutility.wait_in_seconds(4000, 'wait')
  
  
###############################################################################
# Function    : enter_identifier_name_in_content_repository
# Description : Enters a new identifier name in the Content Repository grid 
#               and verifies if it is successfully updated.
# Parameters  : new_identifier (str) - The new identifier name to enter.
###############################################################################
def enter_identifier_name_in_content_repository(new_identifier):
    try:
        obj = eng_obj.workspacetextbox.object
        obj_lst = obj.FindAllChildren("ClrClassName", "GridViewCell", 1000)
        Log.Message(f"Total grid cells found: {len(obj_lst)}")

        if not obj_lst:
            Log.Error("No grid cells found in the Content Repository.")
            return

        Sys.Keys(new_identifier)
        Sys.Keys("[Enter]")
        Applicationutility.wait_in_seconds(2000,'wait')
        for i in range(len(obj_lst)):
          output = obj_lst[i].DataContext.Identifier.OleValue
          if str(output) == str(new_identifier):
              Log.Checkpoint(f"Identifier name successfully updated to: {new_identifier}")
              break
        else:
            Log.Error(f"Failed to update identifier. Expected: '{new_identifier}', Found: '{output}'")

    except Exception as e:
        Log.Error(f"Error while entering identifier name '{new_identifier}': {str(e)}")
        
###############################################################################
# Function    : select_identifier_in_content_repository
# Description : Selects an item in the Content Repository grid based on the 
#               provided identifier. Clicks or double-clicks based on count value.
# Parameters  : param (str) - Format "Identifier$$Count"
###############################################################################
def select_identifier_in_content_repository(param):
    try:
        identifier_value, enter_value = param.split("$$")

        obj = eng_obj.workspacetextbox.object
        obj_lst = obj.FindAllChildren("ClrClassName", "GridViewCell", 1000)
        Log.Message(f"Total grid cells found: {len(obj_lst)}")

        if not obj_lst:
            Log.Error("No grid cells found in the Content Repository.")
            return

        for item in obj_lst:
            output = str(item.DataContext.Identifier.OleValue)
            if output == identifier_value:
                if enter_value == 'Enter':
                    item.Click()
                    Sys.Keys("[Enter]")
                    Log.Checkpoint(f"Single-clicked on identifier: {identifier_value}")
                else:
                    item.DblClick()
                    Log.Checkpoint(f"Double-clicked on identifier: {identifier_value}")
                return

        Log.Error(f"Identifier '{identifier_value}' not found in the Content Repository.")

    except Exception as e:
        Log.Error(f"Error while selecting identifier with param '{param}': {str(e)}")


###############################################################################
# Function    : close_selected_identifier_tab_in_content_repository
# Description : Closes the selected identifier tab in the Content Repository 
#               if it matches the provided value.
# Parameters  : identifier_value (str) - Partial or full text of the tab to close.
###############################################################################
def close_selected_identifier_tab_in_content_repository(identifier_value):
    """
    Closes the selected identifier tab in the Content Repository.

    Args:
        identifier_value (str): Partial or full text of the tab to close.
    """
    try:
        obj = eng_obj.workspacetextbox.object
        close_lst = obj.FindAllChildren("ClrClassName", "CloseableTabItem", 1000)
        Log.Message(f"Total tabs found: {len(close_lst)}")

        if not close_lst:
            Log.Error("No open tabs found in the Content Repository.")
            return

        for tab in close_lst:
            if identifier_value in str(tab.WPFControlText):
                cl_lst = tab.FindAllChildren("ClrClassName", "button", 1000)
                Log.Message(f"Close buttons found: {len(cl_lst)}")
                if cl_lst:
                    cl_lst[0].Click()
                    Log.Checkpoint(f"Closed tab for identifier: {identifier_value}")
                    return
                else:
                    Log.Error(f"No close button found for tab: {identifier_value}")
                    return

        Log.Error(f"No tab found containing identifier: {identifier_value}")

    except Exception as e:
        Log.Error(f"Error while closing tab for identifier '{identifier_value}': {str(e)}")

                          
###############################################################################
# Function    : fetch_identifier_properties_in_content_repository
# Description : Fetches the displayed properties of an identifier in the 
#               Content Repository and compares them to expected values.
# Parameters  : value (str) - Space-separated expected property values.
###############################################################################
def fetch_identifier_properties_in_content_repository(value):
    try:
        actual_values = []
        expected_values = value.split("$$")

        obj = eng_obj.workspacetextbox.object
        properties_lst = obj.FindAllChildren("ClrClassName", "StackPanel", 1000)
        Log.Message(f"Total StackPanel elements found: {len(properties_lst)}")

        if not properties_lst:
            Log.Error("No property panels found in the Content Repository.")
            return

        for panel in properties_lst:
            text_blocks = panel.FindAllChildren("ClrClassName", "TextBlock", 1000)
            for tb in text_blocks:
                text_val = str(tb.WPFControlText).strip()
                if text_val:
                    actual_values.append(text_val)

        if actual_values == expected_values:
            Log.Checkpoint(f"Properties match. Expected & Actual: {actual_values}")
        else:
            Log.Error(f"Property mismatch.\nExpected: {expected_values}\nActual: {actual_values}")

    except Exception as e:
        Log.Error(f"Error while fetching identifier properties: {str(e)}")

###############################################################################
# Function    : verify_workframe_title_contains_text
# Description : Verifies if any WorkFrame title in the Content Repository 
#               contains the specified text.
# Parameters  : expected_text (str) - The text to search for in the WorkFrame title(s).
###############################################################################
def verify_workframe_title_contains_text(expected_text):
    try:
        obj = eng_obj.workspacetextbox.object
        title_lst = obj.FindAllChildren("ClrClassName", "WorkFrameTitle", 1000)
        Log.Message(f"Total WorkFrame titles found: {len(title_lst)}")

        if not title_lst:
            Log.Error("No WorkFrame titles found in the Content Repository.")
            return

        for title_item in title_lst:
            title_value = str(title_item.DataContext.Title.OleValue)
            Log.Message(f"Found WorkFrame title: '{title_value}'")

            if expected_text in title_value:
                Log.Checkpoint(f"Pass - WorkFrame title contains '{expected_text}'. Title: '{title_value}'")
                return

        Log.Error(f"Fail - No WorkFrame title contains '{expected_text}'.")

    except Exception as e:
        Log.Error(f"Error while verifying WorkFrame title: {str(e)}")
        
##########################################################################################
#Function :expand_nodes_CR_editor_Hierarchy_level
#Description : Double clciks and expands the nodes in CR editor page based on its hierarchy level
#Parameter :identifier,hierarchy level(str) - name of the node and hierarchy level of the node
#Example : expand_nodes_CR_editor("Global Root$$1")
##########################################################################################    
def expand_nodes_CR_editor_Hierarchy_level(param):
  identifier,hierarchy = param.split("$$")
  CR_node = ses_obj.systemexplorernodebutton.object
  CR_node_list = CR_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if CR_node_list:
    for items in CR_node_list:
      if items.DataContext.Identifier.OleValue == identifier:
        if hierarchy in str(items.HierarchyLevel):
          items.DblClick()
          Log.Message(f"Double clicked on {items.DataContext.Identifier.OleValue} with hierarchy {items.HierarchyLevel}")
  else:
    Log.Warning(f"No click performed ")

##########################################################################################
#Function :Rclick_nodes_CR_editor
#Description : Right clciks on the nodes in CR editor page based on its hierarchy level
#Parameter :identifier,hierarchy level(str) - name of the node and hierarchy level of the node
#Example : Rclick_nodes_CR_editor("User Contents$$3")
##########################################################################################    
def Rclick_nodes_CR_editor(param):
  identifier,hierarchy = param.split("$$")
  CR_node = ses_obj.systemexplorernodebutton.object
  CR_node_list = CR_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if CR_node_list:
    for items in CR_node_list:
      if items.DataContext.Identifier.OleValue == identifier:
        if hierarchy in str(items.HierarchyLevel):
          items.ClickR()
          Log.Message(f"Right clicked on {items.DataContext.Identifier.OleValue} with hierarchy {items.HierarchyLevel}")
  else:
    Log.Warning(f"No click performed ")
  
##########################################################################################
#Function :Verify_nodes_CR
# Description: Verifies the nodes present in the CR editor page based on its hierarchy level
# Parameter: None
##########################################################################################       
def Verify_nodes_CR():
  CR_node = ses_obj.systemexplorernodebutton.object
  CR_node_list = CR_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if CR_node_list:
    for items in CR_node_list:
      if items.IsVisible == True:
        if items.DataContext.Identifier.OleValue and items.HierarchyLevel:
          Log.Checkpoint(f"{items.DataContext.Identifier.OleValue} is at HierarchyLevel {items.HierarchyLevel} on CR editor screen")
  else:
    Log.Warning(f"No nodes available")
    
##########################################################################################91918
# Function :Verify_folders_created_editable_CR
# Description: Verifies the nodes created in the CR editor page are editable or not
# Parameter: identifier,hierarchy level(str) - name of the node and hierarchy level of the node
# Examples :  Verify_folders_created_editable_CR('Folder_1$$4')
##########################################################################################    
def Verify_folders_created_editable_CR(param):
  identifier,hierarchy = param.split("$$")
  CR_node = ses_obj.systemexplorernodebutton.object
  CR_node_list = CR_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if CR_node_list:
    for item in CR_node_list:
      if item.IsEditing:
        if item.DataContext.Identifier.Olevalue == identifier:
          if str(item.HierarchyLevel) == hierarchy:  
            Log.Message(f'The {item.DataContext.Identifier.Olevalue} with {item.HierarchyLevel} is created and is in editing state')
            break
      else:
        Log.Warning(f"The {item.DataContext.Identifier.Olevalue} with {item.HierarchyLevel} is created and not in editing state")
  else:
    Log.Warning(f"No nodes available")    

##########################################################################################
# Function :editing_nodes_CR_editor
# Description: Edits the nodes in the CR editor page - F2 key
# Parameter: identifier,hierarchy level(str) - name of the node and hierarchy level of the node
# Examples :  Verify_folders_created_editable_CR('Folder_1$$4')
##########################################################################################
def editing_nodes_CR_editor(param):
  identifier,hierarchy = param.split("$$")
  CR_node = ses_obj.systemexplorernodebutton.object
  CR_node_list = CR_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if CR_node_list:
    for items in CR_node_list:
      if items.DataContext.Identifier.OleValue == identifier:
        if hierarchy in str(items.HierarchyLevel):
          items.Click()
          Sys.Keys('[F2]')
          Sys.Keys('[BS]')
          Log.Message(f"clicked on {items.DataContext.Identifier.OleValue} with hierarchy {items.HierarchyLevel}")
  else:
    Log.Warning(f"No click performed ")         

##########################################################################################
# Function :update_folder_prop
# Description: updates the folder properties in CR editor page
# Parameter: identifier,field,value - name of folder,field - either Identifier or Description and 
#             value - new name
# Examples :  update_folder_prop('Folder_1$$Identifier$$Newname')
##########################################################################################
def update_folder_prop(param):
  identifier, field, value = param.split('$$')
  items = ses_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "Grid", 1000)
  if not items: Applicationutility.take_screenshot(); Log.Error("No system explorer nodes found."); return
  for item in items:
    dc = getattr(item, "DataContext", None)
    if hasattr(dc, "Identifier") and str(dc.Identifier) == identifier:
      if hasattr(dc, field):
        setattr(dc, field, value)
        Log.Checkpoint(f"Updated {field} to '{value}' for node '{identifier}'")
      else:
        Applicationutility.take_screenshot(); Log.Error(f"Field '{field}' not found in DataContext.")
      break
  else:
    Applicationutility.take_screenshot(); Log.Error(f"No matching node found for identifier '{identifier}'")

##########################################################################################
# Function :verify_folder_prop_name_valid
# Description: Verifies the new name to folder is valid or not
# Parameter: None
##########################################################################################
def verify_folder_prop_name_valid():
  fol_id = ses_obj.validatefoldernamevalid.object
  fol_chd = fol_id.FindAllChildren("WPFControlAutomationId", "Identifier_FieldEditor", 1000)
  for item in fol_chd:
    if item.tooltip != None:
      if hasattr(item, 'ToolTip'):
        Log.Warning(f" {item.ToolTip} ")
        Applicationutility.wait_in_seconds(1500, 'Wait')
    else:
      Log.Message(f'The folder was updated with {item.Text}')    

##########################################################################################
# Function   : Content_is_in_editing_state
# Description: Checks whether the content repository textbox is in editing state or not.
# Parameter  : None
##########################################################################################
def verify_Content_is_in_editing_state():
  text_blk = con_obj.contentrepositorytextbox.object
  if text_blk.DataContext.IsEditing is True:
    Log.Message('The textbox is editing state')
  else:
    Log.Error('The node is not in editing state')

##########################################################################################
# Function   : Verify_Content_list_of_created_content
# Description: Verifies if the created content with specific Identifier, Version, and Date 
#              exists in the content list. Logs checkpoints if found; logs error otherwise.
# Parameter  : param (str) - A string containing Identifier, Version, and Date separated by '$$'
##########################################################################################
def Verify_Content_list_of_created_content():
#  Identifier,version,Date = param.split('$$')
  icon = eng_obj.workspacetextbox.object.FindAllChildren('ClrClassName','GridViewRow',1000)
  for item in icon:
    if item.DataContext.Identifier.OleValue:
      if item.DataContext.Version.OleValue:
        if item.DataContext.DateTime.OleValue:
           Log.Checkpoint(f'name : {item.DataContext.Identifier.OleValue}')
           Log.Checkpoint(f'version : {item.DataContext.Version.OleValue}')
           Log.Checkpoint(f'Date : {item.DataContext.DateTime.OleValue}')
           break
  else:
    Log.Error('There is no information ')

##########################################################################################
# Function   : rename_content_validation
# Description: Enters a value into the workspace text box to rename content and validates 
#              whether the entered name is valid or shows a tooltip with an error.
# Parameter  : Enter_value (str) - The value to be entered as the new content name.
##########################################################################################
def rename_content_validation(Enter_value):
  column_box = con_obj.workframecontroltextbox.object
  text_box = column_box.FindChild('ClrClassName','GridViewCell',100).FindChild('ClrClassName','TextBox',100)
  Sys.Keys('[F2]')
  Applicationutility.wait_in_seconds(2000, 'Wait')
  text_box.Keys(Enter_value)
  Sys.Keys('[Enter]')   
  Applicationutility.wait_in_seconds(2000, 'Wait')
  if column_box.DataContext.HasErrors:
    if text_box.ToolTip.OleValue:
      Log.Warning(f'No deafault name or invalid : {text_box.ToolTip.OleValue} ')
      return
  else:
    updated_obj = eng_obj.workspacetextbox.object.FindChild('ClrClassName','TextBlock',1000)
    Log.Checkpoint(f'Identifier has a valid text : {updated_obj.WPFControlText}')

##########################################################################################
# Function   : rclick_on_content
# Description: Performs a right-click on a content item in the workspace grid based on 
#              a matching identifier.
# Parameter  : identifier - The identifier string to search within the grid row.
# Example    : rclick_on_content('Folder_1')
##########################################################################################     
def rclick_on_content(identifier):
  Content_text = eng_obj.workspacetextbox.object.FindChild('ClrClassName','GridViewRow',1000)
  if Content_text.Visible:
    if identifier in Content_text.DataContext.Identifier.OleValue:
      Content_text.ClickR()
      Log.Checkpoint(f'RClicked on {Content_text.DataContext.Identifier.OleValue}')
  else:
    Log.Error('No object found with specified identifier')
    
##########################################################################################
# Function   : Select_filters_created_content
# Description: Selects a filter in the workspace grid based on the given filter name.
# Parameter  : filter_name - The name of the filter column to be clicked.
# Example    : Select_filters_created_content('Identifier')
##########################################################################################    
def Select_filters_created_content(filter_name):
  Filtericon = eng_obj.workspacetextbox.object.FindAllChildren('ClrClassName','FilteringDropDown',1000)
  for i in Filtericon:
    if filter_name == i.Column.UniqueName.OleValue:
      i.Click()
      Log.Checkpoint(f"{i.Column.UniqueName.OleValue} filter is clicked")
      Applicationutility.take_screenshot()
      break
  else:
    Log.Error(f"{filter_name} not found")
        
  
  
  