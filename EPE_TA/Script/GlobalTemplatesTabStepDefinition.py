"""GlobalTemplatesTabWorkFlow"""
from GlobalTemplatesTabWorkFlow import GlobalTemplatesTabWorkFlow
import CommonUtil
import Applicationutility
import Globaltemplatesutility
import Engineeringclientutility
import Actionutility
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
    
@when("I Click on control template header in global template explorer")
def step_impl():
    """I Click on control template header in global template explorer"""
    obj.clickcontroltemplateheader()
    
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

@when("I Click on supervision template header in global template explorer")
def step_impl():
    """I Click on supervision template header in global template explorer"""
    obj.clicksupervisiontemplateheader()
    
@when("I Right Click on genie template header in global template explorer")
def step_impl():
    """I Right Click on genie template header in global template explorer"""
    obj.rclickgeniestemplateheader()
    
@when("I Right Click on pump right genie template header in global template explorer")
def step_impl():
    """I Right Click on pump right genie template header in global template explorer"""
    obj.rclickpumprightgenietemplateheader()
    
@when("I Click on fit to content button in global template explorer")
@when("I Click on fit to content button in Application Explorer")
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
  
@when('I Right Click on function in GTE CompositeEdittor as {arg}')
def step_impl(func):
  """I Right Click on function in GTE CompositeEdittor as '<func>'"""
  Globaltemplatesutility.right_click_on_Func(func)   
  
@when('I paste the function into the Composite Editor workspace')
def step_impl():
  """I paste the function into the Composite Editor workspace"""
  Globaltemplatesutility.paste_function()      
  
@then('I Select {arg} and verify it is selected')
def step_impl(identifier):
  """I Select '<identifier>' and verify it is selected"""
  Globaltemplatesutility.click_and_verify(identifier)
  
@then('I Unselect {arg} to verify it is unselected')
def step_impl(identifier):
  """I Unselect '<identifier>' to verify it is unselected"""
  Globaltemplatesutility.verify_unselect(identifier)
 
@when("I Select Document Outline in GTE Composite Edittor")
def step_impl():
    """I Select Document Outline in GTE Composite Edittor"""
    obj.buttondocumentoutlineselected()  
     
@then("I Double click element on Document Outline and verify that element in Composite Edittor as {arg}")
def step_impl(Element):
    """I Double click element on Document Outline and verify that element in Composite Edittor as '<Element>'"""
    Globaltemplatesutility.select_area_and_verify(Element)  

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
     
@when("I click on the menu item bar in the composite editor in GT {arg}")
def step_impl(param):
     """I click on the menu item bar in the composite editor in GT '<title>'"""
     obj.clickeditormenuitem(param)

@when("I verify the header item in EC as {arg}")
def step_impl(header_value):
     """I verify the header item in EC as '<header_value>'"""
     obj.verifyheaderpanelitemsEC(header_value)
     
@then("I verify the context submenu items")
def step_impl():
     """I verify the context submenu items"""
     Globaltemplatesutility.verify_Context_SubMenu_Items_EC()
     
@when("I verify the template on the editor window in GT as {arg}")
def step_impl(template):
     """I verify the template on the editor window in GT as '<template>'"""
     obj.verifytemplateontheeditorwindowGT(template)
     
@when("I verify the element on the editor window in GT as {arg}")
def step_impl(element):
     """I verify the element on the editor window in GT as '<element>'"""
     obj.verifyelementontheeditorwindowGT(element)

@when("I perform copy using keyboard actions")
def step_impl():
    """I perform copy using keyboard actions"""
    CommonUtil.write_text_file("\nWhen I perform copy using keyboard actions")
    Actionutility.Copy_keyboard_action() 
    
@when("I perform paste using keyboard actions")
def step_impl():
    """I perform paste using keyboard actions"""
    CommonUtil.write_text_file("\nWhen I perform paste using keyboard actions")
    Actionutility.Paste_keyboard_action()
     
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
    
@when("I Ctrl+A to select all in the Composite Editor window")
def step_impl():
    """I Ctrl+A to select all in the Composite Editor window"""
    obj.selectallkey()
    
@when("I Ctrl+C to copy the selected in Composite Editor window")
def step_impl():
    """I Ctrl+C to copy the selected in Composite Editor window"""
    obj.copykey()
    
@when("I Ctrl+V to paste the copied in the same Composite Editor window")
def step_impl():
    """I Ctrl+V to paste the copied in the same Composite Editor window"""
    obj.pastekey()
    
@when("I verify the warning message in the GTE pane as {arg}")
def step_impl(param):
    """I verify the warning message in the GTE pane as '<message>'"""
    obj.verifyGTwarningmessage(param)
    
