---
id: fm:cell-cracks
type: FailureMode
name: Cell Cracks
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Wafer slicing, cell production, stringing (soldering residual stress) and embedding can start
    cracks; repetitive crack patterns point to production faults.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h4
    h: 9ddd690f2930
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:transport-damage
  note: Poor packaging, vibration and reloading during transport induce cracks.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h4
    h: 9ddd690f2930
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:installation-error
  note: Dropping modules or stepping on them during installation.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h4
    h: 9ddd690f2930
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:mechanical-stress
  note: Hail, wind and snow loads; dendritic crack patterns indicate heavy mechanical load after lamination.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h4
    h: 9ddd690f2930
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:thermal-cycling
  note: Temperature variations and uneven thermal expansion grow short cracks into longer, wider ones.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h4
    h: 9ddd690f2930
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:solar-cell
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:el-dark-lines
  note: An abrupt EL intensity change at the dark grey line confirms a crack rather than a crystal defect.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.4
    h: 1fb2586fa36b
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:snail-tracks
  note: Discoloured silver gridlines along cracks, typically 3 months to 1 year after installation.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=10
    h: f95eb9235f8d
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:encapsulant-photobleaching
  note: Bleached lines in yellowed encapsulant along cracks and cell borders.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=10
    h: f95eb9235f8d
  review: drafted
  review_note: 'support check: partial - Photobleaching along cracks and cell borders is stated, but ''bleached
    lines'' appearance is only loosely implied.'
- claim_id: c10
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: When the cracked cell is driven into reverse bias.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:burn-marks
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:isc-reduction
  note: Isolated cell area no longer generates current; current reduction is the main loss contributor.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:series-resistance-increase
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:fill-factor-reduction
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:substring-loss
  note: Large inactive areas activate the bypass diode of the affected substring.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:el-imaging
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.4
    h: 1fb2586fa36b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  review: drafted
- claim_id: c17
  rel: detected_by
  target: method:uv-fluorescence
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:photoluminescence
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:ir-thermography
  note: Shows cracked cells only when they heat up under reverse bias.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:visual-inspection
  note: Usually only works once snail tracks, photobleaching or delamination appear, or for large cracks.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h8
    h: ec36b7bfbdb3
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:proper-installation
  note: Avoid mechanical stress during transport and installation.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:close-monitoring
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:module-replacement
  note: For confirmed severe inactive area or hotspot risk.
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=front
    h: a37d82d92ad0
  review: drafted
- claim_id: c25
  rel: mitigated_by
  target: mit:multi-busbar-cells
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: drafted
- claim_id: c26
  rel: leads_to
  target: fm:module-hotspot
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: drafted
- claim_id: c27
  rel: leads_to
  target: fm:delamination
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h7
    h: 8b69da4daaac
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r1
    h: 790734be7823
  review: drafted
- claim_id: c28
  attr: typical_power_loss
  value:
    max: 2.5
    unit: unit:PERCENT
  conditions: Every cell in a 60-cell module cracked but with no electrically separated cell area, at
    STC
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: disputed
  review_note: 'support check: partial - Passages say ''typically below 2.5%'' (an upper bound), not a
    typical value of 2.5%.; possible conflict with c34 (same source; check the conditions)'
  conflicts_with:
  - fm:cell-cracks#c32
  - fm:cell-cracks#c33
  - fm:cell-cracks#c35
- claim_id: c29
  attr: typical_power_loss
  value:
    max: 2.5
    unit: unit:PERCENT
  conditions: Loss from increased recombination current caused by cracks
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  review_note: 'support check: partial - Recombination effect ''remains under 2.5%'' is an upper bound,
    not a typical 2.5% value.; possible conflict with c32 (same source; check the conditions); possible
    conflict with c33 (same source; check the conditions)'
  conflicts_with:
  - fm:cell-cracks#c34
  - fm:cell-cracks#c35
- claim_id: c30
  attr: typical_power_loss
  value:
    nominal: 0.2
    unit: unit:PERCENT
  conditions: Per dendritic-like cracked half-cell in multi-wire PERC modules
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: disputed
  conflicts_with:
  - fm:cell-cracks#c32
  - fm:cell-cracks#c33
  - fm:cell-cracks#c34
  - fm:cell-cracks#c35
