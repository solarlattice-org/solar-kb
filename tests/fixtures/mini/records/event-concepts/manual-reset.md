---
id: ec:manual-reset
type: EventConcept
name: Manual reset (operator restarts or acknowledges)
axis: recovery
aliases: [restart required, power cycle, acknowledge, operator reset]
status: active
---
An operator restarts, power-cycles or acknowledges the device to clear the message; no part is replaced.

Reading rule: "restart the inverter", "switch off and on again", "acknowledge the event" and "clear the fault from the display" read as manual reset, whether done on site or remotely (the two are not distinguished). A row whose first clearing step is to contact service or replace a part reads as service required instead.
