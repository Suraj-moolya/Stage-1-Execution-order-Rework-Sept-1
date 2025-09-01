﻿"""TopologyWorkFlow"""
from TopologyWorkFlow import TopologyWorkFlow
from SystemExplorerScreenWorkFlow import SystemExplorerScreenWorkFlow
from ProjectExplorerTabWorkFlow import ProjectExplorerTabWorkFlow
from RefineOfflineWorkFlow import RefineOfflineWorkFlow
import CommonUtil
import Applicationutility
import Topologyexplorerutility

obj=TopologyWorkFlow()
sobj=SystemExplorerScreenWorkFlow()
pobj=ProjectExplorerTabWorkFlow()
robj=RefineOfflineWorkFlow()

        
@when("I Select context menu item EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    obj.textboxtopologyexplorertreeselectcontextmenuitemec(topologyExplorerTree1)
  
@when("I select deploy popup dropdown value TE project dropdown in topology as {arg}")
def step_impl(projectDropdown2):
    """I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'"""
    obj.textboxprojectdropdownselectdeploypopupdropdownvaluete(projectDropdown2)
  
@when("I select deploy popup dropdown value TE Executables dropdown in topology as {arg}")
def step_impl(executablesDropdown3):
    """I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'"""
    obj.textboxprojectdropdownselectdeploypopupdropdownvaluete(executablesDropdown3)

@when("I entered backup data description in topology as {arg}")
def step_impl(backupDataDescription3):
    """I entered backup data description in topology as '<backup data description3>'"""
    obj.textboxbackupdatadescriptionentered(backupDataDescription3)
  
@when("I Select deploy data from selection grid TE deploy data selection grid in topology")
def step_impl():
    """I Select deploy data from selection grid TE deploy data selection grid in topology"""
    obj.textboxdeploydataselectiongridselectdeploydatafromselectiongridte()  
    
#@when("I select start engine checkbox in in topology")
#def step_impl():
#    """I select start engine checkbox in in topology"""
#    obj.clickstartenginecheckbox()

@when("I Enter Controller Password TE New Password box in topology as {arg}")
def step_impl(newPasswordBox1):
    """I Enter Controller Password TE New Password box in topology as '<New Password box1>'"""
    obj.textboxnewpasswordboxentercontrollerpasswordte(newPasswordBox1)
  
@when("I Enter Controller Password TE Confirm Password box in topology as {arg}")
def step_impl(confirmPasswordBox2):
    """I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'"""
    obj.textboxnewpasswordboxentercontrollerpasswordte(confirmPasswordBox2)
  
@then("Verify entered Controller Password valid invalid TE New Password box in topology as {arg}")
def step_impl(newPasswordBox4):
    """Verify entered Controller Password valid invalid TE New Password box in topology as '<New Password box4>'"""
    obj.textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte(newPasswordBox4)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify entered Controller Password valid invalid TE Confirm Password box in topology as {arg}")
def step_impl(confirmPasswordBox5):
    """Verify entered Controller Password valid invalid TE Confirm Password box in topology as '<Confirm Password box5>'"""
    obj.textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte(confirmPasswordBox5)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I search template browser EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I search template browser EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    obj.textboxtopologyexplorertreesearchtemplatebrowserec(topologyExplorerTree1)
    
@when("I Select template EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Select template EC Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    obj.textboxtopologyexplorertreeselecttemplateec(topologyExplorerTree2)
    
@when("I DblClick template TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    obj.textboxtopologyexplorertreedblclicktemplatete(topologyExplorerTree1)
    
@when("I Expand communication tab TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    obj.textboxtopologyexplorertreeexpandcommunicationtabte(topologyExplorerTree2)
    
@when("I edit IP Address Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree3):
    """I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'"""
    obj.textboxtopologyexplorertreeeditipaddress(topologyExplorerTree3)
    
@when("I RClick template TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I RClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    obj.textboxtopologyexplorertreerclicktemplatete(topologyExplorerTree1)
    
@when("I Click on MenuItem in TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Click on MenuItem in TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    obj.textboxtopologyexplorertreeclickonmenuiteminte(topologyExplorerTree2)
    
@when("I modal dialog window select Item Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree3):
    """I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'"""
    obj.textboxtopologyexplorertreemodaldialogwindowselectitem(topologyExplorerTree3)

@when(r'I double-click on "([^"]+)" "([^"]+)" and "([^"]+)" in the catalog browser')
def step_impl(main_folder, subfolder, final_item):
    """I double-click on '<main_folder>' '<subfolder>' and '<final_item>' in the catalog browser"""
    obj.doubleclickcatalogbrowserte(main_folder, subfolder, final_item)

@when("I set the IP address to '(.*)' and subnet mask to '(.*)' in STBIsland properties")
def step_impl(ip_address, subnet_mask):
    """I set the IP address to '<ip_address>' and subnet mask to '<subnet_mask>' in STBIsland properties"""
    obj.setipandsubnetinstbpropertieste(ip_address, subnet_mask)
    
@when("I selected Close Button in STB Properties Tab")
def step_impl():
    """I selected Close Button in STB Properties Tab"""
    obj.closebuttonstbpropertieste()
    
@when("I Select particular {arg} for each  Controller in physical connection")
def step_impl(network):
    """I Select particular '<network>' for each  Controller in physical connection"""
    obj.configureethernetnetworkinphysicalconnectionte(network)
    
@when("I click {arg} in Tool Bar")
def step_impl(menu):
  """I click '<menu>' in Tool Bar"""
  Applicationutility.wait_in_seconds(1000, 'Wait')
  obj.clickbuttontoolbar(menu)
  
@when("I click {arg} in Tool Bar popup window")
def step_impl(menu_item):
  """I click '<menu_item>' in Tool Bar popup window"""
  obj.clickbuttontoolmenubar(menu_item)
  
@when("I wait for the Build Project window to disappear")
def step_impl():
  """I wait for the Build Project window to disappear"""
  Topologyexplorerutility.wait_for_dtm_update()
  
  
@when("I right-click on {arg} in the Topology Explorer")
def step_impl(node_name):
    """I right-click on '<node_name>' in the Topology Explorer"""
    Applicationutility.wait_for_execution()
    sobj.buttonsystemexplorernoderightclickonnodes(node_name)
    
@when("I Select context menu item EC in Topology Explorer as {arg}")
def step_impl(action):
    """I Select context menu item EC in Topology Explorer as '<action>'"""
    pobj.textboxprojectbrowserselectcontextmenuitemec(action)
    
@when("I selected Close Configuration window in Topology Explorer")
def step_impl():
    """I selected Close Configuration window in Topology Explorer"""
    obj.selectclosebutton()
    
@when("I click modal dialog window {arg} in Topology Explorer")
def step_impl(button):
    """I click modal dialog window '<button>' in Topology Explorer"""
    Applicationutility.wait_for_execution()
    pobj.textboxprojectbrowserclickmodaldialogwindow(button)
    
@when("I Select {arg} in hardware catalog window")
def step_impl(tabname):
    """I Select '<tabname>' in hardware catalog window"""
    obj.selecttabinhardwarecatalog(tabname)
    
@when("I double click on {arg} in hardware catalog window")
def step_impl(property):
    """I double click on '<property>' in hardware catalog window"""
    obj.dblclickpropinhardwarecatalog(property)
    
@when("I click Update button on hardware catalog window")
def step_impl():
    """I click Update button on hardware catalog window"""
    obj.updatebtninhardwarecatalog()
    
@when("I select {arg} on control expert popub window")
def step_impl(button):
    """I select '<button>' on control expert popub window"""
    obj.controlexppopup(button)
    
@when("I double click on the installed {arg} on DTM Browser")
def step_impl(prm):
    """I double click on the installed '<prm>' on DTM Browser"""
    Applicationutility.wait_for_execution()
    obj.dblclickinstalledprm(prm)
    
@when("I right click on the installed {arg} on DTM Browser")
def step_impl(prm):
    """I right click on the installed '<prm>' on DTM Browser"""
    Applicationutility.wait_for_execution()
    obj.rightclickinstalledprm(prm)

@when("I double click on {arg} in PRM Window")
def step_impl(settings):
    """I double click on '<settings>' in PRM Window"""
    Applicationutility.wait_for_execution()
    obj.dblclicksettingsprm(settings)

@when("I update the {arg} in PRM Window")
def step_impl(ip_address):
    """I update the '<ip_address>' in PRM Window"""
    obj.updateipaddresinprm(ip_address)

@when("I click {arg} on PRM Window")
def step_impl(button1):
    """I click '<button1>' on PRM Window"""
    obj.clickbtninprm(button1)
    
@when("I selected Save PRM Configuration in Configuration Window")
def step_impl():
    """I selected Save PRM Configuration in Configuration Window"""
    robj.buttonsaverefineofflineselected()
    Applicationutility.wait_in_seconds(3000, 'Wait')
    
@when("I selected {arg} Button in hardware catalog window")
def step_impl(button):
    """I selected '<button>' Button in hardware catalog window"""
    obj.hardwarecatalogclosebtn(button)
    
@when("I select {arg} in PLC window")
def step_impl(button):
    """I select '<button>' in PLC window"""
    obj.selectbtnplc(button)
    
@when("I select {arg} rack in PLC bus Window")
def step_impl(number):
    """I select '<number>' rack in PLC bus Window"""
    obj.selectrackplc(number)
    
@when("I select {arg} in New Device PopUp Window")
def step_impl(button):
    """I select '<button>' in New Device PopUp Window"""
    obj.clickbtninnewdevicepopup(button)
    
@when("I selected {arg} Button in BME window")
def step_impl(button):
    """I selected '<button>' Button in BME window"""
    obj.bmeselectbtn(button)
    
@when("I selected {arg} in DTM Browser Modal Dialogue window")
def step_impl(option):
    """I selected '<option>' in DTM Browser Modal Dialogue window"""
    obj.selectoptioninmodaldialogue(option)
    
@when("I select {arg} and {arg} in DTM Browser Add device window")
def step_impl(protocol, device):
    """I select '<protocol>' and '<device>' in DTM Browser Add device window"""
    obj.selectprotocolinadddevice(protocol, device)
    
@when("I Double Click on {arg} in channel Window")
def step_impl(property):
    """I Double Click on '<property>' in channel Window"""
    obj.textboxtopologyexplorerdoubleclickonaddwindow(property)
    
@when("I select {arg} in DTM Browser property device window")
def step_impl(button):
    """I select '<button>' in DTM Browser property device window"""
    obj.selectbtninadddeviceprop(button)
    
@when("I selected the checkbox for channel {arg} in the HART configuration")
def step_impl(num):
    """I selected the checkbox for channel '<num>' in the HART configuration"""
    obj.clickchannelcheckboxinhart(num)
    
@when("I click Validate button on control configuration window")
def step_impl():
    """I click Validate button on control configuration window"""
    obj.validatebtnincontrolconfig()
    
@when("I Select {arg} in Workstation Deployment Window")
def step_impl(ip):
    """I Select '<ip>' in Workstation Deployment Window"""
    obj.selectipindeployworkstationte(ip)
    
    
@when("I Verify {arg} in Hardware Catalog Window")
def step_impl(smp):
    """I Verify '<smp>' in Hardware Catalog Window"""
    obj.textboxtopologyexplorerhardwarecatalogdevices(smp)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Double Click open the {arg} in Topology Explorer")
def step_impl(node):
    """I Double Click open the '<node>' in Topology Explorer"""
    obj.opennetworksfolder(node)
    
    
@when("I Double Click open the {arg}")
def step_impl(ethernet):
    """I Double Click open the '<ethernet network>'"""
    obj.opennetwork(ethernet)
    
    
@then("I Expand {arg} and Verify it is mapped to {arg}")
def step_impl(interface, controller):
    """I Expand '<physical interface>' and Verify it is mapped to '<controller>'"""
    obj.verifynetworkpanel(interface, controller)

@when("I selected {arg} from the dropdown in the Reference Filtering tab")
def step_impl(property):
    """I selected '<property>' from the dropdown in the Reference Filtering tab"""
    Applicationutility.wait_in_seconds(2000, 'Loading!!')
    obj.textboxtopologyexplorerdoubleclickonftdconfigurationwindow(property)
    
@when("I selected {arg} and {arg} in the Options Modules tab")
def step_impl(slot, module):
  """I selected '<slot>' and '<module>' in the Options Modules tab"""
  obj.textboxtopologyexplorerselectslotinftdconfigurationwindow(slot, module)
    
@when("I clicked {arg} in the DTM channel window")
def step_impl(button):
  """I clicked '<button>' in the DTM channel window"""
  obj.textboxtopologyexplorerclickbuttoninfigurationwindow(button)
    
@then("I verify the Device Name and Reference in the DTM Channel window")
def step_impl():
  """I verify the Device Name and Reference in the DTM Channel window"""
  obj.textboxtopologyexplorerverifydtmdeviceinfigurationwindow()
  
@when("I selected {arg} from the submenu in the DTM Browser Modal Dialogue window")
def step_impl(option):
  """I selected '<option>' from the submenu in the DTM Browser Modal Dialogue window"""
  obj.selectsubmenuoptioninmodaldialogue(option)
  
@when("I click {arg} in the DTM Browser Modal Dialogue window")
def step_impl(option):
  """I click '<option>' in the DTM Browser Modal Dialogue window"""
  obj.selectfinaloptioninmodaldialogue(option)
  
@when("I import the required module {arg} to configured modules")
def step_impl(module):
  """I import the required module '<module>' to configured modules"""
  obj.importmodulesinftdconfigwindow(module)
  
@when("I click {arg} and close the DTM Window")
def step_impl(button):
  """I click '<button1>' and close the DTM Window"""
  obj.clickbuttoninftdconfigwindow(button)
  
@when("I click on required {arg} on DTM Browser")
def step_impl(channel):
  """I click on required '<channel>' on DTM Browser"""
  obj.clickchannelinftdconfigwindow(channel)
  
@when("I select {arg} in FDT Configuration Window")
def step_impl(tab):
  """I select '<tab>' in FDT Configuration Window"""
  obj.selecttabinftdconfigwindow(tab)
    
@when("I update the {arg} in FDT Configuration Window")
def step_impl(ip_address):
    """I update the '<ip_address>' in FDT Configuration Window"""
    obj.updateipinftdconfigwindow(ip_address) 

@when("I Double Click on propeties as {arg} available when window is open")
def step_impl(text):
    """I Double Click on propeties as {arg} available when window is open"""
    obj.dblclickpropertiesworkstation(text)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Expand on propeties header as {arg} available when window is open")
def step_impl(text):
    """I Expand on propeties header as {arg} available when window is open"""
    obj.expandpropertiesworkstation(text)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Change the port number of workstation as {arg}")
def step_impl(text):
    """I Change the port number of workstation as {arg}"""
    obj.changeportnumberworkstation(text)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Right Click on the {arg} in Project Browser Pane")
def step_impl(item):
    """I Right Click on the '<item>' in Project Browser Pane"""
    obj.rightclickonprojectbrowserpane(item)

@when("I Select {arg} Tab in Project Browser Properties Window")
def step_impl(item):
    """I Select '<item>' Tab in Project Browser Properties Window"""
    obj.selecttabonprojectbrowserproperties(item)
    
@when("I Click Change Password Button for Firmware")
def step_impl():
    """I Click Change Password Button for Firmware"""
    obj.firmwarechangepassword()
    
@when("I Entered {arg} and {arg} in Modify Password Dialogue window")
def step_impl(oldpassword, password):
    """I Entered '<oldpassword>' and '<password>' in Modify Password Dialogue window"""
    obj.setoldpasswordandnewpasswordinmodifypassworddialogue(oldpassword, password)

@when("I Right_click_selected_project_browser_item_CE System Project in topology explorer as {arg}")
def step_impl(systemProject1):
    """I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'"""
    obj.textboxsystemprojectrightclickselectedprojectbrowseritemce(systemProject1)
  
@when("I click_MenuItem_Toolbar_CE System Project in topology explorer as {arg}")
def step_impl(systemProject2):
    """I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'"""
    obj.textboxsystemprojectclickmenuitemtoolbarce(systemProject2)
  
@when("I Select_network_CE System Project in topology explorer as {arg}")
def step_impl(systemProject3):
    """I Select_network_CE System Project in topology explorer as '<System Project3>'"""
    obj.textboxsystemprojectselectnetworkce(systemProject3)
    
@then("Verify_error_messages_in_Console OutputWindowPanel in topology as {arg}")
def step_impl(outputwindowpanel1):
      """Verify_error_messages_in_Console OutputWindowPanel in topology as '<OutputWindowPanel1>'"""
      obj.textboxoutputwindowpanelverifyerrormessagesinconsole(outputwindowpanel1)
      Applicationutility.take_screenshot("Full Screenshot")
      
@when("I Enter Controller Password deploy screen TE Confirm Password box in topology as {arg}")
def step_impl(confirmPasswordBox3):
    """I Enter Controller Password deploy screen TE Confirm Password box in topology as '<Confirm Password box3>'"""
    obj.textboxconfirmpasswordboxentercontrollerpassworddeployscreente(confirmPasswordBox3)
    
@when("I Double click on the Automatic blocking of service port on standby CPU in service port")
def step_impl():
    """I Double click on the Automatic blocking of service port on standby CPU in service port"""
    obj.checkboxcheckautomaticblocking()
    

