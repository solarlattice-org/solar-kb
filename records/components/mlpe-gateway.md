---
id: comp:mlpe-gateway
type: Component
name: MLPE communication gateway
aliases:
- Tigo Gateway
- Gateway Interface Board
- GIB
- Cloud Connect Advanced
- CCA
- rooftop communication kit
- IQ Gateway
---
The MLPE communication gateway is a rooftop radio unit. It talks to module-level devices such as Tigo TS4-R units within its RF range, and wiring carries the signal down to a Cloud Connect Advanced (CCA) or a Gateway Interface Board (GIB) at the inverter. Mount the Tigo Gateway on the roof within 50 ft of the TS4-R units, with line of sight to them. Larger arrays may need more than one gateway to cover the whole array. The GIB sits on the inverter communication assembly and is hardwired to the rooftop gateway, which gets both power and RS485 communication over that wiring; expect 16-22 Vdc across the GIB terminal block. The main failure mode is MLPE gateway communication failure: TS4-R devices do not respond to detection during commissioning, or they lose contact with the gateway. Common causes are a missing or misplaced termination resistor, reversed signal polarity (shown by a red LED on the GIB), crossed or loose signal wires, and electromagnetic interference when signal wires share a conduit with DC cables. If signal wires run in the same conduit as DC cables, use shielded cable rated for 600 Vdc. If there is no voltage at the GIB terminals, check whether the devices are in rapid shutdown because the inverter has no AC. In Enphase systems, if a microinverter loses communication with the IQ Gateway for longer than the configured time limit, it cuts its output to a static safe limit. While the gateway link is lost, its LED flashes orange. I-V curve measurements on strings with MLPE can be started, but the results are not meaningful. Ask the MLPE supplier how to measure those strings.

<!-- review notes
- sentence 4: support check: partial - The passages describe troubleshooting for TS4-R devices not responding to detection or losing communication, but they do not call it the main failure mode.
- sentence 5: support check: partial - The passages cover resistor placement, reverse polarity with the red LED, wire cross connections, loose connections, and EMI from shared conduit. They do not say a missing resistor is a cause, and they do not frame these as the common causes.
- sentence 4: review: partial - The passage covers TS4-R devices that do not respond to detection during commissioning or lose contact with the gateway, but it never calls this the main failure mode.
-->
