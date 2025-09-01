﻿from TopologyExplorerTab import TopologyExplorerTab
from EngineeringClient import EngineeringClient
import Applicationutility
from MessageBox import MessageBox
from RefineOffline import RefineOffline
from ControlExpert import ControlExpert
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
from CurrentScreen import CurrentScreen
import Applicationexplorertabutility

topo_obj = TopologyExplorerTab()
msg_obj = MessageBox()
CS_obj = CurrentScreen()
eng_obj = EngineeringClient()
refo_obj = RefineOffline()
con_obj = ControlExpert()
proj_obj = ProjectExplorerTab()
sys_obj = SystemExplorerScreen()
cur_obj = CurrentScreen()


###############################################################################
# Function: select_tool_drag_drop_default_physical_view_TE
# Description: Selects a tool from the toolbox and drags it to a specified position in the default physical view.
# Parameter: param (str) - Format: "folder1$$folder2$$tool$$dropposition"
# Example: "FolderA$$FolderB$$ToolName$$pos_1"
###############################################################################
def select_tool_drag_drop_default_physical_view_TE(param):
  folder1, folder2, tool, dropposition = param.split('$$')
  drop_positions = {'pos_1': 1, 'pos_2': 1.3, 'pos_3': 1.9, 'pos_4': 3.3}

  if dropposition not in drop_positions:
    Log.Error(f"Invalid drop position: {dropposition}")
    return
  pos = drop_positions[dropposition]

  toolbox = topo_obj.toolboxcatalogbutton
  toolbox_list = toolbox.find_children_for_group_header_row()
  diagram = topo_obj.partdiagramcontroltextbox.object
  tox, toy = diagram.ScreenLeft, diagram.ScreenTop

  for item in toolbox_list:
    if item.Visible:
      item.IsExpanded = (folder1 in item.DataContext.Name.OleValue)
  Applicationutility.wait_in_seconds(1000, 'Wait')

  toolbox_list1 = toolbox.find_children_for_group_header_row()
  for ele in toolbox_list1:
    if ele.Visible and folder2 in ele.DataContext.Name.OleValue:
      ele.IsExpanded = True
  Applicationutility.wait_in_seconds(2000, 'Wait')

  tool_list = toolbox.find_children_for_grid_view_row()
  for row in tool_list:
    if row.Visible and tool in row.DataContext.PartNumber.OleValue:
      row.Drag(50, row.Height / 2, tox - row.ScreenLeft, toy - (row.ScreenTop / pos))
      Log.Checkpoint(f"Tool '{tool}' dragged and dropped to {dropposition}.")
      return

  Applicationutility.take_screenshot()
  Log.Error(f"Tool '{tool}' not found in '{folder2}'.")

###############################################################################
# Function: expand_physical_view_select_default_TE
# Description: Expands the "Physical Views" tree and selects the "Default Physical View".
# Parameter: None
###############################################################################
def expand_physical_view_select_default_TE():
    sys_proj = topo_obj.systemprojecttextbox
    sys_list = sys_proj.find_children_for_treeviewrow()
    Log.Message(f"System Project Items Found: {len(sys_list)}")
    physical_view = next((item for item in sys_list 
                          if item.Visible and 'Physical Views' in item.DataContext.DisplayName.OleValue), None)
    aqObject.CheckProperty(physical_view, "Visible", cmpEqual, True)
    physical_view.DataContext.IsExpanded = True
    Applicationutility.wait_in_seconds(2000, 'Wait')
    sys_list = sys_proj.find_children_for_treeviewrow()
    default_view = next((ele for ele in sys_list 
                         if ele.Visible and 'Default Physical View' in ele.DataContext.DisplayName.OleValue), None)
    aqObject.CheckProperty(default_view, "Visible", cmpEqual, True)
    default_view.DblClick()
    Applicationutility.wait_in_seconds(2000, 'Wait')


###############################################################################
# Function: grid_resize_TE
# Description: Resizes the grid layout in the topology explorer to ensure proper visibility of elements.
# Parameter: None
###############################################################################
def grid_resize_TE():
  dia = topo_obj.managerbutton.object
  sys = topo_obj.systemprojecttextbox
  prop = topo_obj.propertyinspectorviewbutton
  if sys.width < 180:
    dia.drag(sys.width+5, dia.height/2, 100, 0)
  if prop.width < 180:
    dia.drag((dia.width-prop.width-5), dia.height/2, -275, 0)

###############################################################################
# Function: select_cpu_reference_TE
# Description: Selects a CPU reference based on the version number and processor name.
# Parameter: param (str) - Format: "version_number$$processor_name"
# Example: "V1.0$$ProcessorX"
###############################################################################
def select_cpu_reference_TE(param):
  version_number, processor_name = param.split('$$')
  cpu_ref = topo_obj.catalogviewtextbox.object
  cpu_list = cpu_ref.FindAllChildren('ClrClassName', 'GroupHeaderRow', 1000)
  version_found = False
  for version in cpu_list:
    if version.Visible:
      if version_number in str(version.DataContext.Name):
        version.IsExpanded = True
        version_found = True
      else:
        version.IsExpanded = False
  if not version_found:
    Applicationutility.take_screenshot()
    Log.Error(f"Version number '{version_number}' not found in CPU list")

  part = cpu_ref.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  processor_found = False
  for processor in part:
    if processor.Visible:
      if version_number in str(processor.DataContext.PlcVersion.OleValue):
        if processor_name in str(processor.DataContext.PlcReference.OleValue):
          processor.IsSelected = True
          processor_found = True
          break
  if not processor_found:
    Applicationutility.take_screenshot()
    Log.Error(f"Processor '{processor_name}' with version '{version_number}' not found in CPU list")

  Applicationutility.wait_in_seconds(2000, 'Wait')
  ok = topo_obj.okbuttonbutton.object
  ok.Click()
###############################################################################
# Function: click_tab_properties_toolbar_Verify
# Description: Verifies if a specific tab item exists in the "PROPERTIES" toolbar and clicks it.
# Parameter: TabItem (str) - Name of the tab item to verify and click.
###############################################################################
def click_tab_properties_toolbar_Verify(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for i in TabItem_List:
    if TabItem in  i.WPFControlText:
      i.Click()
      Log.Message(f'{i.WPFControlText} has been verified')
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'{i.WPFControlText} has not been verified')

###############################################################################
# Function: Click_on_toolbar_icon_TE
# Description: Clicks on a specific toolbar icon in the topology explorer.
# Parameter: icon_name (str) - Tooltip text of the icon to click.
###############################################################################
def Click_on_toolbar_icon_TE(icon_name):
  manager_list = topo_obj.roottextbox.object.FindAllChildren('ClrClassName', 'Border', 1000)
  for item in manager_list:
    if icon_name in item.DataContext.ToolTip.Data.OleValue:
      item.Click()
      Log.Checkpoint(f"Toolbar icon '{icon_name}' clicked successfully")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Toolbar icon '{icon_name}' not found in the manager list")

