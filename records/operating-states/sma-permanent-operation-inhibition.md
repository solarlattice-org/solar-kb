---
id: state:sma-permanent-operation-inhibition
type: OperatingState
name: Permanent operation inhibition
aliases:
- Permanent Disable Mode
category: Inverters
make: sma
claims:
- claim_id: c1
  rel: subclass_of
  target: state:stopped
  note: The device stops operating and does not restart on its own until it is reset or, in the case of
    a device defect, replaced.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=141.r5
    h: 81d8515bee83
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h45
    h: c0c528d6a6bd
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages say the device switches off and doesn''t switch on again
    and must be replaced for a defect, but the ''until reset'' and the ''Stopped state'' classification
    are only partly shown (event 9102 implies a reset via Start).'
---
Permanent operation inhibition means the device has stopped operating and will not start again on its own. On a Sunny Island battery inverter, event 9102 reports it, and it means charging and discharging have been interrupted permanently. To clear it, set the Operating mode parameter to Start. If arc-fault detection is set to the mode with permanent operation inhibition, the inverter stops to interrupt the arc. It then waits for a manual reset before it runs again. To reset the inhibition, go to Device > Operation, set Reset operating data to Reset operation inhibition, and then start the system. If arc-fault detection is instead set to run without permanent operation inhibition, the inverter restarts by itself after about 10 minutes and checks whether the arc is still there. When the Sunny Island shows Defect at level 5, the permanent inhibition comes from a device defect, and the device has to be replaced. Some inverters, such as the Sunny Boy Smart Energy, report this condition as an event message.

<!-- review notes
- sentence 2: support check: partial - Event 9102 meaning and the corrective measure are stated, but the passage doesn't name Sunny Island explicitly (u1 mentions it only indirectly); 'clear it' is paraphrase of corrective measure.
- sentence 7: support check: partial - The passage shows an event message 'Permanent operation inhibition' but doesn't mention Sunny Boy Smart Energy in the text shown.
- sentence 7: review: partial - The passage does show 'Permanent operation inhibition' as an event message, but its text never names the Sunny Boy Smart Energy.
-->
