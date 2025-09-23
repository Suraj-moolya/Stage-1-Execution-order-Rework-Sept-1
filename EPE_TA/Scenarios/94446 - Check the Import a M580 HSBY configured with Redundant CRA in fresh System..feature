Feature: 94446 - Check the Import a M580 HSBY configured with Redundant CRA in fresh System.

@TC_EPE_HSBY_CRA_94446_001
Scenario Outline: Import Topology Devices
When I Right Click on nodes System Explorer Node in system explorer as '<System>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
#And I Click on Open button from Import TE window
And I click modal dialog window project browser in project explorer as '<Button2>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser8>'

@Import_Topology_System_7
Examples:
  | SlNo. | System   | sub_context_menu | context menu | Button2 | Import3  |  project browser8            |
  | 1     | System_7 | Topology         | Import       | OK      | Test.sbk |  Import Topology (Completed) | 