---
id: meas:network-overloaded-message
type: Measurement
name: Network overloaded message
aliases:
- Network busy
- '[Interface]: network overloaded'
---
This signature is an inverter event message saying that the communication network is overloaded or busy. SMA inverters log it as event 10248 or event 10249, depending on the model and documentation. When the message is active, the devices on the network are not exchanging any data. The usual fix is to reduce the number of devices on the network and, if needed, to lengthen the data query intervals. A related event reports a high packet error rate, which can also point to an overloaded network or to a poor connection to the network switch or router. If the packet error rate is high, check that the Ethernet cable and connectors are undamaged and plugged in correctly.

<!-- review notes
- sentence 2: support check: partial - Events 10248 and 10249 both appear with network busy/overloaded text, but the passages don't say which is used depending on model or documentation.
-->
