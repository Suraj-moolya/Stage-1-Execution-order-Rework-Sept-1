"Control Expert Utility"

from RefineOffline import RefineOffline
from MessageBox import MessageBox
import Applicationutility
from CurrentScreen import CurrentScreen
from DialogCE import DialogCE    
from ControlExpert import ControlExpert  
from ProjectExplorerTab import ProjectExplorerTab
from TopologyExplorerTab import TopologyExplorerTab
from GlobalTemplatesTab import GlobalTemplatesTab
from EngineeringClient import EngineeringClient

diace_obj = DialogCE()
ce_obj = ControlExpert()
cs_obj = CurrentScreen()
msg_obj = MessageBox()
refoff_obj = RefineOffline()
proj_obj = ProjectExplorerTab()
topoexo_obj = TopologyExplorerTab()
globaltemp_obj=GlobalTemplatesTab()
eng_obj = EngineeringClient()

###############################################################################
# Function: select_main_folder_project_browser_CE
# Description: Selects the main folder in the project browser of Control Expert.
# Parameter: None
###############################################################################
def select_main_folder_project_browser_CE():
    project_browser = refoff_obj.projectbrowserrotextbox.object
    project_browser.wItems.Item[0].Select()
    Applicationutility.wait_in_seconds(1000, 'Wait')

###############################################################################
# Function: select_project_browser_item_CE
# Description: Selects a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be selected.
# Example: select_project_browser_item_CE("MainFolder")
###############################################################################
def select_project_browser_item_CE(val):
    project_browser = refoff_obj.projectbrowserrotextbox.object
    count = project_browser.wItemCount
    for i in range(count):
      if len(val) != 1:
        if val in str(project_browser.wItem[i]):
            project_browser.SelectItem(project_browser.wItem[i])
#            Log.Message(project_browser.wItem[i] + 'is selected')
            break
      else:
        if val in str(project_browser.wItem[i]):
          project_browser.SelectItem(val)
          break
    else:
        Log.Error(val + ' is not selected')

###############################################################################
# Function: doubleclick_project_browser_item_CE
# Description: Double-clicks a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be double-clicked.
# Example: doubleclick_project_browser_item_CE("SubFolder")
###############################################################################
def doubleclick_project_browser_item_CE(val):
    project_browser = refoff_obj.projectbrowserrotextbox.object
    count = project_browser.wItems.Item[0].Items.Count
    for i in range(count + 1):
      if len(val) != 1:
        if val in project_browser.wItem[i]:
            project_browser.DblClickItem(project_browser.wItem[i])
#            Log.Message(project_browser.wItem[i] + 'is selected' )
            break
      else:
        if val in project_browser.wItem[i]:
            project_browser.DblClickItem(val)
#            Log.Message(project_browser.wItem[i] + 'is selected' )
            break
        
    else:
        Log.Error(val + ' is not Click')

###############################################################################
# Function: rightclick_project_browser_item_CE
# Description: Right-clicks a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be right-clicked.
# Example: rightclick_project_browser_item_CE("SubFolder")
###############################################################################
def rightclick_project_browser_item_CE(val):
    project_browser = refoff_obj.projectbrowserrotextbox.object
    count = project_browser.wItems.Item[0].Items.Count
    for i in range(count):
        if val in project_browser.wItem[i]:
            project_browser.ClickItemR(val)
            break
    else:
        Log.Error(val + ' is not selected')

###############################################################################
# Function: maximize_window_CE
# Description: Maximizes the currently active window in Control Expert.
# Parameter: None
###############################################################################
def maximize_window_CE():
    try:
        Applicationutility.wait_in_seconds(2000, 'Wait')
        win = refoff_obj.mdiwindowtextbox.object
        win.Maximize()
    except:
        Log.Warning('No Window to Maximize')

###############################################################################
# Function: double_click_selected_project_browser_item_CE
# Description: Navigates through a hierarchy of items in the project browser and double-clicks the last item.
# Parameter: param (str) - A string of items separated by "$$", representing the hierarchy.
# Example: double_click_selected_project_browser_item_CE("MainFolder$$SubFolder$$Item")
###############################################################################
def double_click_selected_project_browser_item_CE(param):
    selection_items_list = param.split('$$')
    select_main_folder_project_browser_CE()
    max = len(selection_items_list)
    for i in range(max):
        if i != (max - 1):
            select_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(500, 'wait')
        else:
            doubleclick_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(1500, 'wait')
            maximize_window_CE()
            Applicationutility.wait_in_seconds(2000, 'wait')
            
###############################################################################
# Function: Right_click_selected_project_browser_item_CE
# Description: Navigates through a hierarchy of items in the project browser and right-clicks the last item.
# Parameter: param (str) - A string of items separated by "$$", representing the hierarchy.
# Example: Right_click_selected_project_browser_item_CE("MainFolder$$SubFolder$$Item")
###############################################################################
def Right_click_selected_project_browser_item_CE(param):
    selection_items_list = param.split('$$')
    select_main_folder_project_browser_CE()
    max = len(selection_items_list)
    for i in range(max):
        if i != (max - 1):
            select_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(500, 'wait')
        else:
            rightclick_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(1500, 'wait')
###############################################################################
# Function: rclick_window_CE
# Description: Performs a right-click action on the center of the active window and interacts with various UI elements.
# Parameter: None
###############################################################################
def rclick_window_CE(): 
    win = refoff_obj.mdiwindowtextbox.object
    win.ClickR((win.Width/2)-100, win.Height/2)
    
    data_selection = refoff_obj.dataselectiontextbox.object
    data_selection.Click()
    
    comb = refoff_obj.windowcomboboxtextbox.object
    comb.Keys('XOR')
    comb.Keys('[Enter]')
    #Topologyexplorerutility.modaldialogue_window_ce("Yes")
    win.Click((win.Width/2)-100, win.Height/2)
    win.Keys('[Esc]')
    win1 = refoff_obj.fbdsectionwindowtextbox.object 
    Applicationutility.wait_in_seconds(1500, 'wait')
    win1.TextObject("IN2").DblClick()
    comb.Keys('Int2')
    comb.Keys('[Enter]')
    Applicationutility.wait_in_seconds(1000, 'wait')
    Sys.Keys('[Enter]')
    Applicationutility.wait_in_seconds(1000, 'wait') 
    win1.TextObject("OUT").DblClick()
    comb.Keys('Int3')
    comb.Keys('[Enter]')
    Applicationutility.wait_in_seconds(1000, 'wait')
    Sys.Keys('[Enter]')
    Applicationutility.wait_in_seconds(1000, 'wait')

###############################################################################
# Function: RClick_on_Block_Refine_Offline
# Description: Right-clicks on a specific block in the Refine Offline window based on its identifier.
# Parameter: identifier (str) - The text identifier of the block to be right-clicked.
# Example: RClick_on_Block_Refine_Offline("BlockName")
###############################################################################
def RClick_on_Block_Refine_Offline(identifier):  
    Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Error("No blocks found in the Refine Offline window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text and Window_Text.Visible:
            Window_Text.ClickR()
            Log.Message(Window_Text.Text + ' is Right Clicked.')
            break
    else:
        Log.Error(Window_Text.Text + ' is not visible in the Window')
        
def Right_Click_Instance_in_FBDRefine(instance):
  for item in refoff_obj.fbdsectionwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000):
    if item.Text == instance:
      item.ClickR()
      Log.Checkpoint(f'Right Clicked On Instance {item.Text}')
      break
  else:
    Log.Error(f'Instance "{instance}" not found')
    
