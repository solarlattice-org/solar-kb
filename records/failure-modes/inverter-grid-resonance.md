---
id: fm:inverter-grid-resonance
type: FailureMode
name: Inverter-grid resonance at low short-circuit ratio
aliases:
- AC voltage resonance
- low grid SCR
- weak grid resonance
- short-circuit ratio limit
- Inverter-grid voltage resonance at low short-circuit ratio
- short-circuit ratio
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:low-grid-scr
  note: At very low SCR, the impedances of the inverters, transformer and grid combine to produce resonance
    on the AC voltage waveform.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:excess-inverters-per-poi
  note: On a weak grid, the number of XGI 1500 inverters that can share one point of interconnection is
    limited. Exceeding that limit risks resonance.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: drafted
  review_note: 'support check: partial - Passages say the inverter count per POI is limited at low SCR
    to avoid resonance, but don''t explicitly say exceeding the limit causes it (implied only).'
- claim_id: c3
  rel: caused_by
  target: stressor:shared-ac-bus-power-electronics
  note: 'Tesla expects excessive resonance on a common 480 V AC bus when two conditions both hold: the
    other power electronics exceed 20% of the Megapack apparent power rating, and their equivalent switching
    frequency is below 35 kHz.'
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.5
    h: 21d12b65f053
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.5
    h: ae4b25eb73b0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:grid-overvoltage
  note: When the resonance is strong enough, the inverter reads the grid AC voltage as too high.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:inverter-shutdown
  note: The inverter shuts down safely after it detects the resonance-driven overvoltage.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-count-limit
  note: Use the manufacturer's configuration tables, which cover SCR values from 2.0 to 6.0, to choose
    the number of systems and the inverters per system for a given plant size.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h156
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h160
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h154
    h: ebc54ead1327
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h19
    h: 06443a278cf0
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: sec=h1
    h: 54850814edb5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c8
  rel: mitigated_by
  target: mit:line-reactor
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.5
    h: 21d12b65f053
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.5
    h: ae4b25eb73b0
  review: drafted
  review_note: 'support check: partial - A line reactor is listed as a mitigation for resonance on a common
    480 V bus, not specifically for low-SCR grid resonance.'
- claim_id: c9
  rel: mitigated_by
  target: mit:isolation-transformer
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.5
    h: 21d12b65f053
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.5
    h: ae4b25eb73b0
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: tbl=60.r3
    h: 610708c02005
  review: drafted
  review_note: 'support check: partial - Isolation transformer is listed as a mitigation for common-bus
    resonance, not specifically low-SCR grid resonance.; review: partial - The passages list an isolation
    transformer as a mitigation for resonance between Megapack and inverters on a common 480 V AC bus,
    but they never mention low short-circuit ratio or grid resonance as such.'
- claim_id: c10
  rel: mitigated_by
  target: mit:equipment-relocation
  note: Move the resonance-prone power electronics off the common AC bus.
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.5
    h: 21d12b65f053
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.5
    h: ae4b25eb73b0
  review: drafted
  review_note: 'support check: partial - Relocating equipment is listed for common-bus resonance, not
    specifically low-SCR grid resonance.'
---
On a weak grid with a very low short-circuit ratio, the impedances of the inverters, the transformer and the grid can combine to cause resonance on the AC voltage waveform. If the resonance is strong enough, the inverter sees the grid voltage as too high and shuts down safely, so it looks like an overvoltage trip. The risk grows with the number of inverters connected at one point of interconnection. Check the site against the manufacturer's configuration tables, which cover SCR values from 2.0 to 6.0 and give the number of systems and the allowed range of inverters per system. Resonance is also expected when power electronics with a low switching frequency share a common 480 V AC bus with a battery system. In that case, move the equipment, add a line reactor or add an isolation transformer.

<!-- review notes
- sentence 3: support check: partial - Passages say the number of inverters per POI is limited at low SCR, implying a relation, but don't state that risk grows with count.
- sentence 5: support check: partial - Resonance is expected on a common 480 V bus with a Megapack, but only when both conditions hold (over 20% rating and under 35 kHz), and the statement omits the rating condition and says 'battery system'.
-->
