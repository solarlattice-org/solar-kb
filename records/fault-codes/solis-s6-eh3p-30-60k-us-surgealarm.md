---
id: fc:solis-s6-eh3p-30-60k-us-surgealarm
type: FaultCode
name: Solis S6-EH3P30-60K Surge Alarm
aliases:
- Surge Alarm
- surgealarm
- Solis Surge Alarm
- On-site grid surge
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: Surge Alarm
code_key: surgealarm
display_message: On-site grid surge
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r1
    h: dbaf2768c8dc
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=26.r1
    h: dbaf2768c8dc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-surge
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r1
    h: dbaf2768c8dc
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r1
    h: dbaf2768c8dc
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r1
    h: dbaf2768c8dc
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - The row says ''Grid side fault'', but the name is ''Surge Alarm''
    and device behavior isn''t stated, so a Fault…'
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact manufacturer service if it persists.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r1
    h: dbaf2768c8dc
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r1
    h: dbaf2768c8dc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Restart then contact service is stated, but ''clears by manual
    reset'' is only loosely implied by a restart suggestion.'
---