###############################################################################
# Function: click_MenuItem_Toolbar
# Description: Clicks on a menu item in the toolbar context menu.
# Parameter: menu_option (str) - Name of the menu option to click.
###############################################################################
def click_MenuItem_Toolbar(menu_option):
  menu_items = eng_obj.rclickmenutextbox.object.FindAllChildren('ClrClassName', 'MenuItem', 1000)
  Log.Message(len(menu_items))
  for item in menu_items:
    Log.Message(item.WPFControlText)
    if menu_option in item.WPFControlText:
      item.Click()
      Log.Checkpoint(f"Menu option '{menu_option}' clicked successfully")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Menu option '{menu_option}' not found in the toolbar menu items")

###############################################################################
# Function: verify_properties_tab_toolbar
# Description: Verifies if a specific tab item exists in the "PROPERTIES" toolbar.
# Parameter: TabItem (str) - Name of the tab item to verify.
###############################################################################
def verify_properties_tab_toolbar(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for i in TabItem_List:
    if TabItem in  i.WPFControlText:
      Log.Message(f'{i.WPFControlText} has been verified')
      break
    else:
      Applicationutility.take_screenshot()
      Log.Error(f'{i.WPFControlText} has not been verified')

###############################################################################
# Function: Expand_Propertiestab
# Description: Expands a specific property item in the "PROPERTIES" tab.
# Parameter: PropertyItem (str) - Name of the property item to expand.
###############################################################################
def Expand_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.IsExpandable:
          view_item.IsExpanded = True
          break
      else:
        Applicationutility.take_screenshot()
        Log.Error(f"Property item '{PropertyItem}' not found or not expandable.")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("Properties tab not found.")

###############################################################################
# Function: Dclick_Propertiestab
# Description: Double-clicks on a specific property item in the "PROPERTIES" tab.
# Parameter: PropertyItem (str) - Name of the property item to double-click.
###############################################################################
def Dclick_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and  view_item.IsExpandable  :
          view_item.DblClick()

###############################################################################
# Function: Create_Logical_Network_Button
# Description: Clicks on a button to create a logical network.
# Parameter: button_name (str) - Name of the button to click.
###############################################################################
def Create_Logical_Network_Button(button_name):
  button_list = topo_obj.createlogicalnetworktextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in button_list:
    if button_name in button.WPFControlText:
      button.Click()
    else:
      Applicationutility.take_screenshot()
      Log.Error("Button doesnt exists")

###############################################################################
# Function: WorkStation_Items
# Description: Clicks on workstation items multiple times based on the count provided.
# Parameter: Item_name_count (str) - Format: "ItemName$$count"
# Example: "Workstation1$$3"
###############################################################################
def WorkStation_Items(Item_name_count):
  Item_name, count = Item_name_count.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for _ in range(int(count)):
        for view_item in ViewList:
          if Item_name in view_item.DataContext.DisplayName.OleValue:
            tox = view_item.Width - 5
            toy = view_item.Height / 2
            view_item.Click(tox, toy)
            break
        else:
          Applicationutility.take_screenshot()
          Log.Error(f"Item '{Item_name}' not found in PropertyGridItem list.")
          break
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("Properties tab not found.")

###############################################################################
# Function: Security_option_properties
# Description: Toggles the security option in the properties tab based on the provided value.
# Parameter: Value (str) - The value to set for the security option (e.g., "Enabled", "Disabled").
###############################################################################
def Security_option_properties(Value):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'EnumEditBox', 1000)
      Log.Message(len(ViewList))
      for view_item in ViewList:
        Log.Message(view_item.Value)
        if Value != view_item.Value:
          view_item.Click()
          Enabled = topo_obj.securityoptionenabledbutton.object
          Disabled = topo_obj.securityoptiondisabledbutton.object
          if Value == Enabled.WPFControlText:
            Enabled.Click()
            break
          else:
            Disabled.Click()
            break
      else:
        Applicationutility.take_screenshot()
        Log.Error(f"Value '{Value}' not found in EnumEditBox list.")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("Properties tab not found.")

###############################################################################
# Function: close_tab_item
# Description: Closes a specific tab item in the topology explorer.
# Parameter: tab_name (str) - Name of the tab to close.
###############################################################################
def close_tab_item(tab_name):
  a = topo_obj.managerbutton.object
  list = a.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for item in list:
    if tab_name in item.DataContext.Title.OleValue:
      item.Click(item.Width - 15, item.Height / 2)
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Tab '{tab_name}' not found to close.")

###############################################################################
# Function: DetailMessageDialogBox_Buttons
# Description: Clicks a button in the detail message dialog box.
# Parameter: button_name (str) - Name of the button to click (e.g., "Yes", "No").
###############################################################################
def DetailMessageDialogBox_Buttons(button_name):
  Popup_buttons = topo_obj.detailmessagedialogboxtextbox.object
  if button_name == "Yes" :
    tox = Popup_buttons.Width*0.8
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)
  else:
    tox = Popup_buttons.Width*0.95
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)

###############################################################################
# Function: Verify_DetailMessageDialogBox
# Description: Verifies if a specific message exists in the detail message dialog box.
# Parameter: message (str) - The message to verify.
###############################################################################
def Verify_DetailMessageDialogBox(message):
  Window_Message = topo_obj.detailmessagedialogboxtextbox.object.Message.OleValue
  if message in Window_Message:
    Log.Message(f'{Window_Message} verified')
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'{Window_Message} not verified')

###############################################################################
# Function: Dclick_Propertiestab_entervalue
# Description: Double-clicks on a property item in the "PROPERTIES" tab and enters a value.
# Parameter: PropertyItemValue (str) - Format: "PropertyItem$$Value"
# Example: "PropertyName$$Value123"
###############################################################################
def Dclick_Propertiestab_entervalue(PropertyItemValue):
  PropertyItem,Value = PropertyItemValue.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.Visible :
          view_item.DblClick()
          Sys.Keys(Value)
          Sys.Keys('[Enter]')
      else:
        Applicationutility.take_screenshot()
        Log.Error("Property doesnt exists")
        break

###############################################################################
# Function: confirmation_pop_up_TE
# Description: Clicks a button in the confirmation pop-up dialog.
# Parameter: button_value (str) - The button text to click (e.g., "Yes", "No").
###############################################################################
def confirmation_pop_up_TE(button_value):
  popup = msg_obj.detailmessagedialogtextbox.object
#  popup = Sys.Process("ControlExpert.Topology").WPFObject("HwndSource: DetailMessageDialog", "*")
#  #popup.ocr_blockby_text('Yes')
  OCR.Recognize(popup).BlockByText(button_value).Click()

###############################################################################
# Function: confirm_pop
# Description: Clicks a button in the confirmation pop-up for logical network creation.
# Parameter: button_value (str) - The button text to click (e.g., "Ok", "Cancel").
###############################################################################
def confirm_pop(button_value):
  popup = msg_obj.createlogicalnetworktextbox.object
  #Sys.Process("ControlExpert.Topology").WPFObject("HwndSource: Window", "Create Logical Network")
  OCR.Recognize(popup).BlockByText(button_value).Click()

