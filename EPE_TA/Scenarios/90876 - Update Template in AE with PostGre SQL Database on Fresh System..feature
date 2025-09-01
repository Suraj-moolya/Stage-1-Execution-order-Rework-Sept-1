Feature: 90876 - Update Template in AE with PostGre SQL Database on Fresh System.


@TC_EPE_AE_PGSQL_90876
Scenario Outline: Update latest version instance in application browser
When I rclick application browser template AE Application browser in application explorer as '<template>'
And I Select context menu item EC Application browser in application explorer as '<Menu Item>'
Then Verify Modal Dialog Window Text in message box as '<Message>'
When I click modal dialog window Modal dialog window in message box as '<Button>'

@Update_latest_version_GenericDeviceGP$$1.0.5_verify_popup_OK
Examples:
  | SlNo. | template               | Menu Item       | Button | Message                                      |
  | 1     | GenericDeviceGP$$1.0.5 | Update Template | OK     | Unable to find a template of a later version |

