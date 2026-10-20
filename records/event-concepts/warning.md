---
id: ec:warning
type: EventConcept
name: Warning (device continues, a condition is flagged)
axis: event_class
aliases: [alarm, warn, warning class]
status: active
---
The device keeps running and flags a condition that deserves attention. Vendor words that read as this class: Chint *Warning* and *Alarm*, Yaskawa Solectria *Warning*, SMA events that say the device continues to feed in.

Reading rule: manuals do not separate *alarm* from *warning* consistently (a Chint Alarm continues, a Sungrow alarm may stop), so both read as this class when the device continues; the vendor's word survives in `vendor_severity`. A message on which the device stops is a fault even when the vendor calls it an alarm.
