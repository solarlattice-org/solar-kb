---
id: fc:yaskawa-solectria-sgi-500-750xtm-shunttrip
type: FaultCode
name: Yaskawa Solectria SGI-XTM Shunt Trip
aliases:
- Shunt Trip
- shunttrip
- Yaskawa Solectria Shunt Trip
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Shunt Trip
code_key: shunttrip
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
  review_note: 'support check: partial - Critical messages are displayed as errors, but the row does not
    state whether the device stops; the fault class is…'
- claim_id: c3
  rel: reports
  target: symptom:remote-shutdown
  note: external command to open the AC breaker
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-disconnect
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: restart after trip command removed; persistent cases escalate to authorized service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r10
    h: 0ecbb686b049
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
---
