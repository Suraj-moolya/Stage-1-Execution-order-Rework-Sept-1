Feature: 90827 To Test the export or import of application in Application explorer with PostGre SQL.

@TC_EPE_AE_PGSQL_90827_1
Scenario Outline: Export instances from Root Node, Folder level and Instance level in AE - Export as XML, verify XML file
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Export Window as '<File detail>'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify Extracted Template XML Data and Template Details Export in ec windows explorer '<File detail>'
Then I Expand '<Message>' and verify the notification message contents '<Scroll count>'

@Export_AE_RootNode_as_xml
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail  | Message            | Scroll count |
  | 1     | System               | Export               | System$$.xml | Export (Completed) | 6            |
  
@Export_AE_Folder_as_xml
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail  | Message            | Scroll count |
  | 1     | Folder_1             | Export               | Folder$$.xml | Export (Completed) | 5            |
  
@Export_AE_instance_as_xml
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail   | Message            | Scroll count |
  | 1     | MotorGP_1            | Export               | MotorGP$$.xml | Export (Completed) | 3            |
  
  
  
@TC_EPE_AE_PGSQL_90827_2
Scenario Outline: Export instances from Root Node, Folder level and Instance level in AE - Export as CSV, verify CSV file
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Export Window as '<File detail>'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify Extracted Template CSV Data and Template Details Export in ec windows explorer '<File detail>'

@Export_AE_RootNode_as_csv
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail  |
  | 1     | System               | Export               | System$$.csv |
  
@Export_AE_Folder_as_csv
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail  |
  | 1     | Folder_1             | Export               | Folder$$.csv |
  
@Export_AE_instance_as_csv
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail   |
  | 1     | MotorGP_1            | Export               | MotorGP$$.csv |
  

    
@TC_EPE_AE_PGSQL_90827_3A 
Scenario Outline: Application Browser pane - Apply Filter
When I select the required filter in AE application browser pane as '<Filter>'
And I select instances to be filtered from the listbox items '<Instance>'
And I select the filter combobox item as '<Comboitem>'
And I enter text to filter in the filter textbox as '<Text>'
And I click on filter button in the filter window
And I click on close button in the filter window
Then I verify the displayed instances in Application Browser

@Select_Identifier_Filter_in_Application_Browser
Examples:
  | SlNo. | Filter     | Instance             | Comboitem             | Text              |
  | 1     | Identifier | MotorGP_1$$ValveGP_1 | combobox1$$StartsWith | textbox1$$MotorGP |
  
@Select_Template_Filter_for_Process_Status_Verification
Examples:
  | SlNo. | Filter                       | Instance | Comboitem             | Text               |
  | 1     | ViewModel.TemplateIdentifier | $ValveGP | combobox1$$StartsWith | textbox1$$$ValveGP |
  
@Select_Link_Filter_for_Process_Status_Verification
Examples:
  | SlNo. | Filter              | Instance | Comboitem             | Text            |
  | 1     | ViewModel.LinkValid | Valid    | combobox1$$StartsWith | textbox1$$Valid |

  

@TC_EPE_AE_PGSQL_90827_3B
Scenario Outline: Application Browser pane - Clear Filter
When I select the required filter in AE application browser pane as '<Filter>'
And I click on clear filter in the filter window
And I click on close button in the filter window
Then I verify if the specific filter action in the AE application browser pane

@Clear_Identifier_Filter_in_Application_Browser
Examples:
  | SlNo. | Filter     |
  | 1     | Identifier |
  
@Clear_Template_Filter_in_Application_Browser
Examples:
  | SlNo. | Filter                       |
  | 1     | ViewModel.TemplateIdentifier |
  
@Clear_Link_Filter_in_Application_Browser
Examples:
  | SlNo. | Filter              |
  | 1     | ViewModel.LinkValid |
  
  

@TC_EPE_AE_PGSQL_90827_4 
Scenario Outline: Import - RightClick on the Root Node and select Import from the context menu
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Import Window as '<File detail>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

@Import_AE_instances_to_System
Examples:
  | SlNo. | Application browser1 | Application browser2 | File detail  |
  | 1     | System               | Import               | System$$.csv |


  
@TC_EPE_AE_PGSQL_90827_5
Scenario Outline: Import - Click on Create all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
And Verify the instances in Application Browser '<scroll count>'
Then Verify Message from notification panel AE Notification Pannel in message box

@Import_AE_instances_Create 
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 | scroll count |
  | 1     | Create All              | OK                      | 5            |
  
  
@TC_EPE_AE_PGSQL_90827_6
Scenario Outline: Import - Click on Update all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify Message from notification panel AE Notification Pannel in message box

@Import_AE_instances_Update 
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Update All              | OK                      |
  
@Import_AE_instances_Skip
Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Skip All                | OK                      |

 
  
@TC_EPE_AE_PGSQL_90827_7
Scenario Outline: Import - Edit the exported csv file, enter invalid template name and Import
When I modify the exported csv file '<File detail>' with invalid template name '<Invalid name>'
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Import Window as '<File detail>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Select button in the modal dialoge window as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

@Edit_exportedcsv_with_Invalid_template_name_and_Import
Examples: 
  | SlNo. | File detail  | Invalid name | Application browser1 | Application browser2 |
  | 1     | System$$.csv | abc          | System               | Import               |
  
  

@TC_EPE_AE_PGSQL_90827_8 
Scenario: Import - Click on Abort in Notification Panel
When I Click on Abort button in Notification Panel
Then Verify Message from notification panel AE Notification Pannel in message box
  

#################################################################################################################
#Execution order for TC_90827
##############################################################

#Tags - @Navigate_to_System1_AE
#Tags - @Templates_for_builds_before_6334
#Scenarios\ApplicationExplorer - Create 2 folders in Application browser
#Scenarios\ApplicationExplorer - Search Template in Template browser and Drag and drop from template browser to folder structure in application browser
#Tags - @Export_AE_RootNode_as_xml
#Scenarios\ApplicationExplorer - Expand Asset workspace
#Tags - @Export_AE_Folder_as_xml
#Tags - @Export_AE_instance_as_xml
#Tags - @Export_AE_Folder_as_csv
#Tags - @Export_AE_RootNode_as_csv
#Tags - @Select_Identifier_Filter_in_Application_Browser
#Tags - @Export_AE_instance_as_csv
#Tags - @Tags - @Clear_Identifier_Filter_in_Application_Browser
#Tags - @Import_AE_instances_to_System
#Tags - @Import_AE_instances_Skip
#Tags - @Import_AE_instances_to_System
#Tags - @Import_AE_instances_Update
#Tags - @Import_AE_instances_to_System
#Tags - @Import_AE_instances_Create
#Scenarios\EnginneringClient - Navigate to System Explorer ( SE )
#Scenarios\EnginneringClient - Creation of System - By Right clicking on System Explorer
#Tags - @Navigate_to_System2_AE
#Tags - @Edit_exportedcsv_with_Invalid_template_name_and_Import

####################################################################################################################

