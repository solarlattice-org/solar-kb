---
id: state:solis-limbyepm
type: OperatingState
name: LimByEPM
aliases:
- Lim by EPM
- limited by EPM
- LimByEMP
- limb by epm
category: Inverters
make: solis
claims:
- claim_id: c1
  rel: subclass_of
  target: state:power-limited
  note: LimByEPM is shown when the inverter output is being limited by the Export Power Manager's export
    (Backflow) limit.
  cite:
  - src: src:kb-solis-44002848827-epm-configuration-and-validation-guide
    loc: sec=h16
    h: 2973ae0d5bcc
  - src: src:solis-soliscloud-monitoring-system-v3-0-organization-20260423
    loc: sec=4.2.3
    h: 835814025d74
  review: drafted
  review_note: 'support check: partial - Passages show LimByEPM displays in the EPM limitation test with
    a Backflow limit set, but don''t explicitly say it''s a power-limited state; the meaning is implied
    only.'
- claim_id: c2
  attr: output_limit
  value:
    nominal: 500
    unit: unit:W
  conditions: 'EPM limitation commissioning test: Backflow (export limit) set to +500 W, after which all
    inverters should display LimByEPM'
  cite:
  - src: src:kb-solis-44002848827-epm-configuration-and-validation-guide
    loc: sec=h16
    h: 2973ae0d5bcc
  review: drafted
---
LimByEPM is an inverter message showing that the inverter's output is being limited by the Export Power Manager (EPM), the external power meter used to control export. The EPM limits the power sent to the grid using the Backflow Power setting, which is the highest export allowed. During commissioning, the EPM limitation test sets a Backflow value and checks that every connected inverter shows LimByEPM. Passing this test is part of the checklist to complete before leaving site. The message can appear when the External EPM fail safe setting is on. Solis notes that it can also appear even when that setting is on as intended. Also check that the Internal EPM Set is OFF. The site checklist also requires the internal EPM functions to be disabled when an external EPM is used. If the message stays after these checks, contact Solis customer support.

<!-- review notes
- sentence 1: support check: partial - The passages link LimByEPM to the EPM limit and external power meter settings, but they never define it as a message showing output is limited by the EPM.
- sentence 4: support check: partial - The passages say the message can occur when the setting is on and even when it is ON, but they don't say 'Solis notes' it as intended behavior; the 'as intended' framing is unsupported.
-->
