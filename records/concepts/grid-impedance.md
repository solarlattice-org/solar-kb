---
id: concept:grid-impedance
type: Concept
name: Grid impedance
aliases:
- network impedance
- source impedance
- virtual grid impedance
- ZPCC
- Grid LV impedance
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: explains
  target: concept:voltage-rise
  note: Impedance between the PV system and the grid raises the voltage seen at the inverter terminals;
    injected power raises voltage at the connection point roughly in proportion.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=3
    h: c1f980e19b60
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-mv-xfmr-req-techinfo
    loc: sec=3
    h: 40033c0d0f22
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h56
    h: 30ae0962fc12
  review: drafted
- claim_id: c2
  rel: explains
  target: fm:inverter-grid-resonance
  note: High-impedance (weak) grids can cause low-frequency resonance instabilities between the grid and
    paralleled inverters; inverter control stability depends on impedance to the PCC.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h112
    h: 1832b34f9198
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=3
    h: c1f980e19b60
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-mv-xfmr-req-techinfo
    loc: sec=3
    h: 40033c0d0f22
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:short-circuit-ratio
  note: Schneider recommends calculating grid impedance at the PCC and keeping short-circuit power at
    least 8 times plant installed power.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h112
    h: 1832b34f9198
  review: drafted
- claim_id: c4
  rel: related_to
  target: symptom:grid-impedance-high
  note: SMA inverters disconnect from the grid when grid voltage or impedance at the connection point
    is too high.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h424
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h429
    h: 9d464275e542
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h434
    h: 9d464275e542
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:point-of-interconnection
  note: Grid impedance is evaluated at the point of common coupling from the available short-circuit power.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=3
    h: c1f980e19b60
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-mv-xfmr-req-techinfo
    loc: sec=3
    h: 40033c0d0f22
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h112
    h: 1832b34f9198
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:voltage-drop
  note: AC conductors should limit voltage drop between inverters and PCC to a maximum of 1% of nominal
    voltage.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=3
    h: c1f980e19b60
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-mv-xfmr-req-techinfo
    loc: sec=3
    h: 40033c0d0f22
  review: drafted
- claim_id: c7
  rel: related_to
  target: comp:mv-transformer
  note: Transformer short-circuit impedance adds to total system impedance seen by the inverter.
  cite:
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=3
    h: c1f980e19b60
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h112
    h: 1832b34f9198
  - src: src:ref-standards-mv-committee-inverter-requirements-with-mv-xmfr-requirements-for-medium-voltage-transf
    loc: sec=h7
    h: b98f50085d22
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:symmetrical-components
  note: Source impedance is expressed as positive-, negative- and zero-sequence components in fault analysis.
  cite:
  - src: src:ref-standards-mv-committee-application-docs-xmfr-protection-sel-59n-3v0-protection
    loc: sec=h5
    h: 1174e69c8460
  - src: src:man-sel-synchrowave-application-guides-visualizing-the-32q-and-32v-directional-elements-in-the-compl
    loc: sec=h22
    h: 9afda1f25756
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - u28 lists positive-, negative- and zero-sequence source impedances
    in fault analysis, but it doesn''t call this ''grid impedance'' explicitly, though it is the utility
    source impedance.'
---
Grid impedance is the electrical impedance of the utility network as seen from the connection point of a PV or storage system, usually derived from the short-circuit power available at the point of common coupling. When a PV system injects power, the impedance of the feeder causes the voltage at the connection point to rise in proportion to the power injected. A low grid impedance means a stiff grid that can absorb a lot of PV power before voltage limits are reached, while a high value points to a resistive feeder or one already loaded with much PV. Impedance between inverters and the grid, including conductors and transformers, can push terminal voltage up enough to cause over-voltage trips and also affects the stability of inverter controls. Some inverters report an event and disconnect from the grid when the grid voltage or grid impedance at their connection point is too high. Weak, high-impedance grids can produce low-frequency resonance between paralleled string inverters and the network, so designers check grid impedance at the PCC and keep short-circuit power well above plant size. For most commercial systems the grid capacity at the PCC dwarfs the PV system, so grid impedance is negligible and the utility supplies the value when it is needed. Related concepts include voltage rise, short-circuit ratio, transformer impedance and symmetrical components.

<!-- review notes
- sentence 1: support check: partial - The passages tie ZPCC to short-circuit power at the PCC, but they don't define grid impedance as the utility network impedance seen from the connection point or say it is 'usually' derived that way.
- sentence 8: support check: partial - Voltage rise, short-circuit power and transformer impedance, and sequence components are all discussed, but the passages don't state them as 'related concepts' of grid impedance; short-circuit ratio appears only as an Ssc/Splant requirement.
- sentence 1: review: partial - The passages tie ZPCC to the short-circuit power available at the PCC, but they never define grid impedance as the utility network's impedance seen from the connection point, nor say it is 'usually' derived that way.
-->