def Delete_Instance_in_Refine(instance):
  for item in refoff_obj.fbdsectionwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000):
    if item.Text == instance:
      item.Click()
      Sys.Keys("[Del]")
      Log.Checkpoint(f'{item.Text} Deleted')
      break
  else:
    Log.Error(f'Instance "{instance}" not found')    
        
  
###############################################################################
# Function: Unlock_Dialog_popup
# Description: Interacts with the "Unlock" dialog popup and clicks a specified button.
# Parameter: button_name (str) - The name of the button to be clicked.
# Example: Unlock_Dialog_popup("Yes")
###############################################################################
def Unlock_Dialog_popup(button_name):
    obj = Sys.Process("ControlExpert", 4).Dialog("Unlock")
    buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
    for button in buttons_list:
        if button_name in str(button.WndCaption):
            button.click()
            Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
            break
    else:
        Log.Error(f"Button name {button_name} mentioned doesnt exists")

###############################################################################
# Function: Delete_link_Refine_Offline
# Description: Deletes a link in the Refine Offline window based on its identifier.
# Parameter: identifier (str) - The text identifier of the link to be deleted.
# Example: Delete_link_Refine_Offline("LinkName")
###############################################################################
def Delete_link_Refine_Offline(identifier):
    Window = refoff_obj.mdiwindowtextbox.object
    Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
    if not Window_lst:
        Log.Error("No links found in the Refine Offline window.")
        return
    for obj in Window_lst:
        if identifier in obj.Text:
            Window.Click(obj.Left+50+obj.Width, obj.Top+40+(obj.Height/2))
            Delay(1000)
            Sys.Keys("[Del]")

###############################################################################
# Function: Consistency_Check_Select_All
# Description: Selects all items in the consistency check popup by interacting with the "Check/Uncheck All" checkbox.
# Parameter: None
###############################################################################
def Consistency_Check_Select_All():
    headers = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
    buttons_list = headers[0].FindAllChildren('ClrClassName', 'CheckBox', 1000)
    if buttons_list:
      for button in buttons_list:
        if "Check/Uncheck All" == button.ToolTip.Content.OleValue:
            button.IsChecked = True
            Log.Message('Select all button is Checked')  
            Applicationutility.take_screenshot()     
            break
        else:
            Log.Message(str(button.WPFControlText) + " button is Enabled")
    else:
      Log.Error("No consistency check popup.")
        
