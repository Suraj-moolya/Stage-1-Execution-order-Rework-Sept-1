Feature: 94676 - Check & Perform the Re-Deploy action for the controller having R-CRA.

@TC_EPE_HSBY_CRA_94676_001
Scenario Outline: Redeploy the project
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I Right Click on nodes System Explorer Node in system explorer as '<node_name>'
And I Select controller in context menu as '<option>'
And I click modal dialog window Modal dialog window in message box as '<button>'
And I Click popup button object project browser in project explorer as '<button1>'
Then Verify notification panel message Notification Pannel in message box as '<content>'

@Redeploy_project_from_Comtroller1
Examples:
  | SlNo. | MainToolBar       | node_name    | option                 | button1                                   | content                            |
  | 1     | Topology Explorer | Controller_1 | Re-Deploy Last Project | MessageBox$$modaldialogwindow1textbox$$OK | Re-Deploy Last Project (Completed) |