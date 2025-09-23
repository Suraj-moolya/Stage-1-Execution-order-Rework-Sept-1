Feature: 92768 - To Test the selection of different type of panes in Composite Editor & Facet Editor

  @92675_1
  Scenario Outline: Navigate to Global Templates and Selecting Template and Verify Different Types of Panes in Composite Editor - Edit 
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplateBrowser>'
    And I Select context menu item EC global template core in global template explorer as '<ContextMenu>'
    And I click on Element Rules if it is visible on screen
    And I click on Toolbox if it is visible on screen
    And I click on Browser if it is visible on screen
    And I click on Interface Rules if it is visible on screen
    And I click on Properties if it is visible on screen
    And I click on Document Outline if it is visible on screen
    And I click on Dependency Tree if it is visible on screen
    And I click on External Reference if it is visible on screen
    And I click on Used By if it is visible on screen
    And I click on Toolbox if it is visible on screen
    And I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<ToolBoxTable>'
    And I selected save as composite editor in composite editor
    And I approve the new template by setting status to Approved and description to Test
    And I click on 'Save' button in Instance Save As window
    And I Close tab items EC main screen in engineering client as 'Test'
    And I Close tab items EC main screen in engineering client as 'Global Templates'
    
  @Select_Template_DINPUTGP_UC_Edit
  Examples:
    | MainToolBar      | TemplateBrowser                  | ContextMenu | ToolBoxTable |
    | Global Templates | DINPUTGP_UC$$DINPUTGP_UC$$1.0.43 | Edit        | Fan In       |
    
  @92675_2
  Scenario Outline: Navigate to Global Templates and Selecting Template and Verify Different Types of Panes in Composite Editor - View 
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplateBrowser>'
    And I Select context menu item EC global template core in global template explorer as '<ContextMenu>'
    And I click on Interface Rules if it is visible on screen
    And I click on Properties if it is visible on screen
    And I click on Document Outline if it is visible on screen
    And I click on Dependency Tree if it is visible on screen
    And I click on External Reference if it is visible on screen
    And I click on Used By if it is visible on screen
    And I Close tab items EC main screen in engineering client as '<GTWindow>'
    And I Close tab items EC main screen in engineering client as '<GTWindow1>'
    
  @Select_Template_DINPUTGP_UC_View
  Examples:
    | MainToolBar      | TemplateBrowser                  | ContextMenu | GTWindow    | GTWindow1        |
    | Global Templates | DINPUTGP_UC$$DINPUTGP_UC$$1.0.43 | View        | DINPUTGP_UC | Global Templates |
    
  @Select_Template_DISignal_UL_View
  Examples:
    | MainToolBar      | TemplateBrowser                 | ContextMenu | GTWindow    | GTWindow1        |
    | Global Templates | DISignal_UL$$DISignal_UL$$6.3.7 | View        | DISignal_UL | Global Templates |
    
    
  @92675_2
  Scenario Outline: Navigate to Global Templates and Selecting Template and Verify Different Types of Panes in Facet Editor
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplateBrowser>'
    And I Select context menu item EC global template core in global template explorer as '<ContextMenu>'
    And I click on Toolbox if it is visible on screen
    And I click on Browser if it is visible on screen
    And I click on Interface Rules if it is visible on screen
    And I click on Properties if it is visible on screen
    And I click on Document Outline if it is visible on screen
    And I click on Dependency Tree if it is visible on screen
    And I click on Used By if it is visible on screen
    And I click on External Reference if it is visible on scree
    And I Close tab items EC main screen in engineering client as '<GTWindow>'
    And I Close tab items EC main screen in engineering client as '<GTWindow1>'
    
  @Select_Template_DISignal_UL_Edit
  Examples:
    | MainToolBar      | TemplateBrowser                 | ContextMenu | GTWindow    | GTWindow1        |
    | Global Templates | DISignal_UL$$DISignal_UL$$6.3.7 | Edit        | DISignal_UL | Global Templates |