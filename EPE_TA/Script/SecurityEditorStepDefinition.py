"""SecurityEditorWorkFlow""" 

from SecurityEditorWorkFlow import SecurityEditorWorkFlow
from TopologyWorkFlow import TopologyWorkFlow
from SystemExplorerScreenWorkFlow import SystemExplorerScreenWorkFlow
from ProjectExplorerTabWorkFlow import ProjectExplorerTabWorkFlow
from RefineOfflineWorkFlow import RefineOfflineWorkFlow
import CommonUtil
import Applicationutility
import Topologyexplorerutility

obj=SecurityEditorWorkFlow()
sobj=SystemExplorerScreenWorkFlow()
pobj=ProjectExplorerTabWorkFlow()
robj=RefineOfflineWorkFlow()

@when("I verify the text checkbox value as {arg}")
def step_impl(identifier):
    """I verify the text checkbox value as '<Identifier>'"""
    obj.verifydropdowntextSE(identifier)

@when("I select a value from the dropdown in policies page tab as {arg}")
def step_impl(identifier):
    """I select a value from the dropdown in policies page tab as '<Identifier>'"""
    obj.selectdropdownvaluepoliciesSE(identifier) 
    
@when("I select a value from the product dropdown in user information page tab as {arg}")
def step_impl(product_name):
    """I select a value from the product dropdown in user information page tab as '<product_name>'"""
    obj.selectdropdownvalueproductuserinformationSE(product_name)

@when("I select a value from the username dropdown in user information page tab as {arg}")
def step_impl(user_name):
    """I select a value from the username dropdown in user information page tab as '<user_name>'"""
    obj.selectdropdownvalueusernameuserinformationSE(user_name)
    
@when("I verify the login radio button as {arg}")
def step_impl(identifier):
    """I verify the login radio button as '<Identifier>'"""
    obj.verifyloginradiobuttonSE(identifier)
    
@when("I select a button in security editor window as {arg}")
def step_impl(identifier):
    """I select a button in security editor window as '<Identifier>'"""
    obj.selectbuttonSE(identifier)

@when("I select a button in policies tab in security editor window as {arg}")
def step_impl(identifier):
    """I select a button in policies tab in security editor window as '<Identifier>'"""
    obj.selectbuttonpoliciestabSE(identifier)

@when("I edit a textbox value in policies tab in security editor window as {arg}")
def step_impl(value):
    """I edit a textbox value in policies tab in security editor window as '<value>'"""
    obj.EdittextboxvaluepoliciestabSE(value) 
    
@when("I verify the textbox value in policies tab in security editor window as {arg}")
def step_impl(value):
    """I verify the textbox value in policies tab in security editor window as '<value>'"""
    obj.verifytextboxvaluepoliciestabSE(value)
    
@when("I verify the static message in security editor window as {arg}")
def step_impl(identifier):
    """I verify the static message in security editor window as '<identifier>'"""
    obj.verifystaticmessageSE(identifier)

@when("I select a page tab in security editor window as {arg}")
def step_impl(identifier):
    """I select a page tab in security editor window as '<identifier>'"""
    obj.selectpagetabSE(identifier)
        
@when("I verify the password validity button in policies tab in security editor window as {arg}")
def step_impl(param):
    """I verify the password validity button in policies tab in security editor window as '<param>'"""
    obj.verifypasswordbuttonpoliciestabSE(param)
    
@when("I edit the textbox1 value in user information tab in security editor window as {arg}")
def step_impl(value):
    """I edit the textbox1 value in user information tab in security editor window as '<value>'"""
    obj.Edittextbox1valueuserinformationtabSE(value)
    
@when("I edit the textbox2 value in user information tab in security editor window as {arg}")
def step_impl(value):
    """I edit the textbox2 value in user information tab in security editor window as '<value>'"""
    obj.Edittextbox2valueuserinformationtabSE(value)
    
@when("I select a button in user information tab in security editor window as {arg}")
def step_impl(identifier):
    """I select a button in user information tab in security editor window as '<identifier>'"""
    obj.selectbuttonuserinformationtabSE(identifier)
    
    
    
    

    
    
    
    

    

    
    
    
    
    
    
    
    
    
        
    
    
    
    