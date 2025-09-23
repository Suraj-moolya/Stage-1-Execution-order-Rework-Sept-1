Feature: 91514 - Check the P2P old method functionality by incrementally adding the network variables 

#Pre-Requisites:
#Start System server of EPE-2024 
#Open Engineering client once System server is ready with out any issue
#Create a system(System_4) and navigate to Project explorer

@TC_EPE_CP_PGSQL_91514_001
Scenario Outline: Create a Control Project for M580_Standalone and M580_HSBY
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer

@Create_M580_standalone_Control_Project_1
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone |
  
@Create_M580_HSBY_Control_Project_2
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name |
  | 1     | System_1         | Create Control Project | M580       | M580_HSBY       |


@TC_EPE_CP_PGSQL_91514_001a  
Scenario Outline: Create Ethernet Network in TE
When I Right Click on nodes System Explorer Node in system explorer as 'System_4'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

@Create_Ethernet_Network_in_TE
Examples:
  | SlNo. | context menu            | project browser1        |
  | 1     | Create Ethernet Network | Create Ethernet Network |
  

@TC_EPE_CP_PGSQL_91514_001b
Scenario Outline: Do Configuration  for Controllers M580 and HSBY
When I Right Click on nodes System Explorer Node in system explorer as '<node>'
And I Select context menu item EC project browser in project explorer as '<item>'
And I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I selected select PLC bus combobox item CE in refine offline as '<Cpu_version>'
And I selected List of modified Yes button CE in dialog ce
And I selected List of modified Yes button CE in dialog ce
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

@Do_configuration_for_M580_Standalone
Examples:
  | SlNo. | item      | node         |Project Browser RO1        |Cpu_version          |
  | 1     | Configure | Controller_1 |Configuration$$0 : PLC bus |BME P58 6040   04.40 |

@Do_configuration_for_HSBY
Examples:
  | SlNo. | item      | node         |Project Browser RO1        |Cpu_version          |
  | 1     | Configure | Controller_1 |Configuration$$0 : PLC bus |BME H58 6040   04.40 |
  

@TC_EPE_CP_PGSQL_91514_002
Scenario Outline: Increase the memory of controllers in server memory start and length 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I enter a values in testbox item in memory start and length as '<Values>'

@increase_memory_of_M580_standalone
Examples:
  | SlNo. | context men | Controller name | Values      |
  | 1     | Properties  | Controller_1    | "101","500" |
  
@increase_memory_of_HSBY
Examples:
  | SlNo. | context men | Controller name | Values      |
  | 1     | Properties  | Controller_2    | "101","500" |
  

@TC_EPE_CP_PGSQL_91514_003
Scenario Outline: Add instance in application explorer
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'

@add_instance_to_AE 
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | Analog             | AnalogOutputGP$$1.0.93 |
  | 2     | Analog             | AnalogInputGP$$1.0.138 |
  | 3     | MotorGP            | MotorGP$$1.0.123       |
  | 4     | ValveGP            | ValveGP$$1.0.100       | 
  

@TC_EPE_CP_PGSQL_91514_004
Scenario Outline: Create 2 control project in PE
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer

@Create_M580_Control_Project_1
Examples:
  | SlNo. |  project browser1 | context menu           | controller | controller_name |
  | 1     |  System_1         | Create Control Project | M580       | M580_Standalone |
  
@Create_M580_Control_Project_2
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name  |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone2 |
  

@TC_EPE_CP_PGSQL_91514_005
Scenario Outline: Assign the facets to the containers 
When I RClick control project browser project browser in project explorer as '<projectBrowser1>'
And I Select context menu item EC project browser in project explorer as '<projectBrowser2>'

@Assign_facets_to_containers_in_CP1_and_CP2
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 |
  | 1     | ControlProject_1 | Assign Facets   |

    
@TC_EPE_CP_PGSQL_91514_006
Scenario Outline: Open Service Mapping Editor and map to Controller to respective controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

@Map_Controller_1_in_ControlExecutable_1
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                 |
  | 1     | ControlProject_1 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Controller_1 | 
  
@Map_Controller_2_in_ControlExecutable_1
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                 |
  | 1     | ControlProject_2 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Controller_2 |


@TC_EPE_CP_PGSQL_91514_007
Scenario Outline: open refine offline for M580 standalone system and add variables 
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I RClick on filter Refine Offline MDI Window in refine offline
And I selected Customize Columns in refine offline
And I Select Column Configuration Customize Columns in refine offline as 'Constant'
And I selected Ok column configuration window in control expert
And I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as '<param>'
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

@ADD_varaibles_in_both_M580_and_HSBY
Examples:
  | SlNo. | project browser1 | project browser2 |Project Browser RO1                            |param                 |
  | 1     | ControlProject_1 | Refine           |Variables & FB instances$$Elementary Variables |ValveGP_1_OPV$$10$$SE |
  
  
@TC_EPE_CP_PGSQL_91514_007a
Scenario Outline: Manage Peer to Peer
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I click modal dialog window project browser in project explorer as '<Button>'

Examples:
  | SlNo. | project browser1 | context menu        | Button |
  | 1     | M580_Standalone  | Manage Peer to Peer | Next   |


@TC_EPE_CP_PGSQL_91514_008
Scenario Outline: Generate and Build from control executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
And I Drag and drop from remote varaibles to source variables in P2P as '<server>'
And I selected Rename Pop up Ok in message box

Examples:
  | SlNo. | project browser1    | project browser2   | project browser3 | server   |
  | 1     | ControlExecutable_1 | Generate and Build | OK               | SE1$$SE3 |



Scenario Outline: Deploying project to respective controller
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
When I Navigate through project browser CE Project Browser RO in refine offline and verify Communication is happening as '<Project Browser RO1>'
And I selected Close Refine Offline in refine offline

@Deploy_the_controller_182.233.63.5__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 | Project Browser RO1                                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.5         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Programs$$Tasks$$MAST$$Logic$$Read_M580_Stand_P2P_1 |
  
  
#######################Execution order of TC 91514 ##########################################################################
#Scenarios 146 Build_Build all the existing executable(if any errors found, clear and build)
#tag-@Build_ControlEcecutable_1 
#tag-@Deploy_the_controller_182.233.63.5__M580_Standalone 
#############################################################################################################################
  