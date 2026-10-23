---
id: symptom:auxiliary-supply-undervoltage
type: Symptom
name: Auxiliary supply undervoltage
---
Auxiliary supply undervoltage means the low-voltage supply that powers control electronics is missing or too low, as opposed to the main DC bus or the grid. On SMA Multicluster Box systems, event 6466 reports a system failure in which the 15 V or 24 V internal supply is defective. The manual gives no field repair for this event, so contact the manufacturer's service. On devices fed from an external auxiliary supply, first check that the supply is connected to the correct input terminals and is within the device's rated input range. Some devices come in more than one supply version, for example high-voltage AC/DC, medium-voltage DC-only and low-voltage DC-only. Orange connectors mark the DC supply ratings, so confirm that the installed supply matches the version. An isolated auxiliary output can have a small rating, such as 24 Vdc at 0.4 A maximum, so check that the connected loads do not exceed it. Do not confuse this with a DC bus undervoltage alarm, which has its own fault code and troubleshooting steps.

<!-- review notes
- sentence 1: support check: partial - Passage says the 15 V/24 V supply in the Multicluster Box is defective, but does not define it as the control-electronics supply or contrast it with the DC bus or grid.
- sentence 4: support check: partial - The passage gives terminals A01/A02 and rated ranges for the SEL-735, but does not say to check these first, and it covers only that device.
- sentence 5: support check: partial - Three supply versions and orange connectors for the DC-only ones are listed, but the passage doesn't say to confirm the installed supply matches, and orange marks only the DC-only versions.
- sentence 6: support check: partial - The 24 Vdc, 0.4 A max isolated auxiliary supply is stated, but the advice to check connected loads isn't in the passage.
- sentence 7: support check: partial - A DC bus undervoltage message with its own code and troubleshooting exists, but the passage does not say it should not be confused with auxiliary undervoltage.
- sentence 1: review: partial - The passage only says the 15 V or 24 V supply in the Multicluster Box is defective; it does not say this supply powers the control electronics or contrast it with the DC bus or the grid.
- sentence 4: review: partial - The SEL-735 passage gives the input terminals (A01/A02) and the rated supply ranges, but it covers only that device and does not say to check these first.
- sentence 7: review: partial - The Solis row shows a DC bus undervoltage alarm with its own code and troubleshooting step, but the warning not to confuse it with auxiliary undervoltage is editorial and not in the passage.
-->