###############################################################################
# Function: select_ContextMenu_Items_TE
# Description: Selects an item from the context menu in the topology explorer.
# Parameter: menu_item (str) - The name of the menu item to select.
###############################################################################
def select_ContextMenu_Items_TE(menu_item):
  menu = topo_obj.rclickmenutetextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 1000)
  
  Applicationutility.wait_in_seconds(2000, 'wait')
  for item in menu_items:
    if item.Header.DisplayName:
      Log.Message(str(item.Header.DisplayName.OleValue))
      if str(item.Header.DisplayName.OleValue) == str(menu_item):
        item.Click()
        Log.Message('The Context Menu Item clicked is : ' + str(menu_item))
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Context menu item '{menu_item}' not found")
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function: select_context_submenu_Items_TE
# Description: Selects a submenu item from the context menu in the topology explorer.
# Parameter: menu_item (str) - The name of the submenu item to select.
###############################################################################
def select_context_submenu_Items_TE(menu_item):
  menu = topo_obj.rclicksubmenutetextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 1000)
  Applicationutility.wait_in_seconds(2000, 'wait')
  for item in menu_items:
    if item.Role.OleValue == "SubmenuItem":
      if str(item.DataContext.DisplayName) == str(menu_item):
        item.Click()
        Log.Message('The Context Menu Item clicked is : ' + str(menu_item))
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Submenu item '{menu_item}' not found")
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function: click_tab_properties_TE
# Description: Clicks on a specific tab item in the "PROPERTIES" tab.
# Parameter: TabItem (str) - Name of the tab item to click.
###############################################################################
def click_tab_properties_TE(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("PROPERTIES tab not found")

  for i in TabItem_List:
    if TabItem in i.WPFControlText:
      i.Click()
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"TabItem '{TabItem}' not found")

###############################################################################
# Function: select_dropdown_value_properties_TE
# Description: Selects a value from a dropdown in the properties tab.
# Parameter: param (str) - Format: "tab_name$$expand_item$$dropdown$$select_value"
# Example: "CONFIGURATION$$Interfaces$$Security Level$$High"
###############################################################################
def select_dropdown_value_properties_TE(param):
  tab_name, expand_item, dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  click_tab_properties_TE(tab_name)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Expand_Propertiestab(expand_item)
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      item.DataContext.Value = select_value
      Log.Message('The dropdown value ' + str(item.DataContext.Value.OleValue) + ' has been selected')
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Dropdown '{dropdown}' not found in properties")

###############################################################################
# Function: select_combobox_TE
# Description: Selects a value from a combobox in the properties tab.
# Parameter: param (str) - Format: "dropdown$$select_value"
# Example: "Logical Network$$New"
###############################################################################
def select_combobox_TE(param):
  dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  Applicationutility.wait_in_seconds(1000, 'Wait')
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      comb_lst = item.FindAllChildren('ClrClassName', 'ComboBox', 1000)
      if len(comb_lst) == 1:
        for i in range(comb_lst[0].wItemCount):
          if select_value in comb_lst[0].Items.Item[i].Identifier.OleValue:
            comb_lst[0].SelectedIndex = i
            Log.Message(str(comb_lst[0].Items.Item[i].Identifier.OleValue) + ' item has been selected.')
            break
        else:
          Applicationutility.take_screenshot()
          Log.Error(f"'{select_value}' not found in combobox items")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Dropdown '{dropdown}' not found in properties")

###############################################################################
# Function: click_enable_disable_properties_TE
# Description: Enables or disables a property in the properties tab.
# Parameter: param (str) - Format: "tab_name$$expand_item$$dropdown$$select_value"
# Example: "SECURITY$$Password Protection$$Controller$$Disabled

      
def click_enable_disable_properties_TE(param):
  tab_name, expand_item, dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  click_tab_properties_TE(tab_name)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Expand_Propertiestab(expand_item)
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      ViewList = item.FindAllChildren('ClrClassName', 'EnumEditBox', 1000)
      for view_item in ViewList:
        if select_value != view_item.Value.OleValue:
          view_item.Click()
          Enabled = topo_obj.securityoptionenabledbutton.object
          Disabled = topo_obj.securityoptiondisabledbutton.object
          if select_value == Enabled.WPFControlText:
            Enabled.Click()
            break
          else:
            Disabled.Click()
            break
      else:
        Applicationutility.take_screenshot()
        Log.Error(f"Value '{select_value}' not found in EnumEditBox")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Dropdown '{dropdown}' not found in properties")

def Properties_disabled_in_services(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue:
          objects = view_item.FindAllChildren('ClrClassName', 'TreeListViewItemCell', 50)
          for obj in objects:
            if not obj.DataContext.CanAddChild:
              Log.Message('Service add icon is disabled')
              Applicationutility.take_screenshot()
              break
          else:
            Log.Message("Service add icon is enabled")
          break
      else:
        Applicationutility.take_screenshot()
        Log.Error(f"Property item '{PropertyItem}' not found in PROPERTIES tab")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("PROPERTIES tab not found")
            
            
def Right_click_physical_view_select_default_TE(item_name):
  sys_proj = topo_obj.systemprojecttextbox
  sys_list = sys_proj.find_children_for_treeviewrow()
  for item in sys_list:
    if item.Visible:
      if item_name in item.DataContext.DisplayName.OleValue:
        item.ClickR()
        Log.Message('The item clicked is : ' + str(item.DataContext.DisplayName.OleValue))
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Item '{item_name}' not found or not visible in physical view")
        

def Verify_ExportDialogBox(message):
  Window_Message = msg_obj.modeldialogfeedback.object.Title.OleValue
  if message in Window_Message:
    Log.Message(f'{Window_Message} verified')
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'{Window_Message} not verified')
    
  
  
def export_item_checkbox(param):
  identifier, state = param.split('$$')
  obj = msg_obj.parttreebutton.object
  obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  checkbox = None
  for item in obj_list:
    if str(identifier) in str(item.DataContext.NameToShow.OleValue):
      checkbox = item.FindAllChildren('ClrClassName', 'CheckBox', 1000)
      break
  if checkbox is None:
    Applicationutility.take_screenshot()
    Log.Error(f"Checkbox for identifier '{identifier}' not found")
  else:
    if int(state) == 1:
      checkbox[0].wState = 1
      Log.Message('Checkbox is Checked')
    elif int(state) == 0:
      checkbox[0].wState = 0
      Log.Message('Checkbox is Unchecked')
    else:
      Applicationutility.take_screenshot()
      Log.Error(f"Invalid state '{state}' for checkbox")
    
    
def enable_disable_properties_TE_WS(param):
  dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  Applicationutility.wait_in_seconds(1000, 'Wait')
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      ViewList = item.FindAllChildren('ClrClassName', 'EnumEditBox', 1000)
      for view_item in ViewList:
        if select_value != view_item.Value.OleValue:
          view_item.Click()
          Enabled = topo_obj.securityoptionenabledbutton.object
          Disabled = topo_obj.securityoptiondisabledbutton.object
          if select_value == Enabled.WPFControlText:
            Enabled.Click()
            break
          else:
            Disabled.Click()
            break
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Dropdown '{dropdown}' not found in properties")
        
