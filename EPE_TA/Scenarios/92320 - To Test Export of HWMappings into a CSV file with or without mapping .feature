Feature: 92320 - To Test Export of HWMappings into a CSV file with or without mapping 

  @TC_EPE_CP_HM_PGSQL_92320
  
  @92320_1
  Scenario Outline: Creating Multiple instances in Application Explorer
    # Note: This case is already covered in 90880.
    # We can reuse it via tag (Create_DigitalInput_10,Create_Digitaloutput_10,Create_AnalogInputGP_10,Create_Analogoutput_10) in Execution Order.
    
  @92320_2
  Scenario Outline: Navigate to Hardware Mapping Window
    When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
    And I Collapse control project browser PE project browser in project explorer
    And I Expand control project browser PE project browser in project explorer as '<project browser1>'
    And I Expand control project browser PE project browser in project explorer as '<project browser2>'
    And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
    And I Click '<tabname>' on service mapping edittor window
    
  @Navigate_to_HardwareMapping
  Examples:
    | MainToolBar1     | project browser1 | project browser2 | project browser3    | tabname          |
    | Project Explorer | M580_Standalone  | Executables      | ControlExecutable_1 | Hardware Mapping |
      
  @92320_2A
  Scenario Outline: Perform Export in Hardware Mapping Window
    When I click the '<action>' button in the Hardware Mapping window
    And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
    Then the exported CSV '<ExportFileName>' should have correct headers
    Then the exported CSV '<ExportFileName>' should list template names
  
  @Export_Before_Mapping
  Examples:
    | action | ExportFileName | ExportFileFormat |
    | Export | Ex1            | .csv             |
  
  @Export_After_Mapping
  Examples:
    | action | ExportFileName | ExportFileFormat |
    | Export | After_Mapping  | .csv             |
    
  @92320_3
  Scenario Outline: Perform Mapping Templates in Hardware Mapping Window
    When I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
    
  Examples:
    | appfacet                                                                                                                                 |
    | AnalogInputGP_10_AInputGP_AIS$$ATV6xxEGP_10_ATV$$AnalogOutputGP_10_AOGP_AOS$$DigitalInputGP_10_DInputGP_DIS$$DigitalOutputGP_10_DOGP_DOS |