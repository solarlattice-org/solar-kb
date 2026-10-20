---
id: symptom:abnormal-string-current
type: Symptom
name: Abnormal string current
aliases:
- String x output current anomaly
- PV Abnormal Alarm
claims:
- claim_id: c1
  rel: observed_as
  target: meas:string-performance-ratio-low
  note: Normalized string DC current is compared with the best-performing string on the same component.
    An alert opens when a string stays below the set ratio for the time threshold in daylight hours.
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h2
    h: 4ec2fde2d167
  review: drafted
---
The inverter flags a string whose current is abnormal. On the Sungrow CX-US units, codes 580 to 587 map to strings 17 to 24. In monitoring data, one string's current moves away from the mean of similar strings, or falls well below the best string on the same inverter or combiner. Before comparing strings, normalize for different string sizes and group inputs that share the same shading, orientation and module type. This avoids false alarms. Check first whether the string's modules are shaded or dirty, and clean or remove the obstruction if so. Next, look at the modules for abnormal aging, check for loose wiring, and check whether the DC fuse is blown. A cable defect or a module hotspot can also show up as a string current that does not match its neighbours. Confirm with IR thermography, an IV curve, insulation testing and visual inspection. For a manual check, measure each string with a clip-on ammeter under stable irradiance. Identical strings should read nearly the same. Only open the DC switch to work on a string once its current has fallen below 0.5 A.

<!-- review notes
- sentence 3: support check: partial - Normalization for different string sizes and grouping inputs with same shading/orientation/module type are stated, but the 'avoids false alarms' rationale and 'before comparing' ordering are only loosely supported (grouping/threshold text mentions avoiding erroneous events).
- sentence 6: support check: partial - Cable defect detection via visual, insulation testing, thermal and string current comparison, and IR/IV curve/visual for modules are supported, but the passages do not explicitly say a hotspot or cable defect shows as a mismatched string current, and the combined confirm list is a blend.
- sentence 8: support check: partial - Passages say to disconnect the DC switch when string current is below 0.5 A, but only in specific fault contexts (reverse connection, current reflux, grounding fault); a general 'only' rule for any string work is stronger.
-->
