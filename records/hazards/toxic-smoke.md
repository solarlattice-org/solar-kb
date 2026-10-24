---
id: hazard:toxic-smoke
type: Hazard
name: Toxic smoke and gas from fire
aliases:
- toxic gas
- smoke inhalation
category: Battery
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:bess-ventilation
  scope:
    products:
    - prod:powin-stack750
  note: The emergency ventilation system ducts carry off any toxic gases produced by the Energy Segments
    or the Collection Segment.
  cite:
  - src: src:powin-pi-s750-stack750-installation-manual-rev-8
    loc: sec=2.3
    h: 516dd72f26f0
  review: drafted
---
At PV plants, grass fires on site, likely started by an arc fault, give off dense smoke that can coat and get inside the PV system. Smoke particles from wildfires can be caustic and conduct electricity. The finest particles may get into connectors that were not torqued or maintained properly, or that were left open during construction. Fires started by the plant itself are becoming more likely. Arc faults from faulty inverters and PV connectors, together with poor vegetation management, drive this risk. Smoke plumes carrying dense particles leave ash and soot on modules and on electrical balance-of-system equipment.

<!-- review notes
- sentence 2: support check: partial - Passage says particulates can be caustic and conductive and PM2.5 likely penetrates connectors not properly torqued/maintained or left open, but notes evidence is lacking; the statement asserts it more firmly.
-->
