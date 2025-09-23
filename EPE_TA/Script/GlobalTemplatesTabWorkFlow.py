"""GlobalTemplatesTabWorkFlow"""  

from GlobalTemplatesTab import GlobalTemplatesTab
import Applicationutility
import Globaltemplatesutility
import Engineeringclientutility
class GlobalTemplatesTabWorkFlow:
    """GlobalTemplatesTabWorkFlow"""
    globaltemplatestab_obj = GlobalTemplatesTab()

        
    def textboxglobaltemplatesearchsearchtextandselectgte(self,param):
        """textboxglobaltemplatesearchsearchtextandselectgte"""
        try:
            Globaltemplatesutility.search_and_double_click_search_text_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecorerightclickonthesearchedtemplategte(self,param):
        """textboxglobaltemplatecorerightclickonthesearchedtemplategte"""
        try:
            Globaltemplatesutility.rclick_idedntifier_explorer_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecoreselectcontextmenuitemec(self,menu_item):
        """textboxglobaltemplatecoreselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonokduuplicateselected(self):
        """globaltemplatestab_obj.okduuplicatebutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.okduuplicatebutton.click()
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox.wait_for_object_disapear()
        
        
    def textboxduplicatewindowwaitforobjectdisapear(self,):
        """textboxduplicatewindowwaitforobjectdisapear"""
        try:
            undefined
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecorewaitforcircularprogressbar(self):
        """textboxglobaltemplatecorewaitforcircularprogressbar"""
        try:
            Engineeringclientutility.circularprogressbar_Wait()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontoolboxselected(self):
        """globaltemplatestab_obj.toolboxbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.toolboxbutton.click()
        
    def buttondocumentoutlineselected(self):
        """globaltemplatestab_obj.documentoutlinebutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.documentoutlinebutton.click()
        
        
    def textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte(self,name):
        """textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte"""
        try:
            Globaltemplatesutility.drag_toolbox_item_drop_composite_editor_GTE(name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsaveascompositeeditorselected(self):
        """globaltemplatestab_obj.saveascompositeeditorbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.saveascompositeeditorbutton.click()
        
        
    def textboxdescriptionentered(self,description7):
        """globaltemplatestab_obj.descriptiontextbox"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.descriptiontextbox.enter_text(description7)
        
    def buttonsaveselected(self):
        """globaltemplatestab_obj.savebutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.click()
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.wait_for_object_disapear()
        
    def buttoncancelselected(self):
        """globaltemplatestab_obj.cancelbutton"""
        Applicationutility.modal_dialog_window_button('Cancel')
        
    def buttonsaveselected1(self):
            """globaltemplatestab_obj.savebutton"""
            GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.click()
            
            
    def closeduuplicateselected(self):
        """globaltemplatestab_obj.okduuplicatebutton"""    
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox.object.Close()
        
        
    def verify_dup_win(self):
       try:
          win = GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox
          if win:
            Log.Message('The Duplicate window is open')
       except:
          Log.Checkpoint('The duplicate window is closed')
               
    def verifytittlebar(self, tabname):
        """verifytittlebar"""
        try:
            Globaltemplatesutility.verify_title_bar(tabname)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesearchsearchtextandrightclickgte(self,param):
        """textboxglobaltemplatesearchsearchtextandselectgte"""
        try:
            Globaltemplatesutility.search_and_right_click_search_text_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplateselecttabgte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.select_tab_in_gtw(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatedraganddroptoolsgte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.drag_and_drop_toolbox_to_window(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindowclickbuttongte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.click_item_in_save_as_window(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindownameandversiongte(self, name, version):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.change_template_name_and_version(name, version)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindowndescgte(self, desc):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.description_for_save_as_window(desc)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonnextselected(self, button):
        """globaltemplatestab_obj.buttonnextselected"""
        try:
            Globaltemplatesutility.panel_button_gtw(button)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonbrowseselected(self):
        """globaltemplatestab_obj.buttonbrowseselected"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.browsebuttonselected.click()
        
    def buttonaddselected(self, elem):
        """globaltemplatestab_obj.buttonaddselected"""
        try:
            Globaltemplatesutility.click_add_icon_gtw(elem)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplateexpandpropertiesgte(self, elem):
        """globaltemplatestab_obj.buttonaddselected"""
        try:
            Globaltemplatesutility.expand_librarys_in_gtw(elem)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplateselecttaggte(self, desc):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.select_tag_gtw(desc)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplatedraganddropgeniegte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.drag_and_drop_genie_to_genie_facet_in_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplateclicklibrarygte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.click_library_in_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplaterightclickcreatedtemplategte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.right_click_created_template_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
            
    def GTimportfilenamefilelocation(self, path, folder, file):
        """GTimportfilenamefilelocation"""
        try:
            Globaltemplatesutility.GlobalTemplates_Import(path, folder, file)
        except Exception as ex:
            raise Exception(ex) from ex
                
    def rclickcontroltemplateheader(self):
        """globaltemplatestab_obj.controltemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.controltemplateheader.right_click()
        
    def clickcontroltemplateheader(self):
        """globaltemplatestab_obj.controltemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.controltemplateheader.click()
        
    def rclickmotortemplateheader(self):
        """globaltemplatestab_obj.motortemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.motortemplateheader.right_click()
        
    def rclicklogictemplateheader(self):
        """globaltemplatestab_obj.controltemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.logictemplateheader.right_click()
        
    def clicktemplatizerbutton(self):
        """globaltemplatestab_obj.templatizerbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.templatizerbutton.click()
        
    def clickopencontrolparticipantbutton(self):
        """globaltemplatestab_obj.opencontrolparticipantbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.opencontrolparticipantbutton.click()
        
    def rclicksupervisiontemplateheader(self):
        """globaltemplatestab_obj.supervisiontemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.supervisiontemplateheader.right_click()

    def clicksupervisiontemplateheader(self):
        """globaltemplatestab_obj.supervisiontemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.supervisiontemplateheader.click()
        
    def rclickgeniestemplateheader(self):
        """globaltemplatestab_obj.geniestemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.geniestemplateheader.right_click()
        
    def rclickpumprightgenietemplateheader(self):
        """globaltemplatestab_obj.pumprightgenietemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.pumprightgenietemplateheader.right_click()
        
    def clickfittocontentbutton(self):
        """globaltemplatestab_obj.fittocontentbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.fittocontentbutton.click()
        
    def clickopenparticipantbutton(self):
        """globaltemplatestab_obj.opencontrolparticipantbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.openparticipantbutton.click()
    
    def clickStateSelectorapprovedinsaveas(self):
        """globaltemplatestab_obj.StateSelectorapprovedinsaveas"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.StateSelectorapprovedinsaveas.click() 
    
    def clickOldStateSelectorapprovedinsaveas(self):
        """globaltemplatestab_obj.StateSelectorapprovedinsaveas"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.oldStateSelectorapprovedinsaveas.click() 
    
    def clickapprovedcomboitem(self):
        """globaltemplatestab_obj.approvedcomboitem"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.approvedcomboitem.click()
        
    def verifyviewmodeCompositeeditor(param):
        """verifyviewmodeCompositeeditor"""
        try:
            Globaltemplatesutility.verify_viewmode_Composite_editor(param)
        except Exception as ex:
            raise Exception(ex) from ex
                
    def clickeditmenuitem(param):
        """clickeditmenuitem"""
        try:
            Globaltemplatesutility.Click_edit_menuitem(param)
        except Exception as ex:
            raise Exception(ex) from ex  
                 
    def verifychangeslogwindow():
        """verifychangeslogwindow"""
        try:
            Globaltemplatesutility.verify_changeslog_window()
        except Exception as ex:
            raise Exception(ex) from ex

    def clickainputsignalfaceteditorheader(self):
            """globaltemplatestab_obj.AInputSignalheadertext"""
            GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.AInputSignalheadertext.click()
            
    def clickDOblockinterfaceeditorheader(self):
            """globaltemplatestab_obj.Doblockinterfaceeditor"""
            GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.Doblockinterfaceeditor.click()   
            
    def verifytemplateisinrenamingstateinterfaceeditor(self,Identifier):
            """verifytemplateisinrenamingstateinterfaceeditor"""
            try:
                Globaltemplatesutility.verify_module_renaming_state_interface_editor(Identifier)
            except Exception as ex:
                raise Exception(ex) from ex             

    def clickeditormenuitem(self,param):
        """clickeditormenuitem"""
        try:
            Globaltemplatesutility.click_editor_menuitem(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def verifyheaderpanelitemsEC(self,header_value):
        """verifyheaderpanelitemsEC"""
        try:
            Globaltemplatesutility.verify_header_panel_items_EC(header_value)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def verifytemplateontheeditorwindowGT(self,template):
        """verifytemplateontheeditorwindowGT"""
        try:
            Globaltemplatesutility.verify_the_template_on_the_editor_window_GT(template)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def verifyelementontheeditorwindowGT(self,element):
        """verifyelementontheeditorwindowGT"""
        try:
            Globaltemplatesutility.verify_element_on_the_editor_window_GT(element)
        except Exception as ex:
            raise Exception(ex) from ex
      
    def selectallkey(self):
        """selectallkey"""
        try:
            Globaltemplatesutility.selectall_key()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def copykey(self):
        """copykey"""
        try:
            Globaltemplatesutility.copy_key()
        except Exception as ex:
            raise Exception(ex) from ex
                
    def pastekey(self):
        """pastekey"""
        try:
            Globaltemplatesutility.paste_key()
        except Exception as ex:
            raise Exception(ex) from ex           
    
    def verifyGTwarningmessage(self, param):
        """verifyGTwarningmessage"""
        try:
            Globaltemplatesutility.verify_warning_text_in_GT_pane(param)
        except Exception as ex:
            raise Exception(ex) from ex
                        
    def findandentersearchtext(self, param):
        """findandentersearchtext"""
        try:
            Globaltemplatesutility.find_and_search_text(param)
        except Exception as ex:
            raise Exception(ex) from ex
                    
    def findandRclicksearchtext(self, param):
        """findandRclicksearchtext"""
        try:
            Globaltemplatesutility.find_and_right_click_search_text_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
     
    def rclickElement(self, param):
        """rclickElement"""
        try:
            Globaltemplatesutility.right_click_on_Elements_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex        
        
    def rclickFunction(self, param):
        """rclickFunction"""
        try:
            Globaltemplatesutility.right_click_on_Func(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def rclickInputValue(self, param):
        """rclickInputValue"""
        try:
            Globaltemplatesutility.right_click_on_InputValue_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def rclickSystemParameter(self, param):
        """rclickSystemParameter"""
        try:
            Globaltemplatesutility.right_click_on_Parameter_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex       
        
    def rclickworkspaceGTE(self): 
        """rclickworkspaceGTE"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.compositeeditorreadview.right_click()
        
    def rclickGreyhexagon(self, param):
        """rclickGreyhexagon""" 
        try:
            Globaltemplatesutility.right_click_on_grey_hexagon_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def rclickOrangehexagon(self, param):
        """rclickOrangehexagon""" 
        try:
            Globaltemplatesutility.right_click_on_orange_hexagon_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def rclickblockinInterfaceeditor(self, param): 
        """rclickblockinInterfaceeditor"""
        try:
            Globaltemplatesutility.right_click_on_block_in_Interface_Editor(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def draganddroptoolboxitemtoInterfaceeditor(self, param): 
        """draganddroptoolboxitemtoInterfaceeditor"""
        try:
            Globaltemplatesutility.drag_and_drop_toolbox_item_to_Interface_Editor_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
                
    def rclicktransformationiteminInterfaceeditor(self, param): 
        """rclicktransformationiteminInterfaceeditor"""
        try:
            Globaltemplatesutility.right_click_on_transformation_item_in_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
                    
    def rclicklinkinInterfaceeditor(self): 
        """rclicklinkinInterfaceeditor"""
        try:
            Globaltemplatesutility.RClick_link_in_Interface_Editor()
        except Exception as ex:
            raise Exception(ex) from ex
                
    def rclicklinkinCompositeeditor(self, param): 
        """rclicklinkinCompositeeditor"""
        try:
            Globaltemplatesutility.RClick_link_in_Composite_Editor(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def multiselectitemsinGTEeditor(self, param): 
        """multiselectitemsinGTEeditor"""
        try:
            Globaltemplatesutility.multiselect_GTE_items(param)
        except Exception as ex:
            raise Exception(ex) from ex

    def verifyContextSubMenuItemsEC():
        """verifyContextSubMenuItemsEC"""
        try:
            Globaltemplatesutility.verify_Context_SubMenu_Items_EC()
        except Exception as ex:
            raise Exception(ex) from ex
             
                     

