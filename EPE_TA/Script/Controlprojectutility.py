    
import Actionutility
import Applicationutility
from ControlProjectTab import ControlProjectTab
from ProjectExplorerTab import ProjectExplorerTab

cont_obj = ControlProjectTab()
proj_obj = ProjectExplorerTab()

##############################################################################################################
#Function:rename_FBDsection
#Description: To rename FBD section and Check for validation rules while creating the FBD section
#Parameters: (str or int) - the name of the FBD Section to create and validate
#Example: rename_FBDsection("Section_1")
#         rename_FBDsection("Fbd_new_1")
# try with more than 32 char, symbols like @,#,%, name ending with underscore
#Note: name should not exceed 32 char and should not end with underscore(exception)
##############################################################################################################

def rename_FBDsection(name): # Redundant method ? fix method
  rename_sec = cont_obj.renamefbdsectionwhilecreation.object
  rename_sec.Keys(name)
  Actionutility.modal_dialog_window_button("OK")
  Applicationutility.wait_in_seconds(1500, 'Wait')                
  try:
    if rename_sec.tooltip:
      Log.Warning(f"Rename Validation Error : {rename_sec.tooltip}")
      Applicationutility.take_screenshot()
      Applicationutility.wait_in_seconds(1500, 'Wait')
      Actionutility.modal_dialog_window_button("Cancel")
  except:
      Log.Checkpoint(f"{name} is created ")

##############################################################################################################
#Function:select_path_of_FBD
#Description: Selects a FBD path from a popup list in the application based on a matching identifier value provided as a parameter      
#Parameters: (str) - The identifier string to match against the list items in the FBD path popup
#Example: select_path_of_FBD("MAST")
##############################################################################################################  
    
def select_path_of_FBD_creation(param):
  path = cont_obj.selectpathoffbdpopup.object
  Applicationutility.wait_in_seconds(2000, 'Wait')
  for i in range(path.Items.Count):
    if param == path.Items.Item[i].Identifier.OleValue:
      Applicationutility.wait_in_seconds(2000, 'Wait')
      path.ClickItem(i)
      if param == path.wText:
        Log.Checkpoint(f'Selected FBD path is {path.wText}')
      else:
        Log.Error(f'Selected FBD path is {path.wText} instaed of {param}')
        
##################################################################################################################
# Function: verify_FBD_order_containerdock
# Description:
#   Verifies the contents of the container dock textbox by retrieving all child elements
#   with the class name "GridViewRow". It waits briefly, checks each element's panel Z-index,
#   and logs the internal order of each FBD section found. If no sections are available,
#   it logs a warning.
# Parameters: None
##################################################################################################################

def verify_FBD_order_containerdock():
  Grid = proj_obj.containerdocktextbox.object.FindAllChildren("ClrClassName","GridViewRow",500)
  
  dict = {}
  key - list.DataContext.InternalOrder
  
  for list in Grid:
    if Grid:
      if list.Panel_ZIndex != 0:
        Log.Checkpoint(f"The order for {list.Item.Identifier.OleValue} is {list.DataContext.InternalOrder}")

    else:
      Log.Error("There is no FBD Sections available")
         
		 
