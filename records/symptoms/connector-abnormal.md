---
id: symptom:connector-abnormal
type: Symptom
name: Abnormal connector state
aliases:
- Bulkhead Connector Abnormal
- pair plug terminal abnormal
- pair plug terminal warning
- Bulkhead Connector Warning
claims:
- claim_id: c1
  rel: observed_as
  target: meas:visible-burn-marks
  note: A damaged DC connector or cable can look melted, burned, brittle, broken, cracked or whitened.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  - src: src:pv-root-cause-connector-defect
    loc: fig=1
    h: 4e82f7c0b6b2
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-hot-connection
  note: Thermography often shows overheating or hot spots on affected connectors at an early stage.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:connector-contact-corrosion
  note: Corrosion can be seen once the connector is opened.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
---
For the abnormal codes Fault5060 and Fault5070, restart the inverter by switching both the AC and DC switches off, waiting 1 minute so stored energy can discharge, then switching them back on. For the warning codes Fault5080 and Fault5090, check that the AC or DC bulkhead connectors are properly connected. If the alarm comes back after that, call after-sales service. For Fault5100, watch for 5 minutes to see if it clears by itself. If it does, open and re-close both DC switches and restart the inverter. Under safe isolation, inspect the connectors and cables by eye and by touch. A damaged part can look melted, burned, brittle, cracked or whitened, and an opened connector may show corrosion. An infrared scan under load often finds overheating at a failing connector early. Comparing string currents and testing insulation resistance help confirm a connector defect. Connector defects mostly come from installation problems: mismatched connector types forced together, poor crimping, or low-quality parts. Left alone, they can lead to open circuits, ground faults, arcing and fire.