###############################################################################
# Function: Verify_modifications_available_in_Refine_Offline
# Description: Verifies if a specific block is available in the Refine Offline window.
# Parameter: identifier (str) - The text identifier of the block to be verified.
# Example: Verify_modifications_available_in_Refine_Offline("BlockName")
###############################################################################
def Verify_modifications_available_in_Refine_Offline(identifier):        
    Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Error("No blocks found in the Refine Offline window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text:
            Log.Checkpoint(Window_Text.Text + " block is available")
            break
    else: 
        Log.Error(identifier + " block is not available")

###############################################################################
# Function: RClick_on_filter_Refine_Offline
# Description: Right-clicks on the filter button in the Refine Offline window.
# Parameter: None
###############################################################################
def RClick_on_filter_Refine_Offline(): 
    Button = refoff_obj.mdiwindowtextbox.object.FindChild("ClassName", "CDFIButton", 1000)
    Button.ClickR()

###############################################################################
# Function: Select_Column_Configuration
# Description: Selects a specific column configuration in a dialog window based on its identifier.
# Parameter: identifier (str) - The text identifier of the column to be selected.
# Example: Select_Column_Configuration("ColumnName")
###############################################################################
def Select_Column_Configuration(identifier):
    Window = refoff_obj.parentdialogwindowce.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Error("No columns found in the dialog window.")
        return
    for obj in Window:
        if identifier in obj.Text:
            Window.Click(obj.Left-50+obj.Width, obj.Top+40+(obj.Height/2))
            Log.Message(obj.Text + " is selected")

###############################################################################
# Function: Add_variable_name_in_name_column
# Description: Adds a variable name in the "Name" column of a grid.
# Parameter: var_name (str) - The variable name to be added.
# Example: Add_variable_name_in_name_column("Variable1")
###############################################################################
def Add_variable_name_in_name_column(var_name):
    Delay(3000)
    for i in range(10):
        Sys.Keys("[Down]")
    Sys.Keys("[Enter]")
    Sys.Keys(var_name)
    Sys.Keys("[Enter]")

###############################################################################
# Function: click_on_elipsis
# Description: Simulates a click on the ellipsis button in the UI.
# Parameter: None
###############################################################################
def click_on_elipsis():
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")

###############################################################################
# Function: select_variable_type_Dialog_popup_CE
# Description: Selects a variable type in a dialog popup and confirms the selection.
# Parameter: None
###############################################################################
def select_variable_type_Dialog_popup_CE():
    Delay(3000,"Wait")
    Click_button_Dialog_popup_CE("REF_TO")
    Click_button_Dialog_popup_CE("OK")

###############################################################################
# Function: Click_button_Dialog_popup_CE
# Description: Clicks a specified button in a dialog popup.
# Parameter: button_name (str) - The name of the button to be clicked.
# Example: Click_button_Dialog_popup_CE("OK")
###############################################################################
def Click_button_Dialog_popup_CE(button_name):
    obj = Sys.Process("ControlExpert", 4).Dialog("*")
    buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
    for button in buttons_list:
        if button_name in str(button.WndCaption):
            button.Click()
            Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
            break
    else:
        Log.Error(f"Button name {button_name} mentioned doesnt exists")

###############################################################################
# Function: select_variable_type
# Description: Selects a variable type from a dropdown menu.
# Parameter: val (str) - The variable type to be selected.
# Example: select_variable_type("Int")
###############################################################################
def select_variable_type(val):
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Sys.Keys(val)
    Sys.Keys("[Enter]") 

###############################################################################
# Function: select_Constant_check_box
# Description: Selects the "Constant" checkbox in the UI.
# Parameter: None
###############################################################################
def select_Constant_check_box():
    Delay(3000)
    for i in range(10):
        Sys.Keys("[Right]")
        Delay(500)
    Delay(1000)
    Sys.Keys("[Enter]")

###############################################################################
# Function: Enter_P2P_in_Custom_box
# Description: Enters "P2P" in a custom input box.
# Parameter: None
###############################################################################
def Enter_P2P_in_Custom_box():
    Delay(3000)
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Sys.Keys("P2P")
    Sys.Keys("[Enter]")  

###############################################################################
# Function: select_AdvSettings_properties_SVP
# Description: Selects advanced settings properties in the supervision project or AVEVA.
# Parameter: param (str) - A string in the format "parent$$val$$val1".
# Example: select_AdvSettings_properties_SVP("supervision project$$MainFolder$$SubFolder")
###############################################################################
def select_AdvSettings_properties_SVP(param):
    parent,val,val1 = param.split('$$')

    if parent.lower() == "supervision project":
        project_browser = refoff_obj.projectbrowserrotextbox.object
    elif parent.lower() == "aveva":
        project_browser = aveva_obj.systreeviewtextbox.object
    else:
        Log.Error("Invalid parent passed") 

    project_browser.wItems.Item[0].Select()
    count = project_browser.wItemCount 
    Log.Message(str(count) + ' PB count')
    for i in range(count):
        if val in project_browser.wItem[i]:
            project_browser.SelectItem(val)
            Log.Message(val + " is selected")
            Applicationutility.wait_in_seconds(1500, 'wait')
            count1 = project_browser.wItems.Item[0].Items.Item[i].Items.Count
            for j in range(count1):
                if val1 in project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Text:
                    project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Select()
                    Log.Message(val1 + " is selected")
                    break
            break  
    else:
        Log.Error('Unable to pass the value')

###############################################################################
# Function: Edit_Parameter_Value_AdvSettings_SVP
# Description: Edits the parameter value in advanced settings.
# Parameter: val (str) - The value to be entered.
# Example: Edit_Parameter_Value_AdvSettings_SVP("NewValue")
###############################################################################
def Edit_Parameter_Value_AdvSettings_SVP(val): 
    obj_Parent = Sys.Process("EngineeringClient")
    obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
    Top = obj_value.Top
    value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
    for value in value_field:
        Sys.HighlightObject(value,1)
        if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10:
            value.wText = val
            if value.wText == val:
                Log.Checkpoint(f" {value.wText} is entered")
            else:
                Log.Error(f'{Val} is not entered')
                Applicationutility.take_screenshot()
            break

###############################################################################
# Function: Verify_Parameter_Value_AdvSettings_SVP
# Description: Verifies the parameter value in advanced settings.
# Parameter: param (str) - A string in the format "parent$$val".
# Example: Verify_Parameter_Value_AdvSettings_SVP("supervision project$$ExpectedValue")
###############################################################################
def Verify_Parameter_Value_AdvSettings_SVP(param): 
    parent,val = param.split('$$')

    if parent.lower() == "supervision project":
        obj_Parent = Sys.Process("EngineeringClient")
    elif parent.lower() == "aveva":
        obj_Parent = aveva_obj.mainparenttextbox.object
    else:
        Log.Error("Invalid parent passed") 

    obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
    Top = obj_value.Top
    value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
    for value in value_field:
        Sys.HighlightObject(value,1)
        if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10:
            if str(value.wText) == str(val):
                Log.Checkpoint(value.wText + " is updated") 
                break
            else:
                Log.Error(val + " updated value is incorrect")

###############################################################################
# Function: drag_instance_drop_container_page_SP
# Description: Drags an instance and drops it onto the container page.
# Parameter: template (str) - The name of the template to be dragged.
# Example: drag_instance_drop_container_page_SP("TemplateName")
###############################################################################
def drag_instance_drop_container_page_SP(template):
    template_list = proj_obj.containerpagedocktextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if not template_list:
        Log.Error("No templates found in the container page.")
        return
    Workspace_editor = proj_obj.mdiclientwindowtextbox.object
    tox = Workspace_editor.ScreenLeft+10
    Applicationutility.wait_in_seconds(5000, 'Wait')
    for i in range(len(template_list)):
        if template_list[i].Visible: 
            Sys.HighlightObject(template_list[i],1)
            if template == str(template_list[i].DataContext.Identifier.OleValue):
                fromx = template_list[i].Width/2
                fromy = template_list[i].Height/2
                Log.Message('The object selected to drag is : ' + str(template_list[i].DataContext.Identifier.OleValue))
                Applicationutility.wait_in_seconds(2000, 'Wait')
                template_list[i].Click()
                Applicationutility.wait_in_seconds(2000, 'Wait')
                template_list[i].Drag(fromx-70, fromy, tox+100, 0)
                Applicationutility.wait_in_seconds(2000, 'Wait')
                break

###############################################################################
# Function: select_value_listview_SVP
# Description: Selects a value from a list view in the supervision project.
# Parameter: val (str) - The value to be selected.
# Example: select_value_listview_SVP("ValueName")
###############################################################################
def select_value_listview_SVP(val):
    list_items = proj_obj.listviewtextbox.object.FindAllChildren('ClrClassName', 'ListViewItem', 100)  
    if not list_items:
        Log.Error("No items found in the list view.")
        return
    for list in list_items:
        if list.DataContext.Identifier.OleValue == val:
            Applicationutility.wait_in_seconds(1000, 'Wait')
            list.Click()
            Applicationutility.wait_in_seconds(2000, 'Wait')
            break
        else:
          Log.Message(f'{list.DataContext.Identifier.OleValue} is present')
    else:
      Log.Error(f'The value {val} is not present in list')
      
###############################################################################
# Function: Double_click_on_header_OC
# Description: Double-clicks on a specific header in the Operation Client.
# Parameter: None
###############################################################################
def Double_click_on_header_OC():
    identifier = "Process Expert"
    parent = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
    object = parent.FindAllChildren("ClrClassName", "TextBlock", 1000)
    for obj in object:
        if identifier in obj.WPFControlText:      
            obj.DblClick() 
            Delay(2000)
            Log.Message("Double clicked")

###############################################################################
# Function: Verify_screen_visible
# Description: Verifies if a specific screen is visible in the Operation Client.
# Parameter: None
###############################################################################
def Verify_screen_visible():
    obj2 = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
    if obj2.VisibleOnScreen:
        Log.Message("Visible On Screen")
    else:
        Log.Error("Not Visible On Screen")  

###############################################################################
# Function: Verify_variable_is_removed_Refine_Offline
# Description: Verifies if a specific variable is removed in the Refine Offline window.
# Parameter: var_name (str) - The name of the variable to be verified.
# Example: Verify_variable_is_removed_Refine_Offline("Variable1")
###############################################################################
def Verify_variable_is_removed_Refine_Offline(var_name):
    var_name = "V1" 
    variables = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 100)
    if not variables:
        Log.Error("No variables found in the Refine Offline window.")
        return
    for var in variables:
        if var.Text == var_name:
            Log.Warning(var.Text + " is not removed")
            break
    else:
        Log.Checkpoint(var_name + " is removed")

###############################################################################
# Function: edit_IP_Address
# Description: Edits the IP address of a specific object in the Refine Offline window.
# Parameter: param (str) - A string in the format "Identifier$$value".
# Example: edit_IP_Address("Device1$$192.168.1.1")
###############################################################################
def edit_IP_Address(param):
    Identifier, value = param.split('$$')
    obj = refoff_obj.mdiwindowtextbox.object.FindAllChildren("ObjectType","IpAddress",100)
    if not obj:
        Log.Error("No IP address objects found.")
        return
    for IP_obj in obj:
      if IP_obj.Enabled:
        Sys.HighlightObject(IP_obj, 10)
        if str(IP_obj.ObjectIdentifier) == Identifier:
            IP_obj.wAddress = value
            aqObject.CheckProperty(IP_obj, "wAddress", cmpEqual, value)
            break
    else: 
        Log.Error(Identifier + " is not updated - IP : " + IP_obj.wAddress)

###############################################################################
# Function: Verify_Mapped_DTM_device_present_CE
# Description: Verifies if a specific DTM device is present in the Control Expert topology explorer.
# Parameter: Identifier (str) - The identifier of the DTM device.
# Example: Verify_Mapped_DTM_device_present_CE("Device1")
###############################################################################
def Verify_Mapped_DTM_device_present_CE(Identifier):
    objects = topoexo_obj.dtmbrowserprop.object.FindAllChildren("ObjectType","OutlineItem",200)
    if not objects:
        Log.Error("No DTM devices found in the topology explorer.")
        return
    for obj in objects:
        if Identifier in str(obj.ObjectIdentifier):
            Log.Checkpoint(str(obj.ObjectIdentifier) + " DTM device added")
            break
    else:
        Log.Error(Identifier + " DTM device not added")

