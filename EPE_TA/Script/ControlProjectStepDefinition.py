from ControlProjectWorkFlow import ControlProjectWorkFlow

import Applicationutility
import CommonUtil
import Controlprojectutility

obj=ControlProjectWorkFlow()

@when("I rename FBD Section in create FBD Section popup as {arg}")
def step_impl(name):
  """I rename FBD Section in create FBD Section popup as {arg}"""
  obj.renamefbdsectioninpopup(name)

@when("I select path of FBD in FBD creation pop up as {arg}")
def step_impl(param):
  """I select path of FBD in FBD creation pop up as {arg}"""
  obj.selectpathaoffbdasmastorfast(param)
  
@then("I verify the order of the FBD section in containerdock")
def step_impl():
  """I verify the order of the FBD section in containerdock"""
  obj.verifycontainerdockforfbdsectionandorder()