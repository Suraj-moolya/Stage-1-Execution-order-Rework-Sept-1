"""ApplicationExplorerTabWorkFlow"""
from ApplicationExplorerTabWorkFlow import ApplicationExplorerTabWorkFlow
import Applicationutility
import Applicationexplorertabutility
import Actionutility
obj=ApplicationExplorerTabWorkFlow()

        
@when("I Expand template browser AE Templates browser Application in application explorer as {arg}")
def step_impl(templatesBrowserApplication1):
    """I Expand template browser AE Templates browser Application in application explorer as '<Templates browser Application1>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(templatesBrowserApplication1)
  
@when("I Expand template browser AE Templates browser STAHL in application explorer as {arg}")
def step_impl(templatesBrowserStahl2):
    """I Expand template browser AE Templates browser STAHL in application explorer as '<Templates browser STAHL2>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(templatesBrowserStahl2)
  
@then("verify composite template AE Templates browser in application explorer")
def step_impl():
    """verify composite template AE Templates browser in application explorer"""
    obj.textboxtemplatesbrowserverifycompositetemplateae()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Collapse template browser AE STAHL in application explorer as {arg}")
def step_impl(stahl3):
    """I Collapse template browser AE STAHL in application explorer as '<STAHL3>'"""
    obj.textboxstahlcollapsetemplatebrowserae(stahl3)
  
@when("I Expand template browser AE Time Stamping in application explorer as {arg}")
def step_impl(timeStamping4):
    """I Expand template browser AE Time Stamping in application explorer as '<Time Stamping4>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(timeStamping4)
  
@when("I scroll down template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser5):
    """I scroll down template browser AE Templates browser in application explorer as '<Templates browser5>'"""
    obj.textboxtemplatesbrowserscrolldowntemplatebrowserae(templatesBrowser5)
  
@when("I Collapse template browser AE Time Stamping in application explorer as {arg}")
def step_impl(timeStamping6):
    """I Collapse template browser AE Time Stamping in application explorer as '<Time Stamping6>'"""
    obj.textboxstahlcollapsetemplatebrowserae(timeStamping6)
  
@when("I Expand template browser AE Unity Array Variables in application explorer as {arg}")
def step_impl(unityArrayVariables7):
    """I Expand template browser AE Unity Array Variables in application explorer as '<Unity Array Variables7>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(unityArrayVariables7)
  
@when("I Collapse template browser AE Unity Array Variables in application explorer as {arg}")
def step_impl(unityArrayVariables8):
    """I Collapse template browser AE Unity Array Variables in application explorer as '<Unity Array Variables8>'"""
    obj.textboxstahlcollapsetemplatebrowserae(unityArrayVariables8)
  
@when("I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as {arg}")
def step_impl(unityElementaryTimeStampedVariables9):
    """I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables9>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(unityElementaryTimeStampedVariables9)
  
@when("I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as {arg}")
def step_impl(unityElementaryTimeStampedVariables11):
    """I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables11>'"""
    obj.textboxstahlcollapsetemplatebrowserae(unityElementaryTimeStampedVariables11)
  
@when("I Expand template browser AE Owner_Consumer Templates in application explorer as {arg}")
def step_impl(ownerconsumerTemplates12):
    """I Expand template browser AE Owner_Consumer Templates in application explorer as '<Owner_Consumer Templates12>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(ownerconsumerTemplates12)
  
@when("I Collapse template browser AE Unity Peer to Peer in application explorer as {arg}")
def step_impl(unityPeerToPeer13):
    """I Collapse template browser AE Unity Peer to Peer in application explorer as '<Unity Peer to Peer13>'"""
    obj.textboxstahlcollapsetemplatebrowserae(unityPeerToPeer13)
  
@when("I Expand template browser AE Advantys in application explorer as {arg}")
def step_impl(advantys14):
    """I Expand template browser AE Advantys in application explorer as '<Advantys14>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(advantys14)
  
@when("I Collapse template browser AE Advantys in application explorer as {arg}")
def step_impl(advantys15):
    """I Collapse template browser AE Advantys in application explorer as '<Advantys15>'"""
    obj.textboxstahlcollapsetemplatebrowserae(advantys15)
  
@when("I Expand template browser AE M340 in application explorer as {arg}")
def step_impl(m34016):
    """I Expand template browser AE M340 in application explorer as '<M34016>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(m34016)
  
@when("I Collapse template browser AE M340 in application explorer as {arg}")
def step_impl(m34017):
    """I Collapse template browser AE M340 in application explorer as '<M34017>'"""
    obj.textboxstahlcollapsetemplatebrowserae(m34017)
  
@when("I Expand template browser AE M580 in application explorer as {arg}")
def step_impl(m58018):
    """I Expand template browser AE M580 in application explorer as '<M58018>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(m58018)
  
