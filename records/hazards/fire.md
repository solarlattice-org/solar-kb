---
id: hazard:fire
type: Hazard
name: Electrical fire
aliases:
- fire hazard
- DC wiring fire
- connector overheating
category: Thermal
claims:
- claim_id: c1
  rel: controlled_by
  target: tool:thermal-imager
  note: Thermal imaging reveals heating anomalies invisible to the eye so they can be fixed before a fire
    starts.
  cite:
  - src: src:test-ir-thermography-t820264-en
    loc: sec=h8
    h: 19759479c740
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:connector-replacement
  note: Replacing damaged or mismatched connectors addresses connector defects that cause resistance heating,
    arcing and fire hazards.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: controlled_by
  target: mit:correct-crimping
  note: Fixing crimping and installation errors on connectors.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:connector-compatibility-check
  note: Confirm connector types are compatible across repaired circuits.
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: mit:flammable-area-mounting-avoidance
  note: SMA manuals say not to mount the product where highly flammable materials or gases are present,
    or in potentially explosive atmospheres.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h102
    h: 768063f0d025
  - src: src:sma-doc-259761
    loc: sec=h96
    h: 78aa46bc2b40
  - src: src:eq-equip-inverters-sma-data-manager-m-firmware-edmm-10-be-en-26
    loc: sec=h92
    h: 768063f0d025
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:vegetation-management
  note: Poor vegetation management, together with arc faults from inverters and connectors, raises the
    risk of fires started by PV plants.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=8.1
    h: befcc24716b4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passage says insufficient vegetation management plus arc faults
    raise PV plant fire risk, but does not explicitly state vegetation management as a mitigation (implied
    only).'
- claim_id: c7
  rel: controlled_by
  target: mit:proper-installation
  note: Incorrectly installed PV systems are linked to fire hazards.
  cite:
  - src: src:test-cx-manuals-seaward-pv-testing-white-paper-harnessing-the-potential
    loc: sec=h4
    h: 1ea9b095e8f7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: controlled_by
  target: mit:regular-inspections
  note: Fire cases point to the need for rigorous inspection standards.
  cite:
  - src: src:test-cx-manuals-seaward-pv-testing-white-paper-harnessing-the-potential
    loc: sec=h4
    h: 1ea9b095e8f7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Even a small electrical fault can waste energy as heat. Left unchecked, that heat can melt connections and throw sparks that start a fire. In PV systems, defective, undertorqued or overheating connectors cause resistance heating and arcing, which create fire hazards. Deformed plastic and shiny surfaces are warning signs. Reported PV fire causes include poor installation, undetected ground faults, arcing, debris under the panels and inverter faults. At ground-mounted plants, arc faults near dry, poorly managed vegetation can start wildfires. On the Sunny Tripower 8000-17000TL-10, the electronic string fuse helps prevent fires. If the inverter is beeping, do not unplug the DC connectors or the ESS, because the reverse current could then flow through the faulty string and cause a fire. Find heating early with infrared inspection under load. Replace damaged or mismatched connectors, correct crimping errors and check that connector types are compatible. Do not mount inverters or data managers near highly flammable materials or gases, or in explosive atmospheres. Only qualified personnel should install or service Enphase microinverters and the IQ Cable.

<!-- review notes
- sentence 2: support check: partial - Connector defects causing resistance heating, arcing and fire hazards, and deformed plastic/shiny signs of overheating are stated, but 'undertorqued' causing arcing/fire is not directly stated.
- sentence 3: support check: partial - Causes listed are supported, but wildfires from arc faults specifically at ground-mounted plants is not stated; the passage is general about arc faults and vegetation.
- sentence 6: support check: partial - Passages say not to mount the product near flammables/explosive atmospheres, but do not mention inverters or data managers specifically; the qualified-personnel claim for Enphase is supported.
- sentence 4: review: partial - The electronic string fuse and the ESS reverse-current fire risk are stated, but the passage gives an electric arc as the risk of unplugging the DC connectors, not reverse current through the faulty string causing a fire.
-->
