---
id: fc:solis-s6-gc-us-boostfal
type: FaultCode
name: Solis S6-GC BoostFal
aliases:
- BoostFal
- boostfal
- Solis BoostFal
- DC Boost converter fault
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: BoostFal
code_key: boostfal
display_message: DC Boost converter fault
page: 75
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  review: drafted
  review_note: 'support check: partial - The passages give a DC boost converter circuit fault but do not
    use ''power stage''.'
- claim_id: c3
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; replace inverter if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r3
    h: 1a26213be321
  review: drafted
  review_note: 'support check: partial - Restart then replace is stated, but the passages never say it
    clears by manual reset specifically.'
- claim_id: c8
  rel: applies_to
  target: prod:solis-s6-gc-us
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r3
    h: 1a26213be321
  review: drafted
---
