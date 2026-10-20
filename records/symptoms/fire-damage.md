---
id: symptom:fire-damage
type: Symptom
name: Fire damage
aliases:
- Fire/burn mark failure
claims:
- claim_id: c1
  rel: observed_as
  target: meas:visible-burn-marks
  note: Burned, melted or charred terminals in combiner boxes, burnt junction boxes after an arc at the
    input lead, and burn marks on module backsheet or front.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h74
    h: 148d5765d67c
  - src: src:pv-root-cause-junction-box-failure
    loc: fig=2
    h: c93b4815ec6c
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=8.r1
    h: 6120db012717
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=8.r2
    h: b42aa9ef2371
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:arc-fault-alarm
  note: The inverter detects electrical noise from a DC series arc and shuts down to prevent fire. The
    event message asks for the PV array and DC wiring to be inspected for damage.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=1.9
    h: adb7a5ad932f
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=6.8
    h: 5bf4984d5c93
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:ir-warm-substring
  note: A substring much hotter than others under equal shading points to a missing or open bypass diode.
    A hot spot in that substring can be a severe fire hazard.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=24.r2
    h: 24ae000fb31a
  review: drafted
---
Fire damage shows up as burned, melted or charred parts, such as terminal blocks in combiner boxes, junction boxes, and burn marks on module backsheets or fronts. A common cause is an arc fault: a burnt junction box can come from an arc at its input lead, and grass fires on site have likely been started by arcs. In monitoring data, look for an arc fault event: the inverter senses the noise of a DC series arc and shuts down, and the troubleshooting step is to inspect the PV array and DC wiring for damage. Thermal damage in a combiner box points to excess heat from the fuse holder or from faulty DC connectors or cables, and loose wire torque can also start a fire. In IR images, a substring that runs much hotter than its neighbours under equal shading points to a missing or open bypass diode, which can become a serious fire hazard. Fires may also come from outside the plant: wildfires can destroy all or part of a plant, and their smoke leaves particles that soil modules and may get into connectors. Fire at the inverter and burned string combiner boxes have also been reported at a PV plant hit by flooding. Thermal damage carries both shock and fire risk, so qualified personnel should isolate it and act right away before further inspection.

<!-- review notes
- sentence 2: support check: partial - Burnt junction box from arc and grass fires likely triggered by arc fault are stated, but 'a common cause' is not established.
- sentence 8: support check: partial - Shock and fire risk and immediate action by qualified personnel are stated, but isolating it and doing so before further inspection is not.
-->
