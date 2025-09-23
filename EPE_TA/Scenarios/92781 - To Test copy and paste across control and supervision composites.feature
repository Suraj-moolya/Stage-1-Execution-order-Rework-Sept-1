Feature: 92781 - To Test copy and paste across control and supervision composites

#Pre-Requisites:
#1.Start System server of EPE-2025 
#2.Open Engineering client once System server is ready with out any issue
#3.Open Global Templates Explorer

Scenario Outline: Search the template and edit in Global Templates Explorer
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on fit to content button in global template explorer


Examples:
  | SlNo. | Templates browser                     | menu item |
  | 1     | Analoginput$$AnalogInputGP_CG$$1.0.14 | Edit      |
  
Examples:
  | SlNo. | Templates browser           | menu item |
  | 1     | Ainput$$AInputGP_UC$$1.0.46 | Edit      |