def Check_controller_submenuitem_Disabled(submenu_item):
  menu = topo_obj.rclicksubmenutetextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 1000)
  for item in menu_items: 
    if item.Role.OleValue == "SubmenuItem": 
      if str(item.DataContext.DisplayName) == submenu_item:
        if item.IsEnabled == False:
          Log.Message(submenu_item + " is disabled")
        else:
          Log.Error(submenu_item + " : is enabled")
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Submenu item '{submenu_item}' not found")
  Applicationutility.wait_in_seconds(1000, 'wait')
    
    
def Configure_and_ManagePassword():
  
  Configure_Controller()
  Conditionsutility.rclick_M580_1()
  Topologyexplorerutility.select_ContextMenu_Items_TE('PAC')
  Topologyexplorerutility.select_context_submenu_Items_TE('Manage Password')
  Applicationutility.wait_for_execution()

  Delay(15000)
  obj  = aet_obj.savechangesdialogboxtextbox.object
  if obj.Visible and obj.Enabled:
    if "Manage Password did not complete" in str(obj.MainText):
      Log.Message(str(obj.MainText) + " is displayed")
    else:
      Log.Error(obj.MainText+" is not displayed")
      
    if "Unable to reach engine with the following IP addresses" in str(obj.DetailsText.OleValue):
      Log.Message(str(obj.DetailsText.OleValue) + " is displayed")
    else:
      Log.Error(str(obj.DetailsText.OleValue)+" is not displayed")
    Log.Message("*********") 
    OCR.Recognize(obj).CheckText("*Manage Password did not complete*")
    OCR.Recognize(obj).CheckText("*Unable to reach engine with the following IP addresses*") 
  
  else:
    Delay(5000,"Waiting for pop up")
  obj_ok = obj.Find("WPFControlText","OK",100)
  obj_ok.Click()

#Verify Notification Message in Topology Explorer page without adding a Logical Network to the Controller   
def Verify_Notification_Msg_with_error_details(param):  
  try:
    message_to_verify, count = param.split('$$') 
    N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
 
    for i in N_Message_List:
        if i.Panel_ZIndex == 0 :
          
          if message_to_verify in str(i.DataContext.Message.OleValue):
              i.DblClick()
              Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')                                
          else:
              Log.Warning(f'{message_to_verify} did not appear in Notification Pannel')
              
    for i in N_Message_List:                   
        if i.Panel_ZIndex > 0 and i.Panel_ZIndex < int(count)+1:
            Log.Message(f'{i.DataContext.Message.OleValue} in Notification Pannel')
            
  except Exception as ex:
      Log.Error(ex)
      
#Verify if there is no error message in the Notification panel           
def Verify_no_errors_in_Notification_Panel():  
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  for i in N_Message_List:
    if i.Visible:
      if "error" not in str(i.DataContext.Message.OleValue) and i.Panel_ZIndex == 0 :
        Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error('error displayed in Notification Pannel')


#This method is used to configure Controller     
def Configure_Controller():
  try:      
    Conditionsutility.click_M580_1()
    Topologyexplorerutility.select_dropdown_value_properties_TE('SECURITY$$Global Policy$$Security Level$$No')
    Topologyexplorerutility.click_enable_disable_properties_TE('SECURITY$$Password Protection$$Controller$$Disabled')
    Topologyexplorerutility.confirmation_pop_up_TE('Yes')
    Topologyexplorerutility.click_tab_properties_TE('CONFIGURATION')
    Topologyexplorerutility.Expand_Propertiestab('Interfaces')
    Topologyexplorerutility.Expand_Propertiestab('Embedded Interface')
    Topologyexplorerutility.Expand_Propertiestab('MainIP')
    Topologyexplorerutility.Expand_Propertiestab('Logical Network')
    Topologyexplorerutility.select_combobox_TE('Logical Network$$New')
    Topologyexplorerutility.confirm_pop('Ok')
    Applicationutility.wait_in_seconds(3000, 'Wait')

    Conditionsutility.rclick_M580_1()
    Topologyexplorerutility.select_ContextMenu_Items_TE('PAC')
    Topologyexplorerutility.select_context_submenu_Items_TE('Configure')
    Applicationutility.wait_for_execution()
    Applicationutility.wait_in_seconds(3000, 'Wait')
    Topologyexplorerutility.close_tab_item('M580_1')
    
  except Exception as ex:
    Log.Message(ex)
    
def expand_system_project_TE(Val):
  sys_proj = topo_obj.systemprojecttextbox
  sys_list = sys_proj.find_children_for_treeviewrow()
  Log.Message(len(sys_list))
  for item in sys_list:
    if item.Visible:
      if Val in item.DataContext.DisplayName.OleValue:
        item.DataContext.IsExpanded = True
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"System project '{Val}' not found")
  Applicationutility.wait_in_seconds(2000, 'Wait')
  
def dblclick_system_project_TE(Val):
  sys_proj = topo_obj.systemprojecttextbox
  sys_list = sys_proj.find_children_for_treeviewrow()
  for ele in sys_list:
    if ele.Visible:
      if Val in ele.DataContext.DisplayName.OleValue:
        ele.DblClick()
        Applicationutility.wait_in_seconds(2000, 'Wait')
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"System project '{Val}' not found")
    
def Verify_status_of_MainIP_and_IPA(val):  # "Valid IP Address"
  logicalnetwork_list = topo_obj.logicalnetworkgridtextbox
  ln_lst = logicalnetwork_list.find_children_for_treeviewrow()
  for ele in ln_lst:
    if ele.Visible:
      if "MainIP" in ele.DataContext.Interface.OleValue:
        if val in ele.DataContext.Status.OleValue:
          Log.Message("MainIP is validated as: " + ele.DataContext.Status.OleValue)
        else:
          Log.Error("MainIP status is: " + ele.DataContext.Status.OleValue)
        break
      elif "IPA" in ele.DataContext.Interface.OleValue:
        if val in ele.DataContext.Status.OleValue:
          Log.Message("IPA is validated as: " + ele.DataContext.Status.OleValue)
        else:
          Log.Error("IPA status is: " + ele.DataContext.Status.OleValue)
        break
  else:
    Applicationutility.take_screenshot()
    Log.Error("Neither MainIP nor IPA interface found")

def wait_in_seconds(count,reson_for_delay):
    """waiting_for_page"""
    aqUtils.Delay(count,reson_for_delay)
  
def edit_Subnet_Address(IP_add):
    obj = msg_obj.createlogicalnetworktextbox.object
    Subnet_Address = obj.FindAllChildren("WPFControlName","AddressMaskEditor",10)
    Subnet_Address[0].Address = IP_add
    Delay(1000)
    if Subnet_Address[0].Address == IP_add:
      Log.Checkpoint("Subnet Address is updated as "+IP_add)
    else:  
      Applicationutility.take_screenshot()
      Log.Error("Subnet Address is updated as "+Subnet_Address[0].Address)
     
     