###############################################################################
# Function: Dblclick_dialog_panel_item_CE
# Description: Double-clicks a specific item in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be double-clicked.
# Example: Dblclick_dialog_panel_item_CE("ItemName")
###############################################################################
def Dblclick_dialog_panel_item_CE(param):
    panel_child = diace_obj.dialogpanelcetextbox.object.FindAllChildren('Text', '*', 100)
    if not panel_child:
        Log.Error("No items found in the dialog panel.")
        return
    for item in panel_child:
        if param == item.Text:
            item.DblClick()
            Log.Checkpoint(item.Text + ' is Double Clicked.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else:
        Log.Error(param + ' not found.')    

###############################################################################
# Function: Click_dialog_panel_item_CE
# Description: Clicks a specific item in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be clicked.
# Example: Click_dialog_panel_item_CE("ItemName")
###############################################################################
def Click_dialog_panel_item_CE(param):
    Applicationutility.wait_in_seconds(1000, 'Wait')
    panel_child = diace_obj.dialogpanelcetextbox.object.FindAllChildren('Text', '*', 100)
    if not panel_child:
        Log.Error("No items found in the dialog panel.")
        return
    for item in panel_child:
        if param == item.Text:
            item.Click()
            Log.Checkpoint(item.Text + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else:
        Log.Error(param + ' not found.')  

###############################################################################
# Function: Select_bottom_listitem_dialog_panel_item_CE
# Description: Selects a specific item from the bottom list in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: Select_bottom_listitem_dialog_panel_item_CE("ItemName")
###############################################################################
def Select_bottom_listitem_dialog_panel_item_CE(param):
    io_device = diace_obj.dialoglistboxcetextbox.object 
    if io_device.wItemCount == 0:
        Log.Error("No items found in the bottom list.")
        return
    for i in range(io_device.wItemCount):
        if param in io_device.wItem[i]:
            io_device.ClickItem(i)
            Log.Message(io_device.wItem[i] + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else: 
        Log.Error(param + ' not found.')

###############################################################################
# Function: Rclick_Drops_EIO_add_new_device_CE
# Description: Right-clicks on the EIO drops section and adds a new device in Control Expert.
# Parameter: None
###############################################################################
def Rclick_Drops_EIO_add_new_device_CE():
  obj = refoff_obj.fbdsectionwindowtextbox.object
  obj.ClickR((obj.Width*.04), (obj.Height*.12))
  ce_obj.newdevicecetextbox.click()

###############################################################################
# Function: Select_bottom_listitem_EIO_dialog_panel_item_CE
# Description: Selects a specific item from the bottom list in the EIO dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: Select_bottom_listitem_EIO_dialog_panel_item_CE("ItemName")
###############################################################################
def Select_bottom_listitem_EIO_dialog_panel_item_CE(param):
    io_device = diace_obj.dialoglistboxce1textbox.object.FindAllChildren('Text', '*')
    if not io_device:
        Log.Error("No items found in the EIO dialog panel.")
        return
    for item in io_device:
        if param in item.Text:
            item.Click()
            Log.Message(item.Text + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else: 
        Log.Error(param + ' not found.')

###############################################################################
# Function: select_PLC_bus_combobox_item_CE
# Description: Selects a specific item from the PLC bus combobox in Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: select_PLC_bus_combobox_item_CE("BusName")
###############################################################################
def select_PLC_bus_combobox_item_CE(param):
    obj = refoff_obj.windowcomboboxtextbox.object
    for _ in range(len(obj.wItemList)):
        if param in obj.wItemList and obj.Visible:
            obj.ClickItem(param)
            Applicationutility.wait_in_seconds(1000, 'Wait')
            Log.Checkpoint(f'{obj.wText} is selected.')
            break
    else:
        Log.Error(f'{param} is not present in combobox.')
    ce_obj.yescebuttonbutton.click()
    Applicationutility.wait_in_seconds(1000, 'Wait')
    ce_obj.yescebuttonbutton.click()

###############################################################################
# Function: create_logical_network
# Description: Creates a logical network by interacting with the controller properties in the topology explorer.
# Parameter: None
###############################################################################
def create_logical_network():
    controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
    for control in controller_row:
        if getattr(getattr(control, "DataContext", None), "DisplayName", None) == "Controller":
            control.Click()
            aqUtils.Delay(500)
            for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10):
                if item.WPFControlText == "False":
                    item.Click() if item.Enabled else Log.Error("Dropdown item 'False' is disabled.")
                    return
    Log.Error("Could not find the specific 'Controller' element.")

###############################################################################
# Function: Click_tab_item_EIO_config_window
# Description: Clicks on a specific tab item in the EIO configuration window.
# Parameter: identifier (str) - The name of the tab to be clicked.
# Example: Click_tab_item_EIO_config_window("TabName")
###############################################################################
def Click_tab_item_EIO_config_window(identifier):
    Window = proj_obj.mdiclientwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Error("No tab items found in the EIO configuration window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text:
            Window_Text.Click()
            Log.Checkpoint(Window_Text.Text + " is Clicked")
            break
    else: 
        Log.Error(identifier + " is not available")

###############################################################################
# Function: Add_Vairable_Logic_Block_link_P2P
# Description: Adds a variable to a logic block link in the P2P configuration.
# Parameter: param (str) - A string in the format "identifier$$variable".
# Example: Add_Vairable_Logic_Block_link_P2P("BlockName$$VariableName")
###############################################################################
def Add_Vairable_Logic_Block_link_P2P(param):
    identifier , variable = param.split("$$")
    Window = proj_obj.mdiclientwindowtextbox.object
    Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
    if not Window_lst:
        Log.Error("No logic blocks found in the P2P configuration.")
        return
    for obj in Window_lst:
        if identifier in obj.Text and obj.Visible:
            obj.DblClick()
            Sys.Keys(variable)
            Sys.Keys("[Enter]")
            Log.Checkpoint(obj.Text + " is Double Clicked")
            break
    else:
        Log.Error(identifier + " is not available")

###############################################################################
# Function: change_Port_Number_PLC_Simulator
# Description: Changes the port number in the PLC simulator.
# Parameter: None
###############################################################################
def change_Port_Number_PLC_Simulator():
    Simulator_Textbox = diace_obj.simulatorporttextbox.object
    Simulator_Textbox.SetText("503")
    
def change_Port_Number_in_PLC_Simulator(port):
    Simulator_Textbox = diace_obj.simulatorporttextbox.object
    Simulator_Textbox.SetText(port)

###############################################################################
# Function: click_MenuItem_Toolbar_CE
# Description: Clicks a specific menu item in the toolbar of Control Expert.
# Parameter: menu_option (str) - The name of the menu option to be clicked.
# Example: click_MenuItem_Toolbar_CE("OptionName")
###############################################################################
def click_MenuItem_Toolbar_CE(menu_option):
    menu_items = ce_obj.modaldialogewindowoptionsce.object.FindAllChildren('ObjectType', 'MenuItem', 1000)
    for item in menu_items:
        if menu_option in str(item.ObjectIdentifier):
            item.click()
            break

###############################################################################
# Function: Select_network_CE
# Description: Selects a specific network in the Control Expert network configuration.
# Parameter: menu_option (str) - The name of the network to be selected.
# Example: Select_network_CE("NetworkName")
###############################################################################
def Select_network_CE(menu_option):
    menu_items = ce_obj.okmodaldialoguewindowce.object.FindChild('wText', 'No Selection', 10)
    menu_items.ClickItem(menu_option)
    Log.Message(menu_items.wText + " is selected")

###############################################################################
# Function: Click_ok_button_add_network_popup_CE
# Description: Clicks the "OK" button in the add network popup of Control Expert.
# Parameter: button (str) - The name of the button to be clicked.
# Example: Click_ok_button_add_network_popup_CE("OK")
###############################################################################
def Click_ok_button_add_network_popup_CE(button):
    try:
        menu_item = ce_obj.okmodaldialoguewindowce.object.FindChild(
            ('WndClass', 'WndCaption'), ('Button', button), 10)

        if menu_item is not None:
            menu_item.Click()
            Log.Checkpoint(f"'{button}' button is clicked.")
        else:
            Log.Error(f"Button with caption '{button}' not found in the OK modal dialog.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while clicking '{button}' button: {str(e)}")


###############################################################################
# Function: select_item_mdi_window_CE
# Description: Selects a specific item in the MDI window of Control Expert.
# Parameter: identifier (str) - The name of the item to be selected.
# Example: select_item_mdi_window_CE("ItemName")
###############################################################################
def select_item_mdi_window_CE(identifier):        
    menu_items = refoff_obj.mdiwindowtextbox.object.FindAllChildren('WndClass', 'ComboBox',20)
    for item in menu_items:
        if identifier in str(item.wItemList): 
            item.ClickItem(identifier)
            Log.Message(item.wText + " is selected")
            break
    else:
        Log.Error(identifier + " is not selected")
        
###############################################################################
# Function   : Click_on_a_text_object_block_Refine_Offline
# Description: Clicks on a text object block in the Refine Offline window.
# Parameter  : identifier (str) - Text to identify the target block.
# Example    : Click_on_a_text_object_block_Refine_Offline("Channel 1")
###############################################################################       
def Click_on_a_text_object_block_Refine_Offline(identifier):  
    Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Warning("No blocks found in the Refine Offline window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text and Window_Text.Visible:
            Window_Text.Click()
            Log.Message(Window_Text.Text + ' is Clicked.')
            break
    else:
        Log.Message(Window_Text.Text + ' is not visible in the Window')

###############################################################################
# Function   : verify_module_in_add_device_window_CE
# Description: Verifies if a given module exists in the "Add Device" window 
#              of Control Expert.
# Parameter  : module (str) - Name of the module to verify.
# Example    : verify_module_in_add_device_window_CE("I/O Expansion Module")
###############################################################################              
def verify_module_in_add_device_window_CE(module):
  window = ce_obj.okmodaldialoguewindowce.object
  devices = window.FindAllChildren('Name', 'TextObject("*")',50)
  for i in devices:
    if i.Text == module:
      Log.Checkpoint(f'The {module} exists in the window')
      break     
  else:
    Log.Checkpoint(f'The {module} does not exists in the window')

###############################################################################
# Function: enter_language_new_section_pop_up
# Description: Opens the language selection dropdown in the New Section Modal 
#             Dialogue Window in refine offline by clicking on the ComboBox element.
# Parameters: None
# Example: enter_language_new_section_pop_up()
###############################################################################
def enter_language_new_section_pop_up():
    try:
        new_sec_items = ce_obj.okmodaldialoguewindowce.object.FindAllChildren('WndClass', 'ComboBox', 20)
        if new_sec_items:
            for item in new_sec_items:
                item.click()
                Log.Checkpoint("Language dropdown clicked in Control Expert Modal Dialogue Window.")
                break
        else:
            Log.Error("No ComboBox items found in Control Expert Modal Dialogue Window.")
    except Exception as e:
        Log.Error(f"Error while clicking language dropdown: {str(e)}")

###############################################################################
# Function: select_language_newSection
# Description: Selects the specified language from the dropdown list in the 
#              New Section Modal Dialogue Window in refine offline.
# Parameters: value (str) - The language to be selected from the dropdown.
# Example: select_language_newSection("English")
###############################################################################
def select_language_newSection(value):
    try:
        enter_language_new_section_pop_up()
        dropdown_lst = refoff_obj.NewSectiondropdown.object.FindAllChildren("ObjectType", "ListItem", 10)
        if dropdown_lst:
            for opt in dropdown_lst:
                if value in opt.ObjectIdentifier:
                    opt.Click()
                    Log.Checkpoint(f"'{value}' was successfully selected in Control Expert Modal Dialogue Window.")
                    return
            Log.Error(f"Option '{value}' not found in the language dropdown.")
        else:
            Log.Error("No items found in language dropdown.")
    except Exception as e:
        Log.Error(f"Error while selecting language '{value}': {str(e)}")


###############################################################################
# Function: enter_name_new_section
# Description: Enters the specified name into the Edit field of the 
#              New Section Modal Dialogue Window in refine offline.
# Parameters: value (str) - The name to be entered into the Edit field.
# Example: enter_name_new_section("SectionName")
###############################################################################
def enter_name_new_section(value):
    try:
        name_sec_items = ce_obj.okmodaldialoguewindowce.object.FindAllChildren('WndClass', 'Edit', 20)
        if name_sec_items:
            for item in name_sec_items:
                item.wText = value
            Log.Checkpoint(f"Entered name '{value}' in Control Expert Modal Dialogue Window.")
        else:
            Log.Error("No Edit fields found to enter the section name.")
    except Exception as e:
        Log.Error(f"Error while entering name '{value}': {str(e)}")

###############################################################################
# Function: create_new_section
# Description: Creates a new section in the Control Expert application by 
#              entering the section name, selecting the language, and clicking 
#              the OK button. Verifies whether the section is successfully created.
# Parameters: param (str) - A string containing section name and language 
#              separated by '$$' (e.g., "SectionName$$English").
# Example: create_new_section("MyNewSection$$English")
###############################################################################
def create_new_section(param):
    try:
        name_value, dropdown_value = param.split('$$')
        
        # Enter the section name
        enter_name_new_section(name_value)
        
        # Select the language
        select_language_newSection(dropdown_value)
        
        # Click OK button to confirm
        Click_ok_button_add_network_popup_CE("OK")
        Applicationutility.wait_in_seconds(2000, 'Wait')
        
        # Validate the new section creation
        title_lst = refoff_obj.NewSectionModelWindow.object.FindAllChildren('ObjectType', 'TitleBar', 20)
        if title_lst:
            title_value = title_lst[0].value
            if name_value in title_value:
                Log.Checkpoint(f"New section '{name_value}' created successfully in Refine Offline.")
            else:
                Log.Error(f"Section name '{name_value}' was not found in the TitleBar. Actual title: '{title_value}'.")
        else:
            Log.Error("TitleBar not found in New Section Model Window after creation.")
    
    except ValueError:
        Log.Error(f"Invalid parameter format: '{param}'. Expected format 'SectionName$$Language'.")
    except Exception as e:
        Log.Error(f"Error while creating new section '{param}': {str(e)}")


###############################################################################
# Function: enter_query_in_move_blocks
# Description: Enters the specified query text into the Move Blocks search field 
#              within the New Section Model Window of Control Expert.
# Parameters: value (str) - The query text to be entered.
# Example: enter_query_in_move_blocks("SearchText")
###############################################################################
def enter_query_in_move_blocks(value):
    move_value,ST_value=value.split('$$')
    try:
        modal_win_lst = proj_obj.mdiclientwindowtextbox.object.FindAllChildren('ObjectType', 'MDIWindow', 20)
        if modal_win_lst:
            for item in modal_win_lst:
                item.click()
                Sys.Keys("^a")
                Sys.Keys("[Del]")
                Sys.Keys(move_value)
                Sys.Keys("[Enter]")
                Sys.Keys(ST_value)
                Log.Checkpoint(f"Entered query '{move_value}' in Move Blocks.")
                return
        else:
            Log.Error("Move Blocks input field not found in New Section Model Window.")
    except Exception as e:
        Log.Error(f"Error while entering query '{move_value}' in Move Blocks: {str(e)}")

###############################################################################
# Function: close_move_block_window
# Description: Closes the Move Blocks window in the New Section Model Window 
#              by clicking the specified button.
# Parameters: None
###############################################################################
def close_move_block_window(value):
    try:
        button_lst = proj_obj.mdiclientwindowtextbox.object.FindAllChildren('ObjectType', 'Button', 20)
        if button_lst:
            for item in button_lst:
                if str(item.ObjectIdentifier) == value:
                    item.click()
                    Log.Checkpoint(f"{value} Button clicked successfully in Move Blocks window.")
                    return
            Log.Error(f"{value} Button not found in Move Blocks window.")
        else:
            Log.Error("No buttons found in Move Blocks window.")
    except Exception as e:
        Log.Error(f"Error while clicking close button in Move Blocks window: {str(e)}")
        
###############################################################################
# Function: right_click_screen_and_select_context_value
# Description: Right-clicks on the first available screen in the New Section 
#              Model Window and selects the specified value from the toolbar menu.
# Parameters: value (str) – The menu item value to select from the toolbar.
###############################################################################
def right_click_screen_and_select_context_value(value):
    try:
        # Find all screen elements
        
        
        screen_value = proj_obj.mdiclientwindowtextbox.object
        screen_lst=screen_value.FindAllChildren('ObjectType', 'MDIWindow', 20)
        

        if screen_lst:
            screen_left = screen_lst[0].ScreenLeft
            screen_top = screen_lst[0].ScreenTop
            screen_height = screen_lst[0].Height
            screen_width = screen_lst[0].Width
        
            absolute_click_x = screen_left + screen_width // 2
            absolute_click_y = screen_top + screen_height - 150
            click_x = absolute_click_x - screen_left
            click_y = absolute_click_y - screen_top
            screen_lst[0].ClickR(click_x, click_y)  # Right-click the first screen
            Log.Message("Right-clicked the first screen successfully.")

            # Call the toolbar menu item click function
            click_MenuItem_Toolbar_CE(value)
            Log.Checkpoint("'{value}' menu item selected successfully from the toolbar.")
        else:
            Log.Error("No screen found in New Section Model Window.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while performing right-click and selecting '{value}': {str(e)}")




def tt():
  right_click_screen_and_select_context_value('FFB')
###############################################################################
# Function: select_input_type_FAB
# Description: Selects the specified input type in the Function Input Assistant 
#              by entering the value into the ComboBox.
# Parameters: value (str) – The input type to enter in the ComboBox.
###############################################################################
def select_input_type_FAB(value):
    try:
        # Find all ComboBox elements inside Function Input Assistant
        input_type_lst = ce_obj.functionInputAssistantType.object.FindAllChildren('WndClass', 'ComboBox', 20)
        
        if input_type_lst:
            input_type_lst[0].Click()  
            Sys.Keys(value)         
            Log.Checkpoint(f"'{value}' successfully entered in the ComboBox.")
        else:
            Log.Error("No ComboBox found in Function Input Assistant.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while selecting input type '{value}': {str(e)}")

###############################################################################
# Function: click_function_assistant_button
# Description: Clicks the specified button inside the Function Input Assistant 
#              window.
# Parameters: button_name (str) – The name of the button to be clicked.
###############################################################################
def click_function_assistant_button(button_name):
  try:
        # Find the button inside Function Input Assistant window
        func_assistant_btn = ce_obj.functionInputAssistantType.object.FindChild(('WndClass', 'WndCaption'),('Button', button_name),20)        
        func_assistant_btn.Click()
        Log.Checkpoint(f"Button '{button_name}' clicked successfully in Function Input Assistant.")
        
  except Exception as e:
        Log.Error(f"Exception occurred while clicking button '{button_name}': {str(e)}")


###############################################################################
# Function: enter_value_in_moveblock
# Description: Enters a specified value into the ComboBox field of the 
#              Move Block window inside the Instance Edit Page tab.
# Parameters: value (str) – The value to be entered into the ComboBox.
###############################################################################
def enter_value_in_moveblock(value):
    try:
        input_lst = proj_obj.instanceeditpagetab.object.FindAllChildren('WndClass', 'ComboBox', 20)
        if input_lst:
          for item in input_lst:
            item.Click()
            Sys.Keys("^a")
            Sys.Keys("[Del]")
            Sys.Keys(value)
            Sys.Keys("[Enter]")
            Log.Checkpoint(f"Value '{value}' entered successfully in ComboBox.")
    except Exception as e:
        Log.Error(f"Failed to enter value '{value}' in ComboBox: {str(e)}")

###############################################################################
# Function: double_click_first_in_block
# Description: Searches for a visible text block in the Instance Edit Page tab 
#              that matches the specified value and performs a double-click on it.
# Parameters: value (str) – The text value to search for in the block.
###############################################################################          
def double_click_first_in_block(value):
    try:
        block_lst = proj_obj.instanceeditpagetab.object.FindAllChildren("Name", "TextObject*", 1000)
        
        if block_lst:
            clicked = False
            for window_text in block_lst:
                if value in window_text.Text and window_text.Visible:
                    window_text.DblClick()
                    Log.Checkpoint(f"Double-clicked on block with text: '{window_text.Text}'")
                    clicked = True
                    break
            
            if not clicked:
                Log.Error("No visible block containing '{value}' found.")
        else:
            Log.Error("No blocks found in instance edit page tab.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while double-clicking on block: {str(e)}")


###############################################################################
# Function: add_move_block
# Description: Adds a new Move Block by performing a sequence of actions 
#              including selecting input type, clicking a button, double-clicking 
#              the block, entering values, and closing the Move Block window.
# Parameters: param (str) – Concatenated parameters separated by '$$' in the 
#                           order: dropdown_value, block_input_value, 
#                           move_block_value, input_value, btn_value.
###############################################################################
def add_move_block(param):
   drp_dwn_value,block_input_value,move_block_value,input_value,btn_value,=param.split('$$')
   right_click_screen_and_select_context_value(drp_dwn_value)
   select_input_type_FAB(block_input_value)
   Applicationutility.wait_in_seconds(1000,'wait for page to load')
   click_function_assistant_button(btn_value)
   screen_lst = proj_obj.mdiclientwindowtextbox.object.FindAllChildren('ObjectType', 'MDIWindow', 20) 
   if screen_lst:   
      screen_left = screen_lst[0].ScreenLeft
      screen_top = screen_lst[0].ScreenTop
      screen_height = screen_lst[0].Height
      screen_width = screen_lst[0].Width
        
      absolute_click_x = screen_left + screen_width // 2
      absolute_click_y = screen_top + screen_height - 250
      
      click_x = absolute_click_x - screen_left
      click_y = absolute_click_y - screen_top 
      screen_lst[0].Click(click_x, click_y)
   double_click_first_in_block(move_block_value)
   enter_value_in_moveblock(input_value)
  

###############################################################################
# Function: edit_move_block
# Description: Edits an existing Move Block by locating the specified block, 
#              updating its value, and closing the Move Block window.
# Parameters: param (str) – Concatenated parameters separated by '$$' in the 
#                           order: move_block_value, input_value.
###############################################################################
def edit_move_block(param):
   move_block_value,input_value=param.split('$$')
   screen_lst = refoff_obj.NewSectionModelWindow.object.FindAllChildren('WndClass', 'AfxFrameOrView140u', 20)  
   if screen_lst:
    screen_lst[0].Click()
   double_click_first_in_block(move_block_value)
   enter_value_in_moveblock(input_value)
   close_move_block_window()
   
###########################################################################################
# Function: right_click_block
# Description: Finds a block within the instance edit page tab whose text matches the
#              specified value, performs a right-click on it, and selects an option from
#              the context menu. 
# Parameters: param (str) – A string in the format "block_value$$dropdown_value", where:
#                         block_value (str) – The text to search for in block elements.
#                         dropdown_value (str) – The context menu option to select after right-click.
###########################################################################################   
def right_click_block(param):
    block_value, dropdown_value = param.split('$$')
    try:
        block_lst = proj_obj.instanceeditpagetab.object.FindAllChildren("Name", "TextObject*", 1000)
        
        if not block_lst:
            Log.Error("No blocks found in instance edit page tab.")
            return
        
        clicked = False
        for window_text in block_lst:
            if block_value in window_text.Text and window_text.Visible:
                window_text.ClickR()
                click_MenuItem_Toolbar_CE(dropdown_value)
                Log.Checkpoint(f"Right-clicked on block with text: '{window_text.Text}' and selected '{dropdown_value}' from context menu.")
                clicked = True
                break
        
        if not clicked:
            Log.Error(f"No visible block containing '{block_value}' found.")
    
    except Exception as e:
        Log.Error(f"Exception occurred while right-clicking on block: {str(e)}")

        
###########################################################################################
# Function: change_block_type
# Description: Changes the block type by entering the block name in the new section dialog,
#              locating the matching text object within the OK modal dialog, and performing
#              a double-click action on it.
# Parameters: value (str) – The name or partial name of the block to be changed.
###########################################################################################        
def change_block_type(value):
    try:
        enter_name_new_section(value)
        
        Applicationutility.wait_in_seconds(1.5, 'Waiting for dialog to update')
        
        text_lst = ce_obj.okmodaldialoguewindowce.object.FindAllChildren("Name", "TextObject*", 1000)
        
        Log.Message(f"Number of text objects found: {len(text_lst)}")

        if not text_lst:
            Log.Error("No text objects found in the OK modal dialog.")
            return
        
        clicked = False
        for window_text in text_lst:
            if value in window_text.Text and window_text.Visible:
                window_text.DblClick()
                Log.Checkpoint(f"Double-clicked on block with text: '{window_text.Text}'")
                clicked = True
                break
        
        if not clicked:
            Log.Error(f"Block with text containing '{value}' was not found or not visible.")

    except Exception as e:
        Log.Error(f"An error occurred while changing block type: {str(e)}")

    
###########################################################################################
# Function: verify_block_type
# Description: Verifies whether a block with the specified text value exists among the
#              visible text objects in the instance editor.
# Parameters: value (str) – The exact text of the block to search for and verify.
###########################################################################################    
def verify_block_type(value):
    try:
        block_lst = proj_obj.instanceeditpagetab.object.FindAllChildren("Name", "TextObject*", 1000)

        if not block_lst:
            Log.Error("No text objects found in instance editor.")
            return

        for window_text in block_lst:
            if window_text.Visible and window_text.Text == value:
                Log.Checkpoint(f"Block type '{value}' is verified successfully.")
                return  

        Log.Error(f"Block type '{value}' not found among visible text objects.")

    except Exception as e:
        Log.Error(f"Error verifying block type '{value}': {str(e)}")

###########################################################################################
# Function: change_block_func_property
# Description: Changes the properties of a block by performing a sequence of interactions:
#              it first double-clicks on the specified block, then clicks the provided
#              buttons in order within the network popup dialog. This function orchestrates
#              the steps to update block properties in the Composite Editor.
# Parameters: param (str) – A string in the format "block_value$$EN_ENO_value$$ok_btn", where:
#                         block_value (str) – The name or text of the block to be modified.
#                         EN_ENO_value (str) – The caption of the first button to click in the popup.
#                         ok_btn (str) – The caption of the second button to click in the popup.
###########################################################################################
def change_block_func_property(param):
    try:
        block_value, EN_ENO_value, ok_btn = param.split('$$')
        
        # Double-click the specified block
        double_click_first_in_block(block_value)
        
        # Click the first button in the network popup
        Click_ok_button_add_network_popup_CE(EN_ENO_value)
        
        # Click the OK button in the network popup
        Click_ok_button_add_network_popup_CE(ok_btn)
        
        Log.Checkpoint(f"Block '{block_value}' properties changed using '{EN_ENO_value}' and '{ok_btn}' buttons.")
    
    except Exception as e:
        Log.Error(f"An error occurred while changing block properties: {str(e)}")
############################################################################################################


def Select_Column_Configuration2(identifier):
    Window = globaltemp_obj.filesavewindow.object.FindAllChildren("WndClass", "AfxWnd140u", 1000)
    if not Window:
        Log.Error("No columns found in the dialog window.")
        return
    for obj in Window:
        Log.Message((obj.Text))
        if identifier in obj.Text:
            Window.Click(obj.Left-50+obj.Width, obj.Top+40+(obj.Height/2))
            Log.Message(obj.Text + " is selected")
            #Sys.Keys['Enter']
#############################################################################################################

def verify_engineering_link_in_security_editor():
  items = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "Static", 100)
  dropdowns = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "ComboBox", 100)
  for i in items:
    if i.WndCaption == "Engineering Link Mode:":
      for d in dropdowns:
        if d.Index == i.Index-1:
          Log.Message(f"{i.WndCaption} is {d.wText}")
          break
      break
  else:
    Log.Message(f"Engineering Link Mode is not found")

##############################################################################################################

def verify_services_in_security_editor():
  required_items = ["FTP  :", "TFTP  : ", "HTTPS : ", "DHCP / BOOTP  : ", "SNMP  : ", "EIP  : "]
  items = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "Static", 100)
  dropdowns = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "ComboBox", 100)
  for i in range(len(items)):
    if items[i].WndCaption in required_items:
      if items[i].Index == dropdowns[i].Index:
        Log.Message(f"{items[i].WndCaption} is {dropdowns[i].wText}")
      else:
        Log.Warning(f"{items[i].WndCaption} is not found")
        
############################################################################################################

def verify_access_control_in_security_editor():
  btns = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "Button", 100)
  dropdowns = ce_obj.securitywindowconfiguration.object.FindAllChildren("WndClass", "ComboBox", 100)
  for i in btns:
    if i.WndCaption == "Access Control":
      for d in dropdowns:
        if d.Index == i.Index:
          Log.Message(f"{i.WndCaption} is {d.wText}")
          break
      break
  else:
    Log.Message(f"Access Control is not found")
    
