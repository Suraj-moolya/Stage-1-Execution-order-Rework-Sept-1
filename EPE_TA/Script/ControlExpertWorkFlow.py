"""ControlExpertWorkFlow"""  

from ControlExpert import ControlExpert
import Applicationutility
import Controlexpertutility
class ControlExpertWorkFlow:
    """ControlExpertWorkFlow"""
    controlexpert_obj = ControlExpert()

        
    def buttonpropertiesofdeviceokceselected(self):
        """controlexpert_obj.propertiesofdeviceokcebutton"""
        ControlExpertWorkFlow.controlexpert_obj.propertiesofdeviceokcebutton.click()
        
        
    def buttonfullscreenceselected(self):
        """controlexpert_obj.fullscreencebutton"""
        ControlExpertWorkFlow.controlexpert_obj.fullscreencebutton.click()
        
        
    def buttonclosefullscreenceselected(self):
        """controlexpert_obj.closefullscreencebutton"""
        ControlExpertWorkFlow.controlexpert_obj.closefullscreencebutton.click()
        
        
    def buttonunlocksafetyprotectionceselected(self):
        """controlexpert_obj.unlocksafetyprotectioncebutton"""
        ControlExpertWorkFlow.controlexpert_obj.unlocksafetyprotectioncebutton.click()
        
    def ClicktabitemEIOconfigwindow(self,identifiers):
            """ClicktabitemEIOconfigwindow"""
            try:
                Controlexpertutility.Click_tab_item_EIO_config_window(identifiers)
            except Exception as ex:
                raise Exception(ex) from ex  
                
    def buttonbuildanddeploychangesselected(self):
            """controlexpert_obj.buildanddeploychangesbutton"""
            ControlExpertWorkFlow.controlexpert_obj.buildanddeploychangesbutton.click()  

    def ClickonatextobjectblockRefineOffline(self,identifier):
            """ClickonatextobjectblockRefineOffline"""
            try:
                Controlexpertutility.Click_on_a_text_object_block_Refine_Offline(identifier)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def DoubleclickprojectbrowseritemCE(self,val):
            """DoubleclickprojectbrowseritemCE"""
            try:
                Controlexpertutility.doubleclick_project_browser_item_CE(val)
            except Exception as ex:
                raise Exception(ex) from ex

    def verifymoduleinadddevicewindowCE(self,module):
            """verifymoduleinadddevicewindowCE"""
            try:
                Controlexpertutility.verify_module_in_add_device_window_CE(module)
            except Exception as ex:
                raise Exception(ex) from ex        
  
    def columnconfigurationokbutton(self):
        """controlexpert_obj.columnconfigurationwindow"""
        ControlExpertWorkFlow.controlexpert_obj.columnconfigurationwindow.click()  
        
    def verifyengineeringlinkinsecurityeditor(self):
                """verifyengineeringlinkinsecurityeditor"""
                try:
                    Controlexpertutility.verify_engineering_link_in_security_editor()
                except Exception as ex:
                    raise Exception(ex) from ex    
                    
    def verifyservicesinsecurityeditor(self):
                    """verifyservicesinsecurityeditor"""
                    try:
                        Controlexpertutility.verify_services_in_security_editor()
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def verifyaccesscontrolinsecurityeditor(self):
                        """verifyaccesscontrolinsecurityeditor"""
                        try:
                            Controlexpertutility.verify_access_control_in_security_editor()
                        except Exception as ex:
                            raise Exception(ex) from ex
                            
    def changeengineeringlinkdropdown(self):
                            """changeengineeringlinkdropdown"""
                            try:
                                Controlexpertutility.change_engineering_link_dropdown()
                            except Exception as ex:
                                raise Exception(ex) from ex