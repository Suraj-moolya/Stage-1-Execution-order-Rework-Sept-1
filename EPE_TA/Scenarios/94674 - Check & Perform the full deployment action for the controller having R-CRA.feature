Feature: 94674 - Check & Perform the full deployment action for the controller having R-CRA

@TC_EPE_HSBY_CRA_94674_001
Scenario Outline: Change CPU Version of controller 
When I selected select PLC bus combobox item CE in refine offline as '<Cpu_version>'

#@Change_CPU_Version_of_controller__BME_P58_4040_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME H58 6040   04.40 |
  
@TC_EPE_HSBY_CRA_94674_002  
Scenario Outline: Automatic blocking of service port in EIO bus 
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
And I select Automatic blocking of service port EIO in control expert

@Check_Automatic_blocking_of_service_port
Examples:
  | SlNo. | identifiers |
  | 1     | ServicePort |

@TC_EPE_HSBY_CRA_94674_003  
Scenario Outline: Add a device to EIO bus 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<Dialog List box CE4>'
And I selected Dialog OK CE in dialog ce

@Add_BME_XBP_1200_to_drop1_of_EIO_bus
Examples:
  | SlNo. | Project Browser RO1        | Dialog Panel CE2 | Dialog Panel CE3 | Dialog List box CE4 | content |
  | 1     | Configuration$$2 : EIO Bus | .X80 remote drop | BME XBP 1200     | BME CRA 313 10      | NA      |
  
@TC_EPE_HSBY_CRA_94674_004  
Scenario Outline: Add a device to a drop in EIO bus 
When I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as '<Dialog List box CE4>'
And I selected Dialog OK CE in dialog ce

@Add_BME_XBP_0602_to_drop2_of_EIO_bus
Examples:
  | SlNo. | Dialog Panel CE2 | Dialog Panel CE3 | Dialog List box CE4 | content |
  | 1     | .X80 remote drop | BME XBP 0602     | BME CRA 313 10      | NA      |
  
@TC_EPE_HSBY_CRA_94674_005 
Scenario Outline: Add a power supply device to EIO bus 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I selected Dialog OK CE in dialog ce

@Add_BMX_CPS_2000_to_drop1_of_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 1200$$(P) | BMX CPS 2000     |
  
@Add_BMX_CPS_3522_to_drop2_of_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                     | Dialog Panel CE2 |
  | 1     | Configuration$$2 : EIO Bus$$2 : .X80 remote drop$$0 : BME XBP 0602$$(P) | BMX CPS 3522     |

@TC_EPE_HSBY_CRA_94674_006
Scenario Outline: Add a new device to EIO bus slot 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
When I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I selected Dialog OK CE in dialog ce

@Add_BME_CRA_31310_to_drop1_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2     | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 1200$$1 | I/O Expansion Module | BME CRA 313 10   |
  
@Add_BME_CRA_31310_to_drop2_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2     | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 0602$$1 | I/O Expansion Module | BME CRA 313 10   |

@TC_EPE_HSBY_CRA_94674_007  
Scenario Outline: Verify if the module exists in the add device window 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
And I verify the module name in add device window as '<module>'
And I selected Dialog Cancel CE in dialog ce

@Verify_I/O_Expansion_Module_in_drop1
Examples:
  | SlNo. | Project Browser RO1                                                   | module               |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 1200$$2 | I/O Expansion Module |
  
@Verify_I/O_Expansion_Module_in_drop2
Examples:
  | SlNo. | Project Browser RO1                                                   | module               |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 0602$$2 | I/O Expansion Module |

@TC_EPE_HSBY_CRA_94674_008  
Scenario Outline: Navigate to the drop 2  
And I perform down arrow using keyboard actions
And I enterkey Project Browser RO in refine offline

Examples:
  | SlNo. | content |
  | 1     | NA      |
  
  