###########################################################################################################

def change_engineering_link_dropdown(param):
  eng_dropdown = ce_obj.securitywindowconfiguration.object.Window("ComboBox", "", 9)
  if eng_dropdown.Exists:
    eng_dropdown.ClickItem(param)
    Log.Message(f"Engineering link changed to {param}")
  else:
    Log.Message("Engineering link dropdown not found")
    
###########################################################################################################
## Function   : click_variable_DDT_Type_data_editor
## Description: To click the given variable in the DDT type data editor.
## Parameter  : variable_name (str) is the variable that needs to be clicked.
## Example    : click_variable_DDT_Type_data_editor("ValveGP_ST_DDT")
########################################################################################################### 
def click_variable_DDT_Type_data_editor(variable_name):
  names = con_obj.DataEditorCE.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in names:
    if variable_name in i.Name:
      i.Click()
      Log.Checkpoint(f'{variable_name} in data editor was clicked')
      break
  else:
    Log.Error(f'{variable_name} does not exists')
        

###########################################################################################################
## Function   : select_type_data_editor
## Description: To select type for an item in the DDT type of data editor.
## Parameter  : val (str) is the value need to be selected in that dropdown
## Example    : select_type_data_editor("<Array>")
###########################################################################################################    
def select_type_data_editor(val):
  type_dd = con_obj.DataEditorCE.object.FindChild("ClassName", "CDSEComboBox", 100)
  if type_dd.Exists:
    type_dd.wText = val
    Log.Checkpoint(f"{val} selected in type")
    con_obj.DataEditorCE.object.Click()
  else:
    Log.Error("Type dropdown not found")
