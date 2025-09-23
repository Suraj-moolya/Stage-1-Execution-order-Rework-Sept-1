Feature: 95249 - Verify the creation and configuration of Modbus TCP Using Explicit Communication

  @TC_EPE_TE_PGSQL_95249
  
  @95249_1
  Scenario Outline: Create Device in Topology Explorer
    When I Right Click on nodes System Explorer Node in system explorer as '<node>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I Select controller in context menu as '<controller>'

  @create_device
  Examples:
    | node    | context menu     | controller |
    | Devices | Create Device-IO | Modbus TCP |
  
  @95249_2
  Scenario Outline: Select Device in Topology Explorer
    When I search template browser EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
    And I Select template EC Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
    And I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
  
  @Device_ATV6xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | button         |
    | ATV6xxHW                | ATV6xxHW$$1.0.10        | Devices$$Close |
  
  @EPM53xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | button         |
    | EPM53xxHW               | EPM53xxHW$$1.0.6        | Devices$$Close |
  
  @Create_Device_ATV61HW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | button         |
    | ATV61HW                 | EATV61HW$$2.2.6         | Devices$$Close |
  
  @Create_Device_ATV71HW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | button         |
    | ATV71HW                 | EATV71HW$$2.2.8         | Devices$$Close |
  
  @95249_3
  Scenario Outline: Perform the Ip configuration, subnet mask in Topology Explorer
    When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
    And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
    And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
    And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
    When I Close the Tab by Clicking on Close as '<identifier>'
  
  @ip_for_ATV6xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3  | Topology Explorer Tree4 | identifier |
    | EATV6xxHW_1             | Communication           | IPAddress$$182.233.64.81 | SubnetMask$$255.255.0.0 | EATV6xxHW  |
  
  @ip_for_PM53xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3  | Topology Explorer Tree4 | identifier |
    | EPM53xxHW_1             | Communication           | IPAddress$$182.233.64.77 | SubnetMask$$255.255.0.0 | EPM53xxHW  |
  
  @ip_for_ATV61
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3  | Topology Explorer Tree4 | identifier |
    | EATV61HW_1              | Communication           | IPAddress$$182.233.64.71 | SubnetMask$$255.255.0.0 | ATV61HW    |
  
  @ip_for_ATV71
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3  | Topology Explorer Tree4 | identifier |
    | EATV71HW_1              | Communication           | IPAddress$$182.233.64.72 | SubnetMask$$255.255.0.0 | ATV71HW    |
  
  @95249_4
  Scenario Outline: select physical connection and map the device to Ethernet network in Topology Explorer
    When I RClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
    And I Click on MenuItem in TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
    And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
    And I click modal dialog window project browser in project explorer as '<Button>'
  
  @Ethernet_for_ATV6xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
    | EATV6xxHW               | Physical Connections    | EATV6xxHW$$SE_Network   | OK     |
  
  @Ethernet_for_PM53xxHW
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
    | EPM53xxHW               | Physical Connections    | EPM53xxHW$$SE_Network   | OK     |
  
  @Ethernet_for_ATV61
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
    | ATV61HW                 | Physical Connections    | ATV61HW$$SE_Network     | OK     |
  
  @Ethernet_for_ATV71
  Examples:
    | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
    | ATV71HW                 | Physical Connections    | ATV71HW$$SE_Network     | OK     |
  
  @95249_4
  Scenario Outline: Create PM53xx, EMPort and ETV6xx instance in AE
    When I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
    And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<TemplatesBrowser2>'
    Then Verify the template is present in Application browser as '<TemplatesBrowser1>'
  
  @drag_drop_ATV6xx
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2           |
    | ATV6xxEGP         | ATV6xxEGP$$1.0.43$$Folder_1 |
  
  @drag_drop_PM53xx
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2          |
    | PM53xxEM          | PM53xxEM$$1.1.11$$Folder_1 |
    
  @drag_drop_EMPortM
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2         |
    | EMPortM           | EMPortM$$1.3.12$$Folder_1 |
  
  @95249_4
  Scenario Outline: Link Instance in AE
    When I rclick asset workspace folder AE Asset workspace in application explorer as '<AssetWorkspace2>'
    And I Select context menu item EC Asset workspace in application explorer as '<AssetWorkspace3>'
    And I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<AssertWorkspaceEditor>'
    And I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<AssertWorkspaceEditor2>'
    And I Click on fit to content button in Application Explorer
    And I link property '<from_property>' of instance '<AssertWorkspaceEditor>' to property '<to_property>' of instance '<AssertWorkspaceEditor2>' in application explorer
  
  @Link_instance_PM53xxEM_EMPortM
  Examples:
    | AssetWorkspace2 | AssetWorkspace3 | AssertWorkspaceEditor | AssertWorkspaceEditor2 | to_property   | from_property   |
    | AssetWorkspace  | Edit Workspace  | EMPortM_1             | PM53xxEM_1             | Ethernet Port | Ethernet Client |
    
  @Link_instance_ATV61_MotorVSGP
  Examples:
    | AssetWorkspace2  | AssetWorkspace3 | AssertWorkspaceEditor | AssertWorkspaceEditor2 | to_property | from_property |
    | AssetWorkspace_2 | Edit Workspace  | ATV61AS_1             | MotorVSGP_1            | DevVS       | DevVarSpeed   |
    
  @Link_instance_ATV71_MotorVSGP
  Examples:
    | AssetWorkspace2  | AssetWorkspace3 | AssertWorkspaceEditor | AssertWorkspaceEditor2 | to_property | from_property |
    | AssetWorkspace_2 | Edit Workspace  | ATV71AS_1             | MotorVSGP_2            | DevVS       | DevVarSpeed   |
    
    
  @95249_4A
  Scenario Outline: Right Click Control Executables and Generate and build with Update all
    When I RClick control project browser project browser in project explorer as '<project browser1>'
    And I Select context menu item EC project browser in project explorer as '<project browser2>'
    And I click the button '<button>' in the CE Conflict Window
    And I click the button '<button1>' in the CE Conflict Window

    Examples:
      | SlNo. | project browser1    | project browser2   | button | button1 |
      | 1     | ControlExecutable_1 | Generate and Build | OK     | Update All |
    
  @95249_5
  Scenario Outline: Assingning Instance in Hardware Mapping
    When I Click '<tabname>' on service mapping edittor window
    And I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<appfacet>'
    And I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
    Then I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance
  
  @map_Emport_ATV6xx_PM53_in_Hardware
  Examples:
    | tabname          | appfacet                                                                        |
    | Hardware Mapping | ATV71AS_1_ATV$$ATV61AS_1_ATV$$EMPortM_1_EMPortM$$ATV6xxEGP_1_ATV$$PM53xxEM_1_PM |
    
  @95249_6
  Scenario Outline: Assingning Instance in Communication Mapping
    When I Click '<tabname>' on service mapping edittor window
    And I Verify if the added device is available for mapping as '<server>'
    And I Drag and drop the EPE Managed Device from devices to channels as '<server>'
    
  @map_STB_ATV61_ATV71_ATV6xx_in_Communication
  Examples:
    | tabname               | server                                           |
    | Communication Mapping | STBIsland_1$$EATV61HW_1$$EATV71HW_1$$EATV6xxHW_1 |
    
    
  @95249_7
  Scenario Outline: Open Refine Online window
    When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
    And I Select context menu item EC project browser in project explorer as '<context menu>'
    And I click modal dialog window Instance editor save in application explorer as '<button>'
    And I Click on OK button from Reconfirm Deploy Built Project Popup window
    
    @open_Refine_in_TE_M580_Standalone
    Examples:
      | context menu  | Controller      | button |
      | Refine Online | M580_Standalone | OK     |
      
  @95249_8
  Scenario Outline: Verify Communication in Refine Online
    When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
    Then I Verify Instance '<instance>' status '<status>' in Refine Window
    When I selected Close Refine Offline in refine offline
    Then Verify notification panel message Notification Pannel in message box as '<content>'
    
    @communication_Verify_ATV6xxEGP_1_ATV
    Examples:
      | Project Browser RO1                    | instance        | status          | content                                |
      | Programs$$Tasks$$MAST$$Logic$$Folder_1 | ATV6xxEGP_1_ATV | CommunicationOK | Close Refine Online Editor (Completed) |