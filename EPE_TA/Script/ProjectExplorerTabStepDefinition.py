﻿"""ProjectExplorerTabWorkFlow"""
from ProjectExplorerTabWorkFlow import ProjectExplorerTabWorkFlow
import CommonUtil
import Applicationutility
import Projectexplorertabutility
import ProjectExplorerTab

obj=ProjectExplorerTabWorkFlow()

        
@when("I RClick control project browser project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I RClick control project browser project browser in project explorer as '<project browser1>'"""
    obj.textboxprojectbrowserrclickcontrolprojectbrowser(projectBrowser1)
       
  
@when("I Select context menu item EC project browser in project explorer as {arg}")
def step_impl(projectBrowser2):
    """I Select context menu item EC project browser in project explorer as '<project browser2>'"""
    Applicationutility.wait_in_seconds(1500, 'Wait')
    obj.textboxprojectbrowserselectcontextmenuitemec(projectBrowser2)
    
@when("I Select controller in context menu as {arg}")
def step_impl(controller):
    """I Select controller in context menu as '<controller name>'"""
    obj.textboxprojectbrowserselectcontextsubmenuitemec(controller)
    
@when("I Rename the Folder as {arg}")  
@when("I rename the ControlProject as {arg}")
def step_impl(controller_name):
    """I rename the ControlProject as '<controller_name>'"""
    Applicationutility.wait_in_seconds(1000, 'Wait')
    obj.textboxprojectbrowserrename(controller_name)        
  
@when("I Wait for Execution project browser in project explorer")
def step_impl():
    """I Wait for Execution project browser in project explorer"""
    obj.textboxprojectbrowserwaitforexecution()

@when("I click {arg} Button in Import Warning Winow") 
@when("I click modal dialog window project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I click modal dialog window project browser in project explorer as '<project browser3>'"""
    Applicationutility.wait_for_execution()
    obj.textboxprojectbrowserclickmodaldialogwindow(projectBrowser3)
    
@when("I Select context submenu item TE project browser in project explorer as {arg}")
def step_impl(projectBrowser6):
    """I Select context submenu item TE project browser in project explorer as '<project browser6>'"""
    obj.textboxprojectbrowserselectcontextsubmenuitemte(projectBrowser6)
    
@when("I Dclick Control project broswer project browser in project explorer as {arg}")
def step_impl(projectBrowser7):
    """I Dclick Control project broswer project browser in project explorer as '<project browser7>'"""
    obj.textboxprojectbrowserdclickcontrolprojectbroswer(projectBrowser7)
  
@when("I Select combo box value properties dock TE project browser in project explorer as {arg}")
def step_impl(projectBrowser9):
    """I Select combo box value properties dock TE project browser in project explorer as '<project browser9>'"""
    obj.textboxprojectbrowserselectcomboboxvaluepropertiesdockte(projectBrowser9)
  
@when("I Executables Properties Executable Property in project explorer as {arg}")
def step_impl(executableProperty10):
    """I Executables Properties Executable Property in project explorer as '<Executable Property10>'"""
    obj.textboxexecutablepropertyexecutablesproperties(executableProperty10)
  
@when("I Generate and build controller project browser in project explorer")
def step_impl():
    """I Generate and build controller project browser in project explorer"""
    obj.textboxprojectbrowsergenerateandbuildcontroller()

  
@when("I Close all tab Deletes system project browser in project explorer")
def step_impl():
    """I Close all tab Deletes system project browser in project explorer"""
    obj.textboxprojectbrowserclosealltabdeletessystem()

@when(r"I Right Click on the Facet in Assignments Section as {arg} {arg}")
def step_impl(facet_name,action):
    obj.assignmentsrightclickunlinkfacets(facet_name,action)

  
@then("I verify Unlinked Status updated in Generation Section as {arg}")
def step_impl(param1):
    """I verify Unlinked Status updated in Generation Section as <param>"""
    obj.assignmentsunlinkfacets(param1)
    
@then("I verify Status updated in Generation Section as {arg}")
def step_impl(param1):
    """I verify Unlinked Status updated in Generation Section as <param>"""
    obj.assignmentsunlinkfacets(param1)
    
@when("I Click on FBDSection in Container Section {arg}")
def step_impl(param1):
    """I Click on FBDSection in Container Section '<FBDSection>'"""
    obj.click_fbdsection_select_pasteinstance(param1)
 
@when("I RClick on Container in Container Dock and select menu item as {arg}") 
@when("I RClick on FBDSection in Container Section and select menu item as {arg}")
def step_impl(param1):
    obj.Rclick_fbdsection_select_pasteinstance(param1)
    
@when("I Copy instances from FBDSection and paste in another FBDSection as {arg}")
def step_impl(param1):
    """I Copy instances from FBDSection and paste in another FBDSection as '<Param1>'"""
    obj.copyfromfbdinstancepastefbd(param1)

  
@when("I Right click container dock context menu item PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'"""
    obj.textboxcontainerdockrightclickcontainerdockcontextmenuitempe(containerDock1)
  
@when("I click modal dialog window container dock in project explorer as {arg}")
def step_impl(containerDock2):
    """I click modal dialog window container dock in project explorer as '<container dock2>'"""
    obj.textboxcontainerdockclickmodaldialogwindow(containerDock2)
  
@then("Verify Section Deleted in Control Project containers container dock in project explorer as {arg}")
def step_impl(containerDock3):
    """Verify Section Deleted in Control Project containers container dock in project explorer as '<container dock3>'"""
    obj.textboxcontainerdockverifysectiondeletedincontrolprojectcontainers(containerDock3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as '<container dock1>'"""
    obj.textboxcontainerdockdeletesectionincontrolprojectbyusingkeyboardactionspe(containerDock1)

@when("I Click on container section PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Click on container section PE container dock in project explorer as '<container dock1>'"""
    obj.textboxcontainerdockclickoncontainersectionpe(containerDock1)
  
@when("I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock2):
    """I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock2>'"""
    obj.textboxassignmentsdockdraganddropfacetfromassignmenttocontainersectionspe(assignmentsdock2)
  
@when("I Right click container dock context menu item PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock3):
    """I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'"""
    obj.textboxassignmentsdockrightclickcontainerdockcontextmenuitempe(assignmentsdock3)
  
@when("I Wait for Execution assignmentsdock in project explorer")
def step_impl():
    """I Wait for Execution assignmentsdock in project explorer"""
    obj.textboxassignmentsdockwaitforexecution()
  
@then("Verify generation status of facet from assignments PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock4):
    """Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'"""
    obj.textboxassignmentsdockverifygenerationstatusoffacetfromassignmentspe(assignmentsdock4)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Select context menu item EC container dock in project explorer as {arg}")
def step_impl(containerDock2):
    """I Select context menu item EC container dock in project explorer as '<container dock2>'"""
    obj.textboxcontainerdockselectcontextmenuitemec(containerDock2)
  
@then("Verify Action message in notification pannel container dock in project explorer as {arg}")
def step_impl(containerDock3):
    """Verify Action message in notification pannel container dock in project explorer as '<container dock3>'"""
    obj.textboxcontainerdockverifyactionmessageinnotificationpannel(containerDock3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify Action message in notification pannel project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """Verify Action message in notification pannel project browser in project explorer as '<project browser3>'"""
    obj.textboxcontainerdockverifyactionmessageinnotificationpannel(projectBrowser3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I customize CPB header checkbox PE project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I customize CPB header checkbox PE project browser in project explorer as '<project browser3>'"""
    obj.textboxprojectbrowsercustomizecpbheadercheckboxpe(projectBrowser3)
  
@when("I Click popup button object project browser in project explorer as {arg}")
def step_impl(projectBrowser4):
    """I Click popup button object project browser in project explorer as '<project browser4>'"""
    Applicationutility.wait_in_seconds(1000, 'wait')
    obj.textboxprojectbrowserclickpopupbuttonobject(projectBrowser4)
  
@then("Verify header control project browser PE project browser in project explorer as {arg}")
def step_impl(projectBrowser5):
    """Verify header control project browser PE project browser in project explorer as '<project browser5>'"""
    obj.textboxprojectbrowserverifyheadercontrolprojectbrowserpe(projectBrowser5)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify context menu item project browser in project explorer as {arg}")
def step_impl(menu_item):
    """verify context menu items project browser in project explorer"""
    obj.textboxprojectbrowserverifycontextmenuitem(menu_item)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when(r"I Right Click Facet in Assignment section as '(.*)' and Click '(.*)'")
def step_impl(facet_name, action):
    """I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'"""
    obj.rightclickinstanceandperformaction(facet_name, action)    
    
@then(r"I verify Status updated in Generation Section as '(.*)' '(.*)'")
def step_impl(facet_name, status):
    """I verify Status updated in Generation Section as '<facet_name>' '<status>'"""
    obj.verifyassignmentsstatus(facet_name, status)
    
@then("I Verify the facet generation status of all facets in Assignments Dock")
def step_impl():
    """I Verify the facet generation status of all facets in Assignments Dock"""
    Applicationutility.wait_for_execution()
    obj.projectexplorertabutilityverifyallfacetgenerationstatusassignmentdock()
    
    
@then("I Verify the new fbd section created")
def step_impl():
    """I Verify the new fbd section created"""
    obj.projectexplorertabutility_verify_section_containers_dock()
    
@when("I Collapse control project browser PE project browser in project explorer")
def step_impl():
    """I Collapse control project browser PE project browser in project explorer"""
    obj.textboxprojectbrowsercollapsecontrolprojectbrowserpe()

  
@when("I Expand control project browser PE project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I Expand control project browser PE project browser in project explorer as '<project browser1>'"""
    obj.textboxprojectbrowserexpandcontrolprojectbrowserpe(projectBrowser1)
    Applicationutility.take_screenshot("Full Screenshot")
  

@then("Verify build state of control executable PE project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """Verify build state of control executable PE project browser in project explorer as '<project browser3>'"""
    obj.textboxprojectbrowserverifybuildstateofcontrolexecutablepe(projectBrowser3)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I selected Close in refine offline")
def step_impl():
    """I selected Close in refine offline"""
    obj.buttoncloseselected()

@when("I entered Refine online window in refine offline")
def step_impl():
    """I entered Refine online window in refine offline"""
    obj.textboxrefineonlinewindowentered()
    
@when("I RClick CPB in project explorer as {arg}")
def step_impl(projectBrowser2):
    """I RClick control project browser project browser in project explorer as '<project browser1>'"""
    obj.textboxprojectbrowserrCPB(projectBrowser2)

#@when("I Dclick Control project broswer project browser in project explorer as {arg}")
#def step_impl(projectBrowser3):
#    """I Dclick Control project broswer project browser in project explorer as '<project browser3>'"""
#    CommonUtil.write_text_file("\nWhen I Dclick Control project broswer project browser in project explorer as \""+projectBrowser3+"\"")
#    obj.textboxprojectbrowserdclickcontrolprojectbroswer(projectBrowser3)
#  
@when("I Control executable dropdown PE project browser in project explorer as {arg}")
def step_impl(projectBrowser4):
    """I Control executable dropdown PE project browser in project explorer as '<project browser4>'"""
    obj.textboxprojectbrowsercontrolexecutabledropdownpe(projectBrowser4)
    
@when("I Right click facet from assignment dock PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock1):
    """I Right click facet from assignment dock PE assignmentsdock in project explorer as '<assignmentsdock1>'"""
    obj.textboxassignmentsdockrightclickfacetfromassignmentdockpe(assignmentsdock1)
  
@when("I select context submenu EC assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock2):
    """I select context submenu EC assignmentsdock in project explorer as '<assignmentsdock2>'"""
    obj.textboxassignmentsdockselectcontextsubmenuec(assignmentsdock2)
  
@then("Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock3):
    """Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as '<assignmentsdock3>'"""
    obj.textboxassignmentsdockverifyfacetsaddedorremovedcontextmenupe(assignmentsdock3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Create multiple FBD Sections and Verify as {arg}")
def step_impl(assignmentsdock2):
    """I Create multiple FBD Sections and Verify as '<assignmentsdock3>'"""
    obj.projectexplorertabutility_Create_Multiple_section_Containers_Dock_verify(assignmentsdock2)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Assign Instances from instance dock to sections in containers dock as {arg}")
def step_impl(param):
    """I Assign Instances from instance dock to sections in containers dock as '<param>'"""
    obj.projectexplorertabutility_Drag_instance_drop_container_section(param)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Double Click on the Facet in Assingnment section as {arg}")
def step_impl(facet_name):
    """I Double Click on the Facet in Assingnment section as '<facet_name>'"""
    obj.doubleclickinstanceinassignments(facet_name)
    
@when("I Check Any of the Facet Boxes to be added as {arg}")
def step_impl(instance_names):
    """I Check Any of the Facet Boxes to be added as '<instance_names>''"""
    obj.clickcheckboxininstanceedittor(instance_names)
    
@when("I click button on the Instance editor window as {arg}")
def step_impl(button_name):
    """I click button on the Instance editor window as '<button_name>''"""
    obj.savebuttoninstanceeditor(button_name) 
      
@when("I Right Click on the Particular Section and Click on Generate {arg}")
def step_impl(container):
    """I Right Click on the Particular Section and Click on Generate '<container>'"""
    obj.rightclickandgeneratecontainerssection(container)
    
@then("I verify the section is generated successfully as '(.*)' '(.*)'")
def step_impl(facet_names, generation_state):
    """I verify the section is generated successfully as '<param>'"""
    Applicationutility.take_screenshot()    
    obj.verifyassignmentsstate(facet_names, generation_state)
    Applicationutility.take_screenshot()
    
@when(r"Right Click on any one of the Facet in Assignments Section of PE-Container and Click Go Into Instance as '(.*)' and perform '(.*)'")
def step_impl(facet_name, action):
    obj.rightclickinstanceandperformaction(facet_name, action)
    
@when("I Double Click on Containers as {arg}")
def step_impl(identifier):
    """I Double Click on Containers as '<identifier>'"""
    obj.textboxprojectbrowserdclickcontrolprojectbroswer(identifier)
    
@when("I Drag and Drop the Instance to in Container as {arg}")
def step_impl(Instance):
    """I Drag and Drop the Instance to in Container"""
    obj.draganddropfrominstancetocontainer(Instance)
    
@when("I drag and Drop the Each instance to Each Sections as '(.*)' '(.*)'")
def step_impl(controller, section):
    """I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'"""
    obj.draganddropfromcontainertosection(controller, section)
    
@when("I Right click on the ControlProject_1 in Containers window and create FBDSections as {arg}")
def step_impl(num_sections):
    """I Right click on the ControlProject_1 in Containers window and create FBDSections as '<num_sections>'"""
    obj.createfbdsections(num_sections)
   
@when("I Click {arg} on service mapping edittor window")
def step_impl(tabname):
    """I Click '<tabname>' on service mapping edittor window"""
    obj.clickonmappingtab(tabname)    
    
@when("I Verify if the added device is available for mapping as {arg}")
def step_impl(variables):
    """I Verify if the added device is available for mapping as '<variables>'"""
    obj.verifydeviceavailbe(variables)
        
@when("I Verify if the Hardware Instances and App Instance Facets are available for mapping as {arg}")
def step_impl(variables):
    """I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<variables>'"""
    obj.verifyhardwareinstanceavailableformapping(variables)
    
@when("I Verify if the Network Variables are available as {arg}")
def step_impl(identifiers):
    """I Verify if the Network Variables are available as '<identifiers>'"""
    obj.verifynetworkvariable(identifiers)    
    
@when("I Drag and drop the EPE Managed Device from devices to channels as {arg}")
def step_impl(server):
    """I Drag and drop the EPE Managed Device from devices to channels as '<server>'"""
    obj.draganddropdevicetochannel(server)
    
@when("I Click on {arg} in the dialog box")
def step_impl(button):
    """I Click on '<button>' in the dialog box"""
    obj.textboxcontainerdockclickmodaldialogwindow(button)


@then("I verify {arg} disappered in assignments")
def step_impl(facet_name):
    """I verify '<facet_name>' disappered in assignments"""
    obj.verifyfacetbeforegenerate(facet_name) 
    Applicationutility.take_screenshot()   
        
@then(r"I verify Status updated in Assignment Section as '(.*)' '(.*)'")
def step_impl(facet_name, status):
    """I verify Status updated in Assignment Section as '<facet_name>' '<status>'"""
    obj.verifyassignmentsstatus(facet_name, status)
    
@when("I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as {arg}")
def step_impl(appfacet):
    """I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'"""
    obj.draganddropprojecttoserver(appfacet)
    
@when("I Right Click on the Communication Channels section of Communication Mapping Editor as {arg}")
def step_impl(server):
    """I Right Click on the Communication Channels section of Communication Mapping Editor as '<server>'"""
    obj.rightclickcommunicationchannel(server)
    

@when("I Drag and Drop variables from network variables to read from server pane as {arg}")
def step_impl(identifiers):
  obj.draganddropnetworktoserver(identifiers)
  
  
@when("I Verify if the Network Variables are available in network variable window as {arg}")
def step_impl(variables):
  obj.verifynetworkvariablemapping(variables)
  
@then("I selected Ok in Manage Network Variable Window")
def step_impl():
    """I selected Ok in Manage Network Variable Window"""
    obj.buttonokselected()
    
@when("I Search and select a template in the Template Section as {arg}")
def step_impl(value):
  obj.createinstance(value)
  
@then("I verify that the template is available in the instance window as {arg}")
def step_impl(value):
    """I verify that the template is available in the instance window as '<value>'"""
    obj.verifyinstance(value)
    
@then("I verify that all App facets {arg} are correctly mapped in the Hardware Instance")
def step_impl(appfacet):
    """I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance"""
    obj.verifyfacetsinhardwaremappingeditor(appfacet)
    
@then("I Verify all {arg} are mapped in read from server pane")
def step_impl(identifiers):
    """I Verify all '<identifiers>' are mapped in read from server pane"""
    obj.verifyservervariables(identifiers)
    
@when("I double-click on a {arg} in the Containers tab")
def step_impl(identifier):
  obj.doubleclickincontainer(identifier)
  
@when(r"I drag and drop the '(.*)' onto the edit page and click on the '(.*)' option afterward")
def step_impl(facetnames, option):
  Applicationutility.wait_for_execution()
  obj.draganddropinstancetoeditpage(facetnames, option)
  
@when("I click on the {arg} in Edit Page Properties")
def step_impl(arg):
  Applicationutility.wait_for_execution()
  obj.clickbuttononspeditpage(arg)
  
@when(r"I Click on the '(.*)' in Scada properties and Click '(.*)'")
def step_impl(button, drop_button):
  Applicationutility.wait_for_execution()
  obj.clickpropertiesonplantscada(button, drop_button)
  
@when("I Click on the {arg} in Restore project window")
def step_impl(arg):
  obj.clickbuttonplantscada(arg)
  
@when("I Select the {arg} in Backup-Restore window")
def step_impl(arg):
  obj.verifyandselectfileplantscada(arg)

@when("I Check Any of the files to be added in Deployment File Section as {arg}")
def step_impl(instance_names):
    """I Check Any of the files to be added in Deployment File Section as '<instance_names>'"""
    obj.checkboxclickindeploymentfilesection(instance_names)
    
@when("I clicks on the {arg} icon from the vertical menubar")
def step_impl(sidebar):
    """I  clicks on the '<sidebar>' icon from the vertical menubar"""
    obj.clicksidebarbuttoninplantscada(sidebar)
    
@when("I Enters the '(.*)' and '(.*)' in Aveva Plant Scada Window")
def step_impl(username, password):
    """I Enters the '<username>' and '<password>' in Aveva Plant Scada Window"""
    Applicationutility.wait_for_execution()
    obj.logintoplantscada(username, password)
    
@when("I clicks the {arg} in the login dialog box")
def step_impl(button):
    """I clicks the '<button>' in the login dialog box"""
    obj.clickbuttontologinscadapage(button)
    
@when("I clicks the {arg} in the Plant Scada popup dialog box")
def step_impl(button):
    """I clicks the '<button>' in the Plant Scada popup dialog box"""
    obj.clickbuttononscadapopup(button)
    
@then("I verifies that the Master (startup) page for HD1080 res window is opened")
def step_impl():
    """I verifies that the Master (startup) page for HD1080 res window is opened"""
    obj.verifymasterpagemainwindow()
    
@then("I verifies that {arg} Created in Project Explorer")
def step_impl(identifier):
    """I verifies that '<identifier>' Created in Project Explorer"""
    obj.verifycontrolproject(identifier)
    
@then("I Verify the Generation PopUp Window Message")
def step_impl():
    """I Verify the Generation PopUp Window Message"""
    obj.projectexplorertabutility_After_Generation_dialog_window_Message()
    
@when("I RClick on Block Refine Offline project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I RClick on Block Refine Offline project browser in project explorer as '<project browser1>'"""
    obj.textboxprojectbrowserrclickonblockrefineoffline(projectBrowser1)
    
@when("I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as {arg}")
def step_impl(communicationPeerToPeerPannel1):
    """I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as '<Communication Peer to Peer Pannel1>'"""
    obj.textboxcommunicationpeertopeerpanneldraganddropp2ptochannel(communicationPeerToPeerPannel1)
  
@when("I edit P2P Properties Communication Channels Pannel in communication mapping as {arg}")
def step_impl(communicationChannelsPannel2):
    """I edit P2P Properties Communication Channels Pannel in communication mapping as '<Communication Channels Pannel2>'"""
    obj.textboxcommunicationchannelspanneleditp2pproperties(communicationChannelsPannel2)
    
@when("I drag instance drop container page SP instance dock in supervision project as {arg}")
def step_impl(instanceDock1):
    """I drag instance drop container page SP instance dock in supervision project as '<instance dock1>'"""
    obj.textboxinstancedockdraginstancedropcontainerpagesp(instanceDock1)
  
@when("I Select value list view SVP instance dock in supervision project as {arg}")
def step_impl(instanceDock2):
    """I Select value list view SVP instance dock in supervision project as '<instance dock2>'"""
    obj.textboxinstancedockselectvaluelistviewsvp(instanceDock2)

@when("I Navigate to {arg} tab in project explorer tab")
def step_impl(CP_SP_Tab):
    """I Navigate to '<CP_SP_Tab>' tab in project explorer tab"""
    obj.Navigate_to_supervision_controlproject_tab(CP_SP_Tab)
    
@then("I Verify Navigation tab in project explorer")
def step_impl():
    """I Verify Navigation tab in project explorer"""
    obj.Verify_supervision_controlproject_tab()
    
@when("I Map workstation available for respective service and engine for supervision project as {arg}")
def step_impl(Service_Engine):
    """I Map workstation available for respective service and engine for supervision project as '<Service_Engine>'"""
    obj.Map_Workstation_Supervision_project(Service_Engine)
  
@when("I double click container PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I double click container PE container dock in project explorer as '<container dock1>'"""
    obj.textboxcontainerdockdoubleclickcontainerpe(containerDock1)
  
@then("verify supervision mapping PE service maping editor in project explorer")
def step_impl():
    """verify supervision mapping PE service maping editor in project explorer"""
    obj.textboxservicemapingeditorverifysupervisionmappingpe()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I change controller properties with drop down options as {arg}")
def step_impl(options):
    """I change controller properties with drop down options as '<options>'"""
    Projectexplorertabutility.Change_Password_Protection_Controller(options)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I change Settings option with drop down options as {arg}")
def step_impl(options):
    """I change Settings option with drop down options as '<options>'"""
    Projectexplorertabutility.Change_SettingsOption(options)
    Applicationutility.take_screenshot("Full Screenshot") 
    
@when("I change SettingsHeader  in settings window as {arg}")
def step_impl(options):
    """I change SettingsHeader  in settings window as '<Setting_Header>'"""
    Projectexplorertabutility.Click_on_Settings_Header(options)
    
@when("I click on Yes button in Message Box")
def step_impl():
    """I click on Yes button in Message Box"""
    obj.yesbuttoninsettings()
    
@when("I Click tabitem in EIO configaration window in control expert as {arg}")
def step_impl(identifiers):
    """I Click tabitem in EIO configaration window in control expert as '<identifiers>'"""
    obj.ClicktabitemEIOconfigwindow(identifiers)  
    
    
@when("I Double Click on Elementary variables in Refine, configure window")
def step_impl():
    """I Double Click on Elementary variables in Refine, configure window"""
    obj.elementvariabledoubleclick()  
    
@when("I Enter Variable name and select HMI option under Data Editor window")
def step_impl():
    """I Enter Variable name and select HMI option under Data Editor window"""
    obj.entervariableselecthmi()
    
@when("I Uncheck the pack CheckBox in P2P Communication Configuration window for variable {arg}")
def step_impl(identifier):
    """I Uncheck the pack CheckBox in P2P Communication Configuration window for variable '<identifier>'"""
    obj.UnpackvariableP2Pconfigurationwindow(identifier)
    
@when("I Unmap variable in P2P communication configuration window by Context menu as {arg}")
def step_impl(identifier):
    """I Unmap variable in P2P communication configuration window by Context menu as '<identifier>'"""
    obj.UnmapP2Pvariablebycontextmenu(identifier)
    
@when("I Unmap variable in P2P communication configuration window by keyboard action as {arg}")
def step_impl(identifier):
    """I Unmap variable in P2P communication configuration window by keyboard action as '<identifier>'"""
    obj.UnmapP2Pvariablebykeyboardaction(identifier)
    
@when("I  Click on Variables from elementary variables tab to initiate animationtable editor window named as {arg}")
def step_impl(identifier):
    """I Right Click on Variables from elementary variables tab named as '<identifier>'"""
    obj.clickvariableelementaryinitiateanimationtabletab(identifier)
    
@when("I Run PLC Simulator")
def step_impl():
    """I Run PLC Simulator"""
    obj.RunPLCsimulator()
    
@when("I Verify backup data PE in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I Verify backup data PE in project explorer as '<project browser2>'"""
    obj.textboxprojectbrowserverifybackupdata(projectBrowser3)
    
@when("I Drag and drop from remote varaibles to source variables in P2P as {arg}")
def step_impl(server):
    """I Drag and drop from remote varaibles to source variables in P2P as '<server>'"""
    Applicationutility.wait_in_seconds(1000,"wait")
    obj.textboxdraganddropremotetolocalP2P(server)
    
@when("I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as {arg}")
def step_impl(server):
    """I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as '<param>'"""
    obj.textboxclickp2pcreateconsecutivevariables(server)
 
    
@when("I change Data type in Data Editor as {arg}")
def step_impl(server):
    """I change Data type in Data Editor as '<param>'"""
    obj.textboxchangedatatypedataeditor(server)  
    
    
@when("I change Data value in Data Editor as {arg}")
def step_impl(server):
    """I change Data value in Data Editor as '<param>'"""
    obj.clickonvariableandchangedatavalueanimationtable(server) 
 
@when("I Expand IO Device section project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I Expand IO Device section project browser in project explorer as '<project browser1>'"""
    obj.textboxprojectbrowserexpandiodevicesection(projectBrowser1)
  
@when("I Edit IO Device Properties project browser in project explorer as {arg}")
def step_impl(projectBrowser2):
    """I Edit IO Device Properties project browser in project explorer as '<project browser2>'"""
    obj.textboxprojectbrowsereditiodeviceproperties(projectBrowser2)
  
@when("I Map IO Devices in PE project browser in project explorer as {arg}")
def step_impl(projectBrowser4):
    """I Map IO Devices in PE project browser in project explorer as '<project browser4>'"""
    obj.textboxprojectbrowsermapiodevicesinpe(projectBrowser4)   

    
@when("I change Data value in FBD Section as {arg}")
def step_impl(server):
    """I change Data value in FBD Section as '<param>'"""
    obj.changeFBDValue(server)
    
@when("I verify {arg} is reflected in FBD section")
def step_impl(server):
    """I verify '<variable>' is reflected in FBD section"""
    obj.verifyvariablevalueFBDBlock(server)
    
@when("I Select page templates sp settings button in project explorer")
def step_impl():
    """I Select page templates sp settings button in project explore"""
    obj.pagetemplatesspsettingsbuttonclick()
    
@when("I click add page template button in project explorer")
def step_impl():
    """I click add page template button in project explorer"""
    obj.addpagetemplatebuttonclick()
   
@when("I check new page template radio button in project explorer")
def step_impl():
    """I check new page template radio button in project explorer"""
    obj.newpagetemplateradiobuttoncheck()
    
@when("I click close tool bar button in project explorer")
def step_impl():
    """I click close tool bar button in project explorerr"""
    obj.closetoolbarbuttonclick()

@when("I click container dock in project explorer")
def step_impl():
    """I click container dock in project explorerr"""
    obj.containerdockclick()
    
@then("I verify the context menu item enabled state as {arg}")
def step_impl(imp):
    """I verify the context menu item"""
    obj.textboxprojectbrowserverifycontextmenuitemes(imp)
    
    
@then("I verify the service mapping to the controller as {arg}")
def step_impl(projectbrowser3):
    """I verify the service mapping to the controller"""
    obj.projectexplorertabutility_verify_control_service_maping_PE(projectbrowser3)
    
@then("Verify the progress status of instance in Instance browser PE when opened as {arg}")
def step_impl(template):
    """Verify the progress status of instance in Instance browser PE"""
    obj.projectexplorertabutility_verify_progress_indicator_PE(template)
    
@when("I Expand folder in Instance Dock PE when opened as {arg}")
def step_impl(Folder):
    """Verify the progress status of instance in Instance browser PE"""
    obj.projectexplorertabutility_expand_folder_instance_browser_PE(Folder)   
    