---
id: ec:auto-reset
type: EventConcept
name: Auto-reset (clears by itself)
axis: recovery
aliases: [automatic restart, self-clearing, resumes automatically]
status: active
---
The device resumes on its own once the condition clears, with no stated limit on the number of attempts.

Reading rule: "reconnects automatically", "resumes when the grid returns", "clears when the temperature drops" and "no action required" read as auto-reset. A stated retry count makes it auto-reset with a retry limit. An escalating sequence (observe, then restart, then contact service) classifies by the first step that clears the normal case; the escalation goes in the claim's note.
