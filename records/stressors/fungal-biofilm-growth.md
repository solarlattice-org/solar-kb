---
id: stressor:fungal-biofilm-growth
type: Stressor
name: Fungal biofilm growth
aliases:
- bio-soiling
- fungal bio-soiling
- sub-aerial biofilms
- biological soiling
- persistent bio-soiling
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production losses from fungal bio-soiling in humid subtropical regions; found
    at North Carolina solar farms in 2024 field work, recoverable only by manual cleaning
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Average annual bio-soiling loss in the humid subtropical (Cfa) climate zone, extrapolated
    from more than 120 cleanings of operating solar farms
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h7
    h: e287af93bef3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Fungal biofilm growth means colonies of microbes, mainly black fungi, growing in sub-aerial biofilms on the module front glass. As the biofilm grows it forms dark masses and catches other particles. This absorbs and scatters incoming light and cuts how much passes through the glass. The biofilm can also pit and etch the glass and give more dust a surface to stick to, so soiling builds up further. The main failure mode it causes is widespread fungal soiling losses. Unlike ordinary dust, these losses often stay after rain and can be mistaken for pollen, dust or a weather-normalization error. Growth is most likely in humid places, such as tropical and humid subtropical climates. Condensation from big swings between day and night temperatures supplies the water the biofilm needs. Expect it to recur at sites with a humid climate, nearby vegetation or nearby water. Usually only targeted or manual cleaning removes the deposits, and some studies suggest adding an anti-fungal agent to the cleaning routine. Treat cleaning as required maintenance at affected sites and check production after each cleaning to confirm it worked.

<!-- review notes
- sentence 4: support check: partial - Persistence after rain and misclassification as dust, pollen or weather-normalization error are stated, but 'main failure mode' is only loosely supported.
- sentence 5: support check: partial - High humidity/tropical and condensation from day-night temperature swings are stated (São Paulo example), but humid subtropical as likely growth region is supported only via the field findings, and condensation is an example not a general rule.
-->
