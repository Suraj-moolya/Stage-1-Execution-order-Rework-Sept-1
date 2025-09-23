Feature: 94675 - Check & Perform the Deploy changes action from Offline to online for the controller having R-CRA.

@TC_EPE_HSBY_CRA_94675_001
Scenario Outline: Add a new device to EIO bus slot 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I enterkey Project Browser RO in refine offline 
When I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE2>'
And I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'
And I selected Dialog OK CE in dialog ce

@Add_BME_AHI_31310_to_drop1_EIO_bus
Examples:
  | SlNo. | Project Browser RO1                                                   | Dialog Panel CE2 | Dialog Panel CE3 |
  | 1     | Configuration$$2 : EIO Bus$$1 : .X80 remote drop$$0 : BME XBP 1200$$2 | Analog           | BME AHI 0812     |
  
@TC_EPE_HSBY_CRA_94675_002 
Scenario Outline: Delete a module from EIO bus
When I perform delete using keyboard actions

Examples:
  | SlNo. | content |
  | 1     | NA      |