def Controller_property():
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    if getattr(getattr(control, "DataContext", None), "DisplayName", None) == "Controller":
      control.Click()
      aqUtils.Delay(500)
      for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10):
        if item.WPFControlText == "False":
          item.Click() if item.Enabled else Log.Error("Dropdown item 'False' is disabled.")
          return
  Applicationutility.take_screenshot()
  Log.Error("Could not find the specific 'Controller' element.")

def Workstation_property():
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    if getattr(getattr(control, "DataContext", None), "DisplayName", None) == "Workstation":
      control.Click()
      aqUtils.Delay(500)
      for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10):
        if item.WPFControlText == "False":
          item.Click() if item.Enabled else Log.Error("Dropdown item 'False' is disabled.")
          return
  Applicationutility.take_screenshot()
  Log.Error("Could not find the specific 'Controller' element.")
  
def Enter_Controller_Password_TE(param):
  field, password = param.split("$$")
  
  if "Password" == field:
    topo_obj.newpasswordboxtextbox.object.Click()
    Sys.Keys("^a")
    Sys.Keys("[BS]")
    topo_obj.newpasswordboxtextbox.object.PasswordText = password
    Log.Message(str(topo_obj.newpasswordboxtextbox.object.PasswordText) + " entered in Password")
  elif "Confirm Password" == field:
    topo_obj.ConfirmPasswordboxtextbox.object.Click()
    Sys.Keys("^a")
    Sys.Keys("[BS]")
    topo_obj.ConfirmPasswordboxtextbox.object.PasswordText = password
    Log.Message(str(topo_obj.ConfirmPasswordboxtextbox.object.PasswordText) + " entered in Confirm Password")
  elif "Current Password" == field:
    topo_obj.oldpasswordboxboxtextbox.object.Click()
    Sys.Keys("^a")
    Sys.Keys("[BS]")
    topo_obj.oldpasswordboxboxtextbox.object.PasswordText = password
    Log.Message(str(topo_obj.oldpasswordboxboxtextbox.object.PasswordText) + " entered in Current Password")
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Unknown field '{field}' provided for password entry")
 
def Click_btn_MessageWindow(button):
  obj = CS_obj.modificationpopupbutton.object.FindAllChildren("ClrClassName", "Button", 10)
  for item in obj:
    if item.WPFControlText == button:
      item.Click()
      Log.Message(item.WPFControlText + " button clicked")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Button '{button}' not found in Message Window")
          
def Verify_entered_Controller_Password_valid_invalid_TE(param):
  if "Password" == param:
    if topo_obj.newpasswordboxtextbox.object.ToolTip == None:
      Log.Message("Password entered is Valid")
    else:
      Log.Message("Password entered is Invalid : " + topo_obj.newpasswordboxtextbox.object.ToolTip.OleValue)

  elif "Confirm Password" == param:
    if topo_obj.ConfirmPasswordboxtextbox.object.ToolTip == None:
      Log.Message("Confirm Password entered is Valid")
    else:
      Log.Message("Confirm Password entered is Invalid : " + topo_obj.ConfirmPasswordboxtextbox.object.ToolTip.OleValue)

  elif "Current Password" == param:
    if topo_obj.oldpasswordboxboxtextbox.object.ToolTip == None:
      Log.Message("Current Password entered is Valid")
    else:
      Log.Message("Current Password entered is Invalid : " + topo_obj.oldpasswordboxboxtextbox.object.ToolTip.OleValue)
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Unexpected parameter: {param}")

def get_clipboard_text():
    return Sys.Clipboard
    
def Get_Authentication_Code_by_clicking_copy_icon():
  try:
    buttons_list = msg_obj.exportpopupbutton.object.Find(('ClrClassName','ToolTip'),( 'Button','Copy To Clipboard'), 1000)
    buttons_list.click()
    copied_info = get_clipboard_text()
    Log.Message(copied_info)
    return copied_info
    
  except Exception as exe:
    Log.Error(str(exe)) 
    
def Get_Authentication_Code_form_textbox():
  try:
    obj = msg_obj.exportpopupbutton.object.Find("Name", "WPFObject('AuthenticationText')", 1000)
    Log.Message(obj.wText)
    return obj.wText
    
  except Exception as exe:
    Log.Error(str(exe)) 
    
def Verify_forgot_password_Authentication_Code():
  try:
    obj = msg_obj.exportpopupbutton.object.Find("Name", "WPFObject('TextBlock', '*Schneider Electric Support*', *)", 10)
    Log.Message(obj.Text)
    
    ACode_copyicon = Get_Authentication_Code_by_clicking_copy_icon()
    ACode_textbox = Get_Authentication_Code_form_textbox()
  
    if ACode_copyicon == ACode_textbox:
      Log.Checkpoint("Authentication Code from copy icon and text box is matching ")
    else:
      Log.Error("Authentication Code from copy icon and text box is not matching ")
  
  except Exception as exe:
    Log.Error(str(exe))

    
def set_ip_and_subnet(ip_address, subnet_mask):
  field_values = {
    "IP address": ip_address,
    "Subnet Mask": subnet_mask
  }
  text_boxes = topo_obj.stbpropertiesbutton.object.FindAllChildren("ClrClassName", "TextBox", 50)
  for text_box in text_boxes:
    for field_name, value in field_values.items():
      if field_name in text_box.WPFControlAutomationId:
        text_box.Keys(value)
        Log.Checkpoint(f"Set {field_name} to {value}")
        break
    else:
      Applicationutility.take_screenshot()
      Log.Error(f"No matching field found for TextBox with AutomationId: {text_box.WPFControlAutomationId}")
  
  
def stbproperties_close_button():
  closebtn = topo_obj.stbpropertiesclosebutton.Click()
  Log.Message(closebtn.Exists)
    
  
  
def configure_ethernet_network(network):
  physical_connections = topo_obj.controllerphysicalconnectiontab.object
  network_rows = physical_connections.FindAllChildren("ClrClassName", "GridViewRow", 10)
  for controller in network_rows:
    controller_name = controller.DataContext.DeviceIdentifier
    controller.Click()
    dropdown_items = eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10)
    for item in dropdown_items:
      if item.WPFControlText == network:
        item.Click()
        Log.Checkpoint(f"'{network}' selected for this '{controller_name}'.")
        break
    else:
      Applicationutility.take_screenshot()
      Log.Error(f"Network '{network}' not found for controller '{controller_name}'.")

  
def get_project_browser():
    return topo_obj.catalogbutton.object

def click_folder_by_name(name):
  project_browser = get_project_browser()
  count = project_browser.wItems.Count
  for i in range(count):
    item = project_browser.wItems.Item[i]
    if item.Text == name:
      item.Click()
      break
  else:
      Applicationutility.take_screenshot()
      Log.Error(f"Folder '{name}' not found in project browser.")

def select_catalog_browser_item_TE(val):
  project_browser = get_project_browser()
  count = project_browser.wItemCount
  for i in range(count):
    if val in project_browser.wItem[i]:
      project_browser.SelectItem(val)
      break
  else:
      Applicationutility.take_screenshot()
      Log.Error(f"Item '{val}' not found in catalog browser.")

