---
id: symptom:battery-deep-discharge
type: Symptom
name: Battery deep discharge protection
aliases:
- Deep discharge protection activated
- Battery fault
- BatRes
claims:
- claim_id: c1
  rel: observed_as
  target: meas:deep-discharge-event-message
  note: Event 9394 'Deep discharge protection activated' is logged when the battery management system
    enables deep discharge protection; on grid-connected systems it is an event, not a warning.
  quote: The battery management system has activated the deep discharge protection.
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h80
    h: 37a9c5d405bc
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h64
    h: 37a9c5d405bc
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h72
    h: 37a9c5d405bc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h805
    h: 4535b16cf07b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h806
    h: 0aebb35044f4
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: A related SMA 'Battery fault' message appears when the deep discharge protection area or deep
    discharge area is reached; a fuse at the grid-connection point may have tripped.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h814
    h: c3887cb0a48f
  review: drafted
---
On SMA battery inverters, event 9394 is logged when the battery management system turns on deep discharge protection. For grid-connected systems this message is only an event and not a warning. A related battery fault message means the battery has reached either the deep discharge protection area or the deep discharge area, and a fuse at the grid-connection point may have tripped. Inside the deep discharge protection range, the system switches to energy-saving mode and tries to recharge the battery automatically from available PV energy. The protection ranges are set as a percentage of battery capacity, and the allowed limits differ between lead-acid and lithium-ion batteries. Check first whether a fuse has tripped at the grid-connection point and whether PV energy is available to recharge the battery. Then review the deep discharge range settings for the battery type.

<!-- review notes
- sentence 6: support check: partial - The fuse and PV recharge facts appear, but the passages give no troubleshooting order or instruction to check them or review settings by battery type.
-->
