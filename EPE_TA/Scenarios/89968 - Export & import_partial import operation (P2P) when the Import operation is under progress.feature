Feature: 89968 - After doing the Manage P2P check for Export & import_partial import operation or Delete the source_Destination executable (P2P) when the Import operation is under progress

  @89968_1
  Scenario Outline: Manage Peer to Peer
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    When I Drag and drop from remote varaibles to source variables in P2P as '<Server>'
    And I selected Rename Pop up Ok in message box
     
  @Navigate_Manage_P2P_Window_for_M580_Standalone
  Examples:
    | ProjectBrowser  | ContextMenu         | Button | Server                         |
    | M580_Standalone | Manage Peer to Peer | Next   | PES_CONST_TRUE$$PES_CONST_TRUE |
    
    
  @89968_2
  Scenario Outline: Performing Variable Mapping in P2P
    When I Drag and drop from remote varaibles to source variables in P2P as '<Server>'
     
  @P2P_Variable_mapping_for_ValveGP
  Examples:
    | Server                                   |
    | ValveGP_1_OpenPosV$$ValveGP_1_OpenPosV   |
    | ValveGP_1_OPV$$ValveGP_1_OPV             |
    | ValveGP_1_ClosePosV$$ValveGP_1_ClosePosV |
    
  @89968_3
  Scenario Outline: Verifying Mapping Status in Notification Pannel
    When I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify Action message in notification pannel project browser in project explorer as '<Message>'
    
  @Verify_P2P_in_NP
  Examples:
    | Button | Message                                       |
    | OK     | Manage Peer To Peer Communication (Completed) |
    
  @89968_4
  Scenario Outline: Export P2P
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'
    
    @Export_P2P_M580_Standalone
    Examples:
      | ProjectBrowser  | ContextMenu | Button | ExportFileName | ExportFileFormat | ExpectedExportMessage      |
      | M580_Standalone | Export      | OK     | P2P_M580       | .sbk             | Export Project (Completed) |
      
      
  #Note: Before deleting close tabs in Control Project (@close_M580_Standalone2.ControlExecutable_1.Manage)  
  @89968_5
  Scenario Outline: Delete P2P
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And I click on Yes button in Message Box
    And I Click Yes button in P2P Message Box
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedMessage>'
    
    @Delete_CP_M580_P2P
    Examples:
      | ProjectBrowser  | ContextMenu | ExpectedMessage                    |
      | M580_Standalone | Delete      | Delete Control Project (Completed) |
      
  @89968_6
  Scenario Outline: Import P2P
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as '<Button>'
    And I Click Yes button in P2P Message Box
    Then Verify notification panel message Notification Pannel in message box as '<ExpectedImportMessage>'

    @Importing_P2P_M580_Standalone
    Examples:
      | ProjectBrowser | ContextMenuOption | ImportFileName | ExpectedImportMessage | Button |
      | System_1       | Import            | P2P_M580       | Import (Completed)    | OK     |
      
  @89968_7
  Scenario Outline: Verify Mapping in P2P
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    Then I verify that the variable '<Identifiers>' are mapped in the Peer to Peer Configuration
    When I click modal dialog window project browser in project explorer as '<Button1>'
    
    @Verify_P2P_Mapping_in_M580_Standalone
    Examples:
      | ProjectBrowser  | ContextMenuOption   | Button | Identifiers                                                            | Button1 |
      | M580_Standalone | Manage Peer to Peer | Next   | ValveGP_1_OPV$$ValveGP_1_ClosePosV$$ValveGP_1_OpenPosV$$PES_CONST_TRUE | OK      |
      
  
      
  @89968_8
  Scenario Outline: Deleting Control Project while Importing
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextMenuOption>'
    And I Enter File Name and File Format in Import Window EC Windows Explorer as '<ImportFileName>'
    And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as '<Button>'
    And I Click Yes button in P2P Message Box
    And I RClick control project browser project browser in project explorer as '<ProjectBrowser1>'
    And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
    And I click on Yes button in Message Box
    And I Click Yes button in P2P Message Box
    Then I verify Lock screen as '<Message>'
    When I click modal dialog window project browser in project explorer as '<Button>'

    @Importing_P2P_M580_Standalone
    Examples:
      | ProjectBrowser | ContextMenuOption | ImportFileName | ExpectedImportMessage | Button | ProjectBrowser1 | ContextMenu | Message                                                               |
      | System_2       | Import            | P2P_M580       | Import (Completed)    | OK     | M580_Standalone | Delete      | The object System_2 is currently locked for creating Control Project. |