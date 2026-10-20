---
id: mit:cleaning-validation
type: Mitigation
name: Cleaning effectiveness validation
aliases:
- validate cleaning response
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Average annual bio-soiling loss in the humid subtropical climate zone, extrapolated from
    more than 120 cleanings of operational solar farms
  note: Shows how measured cleaning results are used to quantify bio-soiling loss.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h7
    h: e287af93bef3
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions, which may
    not recover after rainfall
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: drafted
---
Cleaning effectiveness validation means checking that a cleaning actually restored production. It is listed as a mitigation for widespread fungal soiling losses, alongside adding bio-soiling to cleaning schedules and updating revenue forecasts. A normalized-production deficit that persists after rain but improves after manual cleaning points to biological soiling rather than ordinary dust. Biological deposits can be patchy, so walk several array areas instead of relying on one representative module. Use close inspection or a handheld microscope when you need to know the type of contaminant. Base forecasts and loss assumptions on site cleaning results rather than assuming rainfall resets the loss. One report put the average annual bio-soiling loss at 5 percent, based on more than 120 cleanings. Validating a cleaning process should also cover damage. Cleaning can scratch the glass or its coatings, and mechanical forces can damage cells, so the effectiveness and destructive effect of a cleaning device should be tested under the plant's own soiling conditions and cleaning frequency. A typical test measures Pmpp, runs electroluminescence and does a visual inspection before and after accelerated cleaning. There is no international pass/fail standard for PV module cleaning.

<!-- review notes
- sentence 1: support check: partial - The mitigation list includes 'validate cleaning response' with bio-soiling in schedules and forecast updates, but the passages don't define it as checking that cleaning restored production (though comparing before/after cleaning is implied).
-->
