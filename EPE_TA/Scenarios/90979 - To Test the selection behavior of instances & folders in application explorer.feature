Feature: 90979 - To Test the selection behavior of instances & folders in application explorer

@TC_EPE_AE_PGSQL_90979_1
Scenario Outline: Create and verify multiple folders under the root node in Application Browser
When I create multiple folders under the root node in the Application Browser with value '<folder_value>'

Examples:
    | SlNo | folder_value        |
    | 1    | System$$Folder$$5   |


@TC_EPE_AE_PGSQL_90979_2
Scenario Outline: Add and verify instances in different folders in Application Browser
Then I add and verify that instances are successfully added in different folders in the Application Browser with value '<instance_value>'

Examples:
    | SlNo | instance_value                                                                                  |
    | 1    | MotorGP$$1.0.123,ValveGP$$1.0.100,AnalogInputGP$$1.0.138,HandValveGP$$1.0.58,PIDGP$$1.0.153      |


@TC_EPE_AE_PGSQL_90979_3
Scenario Outline: Select multiple instances and folders, then verify the context menu in Application Browser
Then I select multiple items and verify the context menu in the Application Browser for '<template>'

Examples:
    | SlNo | template  |
    | 1    | ValveGP   |
    | 2    | Folder    |