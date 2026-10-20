---
id: symptom:visible-delamination
type: Symptom
name: Visible delamination
aliases:
- Front delamination
claims:
- claim_id: c1
  rel: observed_as
  target: meas:visible-bubbles-milky-areas
  note: Front delamination shows as bubbles or bright, milky areas between glass and encapsulant or cell
    and encapsulant, continuous or in spots; found by visual inspection.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h59
    h: 2b796b8e0a00
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=9.r1
    h: 2b686438798f
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=11.r1
    h: '206639225730'
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:reflectance-increase
  note: New glass/air and EVA/air interfaces add reflection, about 4% interfacial reflectance per interface.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h59
    h: 2b796b8e0a00
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c3
  rel: observed_as
  target: meas:iv-low-isc
  note: Pmax loss from delamination is mainly a short-circuit current reduction from optical loss and
    corrosion.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h59
    h: 2b796b8e0a00
  review: drafted
  review_note: 'support check: partial - Passages say Pmax loss is via reduced Isc from optical loss and
    corrosion, but nothing on IV curve signals, comparison to peer inputs, or declining over time.'
- claim_id: c4
  rel: observed_as
  target: meas:ir-hotspot
  note: Mismatched cells in delaminated areas heat locally; backsheet bubbles may run slightly warmer
    due to disturbed heat dissipation.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
  review_note: 'support check: partial - Mismatch causing local heating in delaminated area and backsheet
    bubbles running slightly warmer are stated, but IR hotspot observation itself isn''t stated.'
- claim_id: c5
  rel: observed_as
  target: meas:high-leakage-current-alarm
  note: Water ingress along a continuous delaminated path can reduce insulation; the inverter may shut
    down due to leakage current.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h59
    h: 2b796b8e0a00
  review: drafted
  review_note: 'support check: partial - Reduced insulation via continuous path/water ingress and inverter
    shutdown from leakage current are stated, but not a leakage-current alarm as an observation.'
- claim_id: c6
  attr: typical_power_loss
  value:
    max: 20
    unit: unit:PERCENT
  conditions: Pmax drop of a field-deployed EFG-Si module with edge delamination and discoloration in
    the first 3 years of deployment
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
  review_note: 'support check: partial - Pmax dropped nearly 20% in first 3 years for the EFG-Si module,
    but ''typical'' and ''up to'' framing is stronger than a single case; also attributed partly to moisture/corrosion.'
- claim_id: c7
  attr: current_drop
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Isc drop of the same EFG-Si module in the first 3 years, approximate figure
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c8
  attr: typical_power_loss
  value:
    nominal: 11.5
    unit: unit:PERCENT
  conditions: PV system after 12 years of exposure, loss mostly attributed to cell/encapsulant delamination
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
---
Delamination shows up as bubbles or bright, milky patches where layers have come apart: front glass from encapsulant, or cell from encapsulant. The patches can be continuous or in spots. It is mainly found by visual inspection. Pulse thermography and scanning acoustic microscopy can also find it without damaging the module. The separated layers reflect more light, so the affected cells make less current. On an IV curve or in string data this shows mostly as lower short-circuit current. Moisture then gets in and causes corrosion, which raises series resistance. The resulting current mismatch can create local heating and trigger bypass diodes. Wavy bumps or ripples on the rear side point to backsheet delamination rather than front delamination. Advanced potential induced degradation can also show visible delamination. Check first whether the delamination reaches the module edge or the junction box. A continuous path there can let water in, lower insulation and cause leakage current trips. Delamination caused in manufacturing often affects many modules from the same batch, so inspect neighbouring modules as well.

<!-- review notes
- sentence 6: support check: partial - Continuous path to edge allowing water ingress, reduced insulation and inverter shutdown from leakage current are stated, but not the 'check first' advice, and junction box concern is only for backsheet delamination.
- sentence 7: support check: partial - Batch-wide effect of manufacturing delamination is stated, but the advice to inspect neighbouring modules is not.
-->
