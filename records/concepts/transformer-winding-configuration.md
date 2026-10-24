---
id: concept:transformer-winding-configuration
type: Concept
name: Transformer winding configuration
aliases:
- vector group
- delta-wye
- wye-delta
- winding compatibility
- IEC Vector Group
- Winding connection
- Winding types
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:effective-grounding
  note: Grounded wye-wye, wye-wye with a grounding bank, and wye-delta with a neutral grounding reactor
    are shown as grounding configurations. Utilities decide case by case which configurations count as
    effectively grounded.
  cite:
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h14
    h: 0d98a148bbbb
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h18
    h: dce03f8db182
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h10
    h: 15778e0c7446
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-effective-grounding-presentation-final-5-10-18
    loc: sec=h22
    h: 79ceb9748269
  - src: src:ref-reference-zigzag-effective-grounding-luis-email-ju-effective-grounding-for-interconnection-2018
    loc: sec=h5
    h: 9abaa87be95a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:harmonic-distortion
  note: The winding configuration matters for filtering harmonics from the transmission system.
  cite:
  - src: src:std-standards-mv-committee-ieee-standards-mv-equipment-ieee-std-c37-246-2017-protection-systems-of-t
    loc: sec=4.2.2.1.9
    h: b8e25ad57c90
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:grid-following-inverter
  note: Megapack manuals show transformer configurations for on-grid, grid-following operation.
  cite:
  - src: src:eq-equip-bess-tesla-megapack-2-design-and-installation-manual
    loc: fig=98
    h: 94f828c8643f
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: fig=106
    h: ef727517916f
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: fig=107
    h: f3d09107b9ef
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: mit:transformer-configuration-check
  note: Inverter vendors publish tables of compatible transformer windings.
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: fig=107
    h: 0edf872c270a
  - src: src:chint-cps-xfmr-winding-compatibility-rev-2026-03-25
    loc: sec=h3
    h: 4b81e59382c1
  - src: src:chint-cps-xfmr-winding-compatibility-rev-2026-03-25
    loc: tbl=1.r1
    h: 00b939985d7f
  review: drafted
- claim_id: c5
  rel: related_to
  target: prod:solis-s6-gu-ehv-us
  note: Listed as compatible with Y(n)y(n), Dy(n) and Dd windings, and not compatible with Y(n)d.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=26.r1
    h: 5030ccfb8340
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=26.r2
    h: 5be5813e3ab5
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=26.r3
    h: ab616c9b3845
  review: drafted
- claim_id: c6
  rel: related_to
  target: prod:yaskawa-solectria-xgi-1500
  note: Compatible with a grounded-wye winding on the inverter side, neutral bonded to ground, and delta
    on the utility side. The manual also lists prohibited configurations.
  cite:
  - src: src:yaskawa-yss-xgi-interconnection-guidelines-2025-10-23
    loc: tbl=2
    h: aeadb74d12f6
  - src: src:yaskawa-yss-xgi-interconnection-guidelines-2025-10-23
    loc: tbl=2.r1
    h: 074b2fb78d5b
  - src: src:eq-equip-inverters-solectria-xgi-1500-xgi-1500-166-manual-rev-p-17-oct-2022
    loc: fig=51
    h: affb6bb42a24
  review: drafted
- claim_id: c7
  rel: related_to
  target: prod:chint-sca-25ktl-208
  note: 'For the 25 kW 208 V inverter: wye floating, wye grounded and delta floating are allowed. Delta
    grounded is not. Neutral connection is optional.'
  cite:
  - src: src:chint-cps-xfmr-winding-compatibility-rev-2026-03-25
    loc: tbl=1.r2
    h: 4d88cb0108c9
  review: drafted
---
Transformer winding configuration describes how the windings on each side of a transformer are connected, for example delta, wye or grounded wye. It is often written as an IEC vector group such as Dd0 or Dy1. The configuration matters because it affects ground fault detection, whether the system has a voltage reference, and how harmonics are filtered. Some configurations give effective grounding, such as grounded wye on both sides, sometimes with a grounding bank or a neutral grounding reactor. The utility decides this case by case. Inverter makers publish compatibility tables, and only some windings are allowed. For example, some CPS models accept wye floating, wye grounded and delta floating windings, but not delta grounded. Solis S6-GU EHV inverters accept Y(n)y(n), Dy(n) and Dd windings, but not Y(n)d. The Solectria XGI 1500 is compatible with grounded wye on the inverter side and delta on the utility side. Check the transformer against the inverter or storage manual before connecting. Manuals list prohibited configurations, and battery systems like Megapack show which configurations to use for grid-following operation.

<!-- review notes
- sentence 1: support check: partial - Delta/wye/grounded wye and IEC vector groups Dd0, Dy1 appear, but the definition and 'often written as' are only implied.
- sentence 6: support check: partial - Prohibited configurations and grid-following figures are present, but the instruction to check against the manual before connecting and Megapack naming are not stated.
-->