###########################################################################################################
## Function   : analyze_type_data_editor
## Description: To analyze type for an item in the DDT type of data editor.
## Parameter  : var (str) is the name of the item to be analyzed
## Example    : analyze_type_data_editor("Sample")
###########################################################################################################    
def analyze_type_data_editor(var):
  click_variable_DDT_Type_data_editor(var)
  aqUtils.Delay(1000)
  Sys.Keys("^!B")
  names = con_obj.DataEditorCE.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in names:
    if var in i.Name:
      i.ClickR()
      Log.Checkpoint(f'Right clicked on {var} in data editor')
      at = Sys.Process("ControlExpert", 2).Popup("Context").MenuItem("Analyze Type\tCtrl+Shift+B")
      if at.Enabled:
        Log.Error(f"Analyze Type unsuccessful for {var}")
        break
      else:
        Log.Checkpoint(f"Analyze Type successful for {var}")
        break
  else:
    Log.Error(f'{var} does not exists')    
    
       
########################################################################################################### 
## Function   : variable_selection_window_data_editor
## Description: To select a variable type in the variable selection popup in data editor.
## Parameter  : var (str) is the variable type in the selection window.
## Example    : variable_selection_data_editor("INT")
###########################################################################################################   
def variable_selection_window_data_editor(var):
  var_window = con_obj.DataEditorVariableSelection.object
  if var_window.Exists:
    search = var_window.Window("#32770", "Variable types", 1).Window("AfxWnd140u", "", 1).Window("Edit", "", 1)
    search.Click()
    Sys.Keys("^A" + "[Del]")
    Sys.Keys(var + "[Enter]")
    Log.Checkpoint(f"Selected {var} type in variable selection")
    items_box = var_window.Window("#32770", "Variable types", 1).Window("AfxWnd140u", "CommonTreeList", 3)
    items_box.Click()
    ok_btn = var_window.Window("Button", "OK", 2)
    ok_btn.Click()
    Log.Checkpoint("Clicked on OK in Variable Selection popup")
  else:
    Log.Error("Variable selection window not found") 
    
       
