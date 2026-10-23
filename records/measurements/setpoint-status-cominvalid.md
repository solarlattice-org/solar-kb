---
id: meas:setpoint-status-cominvalid
type: Measurement
name: Setpoint status ComInvalid
---
ComInvalid is a status value that SMA Sunny Central CP XT inverters show for the power setpoint function. For active power, it appears when the communication-based mode WCtlCom is selected and the setpoint information the inverter receives has invalid content. For reactive power, it appears when the mode VArCtlCom or PFCtlCom is selected and the received setpoint information is invalid. It is not the same as ComFail. ComFail means no valid reactive power setpoint signal has arrived for at least five minutes, while ComInvalid means a setpoint arrives but its content is not valid. Other values of this status are Off, when no setpoint mode is selected, and OK, when a mode is selected and no error is present. The corrective measure the manufacturer gives is to check the power specification settings.

<!-- review notes
- sentence 1: support check: partial - The passages show ComInvalid as a display value for power setpoint functions, but they never name SMA Sunny Central CP XT as the device.
- sentence 4: support check: partial - The ComFail and ComInvalid definitions are stated, but the claim that a setpoint arrives with invalid content is only an interpretation of the passages.
- sentence 1: review: partial - The passages show ComInvalid as a display value for the power setpoint modes, but the quoted text never names SMA Sunny Central CP XT inverters (only the source id suggests it).
-->
