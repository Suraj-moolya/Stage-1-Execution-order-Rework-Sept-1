"""ControlprojectWorkFlow"""

from ControlProjectTab import ControlProjectTab
import Applicationutility
import Controlprojectutility
import Engineeringclientutility

class ControlProjectWorkFlow:
    """ControlprojectbrowserWorkFlow"""
    cont_obj = ControlProjectTab()
    
    def renamefbdsectioninpopup(self,name):
      """renamefbdsectioninpopup"""
      try:
        Controlprojectutility.rename_FBDsection(name)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def selectpathaoffbdasmastorfast(self,param):
      """selectpathaoffbdasmastorfast"""
      try:
        Controlprojectutility.select_path_of_FBD_creation(param)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def verifycontainerdockforfbdsectionandorder(self):
      """verifycontainerdockforfbdsectionandorder"""
      try:
        Controlprojectutility.verify_FBD_order_containerdock()
      except Exception as ex:
        raise Exception(ex) from ex