- claim_id: c31
  attr: typical_power_loss
  value:
    nominal: 0.2
    unit: unit:PERCENT
  conditions: Simulation, one cell with 5% inactive area
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  review_note: possible conflict with c32 (same source; check the conditions); possible conflict with
    c33 (same source; check the conditions)
  conflicts_with:
  - fm:cell-cracks#c34
  - fm:cell-cracks#c35
- claim_id: c32
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Simulation, one cell with 15% inactive area
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  conflicts_with:
  - fm:cell-cracks#c28
  - fm:cell-cracks#c30
  - fm:cell-cracks#c34
  - fm:cell-cracks#c35
  review_note: possible conflict with c29 (same source; check the conditions); possible conflict with
    c31 (same source; check the conditions); possible conflict with c33 (same source; check the conditions)
- claim_id: c33
  attr: typical_power_loss
  value:
    nominal: 35
    unit: unit:PERCENT
  conditions: Simulation, one cell with 45% inactive area, bypass diode of substring activated
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  conflicts_with:
  - fm:cell-cracks#c28
  - fm:cell-cracks#c30
  - fm:cell-cracks#c34
  review_note: possible conflict with c29 (same source; check the conditions); possible conflict with
    c31 (same source; check the conditions); possible conflict with c32 (same source; check the conditions)
- claim_id: c34
  attr: typical_power_loss
  value:
    nominal: 12
    unit: unit:PERCENT
  conditions: Simulated mean string loss after complete isolation of all cracked cell parts, medium crack
    occurrence
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: disputed
  review_note: possible conflict with c28 (same source; check the conditions)
  conflicts_with:
  - fm:cell-cracks#c29
  - fm:cell-cracks#c30
  - fm:cell-cracks#c31
  - fm:cell-cracks#c32
  - fm:cell-cracks#c33
- claim_id: c35
  attr: typical_power_loss
  value:
    min: 10
    unit: unit:PERCENT
  conditions: Nearly half of 159 modules in one solar park after 6 years of operation
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.2
    h: 17668c52ed6f
  review: disputed
  conflicts_with:
  - fm:cell-cracks#c28
  - fm:cell-cracks#c29
  - fm:cell-cracks#c30
  - fm:cell-cracks#c31
  - fm:cell-cracks#c32
- claim_id: c36
  attr: degradation_rate
  value:
    max: 3
    unit: unit:PERCENT-PER-YR
  conditions: All climate zones except cold and snowy
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: drafted
  review_note: 'support check: partial - Source says below 3% per year, an upper bound, not a rate of
    3%.; possible conflict with c37 (same source; check the conditions)'
- claim_id: c37
  attr: degradation_rate
  value:
    nominal: 8
    unit: unit:PERCENT-PER-YR
  conditions: Affected part in cold and snowy climate zones
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h6
    h: 020d995c9f1f
  review: disputed
  review_note: possible conflict with c36 (same source; check the conditions)
  conflicts_with:
  - fm:cell-cracks#c38
- claim_id: c38
  attr: degradation_rate
  value:
    max: 7
    unit: unit:PERCENT-PER-YR
  conditions: Mean rate for full-cell modules in cold and snow climate zones
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=7.r5
    h: 0a21fb8dc566
  review: disputed
  review_note: 'support check: partial - Source says ''up to 7%/y'', a high bound on mean rates, not a
    typical 7%.'
  conflicts_with:
  - fm:cell-cracks#c37
- claim_id: c39
  attr: time_to_onset
  value:
    min: 1
    max: 2
    unit: unit:YR
  conditions: Cell cracks dominate early failures in the first two years after installation
  cite:
  - src: src:pv-root-cause-cell-cracks
    loc: sec=h5
    h: 451648d48890
  review: drafted
  review_note: 'support check: partial - Cell cracks dominate early failures in years one and two, but
    the range is stated as years rather than an onset time.'
---
Cell cracks are breaks in the brittle silicon of the solar cells and are usually invisible to the naked eye. They start in manufacturing, transport and installation, for example when a module is dropped or stepped on, and grow under wind, snow, hail and temperature changes. Most cracks cost little power, but cracks that isolate part of a cell reduce current, can switch on the bypass diode and can create hotspots and burn marks. In the field, look for snail tracks or bleached lines along cracks, which make small cracks visible. Confirm with electroluminescence imaging, where cracks show as dark lines; UV fluorescence also works, and infrared thermography shows cracked cells that are heating. Use IV curves to judge the electrical impact. Handle modules carefully during transport and installation, monitor cracked modules for progression, and replace those with severe inactive areas or hotspot risk.
