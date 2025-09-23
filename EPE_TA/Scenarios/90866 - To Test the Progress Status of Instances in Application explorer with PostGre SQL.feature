Feature: 90866 To Test the Progress Status of Instances in Application explorer with PostGre SQL.

Scenario Outline: Create 2 folders in Application browser
When I rclick application browser folder AE Application browser in application explorer as '<Application browser54>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu2>'
Examples:
  | SlNo. | Application browser54 | ContextMenu2 |
  | 1     | Folder_1              | Properties   |
 
   
Scenario Outline: Modify the properties of Instances - Close Instance
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

Examples:
  | SlNo. | Instance editor close1 |
  | 1     | Folder_1               |
  

Scenario Outline: Verify Progress Status in AE
Then Verify the progress status of the instances in Application Browser in AE '<instance>'

@verify_MotorGP_instance_for_Progress_Status_0
Examples:
  | SlNo. | instance     |
  | 1     | MotorGP_1$$0 |

@verify_MotorGP_instance_for_Progress_Status_25
Examples:
  | SlNo. | instance      |
  | 1     | MotorGP_1$$25 |

@verify_MotorGP_instance_for_Progress_Status_50
Examples:
  | SlNo. | instance      |
  | 1     | MotorGP_1$$50 |

@verify_MotorGP_instance_for_Progress_Status_100  
Examples:
  | SlNo. | instance       |
  | 1     | MotorGP_1$$100 |
  

Scenario Outline: Trying to Unassign Before Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify '<facet_name>' disappered in assignments
Examples:
  | SlNo. | facet_name        | action   |
  | 1     | ValveGP_1_ValveGP | Unassign |
  
Scenario Outline: Trying to Unassign Multiple Facets Before Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify '<facet_name>' disappered in assignments
@unassign
Examples:
  | SlNo. | facet_name                                                             | action   |
  | 1     | MotorGP_1_MotorGP$$MotorGP_1_CondsumGP$$MotorGP_1_$$MotorGP_1_ILockOn1 | Unassign |