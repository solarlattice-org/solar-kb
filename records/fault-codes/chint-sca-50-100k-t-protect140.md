---
id: fc:chint-sca-50-100k-t-protect140
type: FaultCode
name: CPS SCA50-100K-T Protect0140
aliases:
- Protect0140
- protect140
- CPS Protect0140
- Over Temp Prot
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0140
code_key: protect140
display_message: Over Temp Prot
vendor_severity: Protection
page: 133
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
  review_note: 'support check: partial - Passage says check whether fan is blocked, but doesn''t state
    the fault affects the fan as a component.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Clears on its own once cooled, observed over 30 minutes; persistent case needs service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
  review_note: 'support check: partial - Passage says observe 30 minutes for automatic clearing, implying
    auto-reset, but ''once cooled'' is not stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:proper-installation
  note: Check the ambient temperature and whether the installation location is suitable.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=51.r1
    h: baf7e0c4219d
  review: drafted
---
