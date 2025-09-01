Feature: 90881 - To Test Locking use cases in Application explorer with PostGre SQL Database on Fresh System.

@TC_EPE_AE_PGSQL_90881

@90881_0
Scenario Outline: Create Folder in Application Explorer
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>' 
  
  @Create_Folder 
  Examples:
    | ApplicationBrowserRoot | ContextItem   |
    | System_1               | Create Folder |

@90881_1
Scenario Outline: Drag and Drop Instance from Template Browser to Application Browser
  When I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
  And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<TemplatesBrowser2>'
  Then Verify the template is present in Application browser as '<TemplatesBrowser1>'

  @drag_drop_motorgp
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2          |
    | MotorGP           | MotorGP$$1.0.123$$Folder_1 |

  @drag_drop_valvegp
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2          |
    | ValveGP           | ValveGP$$1.0.100$$Folder_1 |
  
  @drag_drop_analoginputgp
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2                |
    | AnalogInputGP     | AnalogInputGP$$1.0.138$$Folder_1 |
 
@90881_2
Scenario Outline: Instance Properties Panel Open in Application Explorer
  When I rclick application browser template AE Application browser in application explorer as '<TemplatesBrowser2>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>' 
  
  @InstancePropertiy_for_MotorGP   
  Examples:
    | TemplatesBrowser2 | ContextItem |
    | MotorGP$$1.0.123  | Properties  |
     
@90881_3
Scenario Outline: Create Control Project in Project Explorer
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
  And I RClick control project browser project browser in project explorer as '<ProjectBrowser1>'
  And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
  And I Select controller in context menu as '<Controller>'
  And I rename the ControlProject as '<ControllerName>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel1>'

  @creating_control_project_TC_EPE_AE_PGSQL_90881
  Examples:
    | MainToolBar1     | ProjectBrowser1 | ContextMenu            | Controller | ControllerName  | NotificationPanel1                 |
    | Project Explorer | System_1        | Create Control Project | M580       | M580_Standalone | Update Control Project (Completed) |

@90881_4
Scenario Outline: Assigning Facets in Project Explorer with Instance Properties Panel Open in Application Explorer
  When I Dclick Control project broswer project browser in project explorer as '<ProjectBrowser2>'
  And I drag and Drop the Each instance to Each Sections as '<PropertieName>' '<ControllerName>'
  And I click modal dialog window project browser in project explorer as '<Button>'
  Then I verify Lock screen as '<Message>'
  When I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel1>'

  @assigning_facet_in_ControlProject_without_closing_InstanceEditor
  Examples:
    | ProjectBrowser2 | Button | Message                                                            | PropertieName | NotificationPanel1            | ControllerName  |
    | Containers      | OK     | The object MotorGP_1 is currently locked for instance modification | Folder_1      | Facet Assign (Not successful) | M580_Standalone |

@90881_5A
Scenario Outline: Create Supervision Project in Project Explorer
  When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
  And I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
  And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel>'
  When I RClick control project browser project browser in project explorer as '<Project>'
  And I Select context menu item EC project browser in project explorer as '<ContextMenu1>'
  And I rename the ControlProject as '<ControllerName>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel2>'

  @creating_supervision_TC_EPE_AE_PGSQL_90881
  Examples:
    | CP_SP_Tab          | ProjectBrowser | ContextMenu                | Project       | ContextMenu1 | ProjectBrowser2 | ControllerName   | NotificationPanel                      | NotificationPanel2                     |
    | SupervisionProject | System_1       | Create Supervision Project | Supervision_1 | Rename       | Containers      | Supervision_Test | Create Supervision Project (Completed) | Update Supervision Project (Completed) |

