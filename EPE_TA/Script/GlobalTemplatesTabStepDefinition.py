"""GlobalTemplatesTabWorkFlow"""
from GlobalTemplatesTabWorkFlow import GlobalTemplatesTabWorkFlow
import CommonUtil
import Applicationutility
import Globaltemplatesutility
import Engineeringclientutility
obj=GlobalTemplatesTabWorkFlow()

        
@when("I Search text and select GTE global template search in global template explorer as {arg}")
def step_impl(globalTemplateSearch1):
    """I Search text and select GTE global template search in global template explorer as '<global template search1>'"""
    obj.textboxglobaltemplatesearchsearchtextandselectgte(globalTemplateSearch1)
  
@when("I right click on the searched template GTE global template core in global template explorer as {arg}")
def step_impl(globalTemplateCore2):
    """I right click on the searched template GTE global template core in global template explorer as '<global template core2>'"""
    obj.textboxglobaltemplatecorerightclickonthesearchedtemplategte(globalTemplateCore2)
  
@when("I Select context menu item EC global template core in global template explorer as {arg}")
def step_impl(globalTemplateCore3):
    """I Select context menu item EC global template core in global template explorer as '<global template core3>'"""
    obj.textboxglobaltemplatecoreselectcontextmenuitemec(globalTemplateCore3)
  
@when("I selected Ok duuplicate in duplicate")
def step_impl():
    """I selected Ok duuplicate in duplicate"""
    obj.buttonokduuplicateselected()
  
@when("I wait_for_object_disapear Duplicate window in duplicate as {arg}")
def step_impl(duplicateWindow):
    """I wait_for_object_disapear Duplicate window in duplicate as '<Duplicate window>'"""
    obj.textboxduplicatewindowwaitforobjectdisapear(duplicateWindow)
  
@when("I Wait for Circular Progress Bar global template core in global template explorer")
def step_impl():
    """I Wait for Circular Progress Bar global template core in global template explorer"""
    obj.textboxglobaltemplatecorewaitforcircularprogressbar()
  
@when("I selected toolbox in composite editor")
def step_impl():
    """I selected toolbox in composite editor"""
    obj.buttontoolboxselected()
  
@when("I drag and drop toolbox item composite editor GTE toolboox table in composite editor as {arg}")
def step_impl(toolbooxTable6):
    """I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<toolboox table6>'"""
    obj.textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte(toolbooxTable6)
  
@when("I selected save as composite editor in composite editor")
def step_impl():
    """I selected save as composite editor in composite editor"""
    obj.buttonsaveascompositeeditorselected()
  
@when("I entered Description in save as window as {arg}")
def step_impl(description7):
    """I entered Description in save as window as '<Description7>'"""
    obj.textboxdescriptionentered(description7)
  
@when("I selected Save in save as window")
def step_impl():
    """I selected Save in save as window"""
    obj.buttonsaveselected()

@then("verify popup message in the save as window as {arg}")
def step_impl(content):
    Engineeringclientutility.verify_Popup_Message_OK(content)
    
@when("I selected Cancel in save as window")
def step_impl():
    """I selected Cancel in save as window"""
    obj.buttoncancelselected()

@then("verify search text GTE global template search in global template explorer as {arg}")
def step_impl(globaltemplatesearch1):
    """I selected Cancel in save as window"""
    Globaltemplatesutility.verify_search_box_message_GTE(globaltemplatesearch1)
    
@when("I selected Save in save as windowo")
def step_impl():
    """I selected Save in save as window"""
    obj.buttonsaveselected1()
    
@when("I selected Close duuplicate in duplicate")
def step_impl():
    """I selected Close duuplicate in duplicate"""
    Applicationutility.take_screenshot('Full screenshot')
    obj.closeduuplicateselected()
@then("Verify Duplicate window close")
def step_impl():
    """Verify Duplicate window close"""
    obj.verify_dup_win()
    Applicationutility.take_screenshot('Full screenshot')
        
@then("I verify that I have navigated to the {arg}")
def step_impl(tabname):
    """I verify that I have navigated to the '<tabname>'"""
    obj.verifytittlebar(tabname)
    Applicationutility.take_screenshot('Full screenshot') 
    
@when("I Search text and Right-Click GTE global template search in global template explorer as {arg}")
def step_impl(globalTemplateSearch1):
    """I Search text and Right-Click GTE global template search in global template explorer as '<global template search1>'"""
    obj.textboxglobaltemplatesearchsearchtextandrightclickgte(globalTemplateSearch1)
    
@when("I Select {arg} in global template explorer")
def step_impl(tab):
    """I Select '<tab>' in global template explorer"""
    obj.textboxglobaltemplateselecttabgte(tab)
    
@when("I Drag and Drop {arg} from toolbox to the edit page in global template explorer")
def step_impl(source):
    """I Drag and Drop '<source>' from toolbox to the edit page in global template explorer"""
    obj.textboxglobaltemplatedraganddroptoolsgte(source)