def doubleclick_catalog_browser_item_TE(val):
  project_browser = get_project_browser()
  count = project_browser.wItems.Count
  for i in range(count):
    if val in project_browser.wItem[i]:
      project_browser.DblClickItem(val)
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Item '{val}' not found in catalog browser.")

def double_click_selected_catalog_browser_item_TE(main_folder, subfolder, final_item):
    click_folder_by_name(main_folder)
    select_catalog_browser_item_TE(subfolder)
    Applicationutility.wait_in_seconds(500, 'wait')
    doubleclick_catalog_browser_item_TE(final_item)
    Applicationutility.wait_in_seconds(1500, 'wait')
    

#def select_tab_in_topo_config(tabname):
#  objects = []
#  if topo_obj.configurationhardwarecatalog:
#    objects = topo_obj.configurationhardwarecatalog.object.FindAllChildren("ClassName", "SECTabControl", 10)
#  if not objects and topo_obj.configurationhardwarecatalog1:
#    objects = topo_obj.configurationhardwarecatalog1.object.FindAllChildren("ClassName", "SECTabControl", 10)
#  if not objects and topo_obj.dtmbrowserprop:
#    objects = topo_obj.dtmbrowserprop.object.FindAllChildren("ClassName", "SECTabControl", 10)
#  for h in objects:
#    for i in range(h.ChildCount):
#      if tabname in h.Child(i).Text:
#        h.Child(i).Click()
#        Log.Checkpoint(f"Clicking on '{tabname}'")
#        return
#  Log.Warning(f"Could not find '{tabname}'")

def select_tab_in_topo_config(tabname):
  objects = []
  if hasattr(topo_obj, 'configurationhardwarecatalog') and topo_obj.configurationhardwarecatalog:
    objects = topo_obj.configurationhardwarecatalog.object.FindAllChildren("Name", f"TextObject({tabname})", 10)
  if not objects and hasattr(topo_obj, 'configurationhardwarecatalog1') and topo_obj.configurationhardwarecatalog1:
    objects = topo_obj.configurationhardwarecatalog1.object.FindAllChildren("Name", f"TextObject({tabname})", 10)
  for obj in objects:
    if obj.Text == tabname:
      obj.Click()
      Log.Checkpoint(f"Successfully clicked on the tab: '{tabname}'")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"No tabs found with the name '{tabname}'")


#def Dblclick_config_panel_item_TE(property):
#  for h in topo_obj.deviceshardwarecatalog.object.FindAllChildren("ClassName", "CfCatViewDTMTreeQueryView", 10):
#    for i in range(h.ChildCount):
#      if "TextObject" in h.Child(i).Name and h.Child(i).Text == property:
#        h.Child(i).DblClick()
#        Log.Checkpoint(f'{property}' "is Double Clicked.")
#        Applicationutility.wait_in_seconds(1000, 'Wait')
#        return
#  else:
#    Log.Warning(f'{property}' " Was Not found.")
    
def Dblclick_config_panel_item_TE(property):
  for h in topo_obj.deviceshardwarecatalog.object.FindAllChildren("Name", f"TextObject({property})", 10):
    if h.Text == property:
      h.DblClick()
      Log.Checkpoint(f'{property}' "is Double Clicked.")
      Applicationutility.wait_in_seconds(1000, 'Wait')
      return
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'{property}' " Was Not found.")
  
## need to fix this 
def click_update_in_config():
  topo_obj.updatebutton.object.Click()
  Log.Checkpoint("Update Button Clicked")

def update_ip_address(new_ip):
  ip_objects = topo_obj.prmconfigwindow.object.FindAllChildren("ObjectType", "IpAddress", 100)
  for ip_obj in ip_objects:
    if ip_obj.Caption == "IP Address:":
      Log.Message(f"Current IP Address: {ip_obj.Value}")
      ip_obj.Value = new_ip
      Log.Checkpoint(f"IP Address updated to: {new_ip}")
      return
  Applicationutility.take_screenshot()
  Log.Error("IP Address field not found.")
  

def close_button_selected():
  if refo_obj.closerefineofflinebutton.object.WaitProperty("Enabled", True, 30000):
    refo_obj.closerefineofflinebutton.object.Click()
    Log.Checkpoint("Close button clicked successfully.")
  else:
    Applicationutility.take_screenshot()
    Log.Error("Close button was not enabled within the expected time.")
    
def close_hardware_catalog(button):
  for btn in topo_obj.configurationhardwarecatalog.object.FindAllChildren("ObjectType", "Button", 10):
    if btn.ObjectIdentifier == button:
      btn.click()
      Log.Checkpoint(f"'{button}' button was Selectes in Hardware Catalog window")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"'{button}' button Was not Found in Hardware Catalog")


def select_rack_in_PLC(rack_num):
  rack_number = int(rack_num)
  if rack_number >= 0:
    topo_obj.plcbuswindow.object.Click()
    Sys.Keys("[Down]")
    Sys.Keys("[Up]")
    for _ in range(rack_number + 1):
      Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Log.Checkpoint(f"Selected rack number {rack_number} in PLC.")
  else:
    Applicationutility.take_screenshot()
    Log.Error(f"Invalid rack number: {rack_num}")

  
def uncheck_checkbox_in_hart():
  found = False
  for i in range(10):
    values = topo_obj.hartmodulecheckbox.object.FindAllChildren("Name", f"TextObject(' {i}')", 100)
    for value in values:
      value.Click()
      Sys.Keys("[Right]")
      Sys.Keys(" ")
      Sys.Keys("[Down]")
      found = True
  if not found:
    Applicationutility.take_screenshot()
    Log.Error("No checkboxes found in HART module to uncheck")
        
def click_checkbox_in_hart(channel):
  uncheck_checkbox_in_hart()
  for i in range(10):
    values = topo_obj.hartmodulecheckbox.object.FindAllChildren("Name", f"TextObject(' {i}')", 100)
    for value in values:
      if channel in value.Text:
        value.click()
        Sys.Keys("[Right]")
        Sys.Keys(" ")
        Log.Checkpoint(f"Channel '{channel}' check box is clicked")
        return
  Applicationutility.take_screenshot()
  Log.Error(f"Channel '{channel}' check box not found in HART module")

def Select_IP_from_ControlProjectDeployment(IP_address):
  name = topo_obj.primaryaddresslistdropdown.object
  name.Click()
  Checkbox = topo_obj.startenginecheckbox.object
  
  Dropdown_options = eng_obj.userdropdownmenuitemtextbox.object
  Dropdown_IPList = Dropdown_options.FindAllChildren("ClrClassName","RadComboBoxItem",10)
  for IP in Dropdown_IPList:
    if IP_address in IP.DataContext.FormattedAddress.OleValue:
      IP.Click()
      Log.Message(f'{IP.DataContext.FormattedAddress.OleValue} was selected from Dropdown option')
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'{IP_address} did not exist in Dropdown option')
  Checkbox.Click() 
  
###############################################
import Actionutility


