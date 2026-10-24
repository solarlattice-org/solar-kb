---
id: prog:solaredge-warranty
type: Program
name: SolarEdge limited warranty
aliases:
- SolarEdge warranty
- Limited Product Warranty
category: Warranty
program_kind: warranty
claims:
- claim_id: c1
  rel: issued_by
  target: org:solaredge
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
- claim_id: c2
  rel: applies_to
  target: prod:solaredge-power-optimizer
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  - src: src:eq-equip-inverters-solaredge-design-installation-power-optimizer-input-connector-compatibility-v1-3
    loc: sec=h10
    h: 7e367320cd7e
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:solaredge-commercial-gateway
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
- claim_id: c4
  attr: warranty_term
  value:
    nominal: 25
    unit: unit:YR
  scope:
    products:
    - prod:solaredge-power-optimizer
  conditions: Power optimizers; term starts at installation or 4 months after shipment from SolarEdge,
    whichever is earlier. Module-embedded optimizers (CSI and OPJ models) are capped by the module manufacturer's
    product or power warranty period.
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
- claim_id: c5
  attr: warranty_term
  value:
    nominal: 12
    unit: unit:YR
  conditions: Inverters, Safety & Monitoring Interface (SMI) and auto-transformer; term starts at installation
    or 4 months after shipment, whichever is earlier
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: warranty_term
  value:
    nominal: 7
    unit: unit:YR
  conditions: Inverter warranty in certain countries listed on SolarEdge's warranty exceptions page
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: StorEdge Interface; term starts at installation or 4 months after shipment, whichever is
    earlier
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: warranty_term
  value:
    nominal: 5
    unit: unit:YR
  conditions: ZigBee, Commercial and Firefighter Gateways, Smart Energy products, wireless communication
    products (pre-installed in the inverter or not), RS485 Plug-in and Energy Meter; term starts at installation
    or 4 months after shipment, whichever is earlier
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-solaredge-warranty-april-2019
    loc: sec=h1
    h: e7c3cd069b37
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
---
SolarEdge Technologies offers this limited warranty against defects in workmanship and materials. It covers power optimizers, inverters, interfaces, gateways, meters and communication products, and each product group has its own warranty period. Cables, fuses, wires, connectors and other ancillary parts are not covered, including the extension cable between modules. On optimizers whose part number ends in C, the input connector is excluded, but other optimizer failures stay covered. Coverage applies to buyers who purchased from an authorized SolarEdge seller. It can pass to a new owner as long as the product stays in its original country of installation and any reinstallation follows the documentation. To claim, email SolarEdge support promptly with a short description of the defect, the serial number and a copy of the purchase receipt or warranty certificate. The serial label must be legible and attached to the product. SolarEdge decides whether to repair the unit, issue a credit or send a replacement, and it may require a return through its RMA procedure, with shipping paid by SolarEdge. Labor, travel and the cost of uninstalling and reinstalling on site are not covered. Damage from improper installation, poor ventilation, unauthorized opening, surges, lightning or other external events is excluded. Work done by unqualified persons may void the warranty on SolarEdge equipment.
