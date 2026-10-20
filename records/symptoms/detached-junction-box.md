---
id: symptom:detached-junction-box
type: Symptom
name: Detached or open junction box
aliases:
- loose junction box
- j-box
- JB
claims:
- claim_id: c1
  rel: observed_as
  target: meas:open-junction-box
  note: 'Seen on the module rear: open or loose lid, or a box that has shifted or come off the backsheet.
    The adhesive or sealant may look weathered or yellowed, and seals at the lid or wire entry may be
    damaged or missing.'
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r1
    h: 2f54f0d00dad
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=17.r1
    h: 2f54f0d00dad
  - src: src:iea-pvps-t13-01-2014
    loc: fig=30
    h: e257fda96cf2
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:jbox-terminal-corrosion
  note: A defective or detached box lets humidity in, which corrodes the interconnections. A loose box
    also puts mechanical stress on the internal contacts and can break them.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r5
    h: e5cfc2bc593a
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=17.r5
    h: e5cfc2bc593a
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h4
    h: d298ad6bbdd3
  review: drafted
---
On the back of the module, the junction box lid is open or loose, or the whole box has shifted or come away from the backsheet. Look for weathered or yellowed adhesive under the box and for seals at the lid or cable entry that are squeezed, broken, brittle or missing. This symptom belongs to junction box failure. Causes include poor bonding or low-quality adhesive, foam tapes losing grip in cold weather, poor closing at the factory, heat-driven air pressure in boxes with no vent, and delamination near the box. Rough handling during installation also stresses the box, for example lifting modules by their cables, leaving cables unfixed or using string cables that are too short. Once the box is open, moisture can get in and corrode the connections, which lowers output and raises the risk of arcing and fire. A loose box can break its internal contacts and leave live parts exposed, so treat it as a safety hazard before touching it. Check first for burn or melt marks on the housing and for corroded or poorly made wiring inside, since these point to arcing or a bad connection rather than detachment alone.

<!-- review notes
- sentence 6: support check: partial - Risk of breaking contacts and exposing persons to active electrical components is stated, but the advice to treat it as a safety hazard before touching is not in the passages.
- sentence 7: support check: partial - Burned/melted housing, arc-caused burnt box and poor wiring are described, but no passage gives a check-first priority or says these indicate arcing or bad connection rather than detachment alone.
-->