@90881_5B
Scenario Outline: Assigning Facets with Instance Properties Panel Open in Application Explorer
  When I Dclick Control project broswer project browser in project explorer as '<ProjectBrowser2>'
  And I drag and Drop the Each instance to Each Sections as '<PropertieName>' '<ControllerName>'
  And I click modal dialog window project browser in project explorer as '<Button>'
  Then I verify Lock screen as '<Message>'
  When I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel1>'

  @assigning_facet_in_SupervisionProject_without_closing_InstanceEditor
  Examples:
    | ProjectBrowser2 | PropertieName | ControllerName   | Button | Message                                                            | NotificationPanel1            |
    | Containers      | Folder_1      | Supervision_Test | OK     | The object MotorGP_1 is currently locked for instance modification | Facet Assign (Not successful) |
    
    
@90881_6
Scenario Outline: Replace Template from Context Menu in Application Explorer While Instance Properties with Open
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
  And I rclick application browser template AE Application browser in application explorer as '<ApplicationBrowser>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>'
  And I select the template to replace in replace template as '<ReplaceTemplate>'
  And I Select button in the modal dialoge window as '<Button>'
  Then I verify Lock screen as '<Message>'
  When I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel>'
  
  @UpdatingTemplate_without_closing_InstanceEditor
  Examples:
    | MainToolBar          | ApplicationBrowser | ContextItem      | ReplaceTemplate           | Button | Message                                                            | NotificationPanel                          |
    | Application Explorer | MotorGP_1$$1.0.123 | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 | OK     | The object MotorGP_1 is currently locked for instance modification | Replace Instance Template (Not successful) |

    
# ----------------------------------------------------------------
# NOTE: The following scenario Update Template We Should try with lower Version for now i tried with latest Version
# for both Without closing Instance Edittor and After closing Instance Editor
# ----------------------------------------------------------------

@90881_7
Scenario Outline: Update Template from Context Menu in Application Explorer While Instance Properties with Open
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
  And I rclick application browser template AE Application browser in application explorer as '<ApplicationBrowser>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>'
  And I Select button in the modal dialoge window as '<Button>'
  
  @ReplacingTemplate_without_closing_InstanceEditor
  Examples:
    | MainToolBar          | ApplicationBrowser | ContextItem     | ReplaceTemplate           | Button | Message                                                            | NotificationPanel                          |
    | Application Explorer | MotorGP_1$$1.0.123 | Update Template | INTERLOCK4ONGP_UC$$1.0.14 | OK     | The object MotorGP_1 is currently locked for instance modification | Replace Instance Template (Not successful) |
     
       
@90881_8
Scenario Outline: Perform Export at Folder From Root Level While Instance Properties Panel Is Open
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
  Then I verify Lock screen as '<Message>'
  When I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

  @Exporting_Instance_From_RootNode_Of_ApplicationBrowserr_While_Instance_propertie_Open
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ExportFileName | ExportFileFormat | ExpectedExportMessage   | Message                                                            | Button |
    | 1    | System                 | Export            | System_1       | .csv             | Export (Not successful) | The object MotorGP_1 is currently locked for instance modification | OK     |
    
@90881_9
Scenario Outline: Perform Import at Folder From Root Level While Instance Properties Panel Is Open
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
  And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as '<Button>'
  And I click '<Button>' Button in Import Warning Winow
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'

  @Importing_Instance_From_RootNode_Of_ApplicationBrowser_While_Instance_propertie_Open
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ImportFileName | ExpectedImportMessage                                                                 | Button |
    | 1    | System                 | Import            | System_1       | Import is not successful - Folder_1 locked for modification (Completed with warnings) | OK     |
    
@90881_10
Scenario Outline: Perform Delete at Folder From Root Level While Instance Properties Panel Is Open
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Select button in the modal dialoge window as '<Button>'
  Then I verify Lock screen as '<Message>'
  When I click modal dialog window project browser in project explorer as '<Button1>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel>'
  
  @Deleting_Instance_From_RootNode_Of_ApplicationBrowser_While_Instance_propertie_Open
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | Button | Message                                                            | NotificationPanel              | Button1 |
    | 1    | Folder_1               | Delete            | Yes    | The object MotorGP_1 is currently locked for instance modification | Delete Folder (Not successful) | OK      |
    
