---
id: comp:transfer-switch-controller
type: Component
name: Transfer switch controller
aliases:
- PWRcell ATS Controller
- inverter ATS control board
---
The transfer switch controller is the control unit inside an external automatic transfer switch (ATS) that works with a PWRcell inverter. The inverter turns on transfer switch control through its NumTranSwtchs setpoint, which sets how many switches are installed. Set NumTranSwtchs to 1 for AC coupled PV and to 2 for AC generator integration. AC generator integration needs the inverter ATS to carry the upgraded PWRcell ATS Controller, which comes in the PWRcell ATS Controller Upgrade Kit (Model G0080060). This controller can also be used in any other setup that needs a PWRcell ATS. A controller version that does not suit the application can make the PWRcell system behave in unexpected and incorrect ways, so check that the equipment matches the chosen configuration. Configuration error 0X7707 means the inverter is set up for AC generator integration but the installed ATS units do not have the correct controller. Wiring error 0X7726 means the inverter ATS did not transfer back to the grid-connected position. To fix it, check the N terminal wiring, check that the Cat 5 control cable is terminated properly at both the inverter and the ATS control board, and check that the closing coil and relay wiring on the transfer mechanism is fastened securely. High voltages are present in the automatic transfer switch during testing. Do not touch live parts, and disconnect the switch from all voltage sources before fixing any fault. An automatic transfer switch is not a distribution board, so the loads and the PV system still need their own protective devices.

<!-- review notes
- sentence 1: support check: partial - NumTranSwtchs enabling transfer switch controls and setting number of external ATSs is stated, but the 'controller inside an ATS' definition is not in the passages.
-->