def select_dropdown_value_popup_TE():
  obj = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("ExecutableSelection", "", 1).WPFObject("Grid", "", 1).WPFObject("GroupBox", "Select Project and Executable", 1).WPFObject("Grid", "", 1).WPFObject("Projects") 
  for i in range(obj.Items.Count):
    if 'M580_Standalone' in obj.Items.Item[i].Identifier.OleValue:
      obj.SelectedIndex = i
      Log.Checkpoint(f'The selected value is {obj.Items.Item[i].Identifier.OleValue}')
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error(f'The value {obj.Items.Item[i].Identifier.OleValue} is not available in the dropdown')
  
  
def Validate_TE_Window_Keyboard_Action():
  Sys.Keys('^W')
  
def Enter_password_controller_popup():
  Sys.Keys('Schneider0!')
  
def select_ip_in_deploy_workstation(ip):
  for i in proj_obj.assignmentsdocktextbox.object.FindAllChildren("ClrClassName", "GridViewCell", 100):
    prop = i.DataContext.PropertyName
    i.click()
    Applicationutility.wait_in_seconds(1000, "wait")
    break
  dropdown_items = eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "TextBlock", 10)
  for item in dropdown_items:
    if ip in item.WPFControlText:
      item.click()
      Log.Checkpoint(f"'{ip}' selected for this '{prop}'.")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"IP '{ip}' not found in deploy workstation dropdown for property '{prop}'")
      
def open_networks_folder(node):
  test = eng_obj.systemexplorertreeview.object.FindAllChildren("ClrClassName", "ExplorerNode", 100)
  for i in test:
    if i.DataContext.Identifier == node:
      i.DblClick()
      Log.Checkpoint(f"'{node}' network folder opened successfully")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"Network folder '{node}' not found")
  
def open_ethernetnetwork(ethernet):
  network = topo_obj.openethernetnetwork.object.FindAllChildren("ClrClassName", "GridViewRow", 100)
  for i in network:
    if i.DataContext.Identifier == ethernet:
      i.DblClick()
      Log.Checkpoint(f"Double Clicked on '{i.DataContext.Identifier}'")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"Ethernet network '{ethernet}' not found")
      
def network_panel(interface, controller):
  panel = topo_obj.networkpanel.object.FindAllChildren("ClrClassName", "TextBlock", 100)
  for i in panel:
    if i.WPFControlText == interface:
      i.DblClick()
      if controller in i.DataContext.DestinationInstance.OleValue:
        Log.Checkpoint(f"The Ethernet Network is mapped to the {controller}")
        return
      else:
        Applicationutility.take_screenshot()
        Log.Error(f"Controller '{controller}' not mapped to interface '{interface}'")
        return
  Applicationutility.take_screenshot()
  Log.Error(f"Interface '{interface}' not found in network panel")
  
def findallchildern_objecttype(parent, obj_type, identifier, action, success_log, failure_log, depth=100):
  elements = parent.FindAllChildren("ObjectType", obj_type, depth)
  for elem in elements:
    if identifier in getattr(elem, 'Caption', '') and elem.Enabled:
      getattr(elem, action)()
      Log.Checkpoint(success_log)
      return
  Applicationutility.take_screenshot()
  Log.Error(failure_log)

def click_tools_in_topo_configuration(menu):
  findallchildern_objecttype(
    topo_obj.topologyconfigurationwindow.object, "MenuItem", menu, "Click",
    f"'{menu}' was clicked in Tool Bar", f"'{menu}' was not found in Tool Bar"
  )

def click_menu_item_in_topo_configuration(menu_item):
  findallchildern_objecttype(
    con_obj.toolbarpopwindowce.object, "MenuItem", menu_item, "Click",
    f"'{menu_item}' was selected in Tool Bar PopUp Window", f"'{menu_item}' was not found in Tool Bar PopUp Window"
  )

def double_click_item_in_DTM(item):
  findallchildern_objecttype(
    topo_obj.dtmbroswerwindow.object, "OutlineItem", item, "DblClick",
    f"Double-clicked on item: {item}", f"Item with caption '{item}' not found."
  )

def right_click_item_in_DTM(item):
  findallchildern_objecttype(
    topo_obj.dtmbrowserprop.object, "OutlineItem", item, "ClickR",
    f"Right-clicked on item: {item}", f"Item with caption '{item}' not found."
  )
  
def double_click_settings_in_PRM(item):
  findallchildern_objecttype(
    topo_obj.prmconfigwindow.object, "OutlineItem", item, "DblClick",
    f"Double-clicked on item: {item}", f"Item with caption '{item}' not found."
  )


def select_button_BME_window(button):
  findallchildern_objecttype(
    topo_obj.bmehartwindow.object, "Button", button, "Click",
    f"'{button}' button was selected in BME window", f"'{button}' button was not found in BME Window"
  )

def select_button_PLC(button):
  findallchildern_objecttype(
    topo_obj.plcbuswindow.object, "Button", button, "Click",
    f"'{button}' button was selected in Hardware Catalog window", f"'{button}' button was not found in Hardware Catalog"
  )

def Double_Click_on_Channel(property):
  findallchildern_objecttype(
    con_obj.okmodaldialoguewindowce.object, "ListItem", property, "DblClick",
    f"{property} was double-clicked.", f"{property} was not found in window"
  )

def select_options_in_controlexpert_modaldialogue(option):
  findallchildern_objecttype(
    con_obj.toolbarpopwindowce.object, "MenuItem", option, "Click",
    f"'{option}' was selected in Control Expert Modal Dialogue Window", f"'{option}' was not found in Control Expert Modal Dialogue Window"
  )
  
def select_submenu_options_in_controlexpert_modaldialogue(option):
  findallchildern_objecttype(
    con_obj.deviceoptionstabce.object, "MenuItem", option, "Click",
    f"'{option}' was selected in Control Expert Modal Dialogue Window", f"'{option}' was not found in Control Expert Modal Dialogue Window"
  )
  
def select_final_option_in_controlexpert_modaldialogue(option):
  findallchildern_objecttype(
    con_obj.additionaloptionstabce.object, "MenuItem", option, "Click",
    f"'{option}' was selected in Control Expert Modal Dialogue Window", f"'{option}' was not found in Control Expert Modal Dialogue Window"
  )  

def double_click_on_ftdconfiguration_window(property):
  window = topo_obj.fdtconfigurationwindowtextbox.object
  window.Maximize()
  findallchildern_objecttype(
    topo_obj.fdtconfigurationwindowtextbox.object, "ListItem", property, "DblClick",
    f"{property} was double-clicked.", f"{property} was not found in window"
  )

def select_option_module_in_dropdown(channel):
  findallchildern_objecttype(
    con_obj.dropdowntabce.object, "ListItem", channel, "Click",
    f"{channel} was selected in dropdown", f"{channel} was not found in dropdown"
  )

def Click_button_in_ftdconfiguration(button):
  for btn in topo_obj.fdtconfigurationwindowtextbox.object.FindAllChildren("ClrClassName", "PsButton", 100):
    if btn.Text == button:
      btn.click()
      Log.Checkpoint(f"{button} button was clicked in this window")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"{button} was not found in this window")