@when("I click on {arg} in the Save As window")
def step_impl(btn):
    """I click on '<btn>' in the Save As window"""
    obj.textboxglobaltemplatesaveaswindowclickbuttongte(btn)

@when("I select {arg} in Select Tag Window")
def step_impl(btn):
    """I select '<btn>' in Select Tag Window"""
    obj.textboxglobaltemplateselecttaggte(btn)
    
@when("I change the template name to {arg} and version to {arg} in the Save As window")
def step_impl(name, version):
    """I change the template name to '<name>' and version to '<version>' in the Save As window"""
    obj.textboxglobaltemplatesaveaswindownameandversiongte(name, version)
    
@when("I enter the description in the Save As window as {arg}")
def step_impl(desc):
    """I enter the description in the Save As window as '<desc>'"""
    obj.textboxglobaltemplatesaveaswindowndescgte(desc)
    Applicationutility.wait_in_seconds(1000, 'wait')
    
@when("I click on the {arg} button in the Template Creation Wizard")
def step_impl(button):
    """I click on the '<button>' button in the Template Creation Wizard"""
    obj.buttonnextselected(button)
    
@when("I click on the Browse button in the Template Creation Wizard")
def step_impl():
    """I click on the Browse button in the Template Creation Wizard"""
    obj.buttonbrowseselected()
    
@when("I click on the {arg} Add button in the Template Creation Wizard")
def step_impl(elem):
    """I click on the '<elem>' Add button in the Template Creation Wizard"""
    obj.buttonaddselected(elem)
    
@when("I click on the {arg} in Template Creation Wizard")
def step_impl(elem):
    """I click on the '<elem>' in Template Creation Wizard"""
    obj.textboxglobaltemplateclicklibrarygte(elem)
    
@when("I Exapnd the {arg} in Template Creation Wizard")
def step_impl(elem):
    """I Exapnd the '<elem>' in Template Creation Wizard"""
    obj.textboxglobaltemplateexpandpropertiesgte(elem)
    
@when("I Drag and Drop {arg} from Genie to Genie Facet in Template Creation Wizard")
def step_impl(prop):
    """I Drag and Drop '<prop>' from Genie to Genie Facet in Template Creation Wizard"""
    obj.textboxglobaltemplatedraganddropgeniegte(prop)
    
@when("I right click on the created template in global template explorer as {arg}")
def step_impl(prop):
    """I right click on the created template in global template explorer as '<prop>'"""
    obj.textboxglobaltemplaterightclickcreatedtemplategte(prop)
    Applicationutility.take_screenshot('Full screenshot')    
    
@when("I Enter FileLocation {arg}, {arg} and FileName {arg} import window")
def step_impl(path, folder, file):
    """I Enter FileLocation '<path>', '<folder>' and FileName '<file>' import window"""
    obj.GTimportfilenamefilelocation(path, folder, file)

@when("I Right Click on control template header in global template explorer")
def step_impl():
    """I Right Click on control template header in global template explorer"""
    obj.rclickcontroltemplateheader()
    
@when("I Right Click on motor template header in global template explorer")
def step_impl():
    """I Right Click on motor template header in global template explorer"""
    obj.rclickmotortemplateheader()
    
@when("I Right Click on logic template header in global template explorer")
def step_impl():
    """I Right Click on logic template header in global template explorer"""
    obj.rclicklogictemplateheader()
    
@when("I Click on templatizer button in global template explorer")
def step_impl():
    """I Right Click on templatizer button in global template explorer"""
    obj.clicktemplatizerbutton()
 
@when("I Click on open control participant button in global template explorer")
def step_impl():
    """I Right Click on open control participant button in global template explorer"""
    obj.clickopencontrolparticipantbutton()   

@when("I Right Click on supervision template header in global template explorer")
def step_impl():
    """I Right Click on supervision template header in global template explorer"""
    obj.rclicksupervisiontemplateheader()
    
@when("I Right Click on genie template header in global template explorer")
def step_impl():
    """I Right Click on genie template header in global template explorer"""
    obj.rclickgeniestemplateheader()
    
@when("I Right Click on pump right genie template header in global template explorer")
def step_impl():
    """I Right Click on pump right genie template header in global template explorer"""
    obj.rclickpumprightgenietemplateheader()
    
@when("I Click on fit to content button in global template explorer")
def step_impl():
    """I Right Click on fit to content button in global template explorer"""
    obj.clickfittocontentbutton()
  
@when("I Click on open participant button in global template explorer")
def step_impl():
    """I Right Click on open participant button in global template explorer"""
    obj.clickopenparticipantbutton()  
    
@when("I Click on State Selector in global template explorer")
def step_impl():
    """I Right Click on State Selector in global template explorer"""
    obj.clickStateSelectorapprovedinsaveas()    

