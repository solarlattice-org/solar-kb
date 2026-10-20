---
id: mit:contact-manufacturer-service
type: Mitigation
name: Contact manufacturer service
aliases:
- post-sales service
- after-sales service personnel
- CPS Service
- the Service
---
Contacting the manufacturer's service team is the last step in the inverter troubleshooting tables, used after the on-site steps have not cleared the alarm. For a cooling fan alarm (ExtFanErr), first wait 5 minutes to see if the alarm clears by itself, check the fan blades for foreign objects, and reboot by switching the external AC disconnect off and back on. Call post-sales service only if the alarm is still there. For an internal communication alarm (CommErr), the likely cause is poor contact at the terminal block connectors of the internal communication wires. Wait and reboot first, then contact service if the alarm persists. For an internal memory alarm (EepromErr), the only field step is to wait 5 minutes for the alarm to clear itself. After that, the problem goes to post-sales service. For arc alarms (ARC Protect or Arcboard Err), first make sure the logic connector to the arc board is secure and run the Arc Fault Test from the Settings menu. If the alarm comes back, CPS Service replaces the arc board or the wiring box. An older manual says to inspect the arc board, clear the arc fault with ARCFaultClear and check the PV input for an arc or a bad cable connection before calling after-sales service personnel. This action does not fix anything on site. It hands faults with internal causes, such as a damaged arc board or a memory problem, over to the manufacturer.

<!-- review notes
- sentence 1: support check: partial - Passages show contacting service as the final step in several rows after on-site steps, but not that it is the last step in all the troubleshooting tables.
- sentence 5: support check: partial - Passages give the steps for both codes, but the 'CPS Service replaces' is stated as contacting CPS Service to replace arc board or wiring box, and 'make sure connector secure' matches; minor reframing only, though the 'alarm comes back' condition is present, so mostly supported with slight overstatement of who replaces.
- sentence 6: support check: partial - The older manual's ARC Protect and Arcboard Err rows cover these steps, but they are split by code (PV input arc check is only for ARC Protect, board inspection only for Arcboard Err) and the statement merges them.
- sentence 7: support check: partial - Passages show arc board damage and memory problems as causes with escalation to service, but 'does not fix anything on site' is an interpretation; other steps such as waiting and checks do occur, and 'this action' is unspecified.
-->
