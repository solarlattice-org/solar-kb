---
id: symptom:cracked-glass
type: Symptom
name: Cracked front glass
aliases:
- Glass breakage
- Front glass breakage
- Breakage of front glass
- Broken PV module glass
- Shattered (tempered)
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-cell
  note: Damaged front glass often leaves broken cells that show up hot in thermography; tempered glass
    that shatters usually breaks the cells too.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-hotspot
  note: Glass breakage causes hot spots that can overheat the module. Infrared imaging picks up temperature
    anomalies linked to the breakage.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:el-crack-pattern
  note: EL and UV fluorescence can show cell cracks caused by the glass breakage, for example in hail-damaged
    modules.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h7
    h: 9a7ad0612a0a
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: An isolation failure may be the first fault the inverter reports, especially in wet conditions.
    A ground fault and inverter shutdown can follow.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.8
    h: 9bffd3173386
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:string-current-below-average
  note: A module whose glass is completely broken reduces current and power in the whole string.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c6
  attr: time_to_onset
  value:
    max: 9
    unit: unit:MO
  conditions: 'Published case: half of the bifacial 2 mm/2 mm glass/glass modules on rack and tracker
    mounts had broken glass within 9 months of outdoor exposure. Mostly the rear glass broke.'
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.8
    h: 9bffd3173386
  review: drafted
  review_note: 'support check: partial - u8 gives 50% of modules broken within 9 months, with most breaks
    on the rear glass, but it doesn''t say the onset time is ''up to 9 months''. The modules cracked at
    a constant rate over the 9-month test period, so 9 months is the length of the exposure test.'
---
The module glass is cracked in one spot or across the whole module. Tempered glass shatters into small pieces, while annealed glass breaks into large pieces. On non-tempered glass the impact point is easy to find because the glass does not fragment. This helps you tell a surface impact apart from a break that started at the edge. Common causes are hail, stones or other impacts, bad clamps or over-tightened screws, transport damage, and heat from hot spots or arcing. A defective mounting structure can also put extra stress on the glass. Thin glass/glass bifacial modules often crack on the rear glass first, so check the back of the modules as well as the front. Module power often does not drop right away. An inverter isolation or ground fault alarm may be the first sign, especially in wet weather. Visual inspection is the simplest way to find broken glass. IR imaging shows hot spots or hot broken cells, and EL or UV fluorescence shows the cell cracks behind them. Over time, moisture getting in corrodes the cells and circuits. A fully broken module can reduce current in the whole string, so replace modules that pose a safety or insulation risk.

<!-- review notes
- sentence 5: support check: partial - u8 says module power is typically not affected immediately and isolation failure may be a first fault signal at the inverter, and u10 ties insulation loss to wet conditions. Neither passage says the isolation alarm is the first sign especially in wet weather, and the sources say 'isolation failure', not 'ground fault alarm'.
- sentence 6: support check: partial - u20 supports visual inspection as simplest, IR for temperature anomalies, and EL or UV fluorescence for cell cracks. The 'hot broken cells' wording is in u3. The claim that EL or UV fluorescence shows the cracks 'behind' the hot spots is the statement's own framing and is not in the passages.
-->
