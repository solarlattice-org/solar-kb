---
id: ec:fault
type: EventConcept
name: Fault (device stops or needs intervention)
axis: event_class
aliases: [protection, critical, error, fault class]
status: active
---
The message reports a condition on which the device stops or needs someone to intervene. Vendor words that read as this class: Chint *Protection* and *Fault*, Yaskawa Solectria *Critical*, SMA events that interrupt feed-in.

Reading rule: classify by what the row says the device does, not by the vendor's word. The vendor's word is kept as written in the code's `vendor_severity`; this concept only says the message is a fault rather than a warning or a status.
