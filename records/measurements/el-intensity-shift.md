---
id: meas:el-intensity-shift
type: Measurement
name: Lower EL intensity distribution
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 8.7
    unit: unit:PERCENT
  conditions: Power loss of the first of two example PV modules whose EL intensity probability density
    functions were compared
  note: Reported with a second module at 14.2 % loss; the module with the higher loss showed the shifted
    EL intensity distribution.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=40
    h: a4eda1a6b11d
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.1.1
    h: 06ce46a9a853
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - The 8.7 % power loss module is stated, but the passages say the
    higher-loss module shifts (to lower intensities/right), and ''Lower EL intensity distribution'' as
    a label for the 8.7 % module is not what the passages state; ''typical'' is also a framing.; possible
    conflict with c2 (same source; check the conditions)'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 14.2
    unit: unit:PERCENT
  conditions: Power loss of the second of two example PV modules whose EL intensity probability density
    functions were compared
  note: The source text says higher-loss modules shift toward lower EL intensities, while the figure caption
    describes the shift as to the right.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=40
    h: a4eda1a6b11d
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=3.1.1
    h: 06ce46a9a853
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions)
---
This signature is found by counting how many pixels in an EL image fall into each intensity range, then turning that histogram into a probability density function of EL intensity. In general, modules with higher power losses have their intensity distribution shifted toward lower EL intensities. The intensity distribution has not yet been clearly correlated with specific types of defect or cell damage, so the shift shows that power has been lost but not why. EL images are taken with the module in forward bias from a DC power supply, ideally in darkness. In the field this usually means at sunset or at night, or under a curtain. PID-p in an n-type TOPCon bifacial module showed a uniform and strong drop in luminescence compared with an undegraded module. The drop was seen at both Isc and 0.1 Isc and did not depend on the bias current. Mean substring EL intensity from aligned images can be tracked over time, for example during damp-heat exposure, as a quantitative measure of degradation.

<!-- review notes
- sentence 3: support check: partial - The text says no clear correlation with specific defect forms has been established, but the claim that the shift shows power has been lost 'but not why' is an interpretation; the conclusions even say EL can ascertain reasons of power loss.
- sentence 5: support check: partial - Uniform significant decrease (~18 times) at Isc and 0.1 Isc with no current dependency is stated, but 'strong drop' is fine while the claim of PID-p in n-type TOPCon bifacial is stated; minor wording like 'did not depend on bias current' matches, though the ~18x figure is omitted.
-->