@when("I Collapse template browser AE M580 in application explorer as {arg}")
def step_impl(m58019):
    """I Collapse template browser AE M580 in application explorer as '<M58019>'"""
    obj.textboxstahlcollapsetemplatebrowserae(m58019)
  
@when("I Expand template browser AE Quantum in application explorer as {arg}")
def step_impl(quantum20):
    """I Expand template browser AE Quantum in application explorer as '<Quantum20>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(quantum20)
  
@when("I Collapse template browser AE Foundation Library in application explorer as {arg}")
def step_impl(foundationLibrary21):
    """I Collapse template browser AE Foundation Library in application explorer as '<Foundation Library21>'"""
    obj.textboxstahlcollapsetemplatebrowserae(foundationLibrary21)
  
@when("I Expand template browser AE General Purpose Library in application explorer as {arg}")
def step_impl(generalPurposeLibrary22):
    """I Expand template browser AE General Purpose Library in application explorer as '<General Purpose Library22>'"""
    obj.textboxtemplatesbrowserapplicationexpandtemplatebrowserae(generalPurposeLibrary22)
  
@then("verify template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser):
    """verify template browser AE Templates browser in application explorer as '<Templates browser>'"""
    obj.textboxtemplatesbrowserverifytemplatebrowserae()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I close all tabs except system explorer EC Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser23):
    """I close all tabs except system explorer EC Templates browser in application explorer as '<Templates browser23>'"""
    obj.textboxtemplatesbrowserclosealltabsexceptsystemexplorerec()
  
@when("I search text template browser AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser1):
    """I search text template browser AE Templates browser in application explorer as '<Templates browser1>'"""
    obj.textboxtemplatesbrowsersearchtexttemplatebrowserae(templatesBrowser1)
  
@when("I drag composite template drop application browser system1 AE Templates browser in application explorer as {arg}")
def step_impl(templatesBrowser2):
    """I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'"""
    obj.textboxtemplatesbrowserdragcompositetemplatedropapplicationbrowsersystem1ae(templatesBrowser2)
 
