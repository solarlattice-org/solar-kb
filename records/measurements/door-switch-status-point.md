---
id: meas:door-switch-status-point
type: Measurement
name: Door switch status point
aliases:
- Door Switch Open
---
The door switch status point is a monitoring flag that goes active when one or more Megapack enclosure doors are open. The flag does not cover the Customer Interface Bay door, so an open door in that bay will not set it. An open door switch can also open the Megapack enable circuit, which is reported as a separate status point; the enable switch or a remote shutdown can open that circuit too. Before some service tasks, confirm that the battery door shows as closed. Some inverter switch cabinets have door contact switches that can be checked during maintenance, and the switch make depends on the cabinet model and production version.
