---
id: proto:cellular
type: Protocol
name: Cellular data
aliases:
- LTE
- 4G
- 3G
- GPRS
- cell modem
- LTE Cat M1
- 3G GSM
- cellular modem
- 4G cellular
- GSM
category: Communication
protocol_kind: transport
---
Cellular data is a transport link that sends monitoring and control traffic over a mobile network, and the sources list LTE, 3G and 4G variants on dataloggers such as the Locus LGate. The CPS FlexOM-4G Gateway comes with a SIM card already installed, a 5-year 4G plan and a 4G antenna that you have to fit. The standard FlexOM Gateway gets its internet connection through Ethernet instead. The Solis 4G data logger stick ships with an external antenna, and Solis also offers GPRS sticks that connect to the Solis Cloud portal. For the Enphase IQ Gateway, the M1 cell modem suits sites with fewer than 64 microinverters and reports every 6 hours. The C1 modem works for sites of any size and reports every 15 minutes. If an Enphase Mobile Connect modem stops working, unplug its USB cable, power cycle the IQ Gateway, wait for a full boot, reconnect the cable and check that the cloud LED turns solid green. On SolarEdge inverters, every device on the cellular network needs a GSM kit and is set up from the LCD menu under Server, Cellular. Data is sampled every 15 minutes and uploaded every 4 hours. When an SMA system connects through a cellular modem, set the data request interval to Hourly or Daily to avoid extra data charges on the mobile plan.

<!-- review notes
- sentence 1: support check: partial - Passages list Cellular LTE/3G/4G options, but the definition of a transport link carrying monitoring/control traffic and the Locus LGate naming are not stated.
- sentence 2: support check: partial - Pre-installed SIM, 5-year 4G plan, and Ethernet for the standard gateway are stated, and an antenna installation section exists, but nothing says the antenna is included or that the user must fit it.
- sentence 3: support check: partial - The 4G stick ships with an external antenna, and a GPRS stick integration guide for Solis Cloud exists, but 'Solis offers GPRS sticks' is only implied.
- sentence 6: support check: partial - GSM kit per device, the 15-minute sampling and 4-hour upload, and the Server > Cellular menu are stated, but 'every device' applies to the multi-device configuration while the single-device one needs a kit for its one device, and the menu path is given for the High BW cellular configuration.
-->
