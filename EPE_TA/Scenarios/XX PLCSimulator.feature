Feature: XX PLCSimulator

@test0002b
Scenario Outline: Start PLC Simulator
When I Run PLC Simulator
And I click on Start button on PLC Simulator
Examples:
  | SlNo. |
  | 1     | 
  
@test0002b
Scenario Outline: Change port number of simulator to 503 
When I change port number of simulator to 503
And I click on Start button on PLC Simulator
Examples:
  | SlNo. |
  | 1     |
  
Scenario Outline: Open PLC Simulator
When I Run PLC Simulator
Examples:
  | SlNo. |
  | 1     | 
    
Scenario Outline: Change port number of simulator
When I change port number of simulator '<Port>'
And I click on Start button on PLC Simulator

@Change_the_Simulator_port_to_510
Examples:
  | SlNo. | Port |
  | 1     | 510  |
  
@Change_the_Simulator_port_to_511
Examples:
  | SlNo. | Port |
  | 1     | 511  |
  