def select_protocol(protocol):
  con_obj.dropdownbtnce.object.Click()
  for opt in con_obj.dropdownbtnoptionce.object.FindAllChildren("ObjectType", "ListItem", 10):
    if protocol in opt.ObjectIdentifier:
      opt.Click()
      Log.Checkpoint(f"'{protocol}' was selected in Control Expert Modal Dialogue Window")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"'{protocol}' was not found in the dropdown options")
  
def select_device(device):
  scrollable_area = con_obj.addwindowce.object
  while True:
    for bmi in scrollable_area.FindAllChildren("Name", f"TextObject('{device}')", 100):
      if bmi.Text == device:
        Log.Checkpoint(f"{device} has been verified")
        bmi.DblClick()
        Log.Checkpoint(f"'{device}' is selected")
        return
    scrollable_area.MouseWheel(-1)
    aqUtils.Delay(20)
    if not scrollable_area.VisibleOnScreen:
      Applicationutility.take_screenshot()
      Log.Error(f"'{device}' was not found on this window")
      return


def select_protocol_in_add_device(protocol, device):
  select_protocol(protocol)
  select_device(device)  

def find_and_click_button(parent_obj, button_name, max_depth=10):
  buttons = parent_obj.FindAllChildren("WndClass", "Button", max_depth)
  for btn in buttons:
    if hasattr(btn, 'WndCaption') and button_name in btn.WndCaption:
      btn.Click()
      Log.Checkpoint(f"Button '{button_name}' was clicked.")
      return
  Applicationutility.take_screenshot()
  Log.Error(f"'{button_name}' button not found.")

def controlexp_popup(button_name):
  find_and_click_button(con_obj.modaldialogewindowce.object, button_name, 10)
  wait_for_dtm_update()

def click_button_in_prm(button_name):
  find_and_click_button(topo_obj.prmconfigwindow.object, button_name, 100)

def modaldialogue_window_ce(button_name):
  find_and_click_button(con_obj.okmodaldialoguewindowce.object, button_name, 100)
  Applicationutility.wait_in_seconds(2000, "wait")

def select_btn_device_prop(button_name):
  find_and_click_button(con_obj.devicepropertywindowce.object, button_name)

def click_validate_btn_in_control_config():
  topo_obj.paneleditbutton.object.click()
  Log.Checkpoint("Validate Button was Clicked")
  
def wait_for_dtm_update():
  updating_window = con_obj.okmodaldialoguewindowce.object
  if updating_window.WaitProperty("Exists", False, 50000):
    Log.Checkpoint("DTM catalog update completed.")
  else:
    Applicationutility.take_screenshot()
    Log.Error("DTM catalog update window did not close within the expected time.")
    
  
def select_slots_in_ftdconfiguration(slot, channel):
  for slots in topo_obj.fdtconfigurationwindowtextbox.object.FindAllChildren("ClrClassName", "ComboBox", 100):
    if slots.Tag == slot:
      slots.click()
      Log.Checkpoint(f"{slot} Was clicked.")
      if channel:
        select_option_module_in_dropdown(channel)
      return
  Applicationutility.take_screenshot()
  Log.Error(f"{slot} was not found in this window")
  
  
def verify_dtm_device():
  for device in topo_obj.dtmdevicewindowtextbox.object.FindAllChildren("ClrClassName", "Label", 100):
    if isinstance(device, object) and hasattr(device, 'WinFormsControlName') and device.WinFormsControlName in ["lblDeviceName", "lblReference"]:
      Log.Checkpoint(f"{device.WinFormsControlName}: {device.Text}")
      break
  else:
    Applicationutility.take_screenshot()
    Log.Error("No matching DTM device label found")
  window = topo_obj.fdtconfigurationwindowtextbox.object
  window.Close()
      
      
def import_modules_in_ftdconfig(module):
  findallchildern_objecttype(
      topo_obj.prmgensettings.object, "ListItem", module, "Click",
      f"{module} was Clicked.", f"{module} was not found in window"
    )
  find_and_click_button(topo_obj.prmgensettings.object, "->")
    
def click_button_in_fdtconfig(button):
  find_and_click_button(topo_obj.fdtconfigurationwindowtextbox.object, button)
  topo_obj.fdtconfigurationwindowtextbox.object.Close()
  
def click_dtm_channel_in_fdtconfig(prop):
  findallchildern_objecttype(
      topo_obj.fdtconfigurationwindowtextbox.object, "OutlineItem", prop, "Click",
      f"{prop} was clicked.", f"{prop} was not found in window"
    )
    
def select_tab_in_FDTConfig(tab_name):
  findallchildern_objecttype(
        topo_obj.fdtconfigurationwindowtextbox.object, "PageTab", tab_name, "Click",
        f"{tab_name} was clicked.", f"{tab_name} was not found in window"
      )
      
def update_ip_address_in_fdtconfig(new_ip):
  for ip in topo_obj.prmgensettings.object.FindAllChildren("WndClass", "SysIPAddress32", 100):
    if ip.wAddress =='192.168.10.3' and ip.Enabled:
      Log.Message(f"Current IP Address: {ip.Value}")
      ip.Value = new_ip
      Log.Checkpoint(f"IP Address updated to: {new_ip}")
      return
  Applicationutility.take_screenshot()
  Log.Error("IP Address field not found.")
  
def click_icon_on_refine_online(icon):
  for btn in sp_obj.advancesettingswindowspbutton.object.FindAllChildren("ClrClassName", "ContentPresenter", 100):
    if btn.ToolTip == icon:
      btn.click()
      Log.Checkpoint(f'{icon} was clicked in Refine Online Window')
      return
  Applicationutility.take_screenshot()
  Log.Error(f"{icon} Not Found on Refine Online Window")
  
def select_checkbox_in_updateproject(prop):
  for check in topo_obj.updateprojecttab.object.FindAllChildren("ClrClassName", "CheckBox", 100):
    if check.DataContext.Name == prop:
      check.click()
      Log.Checkpoint(f'{prop} check box clicked in Update Project window')
      return
  Applicationutility.take_screenshot()
  Log.Error(f'{prop} Not Found in Update Project Window')

def Right_Click_ProjectBrowser(item):
  findallchildern_objecttype(
      cur_obj.projectbrowserwindow.object, "OutlineItem", item, "ClickR",
      f"Right-clicked on item: {item}", f"Item with caption '{item}' not found."
    )
    
def Select_Tab_in_Project_Properties(item):
  findallchildern_objecttype(
        con_obj.okmodaldialoguewindowce.object, "PageTab", item, "Click",
        f"Clicked on item: {item}", f"Item with caption '{item}' not found."
      )
      
def Set_Password_for_Firmware(oldpassword, newpassword):
  fields = {1: oldpassword, 2: newpassword, 3: newpassword}
  for i in con_obj.okmodaldialoguewindowce.object.FindAllChildren("WndClass", "Edit", 100):
    index = next((k for k, v in fields.items() if i.Name == f'Window("Edit", "", {k})'), None)
    if index:
      i.SetText(fields[index])
      Log.Checkpoint(f'{fields[index]} entered in Password Text Box {index}')
  if not any(i.Name == f'Window("Edit", "", {idx})' for idx in fields):
    Applicationutility.take_screenshot()
    Log.Error("One or more password fields not found")