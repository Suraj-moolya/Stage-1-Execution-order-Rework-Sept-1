"""ControlExpertWorkFlow"""
from ControlExpertWorkFlow import ControlExpertWorkFlow
import CommonUtil
import Applicationutility

obj=ControlExpertWorkFlow()

        
@when("I selected Properties of device OK CE in control expert")
def step_impl():
    """I selected Properties of device OK CE in control expert"""
    obj.buttonpropertiesofdeviceokceselected()
  
@when("I selected Full Screen CE in control expert")
def step_impl():
    """I selected Full Screen CE in control expert"""
    obj.buttonfullscreenceselected()
  
@when("I selected Close Full Screen CE in control expert")
def step_impl():
    """I selected Close Full Screen CE in control expert"""
    obj.buttonclosefullscreenceselected()
  
@when("I selected Unlock Safety Protection CE in control expert")
def step_impl():
    """I selected Unlock Safety Protection CE in control expert"""
    obj.buttonunlocksafetyprotectionceselected()
    
    
@when("I selected Build and Deploy Changes in control expert")
def step_impl():
    """I selected Build and Deploy Changes in control expert"""
    obj.buttonbuildanddeploychangesselected()

@when("I click on text object block in refine offline as {arg}")
def step_impl(identifier):
    """I click on text object block in refine offline as '<identifier>'"""
    obj.ClickonatextobjectblockRefineOffline(identifier)
    
@when("I double click on a project browser item as {arg}")
def step_impl(val):
    """I double click on a project browser item as '<val>'"""
    obj.DoubleclickprojectbrowseritemCE(val)
 
@when("I verify the module name in add device window as {arg}")
def step_impl(module):
    """I verify the module name in add device window as '<module>'"""
    obj.verifymoduleinadddevicewindowCE(module)   
    
@when("I selected Ok column configuration window in control expert")
def step_impl():
    """I selected Ok column configuration window in control expert"""
    obj.columnconfigurationokbutton()    
    
@then("I verify the engineering link mode is default state of security tab window")
def step_impl(module):
    """I verify the engineering link mode is default state of security tab window"""
    obj.verifyengineeringlinkinsecurityeditor(module)
    
@then("I verify the default state of service module in security tab window")
def step_impl(module):
    """I verify the default state of service module in security tab window"""
    obj.verifyservicesinsecurityeditor(module)  
    
@then("I verify the access control button in security tab window")
def step_impl(module):
    """I verify the access control button in security tab window"""
    obj.verifyaccesscontrolinsecurityeditor(module)
    
@when("I select a value from engineering link dropdown in security tab window as {arg}")
def step_impl():
    """I select a value from engineering link dropdown in security tab window as '<Value>'"""
    obj.changeengineeringlinkdropdown()  
    
    
    

        
  