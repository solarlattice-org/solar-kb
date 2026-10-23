---
id: fc:solis-s6-gu-ehv-us-pidrepairing
type: FaultCode
name: Solis S6-GU PID Repairing
aliases:
- PID Repairing
- pidrepairing
- Solis PID Repairing
- Inverter logic fault
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: PID Repairing
code_key: pidrepairing
display_message: Inverter logic fault
page: 48
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Causes given as DSP firmware fault or rapid shutdown fault.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
  review_note: 'support check: partial - DSP FW fault is a cause and the DSP version is checked, but the
    DSP is not stated as the…'
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
  review_note: 'support check: partial - Checking DC voltages at the terminals is a solution step, not
    clearly a detection method for this fault.'
- claim_id: c5
  rel: detected_by
  target: method:inverter-display-check
  note: Firmware version read on display; version 00 indicates fault.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: When DSP firmware version reads 00.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
  review_note: 'support check: partial - Replacement is offered, but only conditional on DSP version reading
    00 (and as an alternative to contacting service).'
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r7
    h: 16ab28c62001
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r7
    h: 16ab28c62001
  review: drafted
  review_note: 'support check: partial - Described as ''Inverter logic fault'' needing service/replacement,
    implying a fault, but not explicitly classed; plausible.'
---
