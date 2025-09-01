
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