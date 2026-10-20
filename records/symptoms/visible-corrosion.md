---
id: symptom:visible-corrosion
type: Symptom
name: Visible corrosion marks
aliases:
- Obvious corrosion
claims:
- claim_id: c1
  rel: observed_as
  target: meas:fill-factor-reduction
  note: IV tracing of corroded modules shows a lower fill factor because series resistance rises.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:iv-low-isc
  note: Metallization corrosion also lowers short-circuit current in the IV signature.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:el-dark-cell-edges
  note: Dark areas at cell borders in EL can show moisture diffusing in from the rear and between cells,
    with front-side corrosion starting at the edges.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h65
    h: 932bed75d53f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h34
    h: 57cc697f982e
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:ir-hot-connection
  note: Damaged connectors, which may show corrosion when opened, often appear overheated or as hot spots
    in thermography at an early stage.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r1
    h: 64afea9d2672
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=27.r1
    h: 64afea9d2672
  review: drafted
- claim_id: c5
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Corrosion of the transmittance layers (glass, antireflection coating) only, not metallization;
    larger losses are possible with heavy soiling, for example in deserts.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h4
    h: de0a5bfe7306
  review: drafted
  review_note: 'support check: partial - The passage gives a maximum impact of 4% for transmittance corrosion,
    not a typical value, though the soiling exception is stated.'
---
Corrosion can be seen by eye on cell metallization and interconnect ribbons, on opened DC connectors, and on module frames or mounting structures. Inside the module, metallization corrosion shows as light yellow to dark brown or black discoloration, sometimes with powdery white, gray, blue or green galvanic deposits, mostly at solder bonds, fingers and ribbons. This points to severe metallization corrosion, which is often found together with delamination, encapsulant discoloration and sometimes burn marks; confirm the electrical impact with IV tracing, EL and thermography. On IV curves, metallization corrosion lowers the fill factor and short-circuit current, and on EL images dark areas at the cell edges can show where moisture has entered. Corrosion found inside opened connectors points to a cable or connector defect; these connectors often show as hot spots under thermography. Corrosion on frames, mounting holes or around fastening screws points to a defective mounting structure, often galvanic corrosion where two different metals touch, for example an aluminium frame on steel, in humid or coastal sites. Check first where the corrosion is located (cells, connectors or structure), then whether the site is humid, coastal or agricultural, since these environments speed up corrosion.

<!-- review notes
- sentence 3: support check: partial - Co-occurrence with delamination, encapsulant discoloration and burn marks and confirmation by IV, EL and thermography are stated, but nothing says a given visible sign indicates severe corrosion.
- sentence 5: support check: partial - Opened connectors can show corrosion and often show hot spots, but the passage does not say corrosion points to a connector defect, since it describes damaged connectors showing corrosion.
- sentence 7: support check: partial - Humid, coastal and agricultural environments accelerating corrosion are stated, but the check order (location first, then site) is not in the passages.
-->
