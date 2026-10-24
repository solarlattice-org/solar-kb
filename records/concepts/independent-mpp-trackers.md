---
id: concept:independent-mpp-trackers
type: Concept
name: Independent MPP trackers
aliases:
- multiple MPPT inputs
- multi-MPPT
- multi-string inverter
- Dual MPPT
- Multi MPP Tracker
- Multiple MPPT
- Individual Maximum Power Point Tracking
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: func:mppt
  note: Each PV input section runs its own MPP tracking loop.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h649
    h: 4d8a109581a3
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: sec=h53
    h: fff56f476d0f
  review: drafted
- claim_id: c2
  rel: related_to
  target: stressor:partial-shading
  note: Separate tracking helps on sites with partial shading or mixed tilt/azimuth.
  cite:
  - src: src:eq-equip-inverters-chint-50-60-kw-inverter-chint-cps-sca50-60ktl-do-us-ver2-2
    loc: sec=h83
    h: 59c4b71ef83a
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=5.2
    h: 81e2b3251163
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:dc-ac-ratio
  note: With independent MPPT zones, DC/AC sizing should be calculated per zone.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=5.2
    h: 81e2b3251163
  review: drafted
- claim_id: c4
  rel: related_to
  target: symptom:unbalanced-mppt-connection
  note: Putting all inputs on one zone uses only half of the inverter power on the cited model.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=5.2
    h: 81e2b3251163
  review: drafted
- claim_id: c5
  rel: related_to
  target: arch:string-inverter-system
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h650
    h: 0fc4ed5a1025
  review: drafted
  review_note: 'support check: partial - Multi-string inverter definition mentions separate MPP tracking
    of strings like string inverters, but doesn''t directly relate independent trackers to a string inverter
    system; loosely supported.'
- claim_id: c6
  rel: related_to
  target: prod:yaskawa-solectria-pvi-50-60tl
  note: Three PV input sections that run only in independent mode.
  cite:
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: tbl=42.r7
    h: edf04f30229d
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: sec=h53
    h: fff56f476d0f
  review: drafted
---
An MPP tracker controls how much power an inverter draws so that the PV field stays as close as possible to its maximum power point, which shifts with irradiance and module temperature. An inverter with independent MPP trackers has several PV input sections, and each section runs its own MPP tracker. A multi-string inverter of this kind tracks individual strings separately, like several string inverters, while keeping the lower specific cost of a central inverter. Separate tracking is useful when part of the array is shaded or when strings face different tilts or azimuths, and it gives more flexibility in array layout. Some inverters let you combine the trackers into one zone, for example when there is an odd number of strings. Others can only run in independent mode, and some offer a menu setting to turn multiple MPPT on or off. In independent mode, treat each zone like a separate inverter: balance the strings between zones and do DC/AC ratio sizing per zone. Wiring every string to one zone can leave much of the inverter's capacity unused. For surge protection, plan an SPD or SPD combination for each tracker input, not one SPD on a combined string bus. Datasheets list the number of MPP trackers. Large central-style units often have just one, while many string inverters have two or three.

<!-- review notes
- sentence 7: support check: partial - Passage says to plan an SPD for each input on multi-tracker inverters, but the 'not one SPD on a combined string bus' contrast is only stated for single-tracker inverters, and fused strings use a common SPD after fuses.
- sentence 8: support check: partial - Datasheets show 1 MPPT for large units and 2–3 for string inverters, but 'datasheets list the number' and 'often/many' generalizations are inferred from a few examples.
-->
