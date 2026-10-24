---
id: concept:power-quality
type: Concept
name: Power quality
aliases:
- voltage sags
- swells
- flicker
- rapid voltage change
- PQ
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:point-of-common-coupling
  note: Rapid voltage change and flicker limits are judged at the PCC, and the utility may record flicker
    at or near the PCC.
  cite:
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: sec=h16
    h: 1976bab3fb7c
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=7.2.1
    h: 6405266c22c2
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:harmonic-distortion
  note: Harmonics and THD are tracked as power quality parameters.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-sp
    loc: sec=h51
    h: 7ab6616df5de
  - src: src:eq-equip-meters-sel-735-sel-735-cutsheet-735-ds-20190115
    loc: sec=h5
    h: 6e1fc8814236
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:phase-unbalance
  note: Voltage and current unbalance are logged as power quality events or parameters.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-sp
    loc: sec=h51
    h: 7ab6616df5de
  - src: src:eq-equip-meters-sel-735-sel-735-cutsheet-735-ds-20190115
    loc: sec=h5
    h: 6e1fc8814236
  - src: src:eq-equip-bess-stem-partner-content-library-epc-resource-library-backup-power-resources-05-data-sheet-7
    loc: tbl=1.r18
    h: 9f0ccabe45a2
  review: drafted
- claim_id: c4
  rel: related_to
  target: stressor:load-inrush-current
  note: Start-ups, inrush currents and the switching of capacitor banks or transformers are listed as
    causes of rapid voltage changes.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=G.2
    h: 1a7557497dc3
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:ieee-519
  note: One utility points to IEEE 519 as guidance when it reviews flicker data.
  cite:
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: sec=h16
    h: 1976bab3fb7c
  review: drafted
- claim_id: c6
  rel: related_to
  target: tool:power-quality-analyzer
  note: Where flicker is a concern, the utility may install a recording power quality meter.
  cite:
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: sec=h16
    h: 1976bab3fb7c
  review: drafted
- claim_id: c7
  rel: related_to
  target: prod:sel-735
  note: This meter complies with IEC 61000-4-30 Class A and measures flicker, sags, swells and interruptions.
  cite:
  - src: src:eq-equip-meters-sel-735-sel-735-cutsheet-735-ds-20190115
    loc: sec=h5
    h: 6e1fc8814236
  - src: src:eq-equip-meters-sel-735-sel-735-datasheet-735-ds-20250711
    loc: sec=h73
    h: 7d6fa37db3a8
  - src: src:eq-equip-meters-sel-735-sel-735-cutsheet-735-ds-20190115
    loc: tbl=2
    h: 6fc453723b2e
  review: drafted
- claim_id: c8
  rel: related_to
  target: prod:accuenergy-acuvim-ii
  note: It logs power quality events such as sags and swells, each with a timestamp.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-advanced-power-and-energy-meter
    loc: sec=h12
    h: 059240ab1b55
  review: drafted
---
Power quality describes how well the electricity supply suits the equipment that uses it. A power quality problem is any deviation in voltage, current or frequency that makes customer equipment misoperate or fail. Common power quality events include voltage sags (also called dips), swells, interruptions, flicker, harmonic distortion and phase unbalance. A voltage sag is a sudden drop in voltage while the load stays connected. Faults on the power system usually cause sags, but starting large motors can also cause them. A rapid voltage change is a quick shift in rms voltage between two steady states that stays inside the sag and swell thresholds. Switching, inrush currents and energizing a transformer can all cause one. Power quality problems can come from the utility, from your own site's equipment, or from a neighbouring facility. Equipment that is sensitive to disturbances can also be the source of them. Revenue and protection meters, such as Class A meters built to IEC 61000-4-30, log sags, swells, flicker and harmonics for this kind of analysis. Power quality analysis is also part of PV commissioning.

<!-- review notes
- sentence 1: support check: partial - u18 gives the power quality problem definition and u1 describes PQ as compatibility of supply with end-use equipment, but u1 only supports this loosely as a general definition.
- sentence 6: support check: partial - Class A IEC 61000-4-30 logging of sags, swells, flicker and harmonics and the commissioning power quality analysis section are supported, but 'revenue and protection meters' generally is not stated.
-->
