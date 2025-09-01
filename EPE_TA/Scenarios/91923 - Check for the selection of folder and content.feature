Feature: 91923 - Check for the selection of folder and content


#Pre-Requisites:
#1.Open Content Repository and Expand Systems/System_1.


@TC_EPE_CR_PGSQL_91923_1
@test001
Scenario Outline: Open Content Repository in Engineering Client
When I selected Open System Explorer in engineering client

Examples:
  | SlNo. | 
  | 1     |
  
  
@TC_EPE_CR_PGSQL_91923_2
@test002  
Scenario Outline: Expand Content Repository node in Content Repository
When I Expand content repository explorer node in content repository as '<Node Name>'
And I Expand content repository explorer node in content repository as '<Node Name 1>'
And I Expand content repository explorer node in content repository as '<Node Name 2>'
And I Expand content repository explorer node in content repository as '<Node Name 3>'

@Expand_Systems_user_content_Content_Repository
Examples:
  | SlNo. | Node Name          | Node Name 1 | Node Name 2 | Node Name 3   | Context Menu 2 | Context Menu |
  | 1     | Content Repository | Systems     | System_1    | User Contents | Create Folder  | Expand       |

@Expand_global_user_content_Content_Repository
Examples:
  | SlNo. | Node Name          | Node Name 1 | Node Name 2     | Node Name 3   | Context Menu 2 | Context Menu |
  | 1     | Content Repository | Global Root | Global Template | User Contents | Create Folder  | Expand       |
  

        
@TC_EPE_CR_PGSQL_91923_3
@test003   
Scenario Outline: Creating Multiple Folder in Content Repository
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<item>'
And I Select multiple folder to check it Select items as '<folders>'

@Create_folder_in_Content_Repository_under_systems_user_content_1_folder
Examples:
  | SlNo. | item          | node          | folders                                          |
  | 1     | Create Folder | User Contents | Folder_1$$Folder_2$$Folder_3$$Folder_4$$Folder_5 |

@Create_folder_in_Content_Repository_under_systems_user_content_6_folder
Examples:
  | SlNo. | item          | node          |
  | 1     | Create Folder | User Contents |
  | 1     | Create Folder | User Contents |
  | 1     | Create Folder | User Contents |
  | 1     | Create Folder | User Contents |
  | 1     | Create Folder | User Contents |
  | 1     | Create Folder | User Contents |
  

    
@TC_EPE_CR_PGSQL_91923_4
@test004
Scenario Outline: Verify Selected Folders in Content Repository
Then Verify multiple folders should be selecting and unselecting as '<folders>'

@Verify_folder_in_Content_Repository_under_systems_user_content_1_folder_in_cr
Examples:
  | SlNo. | item          | node          | folders                                          |
  | 1     | Create Folder | User Contents | Folder_1$$Folder_2$$Folder_3$$Folder_4$$Folder_5 |
  

    
@TC_EPE_CR_PGSQL_91923_5
@test005
Scenario Outline: Right click on folders and create content file in CR
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<item>'
And I Enter Item in Textbox Property Window as '<item_1>'

@create_content_file_under_folder1_CR
Examples:
  | SlNo. | item           | node     |item_1|
  | 1     | Create Content | Folder_1 |Sample|

  
    
@TC_EPE_CR_PGSQL_91923_6
@test006  
Scenario Outline: Export Content Repository from root folder 
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select button in the modal dialoge window as '<button name>'
When I Enter File Name and File Location in Export Window as '<format>'
And I Click on Button in TE Explorer Window Export in ec windows explorer as 'Save'
Then Verify notification panel message Notification Pannel in message box as '<Notification Panne>'

@Export_Content_Repository
Examples:
  | SlNo. | Controllers        | context menu         | Notification Panne               | button name | format |
  | 1     | Content Repository | Export User Contents | Export User Contents (Completed) | OK          | .cbk   |

  
    
@TC_EPE_CR_PGSQL_91923_7
@test007
Scenario Outline: Delete the folder create in User Content in CR
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window Instance editor save in application explorer as '<button name>'

@delete_folder1_under_user_content_cr
Examples:
  | SlNo. | Controllers | context menu | button name |
  | 1     | Folder_1    | Delete       | Yes         |

  
    
@TC_EPE_CR_PGSQL_91923_8
@test008  
Scenario Outline: Import the exported content repository file
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>' 
And I Enter FileLocation and FileName to be Import as '<Import1>'
And I Select button in the modal dialoge window as '<button name>'
Then Verify Message from notification panel AE Notification Pannel in message box 

@import_the_exported_file_in_cr
Examples: 
  | SlNo. | Controllers        | context menu         | Import1    | button name |
  | 1     | Content Repository | Import User Contents | Sample.cbk | OK          |
  
  