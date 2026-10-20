---
id: stressor:humid-climate
type: Stressor
name: Humid climate
aliases:
- Humid subtropical
- Cfa climate zone
- Hot and humid (A-climate)
- Hot and humid climates
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions; may not
    recover after rainfall
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
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
- claim_id: c3
  attr: degradation_rate
  value:
    max: 1
    unit: unit:PERCENT-PER-YR
  conditions: Mean degradation from encapsulant discoloration reported in hot and humid, hot and dry,
    and moderate climate zones
  note: Mean rate stays below this level, so discoloration is seldom the cause of warranty claims.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=3.3.3
    h: 5f7204e75e16
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
A humid climate exposes PV equipment to long periods of high humidity, dew and high surface conductivity, which can trigger hydrolytic degradation of module materials. Moisture that gets into the module, together with acetic acid released when EVA encapsulant hydrolyses, corrodes the cell metallization and causes severe metallization corrosion that shows up as dark areas in EL images. In humid subtropical regions, fungal biofilms grow on module surfaces and cause widespread fungal soiling losses that may not recover after rain. Deep backsheet cracking is often followed by moisture ingress and corrosion, and this happens more often and more severely in hot and humid conditions. Where dissimilar metals touch, such as an aluminium frame on a steel structure, galvanic corrosion forms around fastening screws in humid areas, so the metals should be insulated from each other. Field data from Florida showed modules in a hot, humid subtropical climate degrading almost twice as fast as the same modules at dry or cool sites. To limit losses, include bio-soiling in cleaning schedules and check that cleaning actually restores output, and do not assume rainfall resets the loss. Install modules only within the humidity limits set by the manufacturer; one installation manual specifies below 85 RH%.

<!-- review notes
- sentence 1: support check: partial - Table lists humidity, dew and high surface conductivity as stressors that can induce hydrolytic degradation, but does not link them to humid climates specifically or say 'long periods'.
- sentence 2: support check: partial - Moisture, EVA hydrolysis producing acetic acid, metallization corrosion and EL dark areas are stated, but 'severe' corrosion is not stated and moisture is described as root cause of dark EL areas after long exposure.
- sentence 3: support check: partial - Passages support persistent losses in humid subtropical regions possibly not recovering after rain and mention sub-aerial biofilms, but do not explicitly say fungal biofilms grow on module surfaces (only that biofilms are confirmed by inspection).
- sentence 8: support check: partial - Passage gives humidity < 85RH% as an installation condition, but doesn't state the general 'only within manufacturer limits' principle beyond this one manual, and it doesn't identify the source as one manual's specification explicitly.
-->
