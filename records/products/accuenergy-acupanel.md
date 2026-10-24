---
id: prod:accuenergy-acupanel
type: Product
name: Accuenergy AcuPanel 9100 series
aliases:
- AcuPanel
- AcuPanel 9104
- AcuPanel 9104X
category: Metering
make: accuenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:accuenergy
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-old-accuenergy-acupanel9100series-brochure
    loc: sec=h1
    h: b16fc78182db
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acupanel-acupanel-9104-9104x-datasheet
    loc: sec=h21
    h: ea8b87ce16e5
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: prod:accuenergy-acuvim-ii
  note: Enclosure is designed to house Acuvim II series meters (Acuvim IIv3 in the 9104X).
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-old-accuenergy-acupanel9100series-brochure
    loc: sec=h1
    h: b16fc78182db
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acupanel-acupanel-9104x-ii-install-general-commissioning
    loc: sec=h1
    h: 9b3e4eae56e2
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:accuenergy-acuvim-l
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-old-accuenergy-acupanel9100series-brochure
    loc: sec=h1
    h: b16fc78182db
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:bacnet
  conditions: IIBN meter option, revenue-grade meter with BACnet-IP built in
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acupanel-acupanel-9104-9104x-datasheet
    loc: tbl=3
    h: 3cdca7223465
  review: drafted
- claim_id: c5
  attr: nominal_voltage
  value:
    min: 120
    max: 415
    unit: unit:V
  conditions: Line-line input voltage range of Tesla-listed AcuPanel 9104X P1 part numbers
  cite:
  - src: src:eq-equip-bess-tesla-801-696-01-00-using-acuvim-ii-meters-with-tesla-products
    loc: tbl=7
    h: 14ad946b8972
  - src: src:eq-equip-bess-tesla-using-acuvim-ii-meters-with-tesla-products
    loc: tbl=8
    h: 14ad946b8972
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Line-line input voltage of Tesla-listed AcuPanel 9104X P3 part numbers
  cite:
  - src: src:eq-equip-bess-tesla-801-696-01-00-using-acuvim-ii-meters-with-tesla-products
    loc: tbl=7
    h: 14ad946b8972
  - src: src:eq-equip-bess-tesla-using-acuvim-ii-meters-with-tesla-products
    loc: tbl=8
    h: 14ad946b8972
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: possible conflict with c5 (same source; check the conditions)
---
The Accuenergy AcuPanel 9100 series is an enclosure that comes pre-wired at the factory, so it arrives as a complete energy metering package that installs next to the switchgear. It is built to hold Acuvim II and Acuvim-L series multifunction power and energy meters. It suits retrofit jobs where the distribution panel has no space set aside for a meter. The AcuPanel 9104 is a steel indoor panel rated NEMA 4 or NEMA 3. The AcuPanel 9104X is a waterproof polycarbonate panel rated NEMA 4X for indoor or outdoor use. The standard enclosure contains labelled terminal blocks for the CT and voltage inputs, a CT shorting block, three industrial-grade fuses and a high-voltage label. No neutral is needed near the terminal block. The ordering options cover several CT input types: 5 A or 1 A, Rogowski coil, 333 mV, and milliamp. They also cover several power supplies: P1 for AC or DC, P2 for low-voltage DC, P3 for 480 Vac and P4 for 600 Vac. With the IIBN meter option, the panel holds a revenue-grade meter with BACnet-IP built in. Tesla lists AcuPanel 9104X part numbers with an Acuvim IIR meter for its products. The voltage options are 480 Vac line-line or 120 to 415 Vac line-line, with either Rogowski coil or 5 A CT inputs.

<!-- review notes
- sentence 4: support check: partial - The passage lists the terminal blocks, shorting block, 3 fuses, high-voltage label and no neutral. It says the terminals are 'clearly labelled' but doesn't say the high-voltage label is on the swing panel as stated; this is a minor detail.
-->
