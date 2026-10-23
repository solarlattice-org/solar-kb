---
id: fc:canadian-solar-23-28ktl-ct-pv12reverse
type: FaultCode
name: Canadian Solar 23-28KTL-CT PV1 (2) Reverse
aliases:
- PV1 (2) Reverse
- pv12reverse
- Canadian Solar PV1 (2) Reverse
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 23-28ktl-ct
family_name: CSI 23/28KTL-CT/US-480
code: PV1 (2) Reverse
code_key: pv12reverse
vendor_severity: Protection
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-23-28ktl-ct-inverter-installation-manual
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
  review_note: 'support check: partial - The row identifies reversed polarity and says to check it, but
    does not state detection by a polarity measurement.'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=30.r2
    h: c58068a3df81
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=7.1.2
    h: 796c028bf931
  review: drafted
  review_note: 'support check: partial - The general text says the inverter shuts down on faults, but
    the row does not state production stops for this code.'
---
