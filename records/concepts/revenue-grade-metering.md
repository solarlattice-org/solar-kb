---
id: concept:revenue-grade-metering
type: Concept
name: Revenue-grade metering
aliases:
- revenue grade meter
- RGM
- PBI meter
- RG Meter
- Revenue Grade Energy Meter
- Revenue Metering
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: func:production-metering
  note: Revenue-grade meters measure power and energy production at the inverter AC output or PV production
    circuit.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=8.11
    h: 3a6c64c38d79
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: sec=8.6
    h: 460813f1740e
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: sec=10.9
    h: 14b818e33656
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: tbl=4.r2
    h: 7bd9971bc4aa
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:energy-meter
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=8.11
    h: 3a6c64c38d79
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-14-1
    loc: tbl=2.r13
    h: 84698c0851f3
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: tbl=2.r20
    h: 38889f05fa7b
  review: drafted
  review_note: 'support check: partial - Passages describe a revenue grade meter/energy meter heading,
    but the relation to an energy meter component is only implied by headings (u13, u14) and a metering
    device description.'
- claim_id: c3
  rel: related_to
  target: tool:yaskawa-solectria-solrenview
  note: Factory-integrated revenue grade meter data is monitored through SolrenView services.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=8.11
    h: 3a6c64c38d79
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=9.5
    h: 6c60b2d0009a
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: sec=10.9
    h: 14b818e33656
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:enphase-envoy
  note: Envoy-S Metered includes integrated revenue grade PV production metering.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: tbl=4.r2
    h: 7bd9971bc4aa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Revenue-grade metering means measuring PV power and energy with a meter accurate enough for billing or reporting, typically at the AC output of the inverter. Accuracy is usually stated against ANSI C12.20, for example Class 0.2 for one DIN-rail meter, or plus or minus 0.5% for an integrated production meter. Some inverters offer an optional factory-integrated revenue grade meter whose lifetime energy and power can be read on the inverter display and through the vendor monitoring service. On such inverters the RG Meter menu item is hidden unless the meter is actually installed. Revenue-grade production data can feed agency reporting services offered with the monitoring platform. Other products add revenue-grade metering as a kit with its own current transformers, installed in the factory or in the field, and only for certain applications. Utility revenue metering cabinets and service metering follow the utility's own requirements, so check the local utility specification before installing. Revenue-grade production metering differs from consumption monitoring, which is often less accurate and needs extra CTs.

<!-- review notes
- sentence 1: support check: partial - Measurement of power and energy at the inverter AC output is stated, but accuracy sufficient for billing or reporting is not explicitly defined (only agency reporting use is mentioned).
- sentence 2: support check: partial - Class 0.2 and +/-0.5% against ANSI C12.20 are stated, but 'usually' and 'DIN-rail' are not in the passages.
- sentence 6: support check: partial - The Generac kit includes CTs, is factory or field installed, and is restricted to specific applications, but 'other products' in the plural is only evidenced by one product.
- sentence 7: support check: partial - Metering cabinets 'per utility requirements' is stated, but the advice to check the local utility specification and service metering detail are not in the passages.
- sentence 8: support check: partial - Consumption monitoring is optional, less accurate (+/-2.5% vs 0.5%) and needs additional CTs for the Envoy-S, but 'often' generalization is from one product.
- sentence 1: review: partial - Measuring power and energy at the inverter AC output is stated, but the passages never say the meter is accurate enough for billing or reporting, and 'typically' generalizes from one vendor.
- sentence 7: review: partial - Metering cabinets 'per utility requirements' is stated, but service metering appears only as a section heading, and the advice to check the local utility specification before installing is not in the passages.
-->