@when("I Click on old State Selector in global template explorer")
def step_impl():
    """I Right Click on old State Selector in global template explorer"""
    obj.clickOldStateSelectorapprovedinsaveas()
        
@when("I Click on Approved combo item in global template explorer")
def step_impl():
    """I Right Click on Approved combo item in global template explorer"""
    obj.clickapprovedcomboitem()    
    
@when("I right click on the instance {arg} in device control window")
def step_impl(param):
  """I right click on the instance with identifier and version in the device control window"""
  Globaltemplatesutility.right_click_on_device_control(param)
  
@when("I right click on the {arg} header with UC display type in composite editor workspace")
def step_impl(arg):
  """I right click on the '<arg>' header with UC display type in composite editor workspace"""
  Globaltemplatesutility.right_click_onHeader_UC(arg)
  
@when('I click the {arg} button in the Composite Editor Workspace')
def step_impl(button):
  """Clicks the specified button in the Composite Editor Workspace"""
  Globaltemplatesutility.click_button_in_composite_editor(button)
  
@when('I expand the instance {arg} in the Global Template')
def step_impl(expandinstance):
  """I expand the instance '<expandinstance>' in the Global Template"""
  Globaltemplatesutility.Expand_instance_in_gte(expandinstance)
  
@when('I click the checkbox for instance {arg} in the Global Template')
def step_impl(checkboxname):
  """I click the checkbox for instance '<checkboxname>' in the Global Template"""
  Globaltemplatesutility.check_checkbox_in_gte(checkboxname)
  
@when("I right click on the item '(.*)' under the header '(.*)'")
def step_impl(item_key, header_key):
  """I right click on the item '<item_key>' inside the header '<header_key>'"""
  Globaltemplatesutility.right_click_on_treeview_under_header(header_key, item_key)
  
@when('I approve the new template by setting status to Approved and description to Test')
def step_impl():
  """I approve the new template by setting status to Approved and description to Test"""
  Globaltemplatesutility.new_template_save_as_window_gte()    
  
@when("I perform right click on editor window in GT")
def step_impl():
    """I perform right click on editor window in GT"""
    Globaltemplatesutility.Right_click_on_the_editor_window_GT()
    
@then("Verify the composite editor in read only mode as {arg}")
def step_impl(param):
    """Verify the composite editor in read only mode as <Menu_item1>"""
    Globaltemplatesutility.verify_viewmode_Composite_editor(param) 
    
@when("I Click on Edit menu item in global template explorer as {arg}")
def step_impl(param):
    """I Click on Edit menu item in global template explorer as <Tab1>"""
    Globaltemplatesutility.Click_edit_menuitem(param)  
    
@then("Verify changeslog window is displayed")
def step_impl():
     """Verify changeslog window is displayed"""
     Globaltemplatesutility.verify_changeslog_window()
     
@when("I Click on Editor toolbar in global template explorer as {arg}")   
def step_impl(param):
    """I Click on Editor toolbar in global template explorer as '<Toolbar>'"""
    Globaltemplatesutility.click_editor_menuitem(param)
    
@when("I Click on items in selevt items window in global template explorer as {arg}")   
def step_impl(name):
    """I Click on items in selevt items window in global template explorer as '<Itemname>'"""
    Globaltemplatesutility.Click_on_select_item_in_new_item_tab(name)
    
@when("I Enters the given identifier value in the Select Item window as {arg}")   
def step_impl(val):
    """I Enters the given identifier value in the Select Item window as '<Identifier>'"""
    Globaltemplatesutility.enter_identifier_select_item_window_GT(val)
    
@when("I Open the location selection window in the 'Select Item' window")   
def step_impl():
    """I Open the location selection window in the 'Select Item' window"""
    Globaltemplatesutility.open_location_select_item_window_GT()
    
@when("I Expand a node in the 'Select Item' window tree structure as {arg}")   
def step_impl(name):
    """I Expand a node in the 'Select Item' window tree structure as '<node name>'"""
    Globaltemplatesutility.expand_nodes_select_item_window_GT(name)
    
@when("I select a node in the 'Select Item' window tree as {arg}")   
def step_impl(Name):
    """I select a node in the 'Select Item' window tree as '<SelectNode>'"""
    Globaltemplatesutility.Check_and_select_nodes_select_item_window_GT(Name)
    
@when("I click {arg} 'Select Item' window tree modal dialog window")  
def step_impl(button_name):
    """I click '<button>' 'Select Item' window tree modal dialog window"""
    Globaltemplatesutility.modal_dialog_feedback_window_button(button_name)
    
@when("I expand {arg} in Global template Window")  
def step_impl(node_name):
    """I expand '<node_name>' in Global template Window"""
    Globaltemplatesutility.expand_nodes__GT(node_name)
    
@then("I verify path of item created in Global template Window with {arg}")   
def step_impl(node_name):
    """I verify path of item created in Global template Window with '<Headername>'"""
    Globaltemplatesutility.verify_item_created_under_path(node_name)