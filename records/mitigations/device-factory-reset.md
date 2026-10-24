---
id: mit:device-factory-reset
type: Mitigation
name: Factory reset of controller or communication device
aliases:
- Reset to default settings
- Reset Datalogger
- communication processor restart
- Reset operating parameters
- reset button long press
- factory reset of communication board
- Reset Op. Data
- factory reset logger
- Reset to Factory Defaults
- Restore factory settings
- Reset All
- Reset Device
---
A factory reset returns a communication board, data logger, cluster controller or inverter control unit to its default settings, wiping out the parameters a user has set. It is used when an inverter cannot communicate properly with other devices, or when a data logger password has been forgotten. Try a plain restart or reboot first, because it is the least invasive option and leaves all settings in place. On many devices you start the reset by holding down a reset button: about 30 seconds on one SMA communication board and more than 10 seconds on Solis loggers and the Generac PWRmanager. Other devices do it from a menu, from configuration software or by writing a Modbus register. The reset can delete passwords, network and DHCP settings, system time, stored event and energy data, and regional grid settings. Record the configuration beforehand and enter it again afterwards. After the reset, look up the newly assigned IP address in the router, or reconnect the logger to the network, and check that the device communicates again. A reset cannot fix faulty hardware: if communication still fails or the logger does not broadcast afterwards, contact the manufacturer's service team or ask for a replacement.

<!-- review notes
- sentence 3: support check: partial - SMA says to always try the processor restart first as least invasive and that it doesn't affect settings, but the generic reboot claim for all devices is only partly stated (the u9 soft reboot doesn't say it keeps settings).
- sentence 4: support check: partial - About 30 s on SMA, over 10 s on Solis-type loggers, and menu/software/Modbus register methods are shown, but the passages do not name Generac PWRmanager or Solis (the 10 s button is unattributed).
- sentence 6: support check: partial - SMA says to check the router for a new IP and reapply settings, and network reconfiguration is required, but 'reconnect the logger' and verifying communication are only loosely implied.
- sentence 7: support check: partial - SMA says persistent failure may indicate hardware issues and to contact service, and DLS-W says to contact service for replacement if not broadcasting, but the replacement is conditioned on warranty and the general claim 'reset cannot fix faulty hardware' is only implied.
-->
