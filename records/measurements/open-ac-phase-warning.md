---
id: meas:open-ac-phase-warning
type: Measurement
name: Open AC phase warning
aliases:
- Open Phase Detected
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: one AC phase voltage missing or abnormal compared with the other phases
---
This is an inverter warning, shown as warning event code 4, that reports an open AC phase on the grid side. It is a warning-class event in the inverter event list, separate from the critical events such as an AC contactor failure. To confirm it, measure the AC voltage on each phase with a CAT III multimeter. If one phase has no voltage, check all AC fuses and breakers and look for damage on the AC conductors. If the meter shows no phase loss, the warning may not reflect a real field condition, and the manual says to contact the manufacturer's technical support.

<!-- review notes
- sentence 1: support check: partial - Warning code 4 'Open Phase Detected' with open AC phase condition is stated, but 'grid side' is not mentioned.
- sentence 3: support check: partial - Passage says use a CAT III multimeter to verify AC voltage, but doesn't say to measure on each phase explicitly.
- sentence 4: support check: partial - Check AC fuses/breakers and inspect conductors for damage on phase loss are stated; 'one phase has no voltage' is a paraphrase of phase loss, fairly close but specific wording is not stated.
- sentence 5: support check: partial - Contact Technical Support if no phase loss is stated, but the claim that the warning may not reflect a real field condition is an inference not in the passage.
-->
