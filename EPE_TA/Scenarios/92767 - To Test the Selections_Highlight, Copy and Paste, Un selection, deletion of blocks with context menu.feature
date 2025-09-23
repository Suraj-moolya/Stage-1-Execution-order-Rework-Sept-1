Feature: 92767 - To Test the Selections_Highlight, Copy and Paste, Un selection, deletion of blocks with context menu

  @92767_1
  Scenario Outline: Verify Copy-Paste Functionality of Functions in Template Workspace
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplatesBrowser>'  
    And I Select context menu item EC global template core in global template explorer as '<ContextMenuItem>'
    And I selected toolbox in composite editor
    And I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<ToolBooxTable>'
    And I Right Click on function in GTE CompositeEdittor as '<func>'  
    And I Select context menu item EC global template core in global template explorer as '<ContextMenuItem1>'
    And I paste the function into the Composite Editor workspace
  
  @Add_function_in_toolbox_for_MotorGp  
  Examples:
    | MainToolBar      | TemplatesBrowser          | ContextMenuItem | ToolBooxTable | func    | ContextMenuItem1 |
    | Global Templates | Motorgp$$MotorGP$$1.0.123 | Edit            | Fan In        | FanIn_1 | Copy             |
    
  
  @92767_2
  Scenario Outline: Edit template and verify element block selection
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplatesBrowser>'  
    And I Select context menu item EC global template core in global template explorer as '<ContextMenuItem>'
    Then I Select '<identifier>' and verify it is selected
    Then I Unselect '<identifier>' to verify it is unselected
  
  @Verify_Instance_Selection_for_BoolVar
  Examples:
    | MainToolBar      | TemplatesBrowser            | ContextMenuItem | identifier |
    | Global Templates | BoolVar$$TSBoolVar16$$1.0.0 | Edit            | A          |
    
  
  @92767_3
  Scenario Outline: Edit template and verify block selection in document outline
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
    And I Search text and Right-Click GTE global template search in global template explorer as '<TemplatesBrowser>'  
    And I Select context menu item EC global template core in global template explorer as '<ContextMenuItem>'
    And I Select Document Outline in GTE Composite Edittor
    Then I Double click element on Document Outline and verify that element in Composite Edittor as '<Element>'
  
  @Verify_Element_Area_for_DInputGP
  Examples:
    | MainToolBar      | TemplatesBrowser                 | ContextMenuItem | Element |
    | Global Templates | DINPUTGP_UC$$DINPUTGP_UC$$1.0.43 | Edit            | Area    |