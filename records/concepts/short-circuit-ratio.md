---
id: concept:short-circuit-ratio
type: Concept
name: Short-circuit ratio
aliases:
- SCR
- weak grid
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: explains
  target: fm:inverter-grid-resonance
  note: At very low SCR, the combined impedances of the inverters, transformer and grid can cause resonance
    on the AC voltage waveform.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:grid-impedance
  note: Grid short-circuit power at the MV connection is used to calculate grid impedance on the LV side
    of the transformer.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h83
    h: 3b7ebc798d24
  review: drafted
  review_note: 'support check: partial - u32 uses grid short-circuit power to compute LV-side grid impedance,
    but the passages don''t explicitly tie SCR itself to grid impedance.'
- claim_id: c3
  rel: related_to
  target: concept:point-of-interconnection
  note: Configuration tables give SCR as measured at the point of interconnection (POI).
  cite:
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=4.r1
    h: 3cdd438fcc23
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=3.r1
    h: 4ad59069af20
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=5.r1
    h: 9bc470babdfa
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  review: drafted
- claim_id: c4
  rel: related_to
  target: mit:inverter-count-limit
  note: Where grid SCR is very low, fewer inverters may be connected at one shared POI.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  review: drafted
- claim_id: c5
  rel: related_to
  target: stressor:low-grid-scr
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  rel: related_to
  target: prod:yaskawa-solectria-xgi-1500
  note: The manufacturer publishes configuration limits for SCR scenarios from 2.0 to 6.0.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=4.r1
    h: 3cdd438fcc23
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=3.r1
    h: 4ad59069af20
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=5.r1
    h: 9bc470babdfa
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: prod:sma-sunny-central-up-us
  note: The datasheet gives a minimum short-circuit ratio of greater than 2 at the AC terminals.
  cite:
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=175.r16
    h: 42615f004913
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=186.r5
    h: 42615f004913
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=179.r22
    h: 42615f004913
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=181.r8
    h: 42615f004913
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=177.r3
    h: 42615f004913
  - src: src:eq-equip-inverters-sma-sc-2660up-us-sc-up-us-be-en-14
    loc: tbl=183.r18
    h: 42615f004913
  review: drafted
---
The short-circuit ratio (SCR) is a figure for how strong the grid is where an inverter plant connects. It is usually stated at the point of interconnection or at the inverter AC terminals. At very low SCR values, the impedances of the inverters, the transformer and the grid can combine to cause resonance on the AC voltage waveform. If the resonance gets strong enough, an inverter such as the XGI 1500 sees the grid voltage as too high and shuts down safely. To prevent this, the manufacturer limits how many inverters can share one point of interconnection on a weak grid. Its configuration tables cover SCR scenarios from 2.0 to 6.0. Some central inverter datasheets give a minimum short-circuit ratio at the AC terminals. For the SMA Sunny Central UP-US it is greater than 2. SCR is closely tied to grid impedance: the short-circuit power available from the grid at the medium-voltage connection is used to work out the grid impedance on the low-voltage side of the transformer.

<!-- review notes
- sentence 1: support check: partial - The passages show SCR stated at the POI and at AC terminals, but never define SCR as a measure of grid strength.
- sentence 5: support check: partial - The >2 minimum SCR at the AC terminals is stated, but the passages don't name the model as SMA Sunny Central UP-US or say it is a feature of some central inverters.
- sentence 6: support check: partial - u32 shows grid short-circuit power at the MV connection used to compute LV-side grid impedance, but it doesn't mention SCR or say they are closely tied.
- sentence 1: review: partial - The passages show SCR stated at the POI and at the AC terminals, but they never describe SCR as a measure of grid strength.
-->