@when("I Ctrl+F to search for the block in GTE Editor and enter search text as {arg}")
def step_impl(text):
    """I Ctrl+F to search for the block in GTE Editor and enter search text as '<block>'"""
    obj.findandentersearchtext(text)
    
@when("I Right-Click on the searched block in Editor window as {arg}")
def step_impl(block):
    """I Right-Click on the searched block in Editor window as '<block>'"""
    obj.findandRclicksearchtext(block)
    
@when("I Right Click on block in Interface Editor in global template explorer as {arg}")
def step_impl(param):
    """I Right Click on block in Interface Editor in global template explorer as '<block>'"""
    obj.rclickblockinInterfaceeditor(param)
    
@when("I Right Click System Parameter in global template explorer as {arg}")
def step_impl(param):
    """I Right Click System Parameter in global template explorer as '<param>'"""
    obj.rclickSystemParameter(param)
    
@when("I Right Click on Element in global template explorer as {arg}")
def step_impl(element):
    """I Right Click on Element in global template explorer as '<element>'"""
    obj.rclickElement(element)
    
@when("I Right Click on Function in global template explorer as {arg}")
def step_impl(func):
    """I Right Click on Function in global template explorer as '<function>'"""
    obj.rclickFunction(func)
    
@when("I Right Click Input Value in global template explorer as {arg}")
def step_impl(input):
    """I Right Click Input Value in global template explorer as '<input>'"""
    obj.rclickInputValue(input)
    
@when("I Right Click on workspace in global template explorer")
def step_impl():
    """I Right Click on workspace in global template explorer"""
    obj.rclickworkspaceGTE()
    
@when("I Right Click on Grey Hexagon in global template explorer as {arg}")
def step_impl(hexa):
    """I Right Click on Grey Hexagon in global template explorer as '<hexa>'"""
    obj.rclickGreyhexagon(hexa)
    
@when("I Right Click on Orange Hexagon in global template explorer as {arg}")
def step_impl(hexa1):
    """I Right Click on Orange Hexagon in global template explorer as '<hexa1>'"""
    obj.rclickOrangehexagon(hexa1)

@when("I click toolbar item in select variables window as {arg}")   
def step_impl(param):
    """I click toolbar item in select variables window as '<Button Name>'"""
    Globaltemplatesutility.Click_Toolbaritem_Select_variable_window(param)    
       
    
@when("I right click on {arg} module in templates composite editor window")   
def step_impl(Identifier):
    """I right click on '<Description>' module in templates composite editor window"""
    Globaltemplatesutility.Right_click_module_of_template(Identifier)
    
@then("I check the tooltip of the connecter with controltext as {arg}")   
def step_impl(display_text):
    """I check the tooltip of the connecter with controltext as '<connectortext>'"""
    Globaltemplatesutility.check_connecter_tooltip_by_text(display_text)
    
@when("I check no of links between source and targets as {arg}")   
def step_impl(connector_name):
    """I check no of links between source and targets as '<connectorname>'"""
    Globaltemplatesutility.no_of_target_links_connector(connector_name)   
    
@then("I verify the {arg} is expanded or collapsed after Enter key")   
def step_impl(identifier):
    """I verify the '<node>' is expanded or collapsed after Enter key"""
    Globaltemplatesutility.verify_node_expanded_or_collapsed_enterkey_GT(identifier)
   
@when("I select on {arg} module in composite ediotr window")   
def step_impl(Identifier):
    """I select on '<identifier>' module in composite ediotr window"""
    Globaltemplatesutility.select_module_of_template_composite_editor(Identifier) 
    Applicationutility.wait_in_seconds(2000,'wait')
    
@when("I use keyboard {arg} shortcuts to perform some actions")   
def step_impl(key):
    """I use keyboard '<key>' shortcuts to perform some actions"""
    Globaltemplatesutility.Keyboard_actions(key)   
    Applicationutility.wait_in_seconds(2000,'wait')
    
@then("I verify the module {arg} is in renaming state")   
def step_impl(Identifier):
    """I verify the module '<module>' is in renaming state"""
    Globaltemplatesutility.verify_module_renaming_state_composite_editor(Identifier)    
    
@then("I verify the module {arg} is newly pasted in composite editor")   
def step_impl(Identifier):
    """I verify the module '<module>' is newly pasted in composite editor"""
    Globaltemplatesutility.verify_newly_pasted_module_composite_editor(Identifier)
    
@when("I click on {arg} module in facet ediotr window")   
def step_impl(Identifier):
    """I click on '<identifier>' module in facet ediotr window"""
    Globaltemplatesutility.click_module_in_facet_editor(Identifier) 
    Applicationutility.wait_in_seconds(2000,'wait') 
    
