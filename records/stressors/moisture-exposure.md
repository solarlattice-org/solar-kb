---
id: stressor:moisture-exposure
type: Stressor
name: Moisture exposure
aliases:
- water ingress
- moisture ingress
- humidity ingress
- moisture infiltration
- Humidity
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 80
    unit: unit:PERCENT
  conditions: Worst case of corrosion caused by water ingress, observed in damp-heat tests
  quote: decrease the module maximum power by 80% in the worst-case during damp-heat tests
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h3
    h: '924544636200'
  review: drafted
  review_note: 'support check: partial - Passage says power decreased by 80% in the worst case during
    damp-heat tests, but this is a worst-case bound, not a typical loss.'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 20
    unit: unit:PERCENT
  conditions: Field-deployed EFG-Si module, first 3 years in the field; loss attributed to delamination,
    moisture ingress and corrosion of the electrical contacts
  note: The source says Pmax fell by nearly 20% while Isc fell by about 5%.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
---
Moisture exposure means water or water vapour from the surroundings getting into modules, junction boxes and connectors. It is a key stressor that degrades PV modules. Inside the module, moisture breaks down EVA by hydrolysis, which releases acetic acid. The acid corrodes the silver gridlines and solder bonds, so series resistance rises and current collection drops. This is severe metallization corrosion. Moisture enters through the backsheet, along the module edges and at junction box penetrations. Even glass/glass modules do not keep it out completely. Delamination creates faster paths for water to get in and lets it condense, which speeds up corrosion. Water that gets into damaged or poorly sealed junction boxes corrodes the contacts. This can cause junction box failure, interconnection failure and insulation faults during humid periods. Humidity getting in through a defective or detached junction box also increases corrosion and weakens cell interconnections. This can lead to cell interconnection failure. In potential induced degradation (PID), corrosion caused by moisture getting in is the electrochemical mechanism, and it cannot be reversed. Salt mist in coastal areas has been reported to speed up PID. Exposure is higher on floating plants, in coastal areas and in humid climates. It is reduced by choosing module designs and installation practices that limit moisture, by sealing junction boxes properly and by finding out where the water is getting in.

<!-- review notes
- sentence 1: support check: partial - Passages call humidity a key stressor and mention ingress via backsheet, edges and junction box, but give no definition of moisture exposure as such.
- sentence 7: support check: partial - Floating, coastal and humid exposure and mitigation by module design/installation and investigating ingress causes are supported, but sealing junction boxes properly as a mitigation is not stated.
-->
