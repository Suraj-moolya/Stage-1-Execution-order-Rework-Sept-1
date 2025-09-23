Feature: 91918 - Check for the Menu on CR root folder and User content  folder, User Created Folder and content properties and color icon for folder

@TC_EPE_CR_PGSQL_91918_01
Scenario Outline: Right click on CR root nodes in CR editor and verify the context menu
When I Right Click on nodes System Explorer Node in system explorer as '<node1>'
Then verify context menu items from Rclick menu items in system explorer

@Rclicks_on_Content_Repository_root_node_and_verifies_contextmenu_items
Examples:
  | SlNo. | node1              |
  | 1     | Content Repository |

  
@TC_EPE_CR_PGSQL_91918_02
Scenario Outline: Right click on User Contents node in CR editor and verify the context menu
When I DblClick on '<Identifier$$hierarchy1>' to expand nodes in CReditor screen
And I RClick on '<Identifier$$hierarchy2>' on nodes in CReditor screen
Then verify context menu items from Rclick menu items in system explorer

@Rclicks_on_User_Contents_node_and_verifies_contextmenu_items
Examples:
  | SlNo. | Identifier$$hierarchy1 | Identifier$$hierarchy2 | 
  | 1     | Global Root$$1         | User Contents$$2       |
   
  
@TC_EPE_CR_PGSQL_91918_03
Scenario Outline: Right click on Systems/User Contents node in CR editor and verify the context menu
When I DblClick on '<Identifier$$hierarchy3>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy10>' to expand nodes in CReditor screen
And I RClick on '<Identifier$$hierarchy4>' on nodes in CReditor screen
Then verify context menu items from Rclick menu items in system explorer

@Rclick_on_System_and_User_Contents_node_Verifies_context_menu
Examples:
  | SlNo. | Identifier$$hierarchy3 | Identifier$$hierarchy10 | Identifier$$hierarchy4 |
  | 1     | Root$$1                | System_1$$2             | User Contents$$3       |
  

@TC_EPE_CR_PGSQL_91918_04
Scenario Outline: Create folder inside user content for global and system both
When I RClick on '<Identifier$$hierarchy5>' on nodes in CReditor screen
And I Select context menu item EC in Topology Explorer as '<action1>'
And I enterkey Project Browser RO in refine offline
Then I verify the newly '<folder1>' created folder is editable or not
When I RClick on '<Identifier$$hierarchy6>' on nodes in CReditor screen
And I Select context menu item EC in Topology Explorer as '<action2>'
And I enterkey Project Browser RO in refine offline
Then I verify the newly '<folder2>' created folder is editable or not

@Creates_folder_under_user_contents_and_verify_created_folder_is_editable
Examples:
  | SlNo. | Identifier$$hierarchy5 | action1       | Identifier$$hierarchy6 | action2       | folder1     | folder2     |
  | 1     | User Contents$$2       | Create Folder | User Contents$$3       | Create Folder | Folder_1$$3 | Folder_1$$4 |
  

@TC_EPE_CR_PGSQL_91918_05
Scenario Outline: Rename folder and check the context menu of renamed folder 
When I press F2 to rename nodes in CR editor '<Identifier$$hierarchy7>'
And I Rename Folder as per requirement in system explorer as '<as per requirement1>' 
And I RClick on '<Identifier$$hierarchy8>' on nodes in CReditor screen
Then verify context menu items from Rclick menu items in system explorer

@Rename_folder_Content_repository_using_Keys_and_verify_contextmenu
Examples:
  | SlNo. | Identifier$$hierarchy7 | as per requirement1 | Identifier$$hierarchy8 |
  | 1     | Folder_1$$4            | Folder1             | Folder1$$4             |

  
@TC_EPE_CR_PGSQL_91918_06
Scenario Outline: Open proprties of a newly created folder
When I RClick on '<Identifier$$hierarchy9>' on nodes in CReditor screen
And I Select context menu item EC in Topology Explorer as '<action>'

@Open_properties_of_created_folder
Examples:
  | SlNo. | Identifier$$hierarchy9 | action     |
  | 1     | Folder1$$4             | Properties |

  
@TC_EPE_CR_PGSQL_91918_07
Scenario Outline: Update the properties of the folder in Content repository
When I update properties of folder in Content repository as '<Identifier,field,value>'
Then I verify the folder properties identifier is valid
Then Verify notification panel message Notification Pannel in message box as '<Message>'

@Update_folder_properties_Content_Repository
Examples:
  | SlNo. | Identifier,field,value | Message                   |
  | 1     | Folder1$$Identifier$$  | Update Folder (Completed) |