---
id: mit:low-lid-modules
type: Mitigation
name: Low-LID module selection
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Classic LID in c-Si modules, occurring in the first days of sun exposure
  note: The loss that low-LID module selection is meant to avoid; mostly p-type multi and mono modules
    are affected.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in susceptible modules (first seen with PERC), at module temperatures above 50 °C,
    on top of the LID loss
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 1
    max: 4
    unit: unit:PERCENT
  conditions: Remaining LeTID degradation in modules whose manufacturers mitigate it; the figure depends
    on the manufacturer's method
  note: Shows that mitigation reduces the loss but does not remove it, and results differ between manufacturers.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light soaking or LID effects in general, depending on technology
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage says LID/light soaking could entail losses up to 30%,
    but doesn''t tie it to low-LID module selection or technology dependence explicitly; ''could potentially''
    is a bound.'
---
Choosing module technologies with low susceptibility to light-induced loss, where relevant, is one of the listed mitigations for Light Induced Degradation (LID). Classic LID comes from boron-oxygen complexes. It was strongest in Czochralski-grown p-type mono cells, and mainly p-type multi and mono modules are affected. Gallium-doped p-type cells and n-type cells such as n-type PERC, HJT or n-PERT are affected much less or not at all, so these are the usual low-LID choices. When buying, check that the manufacturer uses LeTID-stable cells, verify the cell type in the bill of materials, and ask for test reports that state the percent power loss. Standard test procedures exist to check LID and LeTID behaviour, including for new technologies. Limits: LID can still appear in gallium-doped and n-type cells because of boron impurities in the wafer, and LeTID results after mitigation still differ between manufacturers. Even with low-LID modules, include stabilization losses in yield assumptions and confirm unexpected early losses with IV and flash testing.

<!-- review notes
- sentence 3: support check: partial - Passages say Ga p-type and n-type (PERC, HJT, n-PERT) are much less/not affected, but 'usual low-LID choices' is an inference; also LID can still occur.
- sentence 7: support check: partial - Passage advises accounting for stabilization in yield assumptions and verifying early losses with IV and flash testing, but doesn't say this applies 'even with' low-LID modules (it lists it alongside selecting them).
-->
