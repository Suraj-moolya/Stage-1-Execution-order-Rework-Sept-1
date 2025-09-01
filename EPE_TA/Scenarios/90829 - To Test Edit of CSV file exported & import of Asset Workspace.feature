Feature: 90829 To Test Edit of CSV file exported & import of Asset Workspace in Application explorer with PostGre SQL.

  
@TC_EPE_AE_PGSQL_90829_1
Scenario Outline: Import - Edit the exported csv file, enter invalid template name and Import
When I modify the exported csv file '<File detail>' by deleting instance and link '<Modification>'
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter File Name and File Location in Import Window as '<File detail>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

@Edit_exportedcsv_with_Invalid_template_name_and_Import
Examples: 
  | SlNo. | File detail         | Modification                   | Asset workspace4 | Application browser2 |
  | 1     | AssetRootNode$$.csv | AnalogInputGP$$AnalogInputGP_1 | System           | Import               |