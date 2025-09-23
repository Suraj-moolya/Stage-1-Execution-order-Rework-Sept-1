Feature: 91119 - To Test the context menu command "Last Action Summary" on all applicable entities

  @TC_EPE_CP_PGSQL_91119
  @91119_1
  Scenario Outline: Create Control Project in Project Explorer
    # Note: This case is already covered in 90881.
    # We can reuse it via tag (creating_ControlProject_TC_EPE_AE_PGSQL_90881) in Execution Order.

  @91119_1-A
  Scenario Outline: Create Supervision Project in Project Explorer
    # Note: This case is already covered in 90881.
    # We can reuse it via tag (creating_supervision_TC_EPE_AE_PGSQL_90881) in Execution Order.
    
  @91119_2
  Scenario Outline: Verify "Last Action Summary" menu item state in Project Explorer
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
    And I RClick control project browser project browser in project explorer as '<Project>'
    Then the menu item '<item_name>' should be '<status>'
  
    @verify_context_menu_item_in_ControlProject
    Examples:
      | CP_SP_Tab            | Project         | item_name           | status   |
      | UnityProjectTreePane | M580_Standalone | Last Action Summary | Disabled |
      
    @verify_context_menu_item_in_Container
    Examples:
      | CP_SP_Tab            | Project    | item_name           | status   |
      | UnityProjectTreePane | Containers | Last Action Summary | Disabled |
  
    @verify_context_menu_item_in_ControlExecutable_1
    Examples:
      | CP_SP_Tab            | Project             | item_name           | status   |
      | UnityProjectTreePane | ControlExecutable_1 | Last Action Summary | Disabled |
    
    @verify_context_menu_item_in_SuperVisionProject
    Examples:
      | CP_SP_Tab          | Project          | item_name           | status   |
      | SupervisionProject | Supervision_Test | Last Action Summary | Disabled |
    
    @verify_context_menu_item_in_SuperVisionProject_Container
    Examples:
      | CP_SP_Tab          | Project    | item_name           | status   |
      | SupervisionProject | Containers | Last Action Summary | Disabled |
    
    @verify_context_menu_item_in_SuperVisionProject_Cluster_1
    Examples:
      | CP_SP_Tab          | Project   | item_name           | status   |
      | SupervisionProject | Cluster_1 | Last Action Summary | Disabled |
      
  @91119_2
  Scenario Outline: Verify "Last Action Summary" menu item state and Message in Project Explorer
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
    And I RClick control project browser project browser in project explorer as '<Project>'
    Then the menu item '<item_name>' should be '<status>'
    When I Select context menu item EC project browser in project explorer as '<item_name>'
    Then I verify Lock screen as '<Message>'
    When I click modal dialog window project browser in project explorer as '<Button>'
  
    @verify_context_menu_item_and_Click_in_ControlProject
    Examples:
      | CP_SP_Tab            | Project         | item_name           | status  | Message                         | Button |
      | UnityProjectTreePane | M580_Standalone | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
  
    @verify_context_menu_item_and_Click_in_SupervisionProject
    Examples:
      | CP_SP_Tab          | Project          | item_name           | status  | Message                         | Button |
      | SupervisionProject | Supervision_Test | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
  
    @verify_context_menu_item_and_Click_in_SupervisionProject_Container
    Examples:
      | CP_SP_Tab          | Project    | item_name           | status  | Message                         | Button |
      | SupervisionProject | Containers | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
  
    @verify_context_menu_item_and_Click_in_SupervisionProject_Cluster_1
    Examples:
      | CP_SP_Tab          | Project   | item_name           | status  | Message                         | Button |
      | SupervisionProject | Cluster_1 | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
  
    @verify_context_menu_item_and_Click_in_SupervisionProject_Tags
    Examples:
      | CP_SP_Tab          | Project | item_name           | status  | Message                         | Button |
      | SupervisionProject | Tags    | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
      
    @verify_context_menu_item_and_Click_in_ControlProject_regenerate
    Examples:
      | CP_SP_Tab            | Project         | item_name           | status  | Message                           | Button |
      | UnityProjectTreePane | M580_Standalone | Last Action Summary | Enabled | ReGenerate Completed Successfully | OK     |
      
    @verify_context_menu_item_and_Click_in_Container
    Examples:
      | CP_SP_Tab            | Project    | item_name           | status  | Message                         | Button |
      | UnityProjectTreePane | Containers | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
      
    @verify_context_menu_item_and_Click_in_Container_regenerate
    Examples:
      | CP_SP_Tab            | Project    | item_name           | status  | Message                           | Button |
      | UnityProjectTreePane | Containers | Last Action Summary | Enabled | Regenerate Completed Successfully | OK     |
      
    @verify_context_menu_item_and_Click_in_ControlExecutable_1_Build_All
    Examples:
      | CP_SP_Tab            | Project             | item_name           | status  | Message                           | Button |
      | UnityProjectTreePane | ControlExecutable_1 | Last Action Summary | Enabled | Build All completed successfully. | OK     |
      
    @verify_context_menu_item_and_Click_in_ControlExecutable_1_Build
    Examples:
      | CP_SP_Tab            | Project             | item_name           | status  | Message                       | Button |
      | UnityProjectTreePane | ControlExecutable_1 | Last Action Summary | Enabled | Build completed successfully. | OK     |
      
    @verify_context_menu_item_and_Click_in_ControlExecutable_1_GenerateAndBuild
    Examples:
      | CP_SP_Tab            | Project             | item_name           | status  | Message                        | Button |
      | UnityProjectTreePane | ControlExecutable_1 | Last Action Summary | Enabled | Generate and Build Successful! | OK     |
      
    # Note: Facet Assigning.
    # We can reuse it via tag (creating_control_project_and_trying_to_assign_facet_after_closing_InstanceEditor)(creating_supervision_project_and_trying_to_assign_facet_after_closing_InstanceEditor) in Execution Order.
    
  @91119_3
  Scenario Outline: right click control project and generate
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I RClick control project browser project browser in project explorer as '<Project>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
  
    @Generate_controlproject_and_Verify
    Examples:
      | CP_SP_Tab            | Project         | ContextMenu | Message                              |
      | UnityProjectTreePane | M580_Standalone | Generate    | Generate Control Project (Completed) |
      
    @Generate_container_and_Verify
    Examples:
      | CP_SP_Tab            | Project    | ContextMenu | Message                              |
      | UnityProjectTreePane | Containers | Generate    | Generate Control Project (Completed) |
  
    @Generate_SuperVisionProject
    Examples:
      | CP_SP_Tab          | Project          | ContextMenu | Message                                  |
      | SupervisionProject | Supervision_Test | Generate    | Generate Supervision Project (Completed) |
  
    @Generate_Containers_SuperVisionProject
    Examples:
      | CP_SP_Tab          | Project    | ContextMenu | Message                                  |
      | SupervisionProject | Containers | Generate    | Generate Supervision Project (Completed) |
  
    @Generate_Cluster_1_SuperVisionProject
    Examples:
      | CP_SP_Tab          | Project   | ContextMenu | Message                      |
      | SupervisionProject | Cluster_1 | Generate    | Generate Cluster (Completed) |
  
    @Generate_Tags_SuperVisionProject
    Examples:
      | CP_SP_Tab          | Project | ContextMenu | Message                   |
      | SupervisionProject | Tags    | Generate    | Generate Tags (Completed) |
      
  @91119_3
  Scenario Outline: right click control project and regenerate
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I RClick control project browser project browser in project explorer as '<Project>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And  I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
      
    @ReGenerate_controlproject_and_Verify
    Examples:
      | CP_SP_Tab            | Project         | ContextMenu | Message                                | Button |
      | UnityProjectTreePane | M580_Standalone | ReGenerate  | ReGenerate Control Project (Completed) | Yes    |
      
    @ReGenerate_containers_and_Verify
    Examples:
      | CP_SP_Tab            | Project    | ContextMenu | Message                                | Button |
      | UnityProjectTreePane | Containers | ReGenerate  | ReGenerate Control Project (Completed) | Yes    |
      
  @91119_4
  Scenario Outline: Verify "Last Action Summary" menu item state in Container Section
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
    And I Right click on container dock in project explorer as '<Project>'
    Then the menu item '<item_name>' should be '<status>'
  
    @verify_context_menu_item_in_Folder_1
    Examples:
      | CP_SP_Tab            | Project  | item_name           | status   |
      | UnityProjectTreePane | Folder_1 | Last Action Summary | Disabled |
  
    @verify_context_menu_item_in_TagContainer_1
    Examples:
      | CP_SP_Tab          | Project        | item_name           | status   |
      | SupervisionProject | TagContainer_1 | Last Action Summary | Disabled |
      
  @91119_5
  Scenario Outline: right click container section and generate
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I Right click on container dock in project explorer as '<container>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
  
    @Generate_Folder_1_in_containerSection
    Examples:
      | CP_SP_Tab            | container | ContextMenu | Message                          |
      | UnityProjectTreePane | Folder_1  | Generate    | Generate FBD Section (Completed) |
  
    @Generate_TagContainer_1_in_containerSection
    Examples:
      | CP_SP_Tab          | container      | ContextMenu | Message                            |
      | SupervisionProject | TagContainer_1 | Generate    | Generate Tag Container (Completed) |
      
  @91119_6
  Scenario Outline: right click container section and regenerate
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I Right click on container dock in project explorer as '<container>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And  I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
      
    @ReGenerate_ContainerSection_Folder_1
    Examples:
      | CP_SP_Tab            | container | ContextMenu | Message                          | Button |
      | UnityProjectTreePane | Folder_1  | ReGenerate  | Generate FBD Section (Completed) | Yes    |
      
  @91119_7
  Scenario Outline: Verify "Last Action Summary" menu item state and Message in Container Section
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I Right click on container dock in project explorer as '<container>'
    Then the menu item '<item_name>' should be '<status>'
    When I Select context menu item EC project browser in project explorer as '<item_name>'
    Then I verify Lock screen as '<Message>'
    When I click modal dialog window project browser in project explorer as '<Button>'    
   
   @verify_context_menu_item_and_Click_in_ContainerSection
    Examples:
      | CP_SP_Tab            | container | item_name           | status  | Message                         | Button |
      | UnityProjectTreePane | Folder_1  | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
   
   @verify_context_menu_item_and_Click_in_TagContainer_1
    Examples:
      | CP_SP_Tab          | container      | item_name           | status  | Message                         | Button |
      | SupervisionProject | TagContainer_1 | Last Action Summary | Enabled | Generate Completed Successfully | OK     |
      
  @verify_context_menu_item_and_Click_in_Folder_1_regenerate
  Examples:
    | CP_SP_Tab            | container | item_name           | status  | Message                           | Button |
    | UnityProjectTreePane | Folder_1  | Last Action Summary | Enabled | ReGenerate Completed Successfully | OK     |
    
  @91119_8
  Scenario Outline: Build All
    # Note: This case is already covered in 91111.
    # We can reuse it via tag (Select_BUILD_ALL_from_ControlExecutable_1_context_menu) in Execution Order.
   
  @91119_8_A
  Scenario Outline: Build 
    # Note: This case is already covered in 146.
    # We can reuse it via tag (Build_ControlEcecutable_1) in Execution Order.
   
  @91119_8_B
  Scenario Outline: Generate and Build 
    # Note: This case is already covered in 146.
    # We can reuse it via tag (GenerateAndBuild_ControlEcecutable_1) in Execution Order.
    
  @91119_9
  Scenario Outline: Genrate Tags in Supervision Project
    When I Expand control project browser PE project browser in project explorer as '<ProjectBrowser>'
    And I RClick control project browser project browser in project explorer as '<Project>'
    Then the menu item '<item_name>' should be '<status>'
    
  @Verify_Last_Action_Summary_for_Tags_in_SP
    Examples:
      | ProjectBrowser | Project | item_name           | status   |
      | Cluster_1      | Tags    | Last Action Summary | Disabled |
      
  @91119_10
  Scenario Outline: Map Workstation to Supervision Project
    When I Collapse control project browser PE project browser in project explorer
    And I Expand control project browser PE project browser in project explorer as '<project browser1>'
    And I Expand control project browser PE project browser in project explorer as '<project browser2>'
    And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
    And I Map workstation available for respective service and engine for supervision project as '<Service_Engine>' 
    Then Verify Action message in notification pannel container dock in project explorer as '<notification panel>'
    
    
  @ExpandAll_items_in_SuperVision_and_Mapping_Workstation_Alarm
    Examples:
      | project browser1 | project browser2 | project browser3 | Service_Engine                         | notification panel                 |
      | Supervision_Test | Executable       | Executable_1     | Alarm_1_P$$Not Assigned$$Workstation_1 | Map Service Executable (Completed) |
      
  @ExpandAll_items_in_SuperVision_and_Mapping_Workstation_IoServer_1
    Examples:
      | project browser1 | project browser2 | project browser3 | Service_Engine                          | notification panel                 |
      | Supervision_Test | Executable       | Executable_1     | IOServer_1$$Not Assigned$$Workstation_1 | Map Service Executable (Completed) |
      
  @ExpandAll_items_in_SuperVision_and_Mapping_Workstation_Report_1_P
    Examples:
      | project browser1 | project browser2 | project browser3 | Service_Engine                          | notification panel                 |
      | Supervision_Test | Executable       | Executable_1     | Report_1_P$$Not Assigned$$Workstation_1 | Map Service Executable (Completed) |
  
  @91119_11    
  Scenario Outline: Generate and Build from control executeable r-click
    When I RClick control project browser project browser in project explorer as '<project browser1>'
    And I Select context menu item EC project browser in project explorer as '<project browser2>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'

  @GenerateAndBuild_SupervisionEcecutable_1
  Examples:
    | SlNo. | project browser1    | project browser2   | ExpectedMessage                                       |
    | 1     | ControlExecutable_1 | Generate and Build | Generate and Build Supervision Executable (Completed) |
      
  @91119_12
  Scenario Outline: Export Control Project and Supervision Project
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I RClick control project browser project browser in project explorer as '<Supervision>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'
    
  @Export_ControlProject_System_1
    Examples:
      | CP_SP_Tab            | Supervision | context menu | Button | ExportFileName      | ExportFileFormat | ExpectedExportMessage      |
      | UnityProjectTreePane | System_1    | Export       | OK     | Last_Action_Summary | .sbk             | Export Project (Completed) |
      
  @Export_SupervisionProject_System_1
    Examples:
      | CP_SP_Tab          | Supervision | context menu | Button | ExportFileName         | ExportFileFormat | ExpectedExportMessage      |
      | SupervisionProject | System_1    | Export       | OK     | Last_Action_Summary_SP | .sbk             | Export Project (Completed) |
    
    
    #Note : Close Tabs After This(Tags - @close_M580_Standalone_Assignment_Editor)
         
  @91119_13
  Scenario Outline: Delete Control Project and Supervision Project
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I RClick control project browser project browser in project explorer as '<Supervision>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I click on Yes button in Message Box
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'
    
  @Delete_ControlProject_System_1
    Examples:
      | CP_SP_Tab            | Supervision     | context menu | ExportFileName      | ExportFileFormat | ExpectedMessage                    |
      | UnityProjectTreePane | M580_Standalone | Delete       | Last_Action_Summary | .sbk             | Delete Control Project (Completed) |
      
  @Delete_SupervisionProject_System_1
    Examples:
      | CP_SP_Tab          | Supervision      | context menu | ExportFileName         | ExportFileFormat | ExpectedMessage                    |
      | SupervisionProject | Supervision_Test | Delete       | Last_Action_Summary_SP | .sbk             | Delete Control Project (Completed) |
      
  @90881_14
  Scenario Outline: Perform Import at Folder From Root Level After Closing Instance Properties
    When I Navigate to '<CP_SP_Tab>' tab in project explorer tab
    And I RClick control project browser project browser in project explorer as '<ApplicationBrowserRoot>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
    And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Button>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'

    @Importing_Instance_From_RootNode_Of_ProjectBrowser
    Examples:
      | CP_SP_Tab            | ApplicationBrowserRoot | ContextMenuOption | ImportFileName      | ExpectedImportMessage | Button |
      | UnityProjectTreePane | System_1               | Import            | Last_Action_Summary | Import (Completed)    | OK     |