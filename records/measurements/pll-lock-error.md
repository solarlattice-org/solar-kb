---
id: meas:pll-lock-error
type: Measurement
name: Phase lock loop error
aliases:
- Phase lock loop failure
- PLL error
signals:
- point: model_103.Hz
  unit: unit:HZ
  pattern: implausible grid frequency reading
- point: model_103.PhVphA
  unit: unit:V
  pattern: implausible phase voltage reading
---
A phase lock loop error is an inverter warning that appears when the inverter cannot synchronize with the grid. While the warning is active, power production is temporarily affected. A common cause is incorrect AC phase rotation: these inverters need an A-B-C positive sequence, and an A-C-B negative sequence keeps them from running. If this error appears, or if the frequency or voltage readings look wrong, check the phase rotation. Swapping any two AC conductors reverses it. If phase rotation is correct, power cycle the inverter. If the warning does not clear, contact technical support. Other inverter families, such as the SGI XTM, report an incorrect phase sequence as a separate fault code.

<!-- review notes
- sentence 3: support check: partial - Passage states A-B-C positive required and A-C-B prevents running, but does not call it a 'common cause' of the PLL error (only says to check it).
- sentence 5: support check: partial - Power cycle then contact support is stated, but the conditional ordering after verifying phase rotation is not stated in the warning row.
- sentence 6: support check: partial - Passage shows a fault 'Incorrect Phase Sequence' code 0020 but does not name the SGI XTM family or contrast with other families in the passage text.
-->