@90881_11
  Scenario Outline: Close Instance properties in Application Explorer - Close ( X )
  When I Close instance editor tab Instance editor close in application explorer as '<Instance editor>'
  
  @Close_Instance_Property_MotorGP
  Examples:
    | SlNo. | Instance editor |
    | 1     | MotorGP_1       |
    
@90881_12
Scenario Outline: Assigning Facet in Project Explorer After Closing Instance Properties Panel
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
  And I Navigate to '<CP_SP_Tab>' tab in project explorer tab
  And I drag and Drop the Each instance to Each Sections as '<PropertieName>' '<ControllerName>'
  And I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel1>'

  @creating_control_project_and_trying_to_assign_facet_after_closing_InstanceEditor
  Examples:
    | MainToolBar1     | Button | PropertieName | NotificationPanel1       | ControllerName  | CP_SP_Tab            |
    | Project Explorer | OK     | Folder_1      | Facet Assign (Completed) | M580_Standalone | UnityProjectTreePane |
    
    
@90881_13
Scenario Outline: Assigning Facet in Supervision After Closing Instance Properties Panel
  When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
  And I drag and Drop the Each instance to Each Sections as '<PropertieName>' '<ControllerName>'
  And I click modal dialog window project browser in project explorer as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel1>'

  @creating_supervision_project_and_trying_to_assign_facet_after_closing_InstanceEditor
  Examples:
    | CP_SP_Tab          | PropertieName | ControllerName   | Button | NotificationPanel1       |
    | SupervisionProject | Folder_1      | Supervision_Test | OK     | Facet Assign (Completed) |
    
@90881_14
Scenario Outline: Replace Template from Context Menu in Application Explorer After Closing Instance Properties
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
  And I rclick application browser template AE Application browser in application explorer as '<ApplicationBrowser>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>'
  And I select the template to replace in replace template as '<ReplaceTemplate>'
  And I Select button in the modal dialoge window as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel>'
  
  @UpdatingTemplate_After_closing_InstanceEditor
  Examples:
    | MainToolBar          | ApplicationBrowser | ContextItem      | ReplaceTemplate           | Button | NotificationPanel                     |
    | Application Explorer | MotorGP_1$$1.0.123 | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 | OK     | Replace Instance Template (Completed) |
    
@90881_15
Scenario Outline: Perform Export at Folder From Root Level After Closing Instance Properties
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

  @Exporting_Instance_From_RootNode_Of_ApplicationBrowser_After_closing_InstanceEditor
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ExportFileName                          | ExportFileFormat | ExpectedExportMessage | Button |
    | 1    | System                 | Export            | MotorGP_1_After_Closing_Instance_Editor | .csv             | Export (Completed)    | OK     |
  
@90881_16
Scenario Outline: Perform Import at Folder From Root Level After Closing Instance Properties
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
  And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as '<Button>'
  And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Button>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'

  @Importing_Instance_From_RootNode_Of_ApplicationBrowser_After_closing_InstanceEditor
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ImportFileName                          | ExpectedImportMessage | Button |
    | 1    | System                 | Import            | MotorGP_1_After_Closing_Instance_Editor | Import (Completed)    | OK     |

@90881_17
Scenario Outline: Perform Delete at Folder From Root Level After Closing Instance Properties
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Select button in the modal dialoge window as '<Button>'
  Then Verify Action message in notification pannel container dock in project explorer as '<NotificationPanel>'
  
  @Deleting_Instance_From_RootNode_Of_ApplicationBrowser_after_closing_InstanceEditor
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | Button | NotificationPanel         |
    | 1    | Folder_1               | Delete            | Yes    | Delete Folder (Completed) |

# ----------------------------------------------------------------
# NOTE: After Deleting Folder Repeat step @90881_0 and @90881_1
# ----------------------------------------------------------------     
      
@90881_18
Scenario Outline: Instance Edit Links Panel Open in Application Explorer
  When I rclick application browser template AE Application browser in application explorer as '<TemplatesBrowser2>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>' 
  
  @EditLink_for_MotorGP   
  Examples:
    | TemplatesBrowser2 | ContextItem |
    | MotorGP$$1.0.123  | Edit Links  |
    