###########################################################################################################
## Function   : create_new_and_analyze_type_data_editor
## Description: To create and analyze type for an item in the DDT type of data editor.
## Parameter  : param (str) - Input in the format "LastItemName$$NewName$$Type$$VarType"
#               where LastItemName is the last text item and NewName is the new item name.
#               where Type is the type to be selected for the item 
#               where Var_Type is the variable type to be selected in variable selection popup.
## Example    : create_new_and_analyze_type_data_editor("ValveGP_ST_DDT$$Sample1$$<Array>$$INT")
###########################################################################################################       
def create_new_and_analyze_type_data_editor(param):
  last_variable_name, desired_variable_name, type, var_type = param.split("$$")
  click_variable_DDT_Type_data_editor(last_variable_name)
  Sys.Keys("[Down]")
  Sys.Keys("[Enter]")
  Sys.Keys(desired_variable_name)
  Log.Checkpoint(f"Created {desired_variable_name} variable succesfully")
  Sys.Keys("[Enter]")
  Sys.Keys("[Right]")
  Sys.Keys("[Enter]")
  select_type_data_editor(type)
  Applicationutility.wait_in_seconds(1000)
  variable_selection_window_data_editor(var_type)
  Applicationutility.wait_in_seconds(1000)
  analyze_type_data_editor(desired_variable_name)

