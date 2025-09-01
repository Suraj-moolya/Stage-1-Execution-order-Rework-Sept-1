﻿"""TopologyExporerTab"""
from MapBase import MapBase

class TopologyExplorerTab(MapBase):
    """TopologyExporerTab"""
        
    @property
    def closeabletabbutton(self):
        """closeabletabbutton"""
        return self.get_element("CloseableTab_TopologyExporerTab")
        
    @property
    def configurationhardwarecatalog1(self):
        """configurationhardwarecatalog1"""
        return self.get_element("ConfigurationHardwareCatalog1_TopologyExporerTab")
              
    @property
    def systemprojectbutton(self):
        """systemprojectbutton"""
        return self.get_element("SystemProject_TopologyExporerTab")
              
    @property
    def toolboxcatalogbutton(self):
        """toolboxcatalogbutton"""
        return self.get_element("ToolboxCatalog_TopologyExporerTab")
        
    @property
    def deviceshardwarecatalog(self):
        """deviceshardwarecatalog"""
        return self.get_element("DevicesHardwareCatalog_TopologyExporerTab")
        
    @property
    def dtmbrowserprop(self):
        """dtmbrowserprop"""
        return self.get_element("DTMBrowserprop_TopologyExporerTab")
        
    @property
    def bmehartwindow(self):
        """bmehartwindow"""
        return self.get_element("BMEHart_TopologyExporerTab")
        
    @property
    def hartmodulecheckbox(self):
        """hartmodulecheckbox"""
        return self.get_element("Hartmodulecheck_TopologyExporerTab")
        
    @property
    def plcbuswindow(self):
        """plcbuswindow"""
        return self.get_element("PLCBuswindow_TopologyExporerTab")
        
    @property
    def prmconfigwindow(self):
        """prmconfigwindow"""
        return self.get_element("PRMconfigwindow_TopologyExporerTab")
        
    @property
    def updatebutton(self):
        """updatebutton"""
        return self.get_element("UpdateButton_TopologyExporerTab")
        
    @property
    def prmgensettings(self):
        """prmgensettings"""
        return self.get_element("PRMgensettings_TopologyExporerTab")
        
    @property
    def prmgensettingsrefineonline(self):
        """prmgensettings"""
        return self.get_element("PRMgensettingsrefineonline_TopologyExporerTab")
        
    @property
    def configurationhardwarecatalog(self):
        """configurationhardwarecatalog"""
        return self.get_element("ConfigurationHardwareCatalog_TopologyExporerTab")
              
    @property
    def catalogbutton(self):
        """catalogbutton"""
        return self.get_element("Catalog_TopologyExporerTab")
              
    @property
    def propertiesgridbutton(self):
        """propertiesgridbutton"""
        return self.get_element("PropertiesGrid_TopologyExporerTab")
              
    @property
    def propertydescriptiontabbutton(self):
        """propertydescriptiontabbutton"""
        return self.get_element("PropertyDescriptionTab_TopologyExporerTab")
              
    @property
    def propertyconfigurationtabbutton(self):
        """propertyconfigurationtabbutton"""
        return self.get_element("PropertyConfigurationTab_TopologyExporerTab")
              
    @property
    def propertyservicestabbutton(self):
        """propertyservicestabbutton"""
        return self.get_element("PropertyServicesTab_TopologyExporerTab")
              
    @property
    def propertyioprofiletabbutton(self):
        """propertyioprofiletabbutton"""
        return self.get_element("PropertyIOProfileTab_TopologyExporerTab")
              
    @property
    def propertysecuritytabbutton(self):
        """propertysecuritytabbutton"""
        return self.get_element("PropertySecurityTab_TopologyExporerTab")
        
    @property
    def passwordgridbutton(self):
        """passwordgridbutton"""
        return self.get_element("Passwordgrid_TopologyExporerTab")
        
    @property
    def newpasswordboxtextbox(self):
        """newpasswordboxtextbox"""
        return self.get_element("NewPasswordbox_TopologyExporerTab")
        
    @property
    def ConfirmPasswordboxtextbox(self):
        """ConfirmPasswordboxtextbox"""
        return self.get_element("ConfirmPasswordbox_TopologyExporerTab")
        
    @property
    def Closetmbutton(self):
        """Closetmbutton"""
        return self.get_element("ClosebuttonTM_TopologyExporerTab")
        
    @property
    def controllerpropertytab(self):
        """controllerpropertytab"""
        return self.get_element("ControllerPropertytab_TopologyExporerTab")
        
    @property
    def oldpasswordboxboxtextbox(self):
        """oldpasswordboxboxtextbox"""
        return self.get_element("OldPasswordBox_TopologyExporerTab")
        
    @property
    def controllerphysicalconnectiontab(self):
        """controllerphysicalconnectiontab"""
        return self.get_element("ControllerPhysicalconnectiontab_TopologyExporerTab")
              
    @property
    def stbpropertiesbutton(self):
        """stbpropertiesbutton"""
        return self.get_element("STBProperties_TopologyExporerTab")
              
    @property
    def stbpropertiesclosebutton(self):
        """stbpropertiesclosebutton"""
        return self.get_element("STBPropertiesClosebutton_TopologyExporerTab")
        
    @property
    def topologyconfigurationwindow(self):
        """topologyconfigurationwindow"""
        return self.get_element("TopologyConfigurationWindow_TopologyExporerTab")
        
    @property
    def dtmbroswerwindow(self):
        """dtmbroswerwindow"""
        return self.get_element("DTMBrowserHost_TopologyExporerTab")
        
    @property
    def paneleditbutton(self):
        """paneleditbutton"""
        return self.get_element("PanelEditButton_TopologyExporerTab")

    def primaryaddresslistdropdown(self):
        """primaryaddresslistdropdown"""
        return self.get_element("PrimaryAddressList_TopologyExporerTab")
        
    @property
    def startenginecheckbox(self):
        """startenginecheckbox"""
        return self.get_element("StartEngineCheckbox_TopologyExporerTab")
   
    @property
    def passwordokbutton(self):
        """startenginecheckbox"""
        return self.get_element("passwordOKButton_TopologyExporerTab")     
    
    @property
    def deployokbutton(self):
        """deployokbutton"""
        return self.get_element("DeployOK_TopologyExporerTab")  
        
    @property
    def deploycheckbox(self):
        """deploycheckbox"""
        return self.get_element("DeployCheckbox_TopologyExporerTab")

    @property
    def openethernetnetwork(self):
        """checkethernetnetwork"""
        return self.get_element("OpenEthernetNetwork_TopologyExplorerTab")
        
    @property
    def networkpanel(self):
        """checkethernetnetwork"""
        return self.get_element("NetworkPanel_TopologyExplorerTab")
     
    @property
    def fdtconfigurationwindowtextbox(self):
        """oldpasswordboxtextbox"""
        return self.get_element("fdtConfigurationWindow_TopologyExporerTab")
              
    @property
    def dtmdevicewindowtextbox(self):
        """dtmdevicewindowtextbox"""
        return self.get_element("DTMDevice_TopologyExporerTab")
              
    @property
    def ipconfigfdtwindowtextbox(self):
        """dtmdevicewindowtextbox"""
        return self.get_element("IPConfigFDT_TopologyExporerTab")
              
    @property
    def updateprojecttab(self):
        """updateprojecttab"""
        return self.get_element("UpdateProjectTab_TopologyExporerTab")
              
    @property
    def templatebrowsertab(self):
        """templatebrowsertab"""
        return self.get_element("TemplateBrowser_TopologyExporerTab")
