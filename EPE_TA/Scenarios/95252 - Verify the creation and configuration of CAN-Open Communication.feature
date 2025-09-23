Feature: 95252 - Verify the creation and configuration of CAN-Open Communication

  @TC_EPE_TE_PGSQL_95252
  
  @95252_1
  Scenario Outline: Open STB Island Configure Window in TE
    When I right-click on '<node_name2>' in the Topology Explorer
    And I Select context menu item EC in Topology Explorer as '<action2>'
    
  @STB_Config_Window
  Examples:
    | node_name2  | action2   |
    | STBIsland_1 | Configure |
  
  @95252_2
  Scenario Outline: Configure Modules in STB Island
    When I double-click on "<main_folder>" "<subfolder1>" and "<final_item1>" in the catalog browser
    And I double-click on device '<subfolder1>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder2>" and "<final_item2>" in the catalog browser
    And I double-click on device '<subfolder2>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder3>" and "<final_item3>" in the catalog browser
    And I double-click on device '<subfolder3>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder4>" and "<final_item4>" in the catalog browser
    And I double-click on device '<subfolder4>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder6>" and "<final_item6>" in the catalog browser
    And I double-click on device '<subfolder6>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder5>" and "<final_item5>" in the catalog browser
    And I double-click on device '<subfolder5>' in the catalog browser
    And I double-click on "<main_folder>" "<subfolder7>" and "<final_item7>" in the catalog browser
    And I double-click on "<main_folder>" "<subfolder8>" and "<final_item8>" in the catalog browser
    And I double-click on device '<device2>' in the catalog browser
  
  @STB_Config_Modules  
  Examples:
    | main_folder   | subfolder1          | final_item1        | subfolder2 | final_item2        | subfolder3    | final_item3        | subfolder4     | final_item4        | subfolder5   | final_item5        | subfolder6    | final_item6        | subfolder7  | final_item7        | subfolder8       | final_item8   | device2            |
    | STB - Catalog | Networking (Legacy) | STBNIP2311 - V4.xx | Power      | STBPDT3100 - V1.xx | Digital Input | STBDDI3725 - V1.xx | Digital Output | STBDDO3705 - V1.xx | Analog Input | STBAVI1400 - V1.xx | Analog Output | STBAVO0200 - V1.xx | Accessories | STBXBE2100 - V1.xx | Enhanced CANopen | ATV61 - V1.xx | STBXMP1100 - V1.xx |
    
    
  @95252_3
  Scenario Outline: Select toolbar option in Island
    When I Double-clicking the '<menu>' item in the STB Config toolbar
    And I Select '<menuitem>' in the STB Config toolbar
    And I Select '<baudrate>' in Baud Rate Window
    And I Click '<btn>' button in Baud Rate Window
    And I Click '<btn>' button in Baud Rate Window PopUP
    And I Click '<btn>' button in Baud Rate Window PopUP
    
    @Select_Island_500kbps
    Examples:
      | menu   | menuitem             | baudrate | btn |
      | Island | Baud Rate Tuning ... | 500 kbps | OK  |
      
      
  @95252_4
  Scenario Outline: Close STB Configure Window
    When I selected Close Configuration window in Topology Explorer
    And I click modal dialog window '<button>' in Topology Explorer
    Then Verify Action message in notification pannel project browser in project explorer as '<notification pannel>'
  
  @close_STB_Edittor
  Examples:
    | button | notification pannel                 |
    | Yes    | Close STB Island Editor (Completed) |
    
  @95252_5
  Scenario Outline: Performing Physical Connection For STBIsland
    When I right-click on '<node_name2>' in the Topology Explorer
    And I Select context menu item EC in Topology Explorer as '<action3>'
    And I set the IP address to '<ip_address>' and subnet mask to '<subnet_mask>' in STBIsland properties
    And I Perform action on the Folder by Clicking on '<close_button>' in Topology Explorer
    
  @Properties_network_STB
  Examples:
    | node_name2  | ip_address    | subnet_mask | action3    | close_button       |
    | STBIsland_1 | 182.233.64.86 | 255.255.0.0 | Properties | STBIsland_1$$Close |
    
  @95252_5
  Scenario Outline: Map STB_Island to Physical Connections
    When I Right Click on nodes System Explorer Node in system explorer as '<Topology Explorer Tree1>'
    And I Select context menu item EC project browser in project explorer as '<Topology Explorer Tree2>'
    And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
    When I click modal dialog window project browser in project explorer as '<Button>'
    
  @Physical_Connection_STB
  Examples:
    | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
    | 1     | STBIsland_1             | Physical Connections    | STBIsland_1$$SE_Network | OK     |
  
  @95252_6
  Scenario Outline: Perform Connect Online and Disconnect in STB
    When I Double-clicking the '<menu>' item in the STB Config toolbar
    And I Select '<menuitem>' in the STB Config toolbar
    
  @STB_Connect_online
    Examples:
      | menu   | menuitem |
      | Online | Connect  |
    
  @STB_DisConnect_online
    Examples:
      | menu   | menuitem   |
      | Online | Disconnect |
      
  @95252_6A
  Scenario Outline: Downloading Project in STB Config Setting Ip Address
    When I Select '<btn>' Radio button in STB Connection Settings
    And I Set Ip Address in STB Connection Settings as '<ip>'
    And I Click button in STB Connection Window as '<button>'
    Then I Verify Notification pannel in STB Configure window as '<msg>'
    When I Click button in Data Transfer window in STB Configuration as '<button2>'
    And I Click button in Data Transfer window in STB Configuration as '<button3>'
    Then I Verify Notification pannel in STB Configure window as '<msg1>'
    When I Click button in Data Transfer window in STB Configuration as '<button>'
    Then I Verify Notification pannel in STB Configure window as '<msg>'
  
  @setting_ip_for_Stb_Online  
  Examples:
    | btn    | ip            | button | button2  | button3 | msg                | msg1                             |
    | TCP/IP | 182.233.64.86 | OK     | Download | Yes     | Island is healthy. | Download completed successfully. |
      
  @95252_6
  Scenario Outline: Create ATV61AS, ATV71AS and MotroVSGP in Appication Explorer
    When I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
    And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<TemplatesBrowser2>'
    Then Verify the template is present in Application browser as '<TemplatesBrowser1>'

  @drag_drop_atvas61
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2        |
    | ATV61AS           | ATV61AS$$2.2.9$$Folder_1 |
  
  @drag_drop_atv71as
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2        |
    | ATV71AS           | ATV71AS$$1.3.8$$Folder_1 |
  
  @drag_drop_motorvsgp
  Examples:
    | TemplatesBrowser1 | TemplatesBrowser2            |
    | MotorVSGP         | MotorVSGP$$1.0.128$$Folder_1 |