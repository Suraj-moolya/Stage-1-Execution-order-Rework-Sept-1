Feature: 91036 To Test the Validity Indicator at Instance & Folder levels
   
Scenario Outline: Search Template in Template browser and Drag and drop from template browser to application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag and drop template from Templates browser to hierarchy folder in Application browser as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'
@Templates_for_Validity_Indicator
Examples:
  | SlNo. | Templates browser1 | Templates browser2        |
  | 1     | Analog             | AnalogInputGP$$1.0.138$$7 |
  | 2     | MotorGP            | MotorGP$$1.0.123$$7       |
  | 3     | ValveGP            | ValveGP$$1.0.100$$7       |
  | 4     | HandValveGP        | HandValveGP$$1.0.58$$7    |
  | 5     | PIDGP              | PIDGP$$1.0.153$$7         |
  
@AnalogOutputGP_Template_for_Validity_Indicator
Examples:
  | SlNo. | Templates browser1 | Templates browser2        |
  | 1     | Analog             | AnalogOutputGP$$1.0.93$$7 |
  
  
Scenario Outline: Right Click on the Instance and click on Edit Links from Apllication explorer
When I rclick application browser template AE Application browser in application explorer as '<facet_name>'
And I Select context menu item as '<action>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>'
  
Examples:
  | SlNo. | facet_name             | action     | Assert Workspace Editor10 |
  | 1     | AnalogInputGP$$1.0.138 | Edit Links | AnalogInputGP_1           |
  
@Opening_Link_Editor_90822
Examples:
  | SlNo. | facet_name             | action     | Assert Workspace Editor10 |
  | 1     | AnalogInputGP$$1.0.138 | Edit Links | AnalogInputGP_1           |
  
  
Scenario Outline: Drag and Drop Template from Application Browser to Link Editor wrt Position
When I drag template in application browser Link Editor as '<Assert Workspace Editor8>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'

@drag_drop_link_editor
Examples:
  | SlNo. | Assert Workspace Editor8 | Assert Workspace Editor9 |
  | 1     | PIDGP_1$$1               | PIDGP_1                  |
  
  
Scenario Outline: Link between facet nodes of respective instances AnalogInputGP and PIDGP 
When I Link from range node to range node AE Node Instance in application explorer as 'PVRanged$$PVRanged'
Then Verify Link Status Node Instance in application explorer

Examples:
  | SlNo. |
  | 1     |

Scenario Outline: Verify the Validity Status of the intances in AE
Then I verify the validity status of the instances in application browser

Examples:
  | SlNo. |
  | 1     |
  
Scenario Outline: Delete instance - from context Menu
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template1>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu2>'
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template3>'
When I Click on buttons in popup window Delete popup in message box as 'Yes'
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
@Delete_instance_MotorGP_from_context_Menu
Examples:
  | SlNo. | MotorGP template1      | ContextMenu2 | container dock3                               |
  | 1     | AnalogOutputGP$$1.0.93 | Delete       | Are you sure you want to delete this Instance |
  
  
Scenario Outline: Rename instance
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
Then verify the status of the instance

@Rename_invalid_for_validity_status_verification_in_AE 
Examples: 
  | SlNo. | Application browser4 | Application browser5 | Name1                |
  | 1     | MotorGP$$1.0.123     | Rename               | Motor123456789012345 |

@Rename_valid_for_validity_status_verification_in_AE   
Examples: 
  | SlNo. | Application browser4          | Application browser5 | Name1     |
  | 1     | Motor123456789012345$$1.0.123 | Rename               | MotorGP_1 |
  
  
Scenario Outline: Drag and Drop instance from one folder to another in AE
When I Drag and Drop instance from one folder to another in Application Browser as '<source_target>' 
@Drag_and_drop_instance_from_folder_to_folder_for_Validity_Status_verification_in_AE
Examples: 
  | SlNo. | source_target                  |
  | 1     | Motor123456789012345$$Folder_3 |
  
  
Scenario Outline: Replace template - Select template to replace template from Application browser 
When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
Then verify window open as '<Window>'
When I select the template to replace in replace template as '<Replace_Template>'
And I take evidence Instance Editor in application explorer
@Replace_template_for_Validity_Status_verification
Examples:
  | SlNo. | Application browser    | Application browser1 | Window           | Replace_Template       |
  | 1     | AnalogOutputGP$$1.0.93 | Replace Template     | Replace Template | AnalogInputGP$$1.0.138 |


Scenario Outline: Replace template - Click on OK in replace template window
When I Select button in the modal dialoge window as '<Button name>'
Then verify template and version in application browser as '<Template>'
@Replace_template_click_OK_for_Validity_Status_verification
Examples:
  | SlNo. | Button name | Template               |
  | 1     | OK          | AnalogInputGP$$1.0.138 |

  
Scenario Outline: Copy and paste the Instance - copy instance from context menu and paste
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template5>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as 'Copy'
And I rclick application browser folder AE Folder_2 in application explorer as '<Folder_26>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu7>'
Then Verify template created Application browser template in application explorer as '<Application browser template8>'
@Copy_Paste_Instance_to_Folder_for_Validity_Status_verification
Examples:
  | SlNo. | MotorGP template5      | Folder_26 | ContextMenu7 | Application browser template8 |
  | 1     | AnalogOutputGP$$1.0.93 | Folder_2  | Paste        | AnalogOutputGP_2_1            |
  


  
  