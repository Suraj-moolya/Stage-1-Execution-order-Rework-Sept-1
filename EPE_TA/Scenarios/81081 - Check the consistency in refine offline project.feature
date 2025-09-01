Feature:  81081 - Check the consistency in refine offline project


# Pre-Requisites:
# 1. Facets to be unlocked and unlinked in the FBD section of Refine Offline section before execution ( Modifications in refine Window )
@TC_EPE_CP_PGSQL_81081_1
Scenario Outline: Save, Check Consistency, Unlink Inconsistent facets and close refine
When I selected Save Refine Offline in refine offline
And I selected Consistency Check in refine offline
And I Consistency Check Select All Consistency Check in refine offline
And I Click on Consistency Check Dialog window button in refine offline as '<Button>'  
Then Verify notification panel message Notification Pannel in message box as '<Message>'
When I selected Close Refine Offline in refine offline
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | Message                       | Button |
  | 1     | Check Consistency (Completed) | Unlink |

  
@TC_EPE_CP_PGSQL_81081_2
@test002
Scenario Outline: Check Consistency of Project and close refine
When I selected Save Refine Offline in refine offline
And I selected Consistency Check in refine offline
And I Click on Consistency Check Dialog window button in refine offline as '<Button>'
Then Verify notification panel message Notification Pannel in message box as '<Message>'
When I selected Close Refine Offline in refine offline
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | Message                       | Button |
  | 1     | Check Consistency (Completed) | OK     |
