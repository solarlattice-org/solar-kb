---
id: fm:hot-cell
type: FailureMode
name: Hot cell
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:current-mismatch
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:cell-reverse-bias
  note: The underperforming cell is driven into reverse bias and dissipates power as heat.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:partial-shading
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c4
  rel: caused_by
  target: fm:cell-cracks
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:solar-cell
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:backsheet
  note: Very high cell temperatures can cause backsheet bubbles and deformation.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:encapsulant
  note: Polymeric materials can discolour, delaminate or embrittle at high temperature.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - Polymeric materials discolour, delaminate and embrittle above
    150°C, but encapsulant is not named explicitly.'
- claim_id: c8
  rel: presents_as
  target: symptom:uniform-cell-heating
  note: Temperature rises evenly over the whole cell area, not at one point.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c9
  rel: detected_by
  target: method:ir-thermography
  note: IR thermography of aged field modules revealed hot cells.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
- claim_id: c10
  rel: distinguished_from
  target: fm:module-hotspot
  by: method:ir-thermography
  note: A hot spot is localised heating from local junction breakdown, mainly in multicrystalline cells;
    a hot cell heats evenly over the whole cell area and is linked to monocrystalline cells.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - The hot spot/hot cell distinction is stated (localised vs homogeneous,
    multi vs mono), but the passages don''t say IR thermography is used to tell them apart.'
- claim_id: c11
  rel: leads_to
  target: fm:encapsulant-discoloration
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c12
  rel: leads_to
  target: fm:cell-interconnection-failure
  note: Solder joints can fail if the cell temperature exceeds the solder melting point.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c13
  rel: leads_to
  target: fm:cell-cracks
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c14
  rel: leads_to
  target: fm:delamination
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c15
  rel: leads_to
  target: fm:insulation-loss
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c16
  rel: leads_to
  target: fm:backsheet-deformation
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c17
  rel: leads_to
  target: fm:glass-breakage
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c18
  rel: leads_to
  target: fm:junction-box-failure
  note: In extreme cases the junction box may detach.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:cell-current-binning
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:cell-shunt-screening
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:bypass-diode-integration
  note: Bypass diodes cap the dissipated power but do not eliminate hot cell effects.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:shade-resistant-modules
  note: Examples include half-cell, shingled and per-cell diode modules.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
  review_note: 'support check: partial - Shade-resistant modules (half-cell, shingled, per-cell diodes)
    are offered, but the text doesn''t explicitly say they mitigate hot cells, and notes shade resistance
    is poorly defined.'
- claim_id: c23
  rel: mitigated_by
  target: mit:fewer-cells-per-bypass-diode
  note: Fewer cells per bypass diode lowers the reverse voltage and hot cell temperature.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c24
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: IBC half-cell module in an indoor hot-spot test at 55°C module temperature; hot cell temperature
    relative to module temperature
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
A hot cell is a solar cell that heats up evenly over its whole area because current mismatch, from shading or cell cracks, pushes it into reverse bias and makes it dissipate power. It is mainly seen in monocrystalline cells, while the classic hot spot is a localised point of heating mostly found in multicrystalline cells. Infrared thermography shows the affected cell as uniformly warmer than its neighbours. A single hot cell usually costs little power, but the heat can lead to discolouration, delamination, interconnection failures, cell cracks, backsheet deformation, glass breakage and loss of insulation. Bypass diodes limit the power a shaded cell can dissipate, but they do not remove the hot cell risk. Preventive measures include binning cells by current, screening cells for low shunt resistance, using shade-resistant module designs and putting fewer cells on each bypass diode.

<!-- review notes
- sentence 3: support check: partial - IRT is said to reveal hot cells and a hot cell has a homogeneous temperature rise, but no passage states the thermographic image shows it uniformly warmer than neighbours.
- sentence 4: support check: partial - The failure modes and that a single hot cell has insignificant power loss are stated, but they come from different passages and the PVFS text concerns hot spots/single hot cells generally.
-->
