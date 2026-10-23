---
id: stressor:poor-connector-contact
type: Stressor
name: Poor connector contact
aliases:
- Bad contacts
- Bad mechanical contacts
---
Poor connector contact is a plug, socket or terminal that is not seated firmly or no longer makes a good electrical connection. Inside inverters, a poorly seated temperature sensor socket is listed as a possible cause of the temperature sensor fault alarm, and the alarm is a prompt that the temperature reading is abnormal. A fan socket with poor contact is listed as a cause of the external fan error alarm, which reports cooling fan failure. A loose logic connector on the arc detection board can raise arc board error or arc protection alarms, and loose terminal blocks on internal communication wires can cause the internal communication error. In module junction boxes, mechanical contacts can loosen from loose clamping or screws and from daily and seasonal thermal cycling, which can lead to interconnection failure. On a failing connector the contact resistance rises, so the connector heats up and the hot spot can be found with thermography. Late failures can show up as ground faults or as a burst connector that opens the string. To fix it, check that the affected connector is secure, then reboot the inverter by switching the external AC disconnect off and back on. For arc board alarms, also run the arc fault test. Call service if the alarm comes back. Proper installation and regular maintenance help prevent connector damage over time.

<!-- review notes
- sentence 1: support check: partial - Passages list poor contact of sockets/terminal connectors as causes and mention loose clamping/screws, but never define the term as 'not seated firmly or no longer makes good electrical connection'.
- sentence 4: support check: partial - CommErr cause (terminal block poor contact) is stated, but arc board passages only say to check the logic connector is secure, not that a loose connector causes the alarms.
- sentence 6: support check: partial - Resistance rise with thermal dissipation found by thermography and ground fault/burst connector opening the string are stated, but 'contact resistance rises so connector heats up' is only roughly stated and these are described as second-phase, fine; mostly supported but the heating causal link is implied.
- sentence 7: support check: partial - Reboot via AC disconnect applies only to TempSensorErr, arc test and call service for arc board; the generalized combined procedure (check connector then reboot) isn't stated for any single alarm.
- sentence 1: review: partial - The passages name poor contact at sockets and terminal connectors and loose clamping or screws, but never give this definition of the term.
- sentence 4: review: partial - CommErr is stated to be caused by poor contact at internal communication terminal blocks, but the arc board rows only say to check that the logic connector is secure; they never say a loose connector causes the alarms.
- sentence 7: review: partial - Each step appears for some alarm (connector check, AC-disconnect reboot for TempSensorErr, arc fault test and service call for arc board), but no passage gives the combined check-then-reboot sequence.
-->
