---
id: symptom:hotspot-ir-image
type: Symptom
name: Hotspot in IR image
aliases:
- hot spots
- thermal abnormalities
- thermal anomaly
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hotspot
  note: Localized heating during loaded operation; linked to poor solder joints, cracked cells, poor connections
    or severe mismatch inside a module.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h13
    h: fd7deb3c6e41
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-hot-cell
  note: Broken front glass often leaves broken hot cells in the damaged module; cracked cells also show
    as hot cells.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.1
    h: 767c056a514a
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:ir-warm-substring
  note: Inactive substrings or modules look warmer than active parts, but the difference is small and
    grows with irradiance, so low-irradiance scans can miss it.
  cite:
  - src: src:pv-root-cause-module-hotspot
    loc: sec=h4
    h: a46a7d318434
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h13
    h: fd7deb3c6e41
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h54
    h: e6e5453ce084
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: observed_as
  target: meas:ir-hot-connection
  note: Covers junction box terminals with loose internal connections, overheated DC connectors, cables
    and fuse clamps.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=7
    h: eb7dd22abf25
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.1.6
    h: 50d53aeafc51
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=5
    h: fc0f2dc6c73f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
A hotspot is a part of a module, connection or other component that shows up hotter than its surroundings in an infrared image taken while the system is under load. Scan in clear, stable weather with high irradiance and the inverter running. Avoid reflections from clouds and nearby objects, then compare the module with its neighbours in the same string. A hot cell or a hot localized area points to cracked cells, broken front glass, solder bond or cell interconnection faults, or mismatch that forces cells into reverse bias. Hot junction box terminals, connectors, cables or fuse clamps usually mean a loose or poor electrical connection, not a fault in the cells. A warm substring or a heated bypass diode suggests the diode is conducting. Check first for shading or debris on that module, and suspect a bad module or a shorted diode if none is found. Treat one thermal image as a screening result only. Confirm it with string current, the IV curve shape and visual inspection, and add EL imaging where cell damage is suspected. Raise the priority when the hotspot appears again on later inspections, when several modules in one string show it, or when there is a safety risk, because strong hotspots can lead to smouldering fires.

<!-- review notes
- sentence 1: support check: partial - Passages support hotter areas in IR during loaded operation for modules and BOS components, but no explicit definition of hotspot as such for any component.
- sentence 4: support check: partial - Passages show overheated terminals/connectors/clamps and loose connections, but do not state that they usually mean a connection problem rather than cell fault.
- sentence 5: support check: partial - u20 gives checking shadowing/debris then suspecting a bad module for hot bypass diodes; but a conducting diode inference and 'shorted diode' are not stated, and warm substring link is only indirect.
- sentence 6: support check: partial - Screening result and confirmation with string current, IV curve and visual inspection are supported, but adding EL where cell damage is suspected is only loosely supported (EL identifies cell cracks).
-->
