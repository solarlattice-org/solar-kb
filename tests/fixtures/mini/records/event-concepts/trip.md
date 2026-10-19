---
id: ec:trip
type: EventConcept
name: Trip (production stops)
axis: production_effect
aliases: [shutdown, disconnect, stops feeding in, does not start]
status: active
---
The device stops exporting power while the condition persists: it disconnects from the grid, stops, interrupts feed-in or does not start. A brief interruption followed by automatic reconnection is still a trip; reduced but non-zero output is a derate.

Reading rule: "interrupts feed-in", "disconnects", "stops", "shuts down" and "does not start" all read as a trip. A row that says nothing about output yields no production-effect claim.
