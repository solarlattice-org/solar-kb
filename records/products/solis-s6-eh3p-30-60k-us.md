---
id: prod:solis-s6-eh3p-30-60k-us
type: Product
name: Solis S6-EH3P(30-60)K-NV-YD-H-US
aliases:
- S6-EH3P30K03-NV-YD-H-US
- S6-EH3P40K04-NV-YD-H-US
- S6-EH3P50K04-NV-YD-H-US
- S6-EH3P60K04-NV-YD-H-US
- S6-EH3P30K03-LV-YD-H-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=front
    h: 65d0ffd891c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=front
    h: 65d0ffd891c8
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: fig=80
    h: 8cd412c25b79
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described as a Solis hybrid inverter.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: fig=80
    h: 8cd412c25b79
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: fig=80
    h: 8cd412c25b79
  review: drafted
- claim_id: c3
  rel: implements
  target: func:dc-arc-fault-protection
  note: Datasheet lists integrated AFCI as Yes for the 40K04 model; an AFCI self-test failure message
    (AFCI-Check) is defined.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=31.r46
    h: b9cbf8ae2d2c
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=31.r46
    h: b9cbf8ae2d2c
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r3
    h: 9662b1a38062
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=29.r3
    h: 9662b1a38062
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:can-bus
  note: CAN communication between inverter and battery; loss raises a CAN Fail alarm.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=h352
    h: fa95d55eedef
  review: drafted
- claim_id: c5
  rel: implements
  target: func:dc-injection-limitation
  note: DCInj-FAULT is raised when the DC component of output current exceeds the limit.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r1
    h: 343ddc0a98d9
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r1
    h: 343ddc0a98d9
  review: drafted
  review_note: 'support check: partial - DCInj-FAULT is raised when DC component exceeds limit, but passages
    don''t explicitly state the inverter implements DC injection limitation (though implied); the core
    is present.'
---
The Solis S6-EH3P(30-60)K-NV-YD-H-US is a family of three-phase hybrid inverters made by Solis for the US market. The family includes the 30K03 LV and NV models and the 40K04, 50K04 and 60K04 NV models, all with the (21A) suffix. The datasheet lists integrated AFCI for the 40K04 model, and the inverter reports an AFCI-Check message if its arc-fault self-test fails. The inverter talks to the battery over CAN. A CAN Fail alarm means that link is lost, so check the CAN cable and make sure the battery is powered on. A BatName-FAIL alarm means the battery model chosen under Battery Setting does not match the battery nameplate. The inverter raises DCInj-FAULT when the DC component of its output current is over the limit. Check the grid and the AC cabling, then restart. The 12Power-FAULT message means a 12V undervoltage failure; start by checking grounding and looking for current leaking to ground.

<!-- review notes
- sentence 1: support check: partial - Three-phase hybrid inverters by Solis are supported by the model names and title, but 'US market' is only implied by the -US suffix and 'three-phase' by EH3P naming, not stated.
- sentence 1: review: partial - The passages back a Solis hybrid inverter family with these models, but 'three-phase' and 'for the US market' are not stated and are only suggested by the model naming.
-->
