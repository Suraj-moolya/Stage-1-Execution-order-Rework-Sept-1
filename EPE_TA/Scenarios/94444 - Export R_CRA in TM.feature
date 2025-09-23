Feature: 94444 - Export R_CRA in TM

@TC_EPE_HSBY_CRA_94444_001
Scenario Outline: Add a device to EIO bus 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<Dialog List box CE4>'
And I selected Dialog OK CE in dialog ce

@Add_BME_XBP_0400_to_drop1_slot0_of_EIO_bus
Examples:
  | SlNo. | Project Browser RO1        | Dialog Panel CE2 | Dialog Panel CE3 | Dialog List box CE4 | content |
  | 1     | Configuration$$2 : EIO Bus | .X80 remote drop | BME XBP 0400     | BME CRA 313 10      | NA      | 
  
@TC_EPE_HSBY_CRA_94444_002
Scenario Outline: Add a new device to EIO bus slot 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
When I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I selected Dialog OK CE in dialog ce

@Add_BME_CRA_31310_to_drop1_slot1_of_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2     | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 0400$$1 | I/O Expansion Module | BME CRA 313 10   |
  
@Add_BMX_DDO_1602_to_expansion_rack_drop1_slot0
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2 | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$1 : BME XBP 0400$$0 | Discrete         | BMX DDO 1602     |
  
@Add_BMX_DDO_AMI_0810_to_expansion_rack_drop2_slot0
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2 | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$1 : BMX XBP 0800$$0 | Analog           | BMX AMI 0810     |
  
@TC_EPE_HSBY_CRA_94444_003  
Scenario Outline: Add a device to a drop in EIO bus 
When I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<Dialog List box CE4>'
And I selected Dialog OK CE in dialog ce

@Add_BMX_XBP_0800_to_drop2_slot0
Examples:
  | SlNo. |  Dialog Panel CE2 | Dialog Panel CE3 | Dialog List box CE4 | content |
  | 1     |  .X80 remote drop | BMX XBP 0800     | BME CRA 313 10      | NA      | 
  
@TC_EPE_HSBY_CRA_94444_004 
Scenario Outline: Add a device to expansion rack in EIO bus 
When I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I selected Dialog OK CE in dialog ce
And I selected Dialog OK CE in dialog ce

@Add_BME_XBP_0400_to_expansion_rack_drop1
Examples:
  | SlNo. |  Dialog Panel CE3 | content |
  | 1     |  BME XBP 0400     | NA      |
  
@Add_BMX_XBP_0800_to_expansion_rack_drop2
Examples:
  | SlNo. |  Dialog Panel CE3 | content |
  | 1     |  BMX XBP 0800     | NA      |
  
@TC_EPE_HSBY_CRA_94444_005 
Scenario Outline: Verify if the module exists in the add device window 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I verify the module name in add device window as '<module>'
And I selected Dialog Cancel CE in dialog ce

@Verify_I/O_Expansion_Module_in_drop2_slot2
Examples:
  | SlNo. | Project Browser RO1                                                   | module               |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BMX XBP 0800$$2 | I/O Expansion Module |
  
  
@TC_EPE_HSBY_CRA_94444_006 
Scenario Outline: Add a power supply device to EIO bus 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I selected Dialog OK CE in dialog ce

@Add_BMX_CPS_2000_to_drop1
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 0400$$(P) | BMX CPS 2000     |
  
@Add_BMX_CPS_3522_to_drop2
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$2 : .X80 remote drop$$0 : BMX XBP 0800$$(P) | BMX CPS 3522     |
  
@Add_BMX_CPS_2000_to_expansion_rack_drop1
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$1 : BME XBP 0400$$(P) | BMX CPS 2000     |
  
@Add_BMX_CPS_3522_to_expansion_rack_drop2
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$2 : .X80 remote drop$$1 : BMX XBP 0800$$(P) | BMX CPS 3522     |

@TC_EPE_HSBY_CRA_94444_007
Scenario Outline: Exporting instance from root node of TE
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<ContextMenuOption>'
And I Select controller in context menu as '<sub_context_menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<ExportFileName>' with format '<ExportFileFormat>'
And I Click on Button in TE Explorer Window Export in ec windows explorer as 'Save'
Then Verify notification panel message Notification Pannel in message box as '<ExpectedExportMessage>'

@Exporting_Instance_From_RootNode_Of_Topology
Examples:
  | SlNo | Controllers | ContextMenuOption | sub_context_menu | ExportFileName               | ExportFileFormat | ExpectedExportMessage       |
  | 1    | System_2    | Export            | Topology         | System_2_Exporting_1Instance | .csv             | Export Topology (Completed) |