@then("I verify the module {arg} is newly pasted in facet editor")   
def step_impl(Identifier):
    """I verify the module '<module>' is newly pasted in facet editor"""
    Globaltemplatesutility.verify_newly_pasted_module_facet_editor(Identifier)  
    
@when("I search a facet in facet editor and select as {arg}")   
def step_impl(param):
    """I search a facet in facet editor and select as '<name$$identifier>'"""
    Globaltemplatesutility.search_and_Dblclick_facet_eitor(param) 
    Applicationutility.wait_in_seconds(3000,'wait')    
     
    
@when("I Click on ainputsignal template header in facet editor")
def step_impl():
    """I Click on ainputsignal template header in facet editor"""
    obj.clickainputsignalfaceteditorheader()
    
@when("I Click on DO template header in interface editor")
def step_impl():
    """I Click on DO template header in interface editor"""
    obj.clickDOblockinterfaceeditorheader()
    
@then("I verify template {arg} is in renaming state interface editor")
def step_impl(Identifier):
    """I verify template '<name>' is in renaming state interface editor"""
    obj.verifytemplateisinrenamingstateinterfaceeditor(Identifier)
    Globaltemplatesutility.Click_Toolbaritem_Select_variable_window(param) 
    
@when("I drag and drop toolbox item in Interface Editor as {arg}")   
def step_impl(param):
    """I drag and drop toolbox item in Interface Editor as '<toolboxitem>'"""
    obj.draganddroptoolboxitemtoInterfaceeditor(param)
    
@when("I RClick on toolbox transformation item in Interface Editor as {arg}")   
def step_impl(param):
    """I RClick on toolbox transformation item in Interface Editor as '<toolboxitem>'"""
    obj.rclicktransformationiteminInterfaceeditor(param)
    
@when("I RClick on graphical link in Interface Editor")   
def step_impl():
    """I RClick on graphical link in Interface Editor"""
    obj.rclicklinkinInterfaceeditor()

@when("I RClick on graphical link in Composite Editor as {arg}")   
def step_impl(link):
    """I RClick on graphical link in Composite Editor as '<identifier>'"""
    obj.rclicklinkinCompositeeditor(link)
    
@when("I select multiple items from the Editor window as {arg}")
def step_impl(items):
    """I select multiple items from the Editor window as '<multipleitems>'"""
    obj.multiselectitemsinGTEeditor(items)
    Globaltemplatesutility.Click_Toolbaritem_Select_variable_window(param)
    
@when("I click on Element Rules if it is visible on screen")   
def step_impl():
    """I click on Element Rules if it is visible on screen"""
    Globaltemplatesutility.click_element_rules()
    
@when("I click on Properties if it is visible on screen")   
def step_impl():
    """I click on Properties if it is visible on screen"""
    Globaltemplatesutility.click_properties()
    
@when("I click on Interface Rules if it is visible on screen")   
def step_impl():
    """I click on Interface Rules if it is visible on screen"""
    Globaltemplatesutility.click_interface_rules()
    
@when("I click on Browser if it is visible on screen")   
def step_impl():
    """I click on Browser if it is visible on screen"""
    Globaltemplatesutility.click_browser()
    
@when("I click on Document Outline if it is visible on screen")   
def step_impl():
    """I click on Document Outline if it is visible on screen"""
    Globaltemplatesutility.click_document_outline()
    
@when("I click on Toolbox if it is visible on screen")   
def step_impl():
    """I click on Toolbox if it is visible on screen"""
    Globaltemplatesutility.click_toolbox() 
    
@when("I click on Dependency Tree if it is visible on screen")   
def step_impl():
    """I click on Dependency Tree if it is visible on screen"""
    Globaltemplatesutility.click_dependencytree() 
    
@when("I click on External Reference if it is visible on screen")   
def step_impl():
    """I click on External Reference if it is visible on screen"""
    Globaltemplatesutility.click_externalref() 
    
@when("I click on Used By if it is visible on screen")   
def step_impl():
    """I click on Used By if it is visible on screen"""
    Globaltemplatesutility.click_usedby()

@then("Verify the editor window in read only mode as {arg}")
def step_impl(param):
    """Verify the editor window in read only mode as <Menu_item1>"""
    Globaltemplatesutility.verify_viewmode_Composite_editor(param) 

@then("Verify context submenu items are displayed")
def step_impl():
     """Verify context submenu items are displayed"""
     Globaltemplatesutility.verify_Context_SubMenu_Items_EC()
     
@then("Verify header panel item is closed as {arg}")
def step_impl(header_value):
     """Verify header panel item is closed as '<panel>'"""
     Globaltemplatesutility.verify_header_panel_items_EC(header_value)

