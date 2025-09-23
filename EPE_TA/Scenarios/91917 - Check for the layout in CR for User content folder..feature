Feature: 91917 - Check for the layout in CR for User content folder.

@TC_EPE_CR_PGSQL_91917_01
Scenario Outline: Open content repository editor and verify the layout 
When I navigate to explorers MainToolBar in system explorer as 'Open Content Repository'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab1>'

@open_content_repository_and_verify
Examples: 
  | SlNo. | Explorer tab1      |
  | 1     | Content Repository |

  
@TC_EPE_CR_PGSQL_91917_02  
Scenario Outline: Check the path of nodes in CR editor screen 
When I DblClick on '<Identifier$$hierarchy1>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy2>' to expand nodes in CReditor screen
Then I verify the nodes available in CR editor screen

@expands_GlobalRoot_and_GlobalTemplates_and_verifies_path
Examples: 
  | SlNo. | Identifier$$hierarchy1 | Identifier$$hierarchy2 |
  | 1     | Global Root$$1         | Global Templates$$2    |
  
@expands_GlobalRoot_UserContents_and_GlobalTemplates_and_verifies_path
Examples: 
  | SlNo. | Identifier$$hierarchy1 | Identifier$$hierarchy2 |
  | 1     | User Contents$$2       | Global Templates$$3    |

@expands_Systems_and_verifies_path
Examples: 
  | SlNo. | Identifier$$hierarchy1 |
  | 1     | Systems$$1             |

  
@TC_EPE_CR_PGSQL_91917_03  
Scenario Outline: Verify GPL and FDL Contents are available after first Start of the Server(fresh DB)
When I DblClick on '<Identifier$$hierarchy4>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy5>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy6>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy7>' to expand nodes in CReditor screen
And I DblClick on '<Identifier$$hierarchy8>' to expand nodes in CReditor screen
Then I verify the nodes available in CR editor screen

@verify_GPL_and_FDL_library_after_fresh_DB
Examples: 
  | SlNo. | Identifier$$hierarchy4 | Identifier$$hierarchy5 | Identifier$$hierarchy6 | Identifier$$hierarchy7     | Identifier$$hierarchy8 |
  | 1     | Global Root$$1         | User Contents$$2       | Global Templates$$3    | General Purpose Library$$4 | Foundation Library$$4  |

