---
id: concept:mppt-voltage-range
type: Concept
name: MPPT voltage range
aliases:
- MPP voltage range
- MPPT operating range
- MPPT operating voltage range
- Operating MPPT voltage range
- MPPT Input Voltage Range
- DC Voltage Range MPPT
- Maximum Power Voltage Range
category: Inverters
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: func:mppt
  note: Datasheets list the MPPT voltage range per tracker, next to the number of MPP trackers.
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=64
    h: 2eb30d32d328
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=13
    h: a5d1522476a0
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-45ktl-us-hv-manual
    loc: tbl=41
    h: 5a371028eb38
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:independent-mpp-trackers
  note: Specification tables give the MPP voltage range alongside the count of independent MPP inputs
    or trackers.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=39
    h: 6d2066c9a85f
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-45ktl-us-hv-manual
    loc: tbl=41
    h: 5a371028eb38
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:maximum-power-point
  note: This source labels the range as the maximum power voltage range (MPPT).
  cite:
  - src: src:eq-equip-inverters-solectria-xgi-1500-fl-xgi1500-04-02-14-2022
    loc: tbl=1.r1
    h: 164fd62eaaac
  review: drafted
  review_note: 'support check: partial - The u3 passage labels a ''Maximum Power Voltage Range (MPPT)'',
    but it is garbled and does not state a relation to the maximum power point concept itself.'
---
The MPPT voltage range is the band of DC input voltage in which an inverter's maximum power point tracker works. Datasheets give it for the whole model or for each tracker. Many datasheets separate a wide operating MPPT range from a narrower full-power MPPT range. For example, the Huawei SUN2000-45KTL-US-HV-D0 lists 600-1450 V for the operating MPPT range and 800-1200 V for the full-power range. The MPPT range falls inside the wider operating DC input range and stays below the maximum input voltage. The CPS SCA25KTL-DO-R/US-480 is an example: 200-950 Vdc operating range, 560-850 Vdc MPPT range and 1000 Vdc maximum. The full-power range can depend on temperature. The Sungrow SG200HX-US gives its full-power MPP voltage range at 40 °C. Microinverters also list an MPPT voltage range among their DC operating parameters. This term goes together with maximum power point tracking and independent MPP trackers, because the range is quoted next to the tracker count.

<!-- review notes
- sentence 1: support check: partial - The passages show MPPT voltage range values (per MPPT and per model) but never define it as the band in which the tracker works.
- sentence 4: support check: partial - The Sungrow gives the full-power range at 40 °C, but the passage does not state that the range depends on temperature in general.
-->
