---
id: ec:derate
type: EventConcept
name: Derate (output reduced or limited)
axis: production_effect
aliases: [power limitation, reduced output, power reduction, derating]
status: active
---
The device keeps exporting but reduces or limits its output while the condition persists.

Reading rule: "reduces power", "limits output", "derates" and "power limitation" read as a derate. A stated magnitude lives on the code's `output_limit` claim with its basis (rated power, current power or absolute); a stated curve or ramp ("derates linearly above 50 °C") is a note on the production-effect claim, never a number. A threshold that triggers the message ("greater than 50 % of rated output") is a condition, not a derate magnitude.