@when("I rclick asset workspace folder AE Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace4):
    """I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'"""
    obj.textboxassetworkspacerclickassetworkspacefolderae(assetWorkspace4)
  
@when("I Select context menu item EC Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace5):
    """I Select context menu item EC Asset workspace in application explorer as '<Asset workspace5>'"""
    obj.textboxassetworkspaceselectcontextmenuitemec(assetWorkspace5)
  
@when("I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as {arg}")
def step_impl(assertWorkspaceEditor8):
    """I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor8>'"""
    obj.textboxassertworkspaceeditordragtemplateinapplicationbrowserdropassetworkspaceeditorae(assertWorkspaceEditor8)
  
@then("Verify Template AE Assert Workspace Editor in application explorer as {arg}")
def step_impl(assertWorkspaceEditor9):
    """Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'"""
    obj.textboxassertworkspaceeditorverifytemplateae(assertWorkspaceEditor9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Link from range node to range node AE Node Instance in application explorer as {arg}")
def step_impl(rsprangedpvranged):
    """I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'"""
    obj.buttonnodeinstancelinkfromrangenodetorangenodeae(rsprangedpvranged)
  
@then("Verify Link Status Node Instance in application explorer")
def step_impl():
    """Verify Link Status Node Instance in application explorer"""
    obj.buttonnodeinstanceverifylinkstatus()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I rclick application browser folder AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser3):
    """I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'"""
    obj.textboxapplicationbrowserrclickapplicationbrowserfolderae(applicationBrowser3)
  
@when("I rclick application browser template AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser4):
    """I rclick application browser template AE Application browser in application explorer as '<Application browser4>'"""
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(applicationBrowser4)
  
@when("I Select context menu item EC Application browser in application explorer as {arg}")
def step_impl(applicationBrowser5):
    """I Select context menu item EC Application browser in application explorer as '<Application browser5>'"""
    obj.textboxapplicationbrowserselectcontextmenuitemec(applicationBrowser5)
    Applicationutility.wait_in_seconds(2000, 'Wait')
    
@when("I Rename the Insatnce to the requirement {arg}")
def step_impl(Name1):
    """I Rename the Insatnce to the requirement '<Name1>'"""
    obj.textboxRenameInsatnce(Name1)
  
@then("verify inspect instance window open Inspect instance tree in inspect instance as {arg}")
def step_impl(inspectInstanceTree6):
    """verify inspect instance window open Inspect instance tree in inspect instance as '<Inspect instance tree6>'"""
    obj.textboxinspectinstancetreeverifyinspectinstancewindowopen(inspectInstanceTree6)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Inspect instance ok in inspect instance")
def step_impl():
    """I selected Inspect instance ok in inspect instance"""
    obj.buttoninspectinstanceokselected()
  
@when("I Close inspect instance window AE Inspect instance window in inspect instance")
def step_impl():
    """I Close inspect instance window AE Inspect instance window in inspect instance as '<Inspect instance window>'"""
    obj.textboxinspectinstancewindowcloseinspectinstancewindowae()
  
@when("I Esc keyboard action Inspect instance window in inspect instance")
def step_impl():
    """I Esc keyboard action Inspect instance window in inspect instance as '<Inspect instance window>'"""
    obj.textboxinspectinstancewindowesckeyboardaction()

@when("I Create system and create instance Create Multiple instance in application explorer")
def step_impl():
    """I Create system and create instance Create Multiple instance in application explorer"""
    obj.buttoncreatemultipleinstancecreatesystemandcreateinstance()
  
@then("Verify folder created Identifier in application browser as {arg}")
def step_impl(identifier1):
    """Verify folder created Identifier in application browser as '<Identifier1>'"""
    obj.textboxidentifierverifyfoldercreated(identifier1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify template created Identifier MotorGP_1 in application browser as {arg}")
def step_impl(identifierMotorgp13):
    """Verify template created Identifier MotorGP_1 in application browser as '<Identifier MotorGP_13>'"""
    obj.textboxidentifiermotorgp1verifytemplatecreated(identifierMotorgp13)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify template created Identifier ValveGP_1 in application browser as {arg}")
def step_impl(identifierValvegp14):
    """Verify template created Identifier ValveGP_1 in application browser as '<Identifier ValveGP_14>'"""
    obj.textboxidentifiermotorgp1verifytemplatecreated(identifierValvegp14)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I double click on template Identifier in application browser as {arg}")
def step_impl(identifier5):
    """I double click on template Identifier in application browser as '<Identifier5>'"""
    obj.textboxidentifierdoubleclickontemplate(identifier5)
  
@then("Verify template instance editor Instance Editor in application explorer as {arg}")
def step_impl(instanceEditor6):
    """Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'"""
    obj.textboxinstanceeditorverifytemplateinstanceeditor(instanceEditor6)
    Applicationutility.take_screenshot("Full Screenshot")
 
@then("I take photo evidence in Engineering Client") 
@when("I take evidence Instance Editor in application explorer")
def step_impl():
    """I take evidence Instance Editor in application explorer"""
    obj.textboxinstanceeditortakeevidence()
  
@when("I Check instance editor Instance editor checklist in application explorer as {arg}")
def step_impl(instanceEditorChecklist7):
    """I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist7>'"""
    obj.textboxinstanceeditorchecklistcheckinstanceeditor(instanceEditorChecklist7)
  
@when("I Enter description AE Instance description in application explorer")
def step_impl():
    """I Enter description AE Instance description in application explorer"""
    obj.buttoninstancedescriptionenterdescriptionae()
  
@when("I selected Instance editor save in application explorer")
def step_impl():
    """I selected Instance editor save in application explorer"""
    obj.buttoninstanceeditorsaveselected()
  
@when("I Close instance editor tab Instance editor close in application explorer as {arg}")
def step_impl(instanceEditorClose8):
    """I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'"""
    obj.textboxinstanceeditorclosecloseinstanceeditortab(instanceEditorClose8)
  
@then("verify popup AE Save changes dialogbox in application explorer as {arg}")
def step_impl(saveChangesDialogbox9):
    """verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'"""
    obj.textboxsavechangesdialogboxverifypopupae(saveChangesDialogbox9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Save changes dialogbox yes in application explorer")
def step_impl():
    """I selected Save changes dialogbox yes in application explorer"""
    obj.buttonsavechangesdialogboxyesselected()
  
@when("I selected Save changes dialogbox no in application explorer")
def step_impl():
    """I selected Save changes dialogbox no in application explorer"""
    obj.buttonsavechangesdialogboxnoselected()
  
@when("I selected Save changes dialogbox cancel in application explorer")
def step_impl():
    """I selected Save changes dialogbox cancel in application explorer"""
    obj.buttonsavechangesdialogboxcancelselected()
  
@when("I rclick application browser template AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate5):
    """I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template5>'"""
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(motorgpTemplate5)
  
@then("verify context menu items ContextMenu in application explorer")
def step_impl():
    """verify context menu items ContextMenu in application explorer"""
    obj.textboxcontextmenuverifycontextmenuitems()
    Applicationutility.take_screenshot("Full Screenshot")
    
@then("verify the status of the instance")
def step_impl():
    obj.textboxverifyinstancevalidity()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Select context menu item EC ContextMenu in application explorer as {arg}")
def step_impl(contextmenu6):
    """I Select context menu item EC ContextMenu in application explorer as '<ContextMenu6>'"""
    obj.textboxassetworkspaceselectcontextmenuitemec(contextmenu6)
  
@when("I rclick application browser folder AE Folder_2 in application explorer as {arg}")
def step_impl(folder27):
    """I rclick application browser folder AE Folder_2 in application explorer as '<Folder_27>'"""
    obj.textboxapplicationbrowserrclickapplicationbrowserfolderae(folder27)
  
@then("Verify template created Application browser template in application explorer as {arg}")
def step_impl(applicationBrowserTemplate9):
    """Verify template created Application browser template in application explorer as '<Application browser template9>'"""
    obj.textboxidentifiermotorgp1verifytemplatecreated(applicationBrowserTemplate9)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I double click on template Identifier ValveGP_1 in application browser as {arg}")
def step_impl(identifierValvegp15):
    """I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'"""
    obj.textboxidentifierdoubleclickontemplate(identifierValvegp15)
  
@then("Verify instance lock popup Warning popup window in application explorer as {arg}")
def step_impl(warningPopupWindow11):
    """Verify instance lock popup Warning popup window in application explorer as '<Warning popup window11>'"""
    obj.textboxwarningpopupwindowverifyinstancelockpopup(warningPopupWindow11)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected AE warning popup ok in application explorer")
def step_impl():
    """I selected AE warning popup ok in application explorer"""
    obj.buttonaewarningpopupokselected()
  
@when("I Create multiple folders and instances AE Create Multiple instance in application explorer")
def step_impl():
    """I Create multiple folders and instances AE Create Multiple instance in application explorer"""
    obj.buttoncreatemultipleinstancecreatemultiplefoldersandinstancesae()
  
@when("I rclick application browser template AE Asset workspace in application explorer as {arg}")
def step_impl(assetWorkspace3):
    """I rclick application browser template AE Asset workspace in application explorer as '<Asset workspace3>'"""
    obj.textboxapplicationbrowserrclickapplicationbrowsertemplateae(assetWorkspace3)

  
@when("I uncheck all filters temp browser AE Templates browser in application explorer")
def step_impl():
    """I uncheck all filters temp browser AE Templates browser in application explorer"""
    obj.textboxtemplatesbrowseruncheckallfilterstempbrowserae()
  
@when("I entered Application browser in application explorer")
def step_impl():
    """I entered Application browser in application explorer"""
    obj.textboxapplicationbrowserentered()

@then("Verify version in application explorer as {arg}")
def step_impl(applicationBrowser):
    """I entered Application browser in application explorer as '<Application browser>'"""
    obj.verifyaeapplicationbrowsertemplate(applicationBrowser)

@when("I Enter FileLocation and FileName to be Imported Import in import dialog as {arg}")
def step_impl(import3):
    """I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'"""
    obj.textboximportenterfilelocationandfilenametobeimported(import3)
  
@when("I Click on Buttons in Import System1 Popup_AE Import in import dialog as {arg}")
def step_impl(import4):
    """I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'"""
    obj.textboximportclickonbuttonsinimportsystem1popupae(import4)
  
@when("I Wait for Import popup Import in import dialog")
def step_impl():
    """I Wait for Import popup Import in import dialog"""
    obj.textboximportwaitforimportpopup()
  
@when("I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as {arg}")
def step_impl(ok):
    """I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'"""
    obj.buttonimportdialogclickonbuttonsinimportdialogpopupae(ok)
  
@then("I Delete the folders created in order")
def step_impl():
    Applicationexplorertabutility.delete_all_folder_system_ord_EC()   

    
@then("I Close the message window")
def step_impl():
    Applicationexplorertabutility.close_Message_Window()
    
    
@when("I Wait for Import Conflict Dialog Box Import Conflict Dialog in import dialog as {arg}")
def step_impl(importConflictDialog):
    """I Wait for Import Conflict Dialog Box Import Conflict Dialog in import dialog as '<Import Conflict Dialog>'"""
    obj.textboximportconflictdialogwaitforimportconflictdialogbox(importConflictDialog)


@when("I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as {arg}")
def step_impl(importConflictDialog7):
    """I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'"""
    obj.textboximportconflictdialogclickonbuttonsinconflictdialogpopup(importConflictDialog7)
  
@then("Verify template added in Application browser AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser9):
    """Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'"""
    obj.textboxapplicationbrowserverifytemplateaddedinapplicationbrowserae(applicationBrowser9)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@then("Verify instance lock popup Application browser in application explorer as {arg}")
def step_impl(applicationBrowser5):
    """Verify instance lock popup Application browser in application explorer as '<Application browser5>'"""
    obj.textboxapplicationbrowserverifyinstancelockpopup(applicationBrowser5)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Click on Buttons in Import Dialog popup AE Application browser in application explorer as {arg}")
def step_impl(applicationBrowser6):
    """I Click on Buttons in Import Dialog popup AE Application browser in application explorer as '<Application browser6>'"""
    obj.buttonimportdialogclickonbuttonsinimportdialogpopupae(applicationBrowser6)
    
    
@when("I selected Relative Radio in import dialog")
def step_impl():
    """I selected Relative Radio in import dialog"""
    obj.buttonrelativeradioselected()
    
@when("I Click on buttons in popup window Application browser in application explorer as {arg}")
def step_impl(applicationBrowser6):
    """I Click on buttons in popup window Application browser in application explorer as '<Application browser6>'"""
    obj.textboxapplicationbrowserclickonbuttonsinpopupwindow(applicationBrowser6)

  
@when("I close all tabs except system explorer in Engineering Client")
def step_impl():
    """I close all tabs except system explorer EC Templates browser in application explorer as '<Templates browser23>'"""
    obj.textboxtemplatesbrowserclosealltabsexceptsystemexplorerec()

    
@when("I Copy and paste using shortcut keys Specific template in application browser")
def step_impl():
    """I Copy and paste using shortcut keys Specific template in application browser"""
    obj.buttonspecifictemplatecopyandpasteusingshortcutkeys()    
    
    
@then("Verify delete window AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate3):
    """Verify delete window AE MotorGP template in application explorer as '<MotorGP template3>'"""
    obj.textboxmotorgptemplateverifydeletewindowae(motorgpTemplate3)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I take evidence Identifier MotorGP_1 in application browser")
def step_impl():
    """I take evidence Identifier MotorGP_1 in application browser"""
    obj.textboxinstanceeditortakeevidence()
    
    
@when("I Click template AE MotorGP template in application explorer as {arg}")
def step_impl(motorgpTemplate1):
    """I Click template AE MotorGP template in application explorer as '<MotorGP template1>'"""
    obj.textboxmotorgptemplateclicktemplateae(motorgpTemplate1)
    
    
@when("I Press short keys MotorGP template in application explorer")
def step_impl():
    """I Press short keys MotorGP template in application explorer"""
    obj.textboxmotorgptemplatepressshortkeys()
    
    
@when("I double click on template Identifier MotorGP_1 in application browser as {arg}")
def step_impl(identifierMotorgp11):
    """I double click on template Identifier MotorGP_1 in application browser as '<Identifier MotorGP_11>'"""
    obj.textboxidentifierdoubleclickontemplate(identifierMotorgp11)
    

@when("I Click on buttons in popup window Warning popup window in application explorer as {arg}")
def step_impl(warningPopupWindow7):
    """I Click on buttons in popup window Warning popup window in application explorer as '<Warning popup window7>'"""
    obj.textboxwarningpopupwindowclickonbuttonsinpopupwindow(warningPopupWindow7)
    
    
@when("I Warning popup close Warning popup window in application explorer")
def step_impl():
    """I Warning popup close Warning popup window in application explorer"""
    obj.textboxwarningpopupwindowwarningpopupclose()
    
    
@then("Verify Message from notification panel AE Delete popup in message box as {arg}")
def step_impl(deleteInstance):
    """Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'"""
    obj.buttondeletepopupverifymessagefromnotificationpanelae(deleteInstance)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I Copy and paste using shortcut keys value template in application browser")
def step_impl():
    """I Copy and paste using shortcut keys Specific template in application browser"""
    obj.buttonspecifictemplatecopyandpasteusingshortcutkeys_1()
    
@then("I verify the file existance")##
def step_impl():
    Applicationexplorertabutility.Verify_file_existance()
    

@then("Verify the template is present in Application browser as {arg}")
def step_impl(Templatesbrowser1):
    """Verify the template is present in Application browser"""
    Applicationexplorertabutility.verify_instance_application_browser(Templatesbrowser1)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Expand System and Folder in Application browser")
def step_impl():
    """When I Expand System and Folder in Application browser"""
    obj.expandfoldersystem()
    
@then("I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message")
def step_impl():
    """I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message"""
    obj.verifySameNameErrorboxapplicationbrowser()
    
@when("I Click on buttons as {arg}")
def step_impl(button_1):
    obj.renameinstancepopupbutton(button_1)
    
@when("I Close Lockup pop up window")
def step_impl():
    """I Close Lockup pop up window"""
    obj.modaldialogwindowclose()
    
@then("Verify application browser folder AE")
def step_impl(applicationBrowser3):
    """Verify application browser folder AE"""
    Applicationexplorertabutility.verify_instance_application_browser()  
    
@then("verify window open as {arg}")
def step_impl(Window):
    """I Rename the Insatnce to the requirement '<Name1>'"""
    Applicationutility.wait_in_seconds(2000, 'Wait')
    obj.verifyobject(Window)

@when("I select the template to replace in replace template as {arg}")
def step_impl(Replace_Template):    
    obj.replacetemplatecomb(Replace_Template)
    
@then("I wait for Import Dialogue Window to appear")
def step_impl():    
    obj.replacetemplatecomb(ReplaceTemplate)


@when("I Select button in the modal dialoge window as {arg}")
def step_impl(Buttonname):    
    """I Select button in the modal dialoge window as '<Buttonname>'"""
    obj.modaldiawindow(Buttonname)
    Applicationutility.wait_in_seconds(5000, 'Wait')

@when("I Close modal dialog window")
def step_impl():
    """I Close Lockup pop up window"""
    obj.modaldialogwindowclose()
    
@then("verify template and version in application browser as {arg}")
def step_impl(Template):
    """verify template and version in application browser"""
    Applicationutility.wait_in_seconds(3000, 'Wait')
    obj.verifytemplatebrowserinae(Template)
    Applicationutility.take_screenshot('Full screenshot !!')

    
@when("I Select context menu item as {arg}")
def step_impl(action):
    obj.textboxassetworkspaceselectcontextmenuitemec(action)
  
@when("I click modal dialog window Instance editor save in application explorer as {arg}")
def step_impl(yes):
    """I click modal dialog window Instance editor save in application explorer as 'Yes'"""
    Applicationutility.wait_in_seconds(1000,"Wait")
    obj.buttoninstanceeditorsaveclickmodaldialogwindow(yes)
    
@when("I drag template in application browser Link Editor as {arg}")
def step_impl(assertWorkspaceEditor8):
    """I drag template in application browser Link Editor as '<Assert Workspace Editor8>'"""
    obj.dragtemplatefromapplicationbrowsertolinkeditor(assertWorkspaceEditor8)

@when("I Remove PVRanged link AE Assert Workspace Editor in application explorer")
def step_impl():
    """I Remove PVRanged link AE Assert Workspace Editor in application explorer"""
    obj.textboxassertworkspaceeditorremovepvrangedlinkae()
  
@then("Verify link two instances asset workspace Assert Workspace Editor in application explorer")
def step_impl():
    """Verify link two instances asset workspace Assert Workspace Editor in application explorer"""
    obj.textboxassertworkspaceeditorverifylinktwoinstancesassetworkspace()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Enter FileLocation and FileName in empty pages import dialog as {arg}")
def step_impl(importfile):
    """I Enter FileLocation and FileName in empty pages import dialog as '<Import3>'"""
    obj.textboximportemptypagesenterfilelocationandfilenametobeimported(importfile)

@when("I drag Template from Template browser and drop to the Folders in Application browser with folder name as {arg}")
def step_impl(templatesBrowser2):
    """I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<Templates browser2>'"""
    Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE(templatesBrowser2)

@then("Verify the progress status of the instances in Application Browser in AE {arg}") 
@then("Verify the progress status of instance in Application browser when opened as {arg}")   
@then("Verify the instance is locked in Application browser when opened as {arg}")
def step_impl(templatesBrowser2):
  """Verify the instace is locked when opened as '<templatesBrowser2>'"""
  Applicationexplorertabutility.verify_progress_indicator_AE(templatesBrowser2)
  
@when("Export the instance in Application browser when opened as {arg}")
def step_impl(param):
  """Export the instance in Application browser when opened as '<param>'"""
  Actionutility.Enter_filename_fileformat_Export_Window(param)
  
@when("Import the instance in Application browser when opened as {arg}")
def step_impl(param):
  """Import the instance in Application browser when opened as '<param>'"""
  Actionutility.Enter_fileName_fileformat_Import_Window(param)
  
@when("I Enter File Name and File Location in Export Window as {arg}")
def step_impl(xml):
    """I Enter File Name and File Location in Export Window as '<File details>'"""
    obj.enterfilenameandfilelocationinexportwindowae(xml)
    
@when("I Enter File Name and File Location in Import Window as {arg}")
def step_impl(file):
    """I Enter File Name and File Location in Import Window as '<File detail>'"""
    obj.enterfilenameandfilelocationinimportwindowae(file)
  
@when("Verify the instances in Application Browser {arg}")
def step_impl(count):
    """Verify the instances in Application Browser '<scroll count>''"""
    obj.veryifyappbrowserinstances(count)
    
@when("I Click on Abort button in Notification Panel")
def step_impl():
    """I Click on Abort button in Notification Panel"""
    obj.aborttheimportinae()
    
@when("I apply the required filter in AE application browser pane as {arg}, {arg}")
def step_impl(filter, name):
    """I apply the required filter in AE application browser pane as '<Filter>', '<Name>'"""
    obj.applyfilterinappbrowserpane(filter, name)
    
@then("I verify if the specific filter action in the AE application browser pane")
def step_impl():
    """I verify if the specific filter action in the AE application browser pane"""
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I clear the applied filter {arg} in AE application browser pane")
def step_impl(filter):
    """I clear the applied filter '<Filter>' in AE application browser pane"""
    obj.clearfilterinappbrowserpane(filter)
    
@then("I Expand {arg} and verify the notification message contents {arg}")
def step_impl(message, count):
    """I Expand '<Message>' and verify the notification message contents '<Scroll count>''"""
    obj.scrollnotificationpanel(message, count)
    
@when("I modify the exported csv file {arg} with invalid template name {arg}")
def step_impl(File, invalidname):
    """I modify the exported csv file '<File detail>' with invalid template name '<Invalid name>'"""
    obj.aefaultynameimport(File, invalidname)
    
@then("Verify Modal Dialog Window Text in message box as {arg}")
def step_impl(Message):
    """Verify Modal Dialog Window Text in message box as '<Modal Dialog Window 15>'"""
    Actionutility.modal_dialog_window_dialog(Message)
    
@when("I drag Template from Template browser and drop to Application browser '(.*)' times with template as '(.*)'")
def step_impl(count, param):
    """I drag Template from Template browser and drop to Application browser '<count>' times with template as '<param>' """
    count_int = int(count)
    Applicationexplorertabutility.run_drag_and_drop_multiple_times(param, count_int)
    
    
@then("I Verifies time taken to load the Application Tree Pane")
def step_impl():
    """I Verifies time taken to load the Application Tree Pane"""
    Actionutility.reload_application_explorer_and_measure_time()
    
@when("I Enter File Name and File Format in Import Window EC Windows Explorer as {arg}")
def step_impl(filename):
    """I Enter File Name and File Format in Import Window EC Windows Explorer as '<filename>'"""
    obj.import_file_from_ae_explorer_window(filename)
    
@when("I Handle the import conflict by updating the instance {arg} and skipping the rest")
def step_impl(instance_name):
    """I Handle the import conflict by updating the instance '<instance_name>' and skipping the rest"""
    obj.handling_import_conlicts(instance_name)
  
@then("Verify the progress status and tooltip for all visible instances in the Application browser")
def step_impl():
    """Verify the progress status and tooltip for all visible instances in the Application browser"""
    Applicationexplorertabutility.verify_progress_status_of_all_templates()
  
@when("I Switch Application Explorer view to {arg}")
def step_impl(view):
    """I Switch Application Explorer view to '<view>'"""
    Applicationexplorertabutility.switch_view_if_needed(view)
    
@when("I Update values of '(.*)' for instance '(.*)' in exported file '(.*)'")
def step_impl(headings, instance_name, file_name):
    """I Update values of '<headings>' for instance '<instance_name>' in exported file '<file_name>'"""
    Actionutility.changing_values_in_csv(file_name, instance_name, headings)
    
@then("I verify all folders are expanded in the Application Browser")
def step_impl():
    """I verify all folders are expanded in the Application Browser"""
    Applicationexplorertabutility.verify_all_folders_expanded_or_Collapsed()
  
@when("I press '(.*)' arrow key on identifier '(.*)' in the Application Browser")
def step_impl(direction, identifier):
    """I press '<direction>' arrow key on identifier '<identifier>' in the Application Browser"""
    Applicationexplorertabutility.navigate_identifier_application_browser(identifier, direction)
  
@when("I double click on the instance {arg} in the Instance Editor")
def step_impl(identifier):
    """I double click on the instance '<identifier>' in the Instance Editor"""
    Applicationexplorertabutility.double_click_instance_in_instance_editor(identifier)
  
@when("I double click on the {arg} folder in the Asset Workspace")
def step_impl(identifier):
    """I double click on the '<identifier>' folder in the Asset Workspace"""
    Applicationexplorertabutility.double_click_asset_workspace_folder(identifier)
  
@when("I press the '(.*)' arrow key on the '(.*)' folder in the Asset Workspace")
def step_impl(direction, identifier):
    """I press '<direction>' arrow key on the '<identifier>' in the Asset Workspace"""
    Applicationexplorertabutility.key_action_asset_workspace_folder(identifier, direction)
  
@when("I double click on the {arg} folder in the Template browser")
def step_impl(identifier):
    """I double click on the '<identifier>' folder in the Template browser"""
    Applicationexplorertabutility.double_click_templatebrowser_folder(identifier)
  
@when("I press the '(.*)' arrow key on the '(.*)' folder in Template browser")
def step_impl(direction, identifier):
    """I press the '<direction>' arrow key on the '<identifier>' folder in Template browser"""
    Applicationexplorertabutility.key_action_template_browser_folder(identifier, direction)

@then("Verify the status of Identifier in application browser with instance editor window")
def step_impl():
    """Verify the status of Identifier in application browser with instance editor window"""
    Applicationexplorertabutility.verify_status_instance_editor()

@then("Verify the details of invalid status in isntance editor window in Application Browser")
def step_impl():
    """Verify the details of invalid status in isntance editor window in Application Browser"""
    Applicationexplorertabutility.verify_invalid_details()

@when("I select the required filter in AE application browser pane as {arg}")
def step_impl(filter):
    """I select the required filter in AE application browser pane as '<Filter>'"""
    obj.selectfilterinappbrowserpane(filter)

@when("I select instances to be filtered from the listbox items {arg}")
def step_impl(instance):
    """I select instances to be filtered from the listbox items '<Instance>'"""
    obj.selectinstancefromfilterlistbox(instance)

@when("I select the filter combobox item as {arg}")
def step_impl(comboitem):
    """I select the filter combobox item as '<Comboitem>'"""
    obj.selectcomboboxitemfromfilterwindow(comboitem)

@when("I enter text to filter in the filter textbox as {arg}")
def step_impl(text):
    """I enter text to filter in the filter textbox as '<Text>'"""
    obj.enterfiltertextintextbox(text)

@when("I enter text to filter in the filter textbox of Asset Workspace as {arg}")
def step_impl(text):
    """I enter text to filter in the filter textbox of Asset Workspace as '<Text>'"""
    obj.enterfiltertextinassertworkspacetextbox(text)

@when("I select the filter in AE Asset Workspace pane as {arg}")
def step_impl(filter):
    """I select the filter in AE Asset Workspace pane as '<Filter>'"""
    obj.selectfilterinassetworkspace(filter) 

@when("I Enter FileLocation and FileName to be Import as {arg}")
def step_impl(import3):
    """I Enter FileLocation and FileName to be Import as'<Import1>'"""
    obj.enterfilelocationandfilenametobeimported(import1)
    
@when("I double click on the asset workspace in navigate to assetworkspace window as {arg}")
def step_impl(identifier):
    """I double click on the asset workspace in navigate to assetworkspace window as '<identifier>'"""
    obj.navigatetoassetworkspacemodaldialogwindowofaninstance(identifier)    
    
@when("I select multiple instances in application browser as {arg}")
def step_impl(param):
    """I select multiple instances in application browser as '<instance name>'"""
    Applicationexplorertabutility.multiclick_application_browser_template_AE(param)

@then("I verify instance is added in multiple workspace in context menu listing")
def step_impl():
    """I verify instance is added in multiple workspace in context menu listing"""
    Actionutility.verify_modal_dialog_window_navigate_asset_worskspace()
    
@then("I add and verify that instances are successfully added in different folders in the Application Browser with value {arg}")
def step_impl(instance_value):
  """I add and verify that instances are successfully added in different folders in the Application Browser with value '<instance_value>'"""
  Applicationexplorertabutility.add_instance_under_each_folders(instance_value)
  
@then("I select multiple items and verify the context menu in the Application Browser for {arg}")
def step_impl(instance_value):
  """I select multiple items and verify the context menu in the Application Browser for '<instance_value>'"""
  Applicationexplorertabutility.verify_contextMenu_MultipleSelection(instance_value)
  
@when("I create multiple folders under the root node in the Application Browser with value {arg}")
def step_impl(folder_value):
  """I create multiple folders under the root node in the Application Browser with value '<folder_value>'"""
  Applicationexplorertabutility.mutiple_folder_creation(folder_value)
  
@then("Verify mutiple instances can be opened in Application browser")
def step_impl():
  """Verify mutiple instances can be opened in Application browser"""
  Applicationexplorertabutility.verify_mutiple_instance_window()
  
  
@then("Verify the column names in Application Browser {arg}")
def step_impl(col_values):
  """Verify the column names in Application Browser '<col_values>'"""
  Applicationexplorertabutility.instance_column_names(col_values)
  
  
@then("Verify the * symbol is reflected when istance is modified in Application Browser {arg}")
def step_impl(templates):
  """Verify the * symbol is reflected when istance is modified in Application Browser '<templates>'"""
  Applicationexplorertabutility.verify_asterik_visibility(templates)
  
@when("I modify the exported csv file {arg} by deleting instance and link {arg}")
def step_impl(file, modify):
    """I modify the exported csv file '<File detail>' by deleting instance and link '<Modification>'"""
    obj.modifycsv(file, modify)
  
@when("I click on the status filter arrow in Application browser")
def step_impl():
    """I click on the status filter arrow in Application browser"""
    obj.clickonstatusfilterinae()
    
@then("I verify the checkboxes available in the status filter of Application browser")
def step_impl():
    """I verify the checkboxes available in the status filter of Application browser"""
    obj.verifycheckboxesinstatusfilter()
    
@when("I select the status filter in Application Browser as {arg}")
def step_impl(param):
    """I select the status filter in Application Browser as '<status_filter>'"""
    obj.selectstatusfilterinae(param)
    
@then("I verify the displayed instances in Application Browser")
def step_impl():
    """I verify the displayed instances in Application Browser"""
    obj.verifyinstancesinae()
    
@when("I click on the Grid/Tree view icon in Application Browser")
def step_impl():
    """I click on the Grid/Tree view icon in Application Browser"""
    obj.clickontogglebuttoninappbrowser() 