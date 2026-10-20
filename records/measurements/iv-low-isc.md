---
id: meas:iv-low-isc
type: Measurement
name: Lowered Isc on IV curve
aliases:
- case S1
- decrease of Isc
signals:
- point: model_160.DCA
  unit: unit:A
  pattern: slow, long-term decline in irradiance-normalized string current
- point: model_502.A
  unit: unit:A
  pattern: affected modules show lower current than neighbours at the same irradiance
- point: model_403.InDCA
  unit: unit:A
  pattern: affected string current below peer strings
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Power loss from delamination, one of the failures that lowers Isc; reported as a limited-loss
    failure
  note: Applies to fm:delamination
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 3
    unit: unit:PERCENT
  conditions: Power loss from glass corrosion, one of the failures that lowers Isc
  note: Applies to fm:glass-corrosion-abrasion
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
---
This signature is a short-circuit current on the IV curve that is lower than expected. The expected value can come from the cell area, technology and layout, from the label or flash report, or from an earlier curve measured under comparable conditions. Isc mainly reflects optical influences, so a low Isc points to light not reaching the cells, and the effect resembles a reduction in irradiance. Typical causes are loss of encapsulant transparency from yellowing or browning, glass corrosion, and delamination that optically uncouples the layers. Uniform cases lower Isc and Pmax only. Non-uniform cases also give a sloped region near Isc and steps in the curve. Severe metallization corrosion lowers Isc together with fill factor, because series resistance rises. Light-induced degradation lowers Isc, fill factor and Voc. In bifacial PERC and TOPCon modules affected by PID-p, STC IV curves have shown a significant drop in Isc but no noticeable drop in shunt resistance. String Isc can be taken from an IV curve trace on an isolated string. Before reading a deviation as a fault, check for measurement errors, instrument set-up problems, wrongly entered module data, shading and soiling.

<!-- review notes
- sentence 5: support check: partial - Corrosion lowering Isc and FF via Rs and LID lowering Isc, FF, Voc are stated, but 'severe' metallization corrosion is not specified (passage just says corrosion).
-->
