---
id: method:ir-thermography
type: DetectionMethod
name: Infrared thermography
aliases:
- IRT
- IR imaging
- Thermography
- infrared imaging
- thermal inspection
- infrared inspection
claims:
- claim_id: c1
  rel: produces
  target: meas:ir-hotspot
  note: Hot spots appear as areas much warmer than surrounding normally operating cells; histograms of
    the region become bi- or multi-modal.
  cite:
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.3.1
    h: 4a9513426868
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
  review_note: 'support check: partial - Hot spots as bi-/multi-modal histograms and severe defects (>15
    °C) correlating with reduced string current are stated, but ''much warmer than surrounding normally
    operating cells'' is only loosely supported (multiples of 10 K vs. vicinity).'
- claim_id: c2
  rel: produces
  target: meas:ir-warm-substring
  note: One substring warmer than the others, pointing to a shorted bypass diode, an activated diode or
    an internal short; goes with a lower Voc and lost substring power.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r2
    h: 7f244db9dbab
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h7
    h: 698184845b6b
  review: drafted
  review_note: 'support check: partial - Warmer sub-string, bypass diode SC, internal SC, power loss and
    Voc reduction are in u20, but the ''activated diode'' cause is only in u10 generally and the input-voltage
    signal is not stated.'
- claim_id: c3
  rel: produces
  target: meas:ir-hot-cell
  note: Single heated cells from cell fracture, shunts or broken glass.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  review: drafted
- claim_id: c4
  rel: produces
  target: meas:ir-cold-area
  note: Delamination bubbles were seen as colder areas in aged modules.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
- claim_id: c5
  rel: produces
  target: meas:ir-hot-connection
  note: Resistance heating at connectors or cable interconnections, inspected under load.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=47.r1
    h: c0df59a521bc
  review: drafted
  review_note: 'support check: partial - Connector defects cause resistance heating and IR inspection
    under load is recommended, but IR image of a hot connection is not explicitly stated for cable interconnections
    beyond combiner-box thermal damage.'
- claim_id: c6
  attr: temperature_rise
  value:
    min: 15
    unit: unit:K
  conditions: Severe cell defects in drone-based IR survey of a plant with over ten thousand modules;
    these correlated strongly with reduced string current
  quote: severe cell defects with significant ΔΤ (>15 ο C) strongly correlate with a reduced current
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
  review_note: 'support check: partial - Passage says ΔT >15 °C (above 15) for severe cell defects correlating
    with reduced string current in a plant of over ten thousand modules via aerial IRT; ''drone'' is implied
    by UAV, and strict ''>'' vs ''at least'' is a minor difference.; possible conflict with c7 (same source;
    check the conditions)'
- claim_id: c7
  attr: temperature_rise
  value:
    nominal: 3
    unit: unit:K
  conditions: Cells next to junction boxes compared with the rest of the cell matrix, 2 kWp c-Si installation
    after 12 years of exposure
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: disputed
  review_note: possible conflict with c6 (same source; check the conditions)
  conflicts_with:
  - method:ir-thermography#c8
- claim_id: c8
  attr: temperature_rise
  value:
    min: 10
    unit: unit:K
  conditions: Hot spots compared with normally operating parts nearby, outdoor illuminated thermography
  note: Natural gradients of up to 13 K across a roof plant and 3-5 K within a module must be taken into
    account.
  quote: Multiples of 10 K temperature differences may be reached between hot spots in comparison to the
    normal operating parts
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.3.1
    h: 4a9513426868
  review: disputed
  conflicts_with:
  - method:ir-thermography#c7
---
Infrared thermography is a non-destructive, contactless imaging method. It maps temperature differences across PV modules and can be used on single modules or to scan large plants while they operate. For outdoor work, measure on a sunny, cloudless day with at least 700 W/m2 on the array, ideally with low ambient temperature and low wind. The modules must be in steady state. Keep the viewing angle close to 90 degrees and never below 60 degrees to the glass. Set the correct ambient temperature and emissivity in the camera, and watch for reflections from buildings, clouds or yourself. Comparing images taken at short circuit, open circuit and maximum power point helps tell defects apart. Drone-mounted cameras allow fast surveys of large plants. The method reveals hot spots, hot cells and warm substrings. It can point to bypass diode failure, cell cracks, cell interconnection failure, glass breakage, and overheated connectors, cables or combiner box parts. Not every failure raises temperature, so thermography misses some defects. An open-circuit bypass diode, for example, is hard to see unless the module is strongly mismatched. Combining thermography with electroluminescence imaging finds the most defects. Illuminated thermography works best for crystalline modules, while dark thermography suits thin-film modules. In dark thermography of thin-film modules, keep the injected current below 30 percent above Isc to avoid thermal damage. Inspect connectors with infrared while they are under load, but do visual and tactile checks only after safe isolation.

<!-- review notes
- sentence 8: support check: partial - The 30% Isc limit for thin-film and IR under load with visual/tactile under safe isolation are stated, but the limit is 'Isc not exceeded by more than 30%', and the isolation point is for connectors generally, which fits; minor framing but acceptable.
-->
