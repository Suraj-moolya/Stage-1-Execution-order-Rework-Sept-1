
"""ContentRepositoryStepDefinition"""
from   ContentRepositoryWorkFlow import ContentRepositoryWorkFlow
import CommonUtil
import Applicationutility
import Contentrepositoryutility
import Engineeringclientutility


obj=ContentRepositoryWorkFlow()

@when("I Expand topology explorer node in topology as {arg}")
@when("I Expand content repository explorer node in content repository as {arg}")
def step_impl(identifiers):
  """I Expand the Node in Content Repository """
  obj.expandnodecontentrepository(identifiers)
  
@when("I Select multiple folder to check it Select items as {arg}")
def step_impl(param):
  """I Select multiple folder to check it Select items"""
  obj.selectfolderscontentrepository(param)
  
@then("Verify multiple folders should be selecting and unselecting as {arg}")
def step_impl(param):
  """Verify multiple folders should be selecting and unselecting as <folders> """
  obj.verifyfolderscontentrepository(param)
  
@when("I Enter Item in Textbox Property Window as {arg}")
def step_impl(param):
  """I Enter Item in Textbox Property Window as'<item_1>'"""
  obj.propertywindowcontentrepository(param)
  
@when("I select a particular folder in content repository as {arg}")
def step_impl(folder_name):
    """I select a particular folder in content repository as '<folder_name>'"""
    Contentrepositoryutility.select_folder_in_content_repository(folder_name)
    
@when("I rclick folder in content repository as {arg}")
def step_impl(folder_name):
    """I rclick folder in content repository as '<folder_name>'"""
    Contentrepositoryutility.right_click_folder_in_content_repository(folder_name)
    
@when("I rclick identifier in content repository as {arg}")
def step_impl(identifier_name):
    """I rclick identifier in content repository as '<identifier_name>'"""
    Contentrepositoryutility.right_click_identifier_in_content_repository(identifier_name)
    
@when("I should be able to enter identifier name in content repository as {arg}")
def step_impl(identifier_name):
    """I should be able to enter identifier name in content repository as '<identifier_name>'"""
    Contentrepositoryutility.enter_identifier_name_in_content_repository(identifier_name)
    
@when("Open the identifier properties either by pressing enter or double click on the selected identifier in content repository as {arg}")
def step_impl(identifier_name):
    """Open the identifier properties either by pressing enter or double click on the selected identifier in content repository as '<identifier_name>'"""
    Contentrepositoryutility.select_identifier_in_content_repository(identifier_name)

@when("User closes the selected identifier by clicking on X button in content repository as {arg}")
def step_impl(identifier_name):
    """User closes the selected identifier by clicking on X button in content repository as '<identifier_name>'"""
    Contentrepositoryutility.close_selected_identifier_tab_in_content_repository(identifier_name)
    
@when("User fetches the properties of selected identifier in content repository as {arg}")
def step_impl(identifier_name):
    """User fetches the properties of selected identifier in content repository as '<identifier_name>'"""
    Contentrepositoryutility.fetch_identifier_properties_in_content_repository(identifier_name)
    
@when("Verify the title of the selected identifier in content repository as {arg}")
def step_impl(identifier_name):
    """Verify the title of the selected identifier in content repository as '<identifier_name>'"""
    Contentrepositoryutility.verify_workframe_title_contains_text(identifier_name)
    
@when("I DblClick on {arg} to expand nodes in CReditor screen")
def step_impl(param):
    """I DblClick on '<Identifier$$hierarchy>' to expand nodes in CReditor screen"""
    obj.doubleclickexpandnodesCReditor(param)

@when("I RClick on {arg} on nodes in CReditor screen")
def step_impl(param):
    """I RClick on '<Identifier$$hierarchy>' on nodes in CReditor screen"""
    obj.rightclickonnodesCReditor(param)
    
@then("I verify the nodes available in CR editor screen")
def step_impl():
    """I verify the nodes available in CR editor screen"""
    Contentrepositoryutility.Verify_nodes_CR()
   
@then("I verify the newly {arg} created folder is editable or not")
def step_impl(param):
    """I verify the newly '<folder>' created folder is editable or not"""
    obj.verifyfolderiseditableCReditor(param) 

@when("I press F2 to rename nodes in CR editor {arg}")
def step_impl(param):
    """I press F2 to rename nodes in CR editor '<Identifier$$hierarchy>'"""
    obj.renamefolderF2key(param) 

@when("I update properties of folder in Content repository as {arg}")
def step_impl(param):
    """I update properties of folder in Content repository as'<Identifier,field,value>'"""
    obj.updatefolderproperties(param)
    
@then("I verify the folder properties identifier is valid")
def step_impl():
    """I verify the folder properties identifier is valid"""
    obj.verifyvalidationrulesfolderprop()
    
@then("I verify the content list of the created content")
def step_impl():
    """I verify the content list of the created content"""
    Contentrepositoryutility.Verify_Content_list_of_created_content()

@then("I verify the created content is in editing state")
def step_impl():
    """I verify the created content is in editing state"""
    Contentrepositoryutility.verify_Content_is_in_editing_state()
    
@when("I check naming validation of created content as {arg}")
def step_impl(Enter_name):
    """I check naming validation of created content as '<Enter_name>'"""
    Contentrepositoryutility.rename_content_validation(Enter_name)
    
@when("I Right click on created content as {arg}")
def step_impl(identifier):
    """I Right click on created content as '<identifier>'"""
    Contentrepositoryutility.rclick_on_content(identifier)

@then("I verify sorting and filter of content as {arg}")
def step_impl(identifier):
    """I verify sorting and filter of content as '<filter_name>'"""
    Contentrepositoryutility.Select_filters_created_content(filter_name)
