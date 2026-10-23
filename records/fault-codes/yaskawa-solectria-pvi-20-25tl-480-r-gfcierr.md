---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-gfcierr
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R GFCI.Err
aliases:
- GFCI.Err
- gfcierr
- Yaskawa Solectria GFCI.Err
- leakage current high
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: GFCI.Err
code_key: gfcierr
display_message: leakage current high
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r5
    h: 966dd7a51877
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14
    h: 09849534a48f
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r5
    h: 966dd7a51877
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14
    h: 09849534a48f
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r5
    h: 966dd7a51877
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  note: String-by-string isolation to find the leaking string.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r5
    h: 966dd7a51877
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r1
    h: f0a8ea15b675
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r2
    h: bcea6533f17c
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Watch for automatic clearing first; then installer ground fault check; then service.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r3
    h: 56ce51f2493f
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14
    h: 09849534a48f
  review: drafted
---
