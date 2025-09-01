Feature: 91034 To Test the Status filter options in application explorer with various combinations

Scenario Outline: Search Template in Template browser and Drag and drop from template browser to application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'
@Templates_to_verify_progress_status
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | Analog             | AnalogOutputGP$$1.0.93 |
  | 2     | Analog             | AnalogOutputGP$$1.0.93 |
  | 3     | Analog             | AnalogInputGP$$1.0.138 |
  | 4     | MotorGP            | MotorGP$$1.0.123       |
  | 5     | ValveGP            | ValveGP$$1.0.100       |
  | 6     | ValveGP            | ValveGP$$1.0.100       |
  
  
Scenario Outline: Rename instance
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
Then verify the status of the instance

@Rename_instances_verify_progress_status 
Examples: 

  | SlNo. | Application browser4     | Application browser5 | Name1         |
  | 1     | ValveGP_2$$1.0.100       | Rename               | Valve@        |
  | 2     | AnalogOutputGP_2$$1.0.93 | Rename               | AnalogOutput@ |
  
  
Scenario Outline: Assign Instance to Containers in PE
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock

@Assign_Verify_Status_Instance_to_Containers_in_M580_Standalone
Examples:
  | SlNo. | controller      | section         | Button |
  | 1     | ValveGP_1       | M580_Standalone | OK     |
  | 2     | AnalogInputGP_1 | M580_Standalone | OK     |

  
Scenario Outline: Assign Instance to Containers in Supervision in PE
When I drag and Drop the Each instance to Each Sections as '<Instance>' '<section>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock

@Assign_Progress_Status_Instance_to_Containers_in_SP
Examples:
  | SlNo. | Instance        | Button | section          |
  | 1     | AnalogInputGP_1 | OK     | Supervision_Test |
  
  
Scenario Outline: Verify Progress Status in AE
Then Verify the progress status of the instances in Application Browser in AE '<instance>'

@Verify_Progress_Status_of_instances_in_App_Browser
Examples:
  | SlNo. | instance             |
  | 1     | AnalogInputGP_1$$100 |
  | 2     | AnalogOutputGP_1$$0  |
  | 3     | AnalogOutput@$$25    |
  | 4     | MotorGP_1$$0         |
  | 5     | ValveGP_1$$50        |
  | 6     | Valve@$$25           |
  

Scenario Outline: Click on Status Filter Arrow
When I click on the status filter arrow in Application browser
Then I verify the checkboxes available in the status filter of Application browser

@Click_on_Status_Filter_Arrow
Examples:
  | SlNo. |
  | 1     |


Scenario Outline: Select the Status Filter Checkbox
When I select the status filter in Application Browser as '<checkboxes>'
Then I verify the displayed instances in Application Browser

@Select_Needs_Attention_Status_Checkbox
Examples:
  | SlNo. | checkboxes         |
  | 1     | Needs Attention$$1 |
  
@Unselect_Needs_Attention_Status_Checkbox
Examples:
  | SlNo. | checkboxes         |
  | 1     | Needs Attention$$0 |
  
@Select_Link_Invalid_Status_Checkbox
Examples:
  | SlNo. | checkboxes      |
  | 1     | Link Invalid$$1 |
  
@Unselect_Link_Invalid_Status_Checkbox
Examples:
  | SlNo. | checkboxes      |
  | 1     | Link Invalid$$0 |
  
@Select_Data_Invalid_Status_Checkbox
Examples:
  | SlNo. | checkboxes      |
  | 1     | Data Invalid$$1 |
  
@Unselect_Data_Invalid_Status_Checkbox
Examples:
  | SlNo. | checkboxes      |
  | 1     | Data Invalid$$0 |
  
@Select_Progress_Status_Checkbox
Examples:
  | SlNo. | checkboxes  |
  | 1     | Progress$$1 |
  
@Unselect_Progress_Status_Checkbox
Examples:
  | SlNo. | checkboxes  |
  | 1     | Progress$$0 |

@Select_Link_Invalid_and_Data_Invalid_Status_Checkbox
Examples:
  | SlNo. | checkboxes                      |
  | 1     | Link Invalid$$1,Data Invalid$$1 |
  
