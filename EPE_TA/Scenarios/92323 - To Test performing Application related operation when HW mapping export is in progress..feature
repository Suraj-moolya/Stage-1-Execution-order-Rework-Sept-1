Feature: 92323 - To Test performing Application related operation when HW mapping export is in progress.

  @92323_1
  Scenario Outline: Change the Description Of Instance
  When I rclick application browser template AE Application browser in application explorer as '<TemplatesBrowser>'
  And I Select context menu item EC Application browser in application explorer as '<ContextItem>' 
  And I Enter description AE Instance description in application explorer
  And I selected Instance editor save in application explorer
  And I Click on buttons as '<button>'
  And I Close instance editor tab Instance editor close in application explorer as '<InstanceEdittor>'
  
  @Changing_Desc_for_DigitalInput_1.0.81  
  Examples:
    | TemplatesBrowser         | ContextItem | InstanceEdittor  | button |
    | DigitalInputGP_1$$1.0.81 | Properties  | DigitalInputGP_1 | Yes    |
    
  @Changing_Desc_for_DigitalInput_1.0.83  
  Examples:
    | TemplatesBrowser         | ContextItem | InstanceEdittor  | button |
    | DigitalInputGP_1$$1.0.83 | Properties  | DigitalInputGP_1 | Yes    |
    
    
  @92323_1A
  Scenario Outline: Verify Facet Assignment Status
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Dclick Control project broswer project browser in project explorer as '<projectBrowser>'
    Then I verify the section is generated successfully as '<Facet_Name>' '<Facet_State>'
  
  @Verify_Status_for_DigitalInput 
  Examples:
    | MainToolBar      | Facet_Name                | projectBrowser | Facet_State |
    | Project Explorer | DigitalInputGP_1_DInputGP | Containers     | OutOfDate   |
    
  @92323_2
  Scenario Outline: creating new version of DI input
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and select GTE global template search in global template explorer as '<Instance>'
    And I right click on the instance '<Identifier>' in device control window
    And I Select context menu item EC global template core in global template explorer as '<ContextMenu>'
    And I selected save as composite editor in composite editor
    And I click on '<btn>' in the Save As window
    And I change the template name to '<name>' and version to '<version>' in the Save As window
    And I enter the description in the Save As window as '<desc>'
    And I Click on old State Selector in global template explorer
    And I Click on Approved combo item in global template explorer
    And I Click on State Selector in global template explorer
    And I Click on Approved combo item in global template explorer
    And I selected Save in save as windowo
    And I Close tab items EC main screen in engineering client as '<name>'
    And I Close tab items EC main screen in engineering client as '<MainToolBar>'
    
  @Creating_New_Template_in_GTE_DigitanInput 
  Examples:
    | MainToolBar      | Instance                               | Identifier              | ContextMenu | btn   | name           | version | desc               |
    | Global Templates | DigitalInputGP$$DigitalInputGP$$1.0.81 | $DigitalInputGP$$1.0.81 | Edit        | Other | DigitalInputGP | 1.0.83  | Sample Description |