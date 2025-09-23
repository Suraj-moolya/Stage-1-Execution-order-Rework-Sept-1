Feature: 90814 - To Test the UI & Functionality of parameter pane in Application explorer with PostGre SQL


Scenario Outline: Creating folder inside folder
When I rclick application browser folder AE Application browser in application explorer as '<ApplicationBrowserRoot>'
And I selected Create Folder in context menu

@create_folder
Examples:
    | SlNo | ApplicationBrowserRoot |
    | 1    | Folder_1                |

  

@TC_EPE_AE_PGSQL_90814
Scenario Outline: Modify the Folder name by giving Alias name
When I rclick application browser folder AE Application browser in application explorer as '<Templates browser2>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC Application browser in application explorer as '<Application browser5>'
Then I enter the value for the alias field of properties in Application Browser as '<Properties value>'
When I clicked Enter in keyboard shortcut
Then I verify the alias name is present for the folder in Application Broswer as '<Alias Name>'
When I Close instance editor tab Instance editor close in application explorer as '<Templates browser2>'

@Add_Verify_Alias_Name
Examples:
  | SlNo. | Templates browser2     | Application browser5 | Properties value | Alias Name |
  | 1     | Folder_1                 | Properties           | Alias$$Sample    | Sample     |
  
  

@TC_EPE_AE_PGSQL_90814_1
Scenario Outline: Modify the Instance properties - Close ( X ) and Yes in Popup
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'
When I click on Yes button in Message Box
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'

@save_the_updates_details
Examples:
  | SlNo. | Instance editor close8 | Save changes dialogbox9    |
  | 1     | Folder_1               | Folder_1: Save Changes(s)  |


@TC_EPE_AE_PGSQL_90814_2
Scenario Outline: Verify the Insatnce value after adding alias name
Then Verify the template is present in Application browser as '<Templates browser>'

@verify_instance_value_with_alias_name
Examples:
  | SlNo. | Templates browser |
  | 1     | SampleMotorGP_1   |
  
@verify_insatnce_value_without_alias_name
Examples:
  | SlNo. | Templates browser |
  | 1     | MotorGP_1   |
  
@TC_EPE_AE_PGSQL_90814_3
Scenario Outline: Check or Uncheck the Instance Editor checkbox
When I double click on template Identifier ValveGP_1 in application browser as '<Templates browser>'
Then I check the checkbox of the instance editor window in Application Broswer as '<Checkbox Value>'


@uncheck_hierarchical_value
Examples:
  | SlNo. | Templates browser | Checkbox Value|
  | 1     | SampleMotorGP_1   | Hierarchical Name |
  

Scenario Outline: Drag and drop instance from one folder to another
Then I drag and drown the template from one folder to another in Application Broswer as '<Templates browser>'

@drag_drop_instance_to_below_folder
Examples:
  | SlNo. | Templates browser |
  | 1     | MotorGP_1$$Folder_2$$Down   | 

@drag_drop_instance_to_above_folder
Examples:
  | SlNo. | Templates browser |
  | 1     | MotorGP_1$$Folder_1$$Up   | 
  
@drag_drop_folder_inside_folder
Examples:
  | SlNo. | Templates browser           |
  | 1     | Folder_1$$Folder_2$$Down    |

@drag_instance_to_folder3
Examples:
  | SlNo. | Templates browser           |
  | 1     | MotorGP_1$$Folder_3$$Down   |

@drag_instance_to_folder2
Examples:
  | SlNo. | Templates browser           |
  | 1     | MotorGP_1$$Folder_2$$Up     |
    
  
Scenario Outline: Update the parameter description in the instance editor and save it
When I double click on template Identifier ValveGP_1 in application browser as '<Templates browser>'
Then I select a particular sub template value in Application Broswer of Instance Editor as '<Sub Template Value>'
Then I add the value for the paramters description in Application Broswer of Instance Editor as '<Paramter Value>'

@updating_parameter_desc_value
Examples:
  | SlNo. | Templates browser           |Sub Template Value|Paramter Value           |
  | 1     | MotorGP_1                   |Motor$$Logic      |Failure$$Timeout$$15     |  
  
  

#execution order
#@DragDrop_Instance_MotorGP_To_Folder_1_Times
#@TC_EPE_AE_00
#@Add_Alias_Name
#@save_the_updates_details
#@verify_instance_value_with_alias_name
#@drag_drop_below_folder
#@verify_insatnce_value_without_alias_name
#@drag_drop_above_folder
#@verify_instance_value_with_alias_name
#@uncheck_hierarchical_value
#@TC_EPE_AE_0012
#@verify_insatnce_value_without_alias_name




