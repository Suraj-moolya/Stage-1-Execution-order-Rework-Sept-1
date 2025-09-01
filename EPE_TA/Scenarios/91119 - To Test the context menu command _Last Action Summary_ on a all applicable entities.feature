Feature: 91119 - To Test the context menu command Last Action Summary on a all applicable entities

@TC_EPE_CP_PGSQL_91119

@91119_1
Scenario Outline: Create Control Project and Assign Facet with Instance Properties Panel Open in Application Explorer
  When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
  And I RClick control project browser project browser in project explorer as '<ProjectBrowser1>'
  And I Select context menu item EC project browser in project explorer as '<ContextMenu>'
  And I Select controller in context menu as '<Controller>'
  And I rename the ControlProject as '<ControllerName>'

  @sdf
  Examples:
    | MainToolBar1     | ProjectBrowser1 | ContextMenu            | Controller | ControllerName  |
    | Project Explorer | System_1        | Create Control Project | M580       | M580_Standalone |
