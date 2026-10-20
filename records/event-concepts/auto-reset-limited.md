---
id: ec:auto-reset-limited
type: EventConcept
name: Auto-reset with a retry limit
axis: recovery
aliases: [limited automatic restarts, retry limit, restarts up to a stated count]
status: active
---
The device restarts automatically up to a stated number of times (or within a stated window) and then stays off until an operator acts.

Reading rule: a row that states a count or a window of automatic restarts ("restarts up to three times", "after the fifth occurrence in 24 hours the inverter stays off") reads as this concept. Without a stated limit it is auto-reset.
