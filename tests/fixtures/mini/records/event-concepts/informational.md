---
id: ec:informational
type: EventConcept
name: Informational (status or configuration message)
axis: event_class
aliases: [status, info, information, informational class]
status: active
---
A status, progress or configuration message that reports no abnormal condition: a firmware update started, a parameter was changed, a connection was established.

Reading rule: if the row describes nothing wrong and asks for nothing, the message is informational. If it asks the reader to check or do something, it is a warning or a fault.
