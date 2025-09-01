Feature: 90882 - To Test the Progress Status of Instances when assigned instance is imported with PostGre SQL

@TC_EPE_AE_PGSQL_90882
@90882_1
Scenario Outline: Creating multiple instances by dragging and dropping template to folder
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I selected Create Folder in context menu
  And I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
  And I drag Template from Template browser and drop to Application browser '<Count>' times with template as '<TemplateBrowser2>'
  Then Verify the template is present in Application browser as '<TemplatesBrowser1>'

  @DragDrop_Instance_MotorGP_To_Folder_5_Times
  Examples:
    | SlNo | ApplicationBrowserRoot | TemplatesBrowser1 | TemplateBrowser2           | Count |
    | 1    | System                 | MotorGP           | MotorGP$$1.0.123$$Folder_1 | 5     |


@90882_2
Scenario Outline: Exporting instance from root node of AE
  When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

  @Exporting_Instance_From_RootNode_Of_ApplicationBrowser
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ExportFileName               | ExportFileFormat | ExpectedExportMessage |
    | 1    | System                 | Export            | System_1_Exporting_5Instance | .csv             | Export (Completed)    |
    

  @Exporting_Instance_From_RootNode_Of_ApplicationBrowser_Before_instance_prop_open
  Examples:
    | SlNo | ApplicationBrowserRoot | ContextMenuOption | ExportFileName | ExportFileFormat | ExpectedExportMessage |
    | 1    | System                 | Export            | System_1       | .csv             | Export (Completed)    |

# ----------------------------------------------------------------
# NOTE: Create Control Project Covered in TC_EPE_AE_PGSQL_90881 
# Used Via Tags in Execution
# ----------------------------------------------------------------
    
@90882_3
Scenario Outline: Assigning All Instances to Control Project
  When I navigate to explorers MainToolBar in system explorer as '<TabName>'
  And I Navigate to '<CP_SP_Tab>' tab in project explorer tab
  And I Dclick Control project broswer project browser in project explorer as '<ContainerNode>'
  And I drag and Drop the Each instance to Each Sections as '<InstanceName>' '<ControlProjectName>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'

  @Assigning_All_Instances_in_ControlProject_TC_EPE_AE_PGSQL_90882
  Examples:
    | ControlProjectName | ContainerNode | InstanceName | Button | TabName          | ExpectedMessage          | CP_SP_Tab            |
    | M580_Standalone    | Containers    | Folder_1     | OK     | Project Explorer | Facet Assign (Completed) | UnityProjectTreePane |


# ----------------------------------------------------------------
# NOTE: Create SuperVision Project Covered in TC_EPE_AE_PGSQL_90881 
# Used Via Tags in Execution
# ----------------------------------------------------------------
@90882_4
Scenario Outline: Assigning All Instances to Supervision Project
  When I Navigate to '<TabName>' tab in project explorer tab
  And I Dclick Control project broswer project browser in project explorer as '<ContainerNode>'
  And I drag and Drop the Each instance to Each Sections as '<InstanceName>' '<ControllerName>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'

  @Assigning_All_Instances_in_SuperVisionProject_TC_EPE_AE_PGSQL_90882
  Examples:
    | ControllerName   | TabName            | ContainerNode | InstanceName | ExpectedMessage          |
    | Supervision_Test | SupervisionProject | Containers    | Folder_1     | Facet Assign (Completed) |


@90882_5  
Scenario Outline: Verify Progress Status
  When I navigate to explorers MainToolBar in system explorer as '<TabName1>'
  Then Verify the progress status and tooltip for all visible instances in the Application browser  
  
  @Verify_status_progress
  Examples:
    | SlNo | TabName1             |
    | 1    | Application Explorer |
    
@90882_6
Scenario Outline: Update exported file for Instance by setting Control Logic Failure and Control Logic Interlocks to False
  When I Update values of '<headings>' for instance '<instance_name>' in exported file '<file_name>'
  
  @csv_edit
  @revert
  Examples:
    | SlNo | file_name                        | instance_name | headings                                             |
    | 1    | System_1_Exporting_5Instance.csv | MotorGP_1     | Control.Failures.Enabled$$Control.Interlocks.Enabled |


@90882_7
Scenario Outline: Verify importing instances via right-click on system node and handling conflicts during import
  When I navigate to explorers MainToolBar in system explorer as '<TabName>'
  And I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
  And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileNameWithFormat>'
  And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as '<PrimaryButton>'
  And I Handle the import conflict by updating the instance '<InstanceName>' and skipping the rest
  And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<PrimaryButton>'
  Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'
  Then Verify the progress status and tooltip for all visible instances in the Application browser

@Import_From_ApplicationRoot_after_chnging_Data_in_CSV
@Import_From_ApplicationRoot_After_Revert
Examples:
  | SlNo | ApplicationBrowserRoot | ContextMenuOption | TabName              | ImportFileNameWithFormat     | PrimaryButton | InstanceName | ExpectedMessage    |
  | 1    | System_1               | Import            | Application Explorer | System_1_Exporting_5Instance | OK            | MotorGP_1    | Import (Completed) |