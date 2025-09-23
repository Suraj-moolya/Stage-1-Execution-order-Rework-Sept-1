Feature: 91115 - Check for the lock generation of facets with various state in different FBD section.

  @91115_1
  Scenario Outline: Change the Description Of Instance and Verify Assignment State
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I rclick application browser template AE Application browser in application explorer as '<TemplatesBrowser>'
    And I Select context menu item EC Application browser in application explorer as '<ContextItem>' 
    And I Enter description AE Instance description in application explorer
    And I selected Instance editor save in application explorer
    And I Click on buttons as '<button>'
    And I Close instance editor tab Instance editor close in application explorer as '<InstanceEdittor>'
    And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I Click on FBDSection in Container Section '<projectBrowser>'
    Then I verify the section is generated successfully as '<Facet_Name>' '<Facet_State>'
    
  @Changing_Desc_for_MotorGP_1.0.123_Verify_Assignment  
  Examples:
    | MainToolBar          | TemplatesBrowser   | ContextItem | InstanceEdittor | button | MainToolBar1     | Facet_Name        | projectBrowser | Facet_State |
    | Application Explorer | MotorGP_1$$1.0.123 | Properties  | MotorGP_1       | Yes    | Project Explorer | MotorGP_1_MotorGP | FBDSection_1   | OutOfDate   |
    
  @Changing_Desc_for_MotorGP_2.0.123_Verify_Assignment  
  Examples:
    | MainToolBar          | TemplatesBrowser   | ContextItem | InstanceEdittor | button | MainToolBar1     | Facet_Name        | projectBrowser | Facet_State |
    | Application Explorer | MotorGP_2$$1.0.123 | Properties  | MotorGP_2       | Yes    | Project Explorer | MotorGP_2_MotorGP | FBDSection_2   | OutOfDate   |
    
    
  @91115_2
  Scenario Outline: Delete 2 FBDSection
    When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
    And I click modal dialog window project browser in project explorer as '<Button>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    
    @delete_FBD_Section_5
    Examples:
      | containerinstance    | Button | Message                        |
      | FBDSection_5$$Delete | Yes    | Delete FBD Section (Completed) |
      
    @delete_FBD_Section_6
    Examples:
      | containerinstance    | Button | Message                        |
      | FBDSection_6$$Delete | Yes    | Delete FBD Section (Completed) |
      
      
  @91115_3
  Scenario Outline: Generate FBDSection
    When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
    Then I Verify the facet generation status of all facets in Assignments Dock
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    
    @Generate_FBD_Section_2
    Examples:
      | containerinstance      | Message                          |
      | FBDSection_2$$Generate | Generate FBD Section (Completed) |
      
      
  @91115_4
  Scenario Outline: Verify Genlock and Delete block in FBDSection
    When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    Then I Verify FBD Section in Locked
    When I RClick on Instance Refine Offline project browser in project explorer as '<FBDSection>'
    And I selected Unlock in refine offline
    And I select '<button>' in New Device PopUp Window
    And I Delete instance in FBDRefine window as '<FBDSection>'
    When I selected Close Refine Offline in refine offline
    Then Verify Action message in notification pannel container dock in project explorer as '<Message1>'
    Then Verify build state of control executable PE project browser in project explorer as '<BuildState>'
    
    Examples:
      | containerinstance    | Message                             | Message1                             | FBDSection        | button | BuildState                                       |
      | FBDSection_2$$Refine | Open FBD Section Editor (Completed) | Close FBD Section Editor (Completed) | MotorGP_2_MotorGP | Yes    | ControlProject_1$$ControlExecutable_1$$OutOfDate |
      
      
  @91115_4
  Scenario Outline: Verify Inconsistoncy in FBDSection
    When I RClick control project browser project browser in project explorer as '<ProjectBrowser1>'
    And I Select context menu item EC project browser in project explorer as '<ProjectBrowser2>'
    And I click modal dialog window project browser in project explorer as '<ProjectBrowser3>'
    And I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    Then I Verify FBD Section in Locked
    When I selected Consistency Check in refine offline
    And I Consistency Check Select All Consistency Check in refine offline
    And I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as 'Unlink'
    Then Verify notification panel message Notification Pannel in message box as '<content>'
    When I selected Close Refine Offline in refine offline
    Then Verify Action message in notification pannel container dock in project explorer as '<Message1>'
    
    Examples:
      | ProjectBrowser1     | ProjectBrowser2    | ProjectBrowser3 | containerinstance    | Message                             | Message1                             | content                       |
      | ControlExecutable_1 | Generate and Build | OK              | FBDSection_2$$Refine | Open FBD Section Editor (Completed) | Close FBD Section Editor (Completed) | Check Consistency (Completed) |
      
      
  @91115_5
  Scenario Outline: Verify Consistancy in FBDSection
    When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    Then I Verify FBD Section in Locked
    When I selected Consistency Check in refine offline
    And I Click on Consistency Check Dialog window button in refine offline as '<Button>'
    Then Verify notification panel message Notification Pannel in message box as '<Message1>'
    When I selected Close Refine Offline in refine offline
    Then Verify Action message in notification pannel container dock in project explorer as '<Message2>'
    
  Examples:
    | containerinstance    | Message                             | Message1                      | Button | Message2                             |
    | FBDSection_2$$Refine | Open FBD Section Editor (Completed) | Check Consistency (Completed) | OK     | Close FBD Section Editor (Completed) |
    
    
  @91115_6
  Scenario Outline: Performing Unlink, Relink and Unassign in FBD Section
    When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
    Then Verify Action message in notification pannel container dock in project explorer as '<Message>'
    
    Examples:
      | facet_name        | action | Message                  |
      | MotorGP_1_MotorGP | Relink | Facet Relink (Completed) |
    