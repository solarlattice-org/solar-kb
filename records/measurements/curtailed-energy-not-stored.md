---
id: meas:curtailed-energy-not-stored
type: Measurement
name: Curtailed energy not stored
---
In PV-plus-storage plants, curtailment turns available solar resource into energy that goes unused. A DC-coupled or AC-coupled battery can recover part of that energy by charging. The battery can only capture curtailed energy if it has spare capacity, power headroom and control permission, and if its operating objective values the charge. Once the battery reaches its Maximum Off-Grid state-of-energy setting, it stops charging and solar output is curtailed. The Maximum Off-Grid state-of-energy setpoint is a controller parameter that can be read and written, so check it during a battery charging review. This pattern belongs to grid curtailment yield losses. A low performance ratio during curtailed hours may reflect grid instructions rather than a module, inverter or tracker problem.

<!-- review notes
- sentence 4: support check: partial - The parameter is shown as R/W, but nothing in the passages says to check it during a battery charging review.
- sentence 5: support check: partial - The low PR vs grid instructions point is stated, but the passage doesn't classify the pattern as 'grid curtailment yield losses' beyond the Loss Mechanisms heading about curtailment.
-->
