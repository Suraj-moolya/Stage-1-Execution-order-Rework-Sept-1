"""SecurityEditorWorkFlow"""  

from SecurityEditor import SecurityEditor
from Topology import Topology
import Securityeditorutility
import Applicationutility
import Engineeringclientutility
import Topologyutility
import Actionutility
import Topologyexplorerutility
from SystemExplorerScreen import SystemExplorerScreen
from ControlExpert import ControlExpert

class SecurityEditorWorkFlow:
    """SecurityEditorWorkFlow"""
    securityeditor_obj = SecurityEditor()
    ses_obj = SystemExplorerScreen()
    con_obj = ControlExpert()
    
    
    def verifydropdowntextSE(self,identifier):
        """verifydropdowntextSE"""
        try:
            Securityeditorutility.verify_the_dropdown_text_SE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def selectdropdownvaluepoliciesSE(self,identifier):
        """selectdropdownvaluepoliciesSE"""
        try:
            Securityeditorutility.select_a_dropdown_value_policies_SE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def selectdropdownvalueproductuserinformationSE(self,product_name):
        """selectdropdownvalueproductuserinformationSE"""
        try:
            Securityeditorutility.select_a_dropdown_value_product_user_information_SE(product_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def selectdropdownvalueusernameuserinformationSE(self,user_name):
        """selectdropdownvalueusernameuserinformationSE"""
        try:
            Securityeditorutility.select_a_dropdown_value_username_user_information_SE(user_name)
        except Exception as ex:
            raise Exception(ex) from ex         
            
    def verifyloginradiobuttonSE(self,identifier):
        """verifyloginradiobuttonSE"""
        try:
            Securityeditorutility.verify_the_login_radiobutton_SE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex      

    def selectbuttonSE(self,identifier):
        """selectbuttonSE"""
        try:
            Securityeditorutility.select_a_button_security_editor_window(identifier)
        except Exception as ex:
            raise Exception(ex) from ex            
            
    def selectbuttonpoliciestabSE(self,identifier):
        """selectbuttonpoliciestabSE"""
        try:
            Securityeditorutility.select_a_button_policies_security_editor_window(identifier)
        except Exception as ex:
            raise Exception(ex) from ex     

    def EdittextboxvaluepoliciestabSE(self,value):
        """EdittextboxvaluepoliciestabSE"""
        try:
            Securityeditorutility.Edit_textbox_value_policies_SE(value)
        except Exception as ex:
            raise Exception(ex) from ex 
            
    def verifytextboxvaluepoliciestabSE(self,value):
        """verifytextboxvaluepoliciestabSE"""
        try:
            Securityeditorutility.Verify_textbox_value_policies_SE(value)
        except Exception as ex:
            raise Exception(ex) from ex 
 
    def verifystaticmessageSE(self,identifier):
        """verifystaticmessageSE"""
        try:
            Securityeditorutility.verify_static_message_security_editor_window(identifier)
        except Exception as ex:
            raise Exception(ex) from ex  
            
    def selectpagetabSE(self,identifier):
        """selectpagetabSE"""
        try:
            Securityeditorutility.select_a_page_tab_security_editor_window(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def verifypasswordbuttonpoliciestabSE(self,param):
        """verifypasswordbuttonpoliciestabSE"""
        try:
            Securityeditorutility.verify_the_password_button_policies_SE(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def Edittextbox1valueuserinformationtabSE(self,value):
        """Edittextbox1valueuserinformationtabSE"""
        try:
            Securityeditorutility.Edit_textbox1_value_user_information_SE(value)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def Edittextbox2valueuserinformationtabSE(self,value):
        """Edittextbox2valueuserinformationtabSE"""
        try:
            Securityeditorutility.Edit_textbox2_value_user_information_SE(value)
        except Exception as ex:
            raise Exception(ex) from ex

    def selectbuttonuserinformationtabSE(self,identifier):
        """selectbuttonuserinformationtabSE"""
        try:
            Securityeditorutility.select_a_button_user_information_security_editor_window(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
        
            
            
            
            
            
            
                     
            
        
            
        
            
            
            
            
            
            