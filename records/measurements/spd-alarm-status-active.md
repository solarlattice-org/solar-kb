---
id: meas:spd-alarm-status-active
type: Measurement
name: SPD active alarm status
aliases:
- Active Alarm Replace SPD
- Protection loss
---
On a Power Xpert SPD, the alarm status point shows the protection state of the device. It reads either Protected or Active Alarm Replace SPD. Over the BACnet interface, alarm status is a read-only binary object. Its inactive text is Protected and its active text is Protection loss. Some SPD units can also report status remotely through a form C relay contact, wired to a three-terminal connector. On the display, an active alarm matches red phase LEDs, which mean a loss of protection, and an audible alarm on units that have one. When every phase shows red, possible causes are lost protection on all phases, an SPD rated below the system voltage, or an extended temporary overvoltage. The fix is to replace the SPD after removing any overvoltage source. A single red LED can follow a significant surge event. Silencing the audible alarm does not clear the fault, and the alarm comes back after a power cycle if the fault is still there.

<!-- review notes
- sentence 4: support check: partial - Red LED means loss of protection and audible alarm sounds on equipped units, but the passages do not mention an 'active alarm' on the display matching these; the link is inferred (and red LED is not specific to 'phase LEDs' for the Power Xpert).
- sentence 4: review: partial - The passages say red LEDs mean loss of protection and an audible alarm sounds on units that have one, but nothing in them ties these to an 'active alarm' status point.
-->
