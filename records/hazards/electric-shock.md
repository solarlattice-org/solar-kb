---
id: hazard:electric-shock
type: Hazard
name: Electric shock
aliases:
- shock hazard
- electrocution
category: Electrical
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:safety-isolation
  note: Disconnect the device or grid connection point from all voltage sources, secure it against reconnection
    and confirm it is voltage-free before work.
  cite:
  - src: src:sma-doc-278879
    loc: sec=h21
    h: 044c024ea1db
  - src: src:sma-sc-wa-en-31
    loc: sec=h93
    h: 7b467ad0d922
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h29
    h: bdd44725c42e
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h513
    h: bdd44725c42e
  - src: src:sma-doc-stp33-62-us-41-rm-en-10
    loc: sec=h23
    h: e7beae9f7d99
  - src: src:sma-sc-wa-en-31
    loc: sec=h135
    h: 59f97c554256
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:connector-sealing-caps
  scope:
    products:
    - prod:enphase-iq-cable
  note: Unused AC connectors on the Enphase Q/IQ Cable are live whenever the system is energized, so each
    one must be covered with a sealing cap.
  cite:
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: tbl=7
    h: 6df13922912c
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=h17
    h: ea87fbca0d9d
  - src: src:enphase-enphase-iq7-series-mc4-microinverter-installation-and-operation-manual
    loc: tbl=7.r3
    h: 55ec91820040
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:regular-inspections
  note: Check the equipment for visible damage regularly. Operate it only when it is technically faultless,
    because defective cables or a damaged enclosure can cause a fatal shock.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=2.1.1
    h: 88ee41b1d427
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h48
    h: 87024b8a518c
  review: drafted
---
Electric shock happens when someone touches live parts or cables. In inverters and at the grid connection point, the voltages present can be lethal. Damaged equipment, such as defective cables or a damaged enclosure, can put high voltage on parts you can reach. Only operate equipment that has no visible damage, check it regularly and keep its safety equipment accessible and working. Before any work, disconnect the device from all voltage sources, make sure it cannot be reconnected and confirm it is voltage-free. Capacitors can stay charged after the supply is disconnected. Wait the time the manufacturer specifies before opening the cover: 5 minutes for the CPS inverter and 15 minutes for the Sunny Island. During a ground fault, parts of the PV system may still be live. Touch PV cables only on their insulation, stay away from the array frame and substructure, and never connect a string with a ground fault to the inverter. On the Enphase Q and IQ Cable, unused AC connectors are live whenever the system is energized. Cover each one with a sealing cap, and never install the terminator while power is connected. Only qualified personnel should install, troubleshoot or replace microinverters and their cabling. Wear suitable personal protective equipment for all work on the product.
