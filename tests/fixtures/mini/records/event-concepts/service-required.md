---
id: ec:service-required
type: EventConcept
name: Service required
axis: recovery
aliases: [contact service, replace, repair, service call]
status: active
---
The row tells the reader to contact the manufacturer's service, or to replace or repair a part, before the device returns to normal operation.

Reading rule: "contact Service", "contact your installer", "replace the fan" and "the device must be repaired" read as service required. Escalating sequences (observe, then restart, then contact service) classify by the first step that clears the normal case, so a row that says "restart; if the message persists, contact Service" is a manual reset with the escalation in the claim's note.