@Select_Data_Invalid_and_Progress_Status_Checkbox
Examples:
  | SlNo. | checkboxes                  |
  | 1     | Data Invalid$$1,Progress$$1 |
  
@Select_Link_Invalid_and_Progress_Status_Checkbox
Examples:
  | SlNo. | checkboxes                  |
  | 1     | Link Invalid$$1,Progress$$1 |
  
@Select_Link_Invalid_Data_Invalid_and_Progress_Status_Checkbox
Examples:
  | SlNo. | checkboxes                                  |
  | 1     | Link Invalid$$1,Data Invalid$$1,Progress$$1 |
  
  
Scenario Outline: Select the Grid/Tree view in Application Browser
When I click on the Grid/Tree view icon in Application Browser
Then I verify the displayed instances in Application Browser

@Select_Grid_or_Tree_view_in_Application_Browser
Examples:
  | SlNo. |
  | 1     |
  
  


#################################################################################################################
#Execution order for TC_90827
##############################################################
#Tags - @Navigate_to_System1_AE
#Tags - @Templates_to_verify_progress_status
#Tags - @Rename_instances_verify_progress_status
#Scenarios\EnginneringClient - Navigation To Project Explorer(PE) - Main Tool Bar
#Tags - @Create_standalone_Control_Project_1
#Tags - @Double_Click_Containers
#Tags - @Assign_Verify_Status_Instance_to_Containers_in_M580_Standalone
#Scenarios\210 Navigate SP - Navigate SP
#Scenarios\210 Navigate SP - Create a Supervision Project
#Tags - @Double_Click_Containers
#Tags - @Assign_Progress_Status_Instance_to_Containers_in_SP
#Scenarios\EnginneringClient - Navigation To Application Explorer(AE) - Main Tool Bar
#Tags - @Verify_Progress_Status_of_instances_in_App_Browser
#Tags - @Click_on_Status_Filter_Arrow
#Tags - @Select_Needs_Attention_Status_Checkbox
#Tags - @Unselect_Needs_Attention_Status_Checkbox
#Tags - @Select_Link_Invalid_Status_Checkbox
#Tags - @Unselect_Link_Invalid_Status_Checkbox
#Tags - @Select_Data_Invalid_Status_Checkbox
#Tags - @Unselect_Data_Invalid_Status_Checkbox
#Tags - @Select_Progress_Status_Checkbox
#Tags - @Unselect_Progress_Status_Checkbox
#Tags - @Select_Link_Invalid_and_Data_Invalid_Status_Checkbox
#Tags - @Unselect_Needs_Attention_Status_Checkbox
#Tags - @Select_Data_Invalid_and_Progress_Status_Checkbox
#Tags - @Unselect_Needs_Attention_Status_Checkbox
#Tags - @Select_Link_Invalid_and_Progress_Status_Checkbox
#Tags - @Select_Data_Invalid_Status_Checkbox
#Tags - @Unselect_Needs_Attention_Status_Checkbox
#Tags - @Select_Template_Filter_for_Process_Status_Verification
#Tags - @Select_Data_Invalid_Status_Checkbox
#Tags - @Clear_Template_Filter_in_Application_Browser
#Tags - @Unselect_Data_Invalid_Status_Checkbox
#Tags - @Select_Link_Filter_for_Process_Status_Verification
#Tags - @Select_Link_Invalid_Status_Checkbox
#Tags - @Unselect_Needs_Attention_Status_Checkbox
#Tags - @Clear_Link_Filter_in_Application_Browser
#Tags - @Select_Grid_or_Tree_view_in_Application_Browser
#Tags - @Select_Link_Invalid_Status_Checkbox
#Tags - @Select_Grid_or_Tree_view_in_Application_Browser
#Tags - @Export_AE_RootNode_as_csv
#Scenarios\EnginneringClient - Navigate to System Explorer ( SE )
#Scenarios\EnginneringClient - Creation of System - By Right clicking on System Explorer
#Tags - @Navigate_to_System2_AE
#Tags - @Import_AE_instances_to_System
#Tags - @Click_on_Status_Filter_Arrow
#Tags - @Select_Link_Invalid_Status_Checkbox
#Tags - @close_Application_explorer
#Scenarios\EnginneringClient - Navigate to System Explorer ( SE )
#Tags - @Navigate_to_System2_AE


###########################################################################################################