#from_node, to_node = param.split('$$')
#  node_element_parent = aet_obj.nodeinstancebutton.object
#  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
#  if node_element_list:
#    for node_element in node_element_list:
#      if from_node == str(node_element.DataContext.Identifier) :
#            tox = node_element.ScreenLeft
#            toy = node_element.ScreenTop
#
#    for node_element in node_element_list:
#      if to_node == str(node_element.DataContext.Identifier) :
#        fromx = node_element.Width
#        regulator1 = node_element.ScreenLeft
#        regulator2 = node_element.ScreenTop
#        fromy = node_element.Height
#        node_element.Drag(fromx-15, fromy/2, tox-regulator1, toy-regulator2)
#  else:
#    Log.Error("No nodes found in the editor.")

def link_move_blocks():
  block_lst = proj_obj.instanceeditpagetab.object.FindAllChildren("Name", "TextObject*", 1000)
  Log.Message(f"Total text objects found: {len(block_lst)}")

  tox = None
  toy = None

  # Find the 'Out' window
  for window_text in block_lst:
      Log.Message("Checking window for 'Out'")
      if 'Out' in window_text.Text and window_text.Visible:
          Log.Message("Found 'Out' window")
          tox = window_text.ScreenLeft
          toy = window_text.ScreenTop
          break

  if tox is not None and toy is not None:
      Log.Message(f"'Out' window located at ({tox}, {toy})")
  else:
      Log.Error("No 'Out' window found! Drag action cannot proceed.")
      # Optionally exit or skip further steps if 'Out' window not found
      # return or raise Exception here if needed

  # Find the 'ExtCTLD' window and perform drag
  for window_text in block_lst:
      Log.Message("Checking window for 'ExtCTLD'")
      if 'ExtCTLD' in window_text.Text and window_text.Visible:
          Log.Message("Found 'ExtCTLD' window")
          fromx = window_text.Width
          fromy = window_text.Height
          regulator1 = window_text.ScreenLeft
          regulator2 = window_text.ScreenTop

          if tox is not None and toy is not None:
              delta_x = tox - regulator1
              delta_y = toy - regulator2
              Log.Message(f"Dragging from ({regulator1}, {regulator2}) to ({tox}, {toy})")
              window_text.Drag(fromx - 15, fromy / 2, delta_x, delta_y)
          else:
              Log.Error("Cannot perform drag because 'Out' window was not found.")
          break