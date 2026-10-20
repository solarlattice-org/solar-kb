---
id: symptom:phase-loss
type: Symptom
name: Phase loss
aliases:
- Open Phase Detected
- open AC phase
claims:
- claim_id: c1
  rel: observed_as
  target: meas:open-ac-phase-warning
  note: 'Reported by a central inverter as a warning event (Open Phase Detected) when an open AC phase
    condition is detected. Troubleshooting: measure AC voltage with a CAT III multimeter, then check AC
    fuses or breakers and inspect AC conductors for damage; if no phase loss is found, contact technical
    support.'
  quote: Open AC phase condition has been detected.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r4
    h: 950687df8242
  review: drafted
---
Phase loss means one AC phase at the inverter output is open, and the inverter can flag it as an open phase warning event. First, use a CAT III rated multimeter to measure the AC voltage on each phase and confirm whether a phase is actually missing. If a phase is missing, check every AC fuse and breaker in the output path and look over the AC conductors for damage. If all phases measure normally, the alarm cannot be explained in the field and should be referred to the manufacturer's technical support.

<!-- review notes
- sentence 1: support check: partial - The passage states an open AC phase condition is flagged as a warning, but it does not say the phase is at the inverter output.
- sentence 4: support check: partial - The passage says to contact Technical Support if no phase loss is identified. It does not say the alarm cannot be explained in the field.
-->
