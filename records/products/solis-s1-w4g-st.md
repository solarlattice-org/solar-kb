---
id: prod:solis-s1-w4g-st
type: Product
name: Solis S1-W4G-ST data logging stick
aliases:
- S1-W4G-ST
- S1-W4G-ST-4PIN
- S1-W4G-ST-USB
- S1-W4G-ST (4 Pin)
category: Monitoring and communications
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:kb-solis-44002762194-troubleshooting-s1-w4g-st-datalogger-network-connection-errors
    loc: sec=front
    h: f703e49896a7
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: sec=h1
    h: 8eb0a6e5c4d6
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:wifi
  note: 2.4 GHz Wi-Fi per the inverter manual table
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: sec=h1
    h: 8eb0a6e5c4d6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=17
    h: 5baddca7780d
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:cellular
  note: 'Cellular carriers listed: Sprint, Verizon, T-Mobile; described as Wi-Fi with cellular backup'
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: sec=h1
    h: 8eb0a6e5c4d6
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=17
    h: 5baddca7780d
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=6.2.2
    h: 539df07c76b3
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:bluetooth
  note: BLE 4.2 used for near-end communication
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: tbl=4.r8
    h: 970d0b87a4a8
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:solis-epm
  scope:
    products:
    - prod:solis-epm
  conditions: 4-pin version plugged into the EPM 4-pin communication port, not into the inverter
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=h63
    h: c7ef4f99c4f1
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:solis-s6-eh1p-h-us
  conditions: USB version only; the USB version supports only these models
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: tbl=4.r2
    h: dc1eaf71914b
  review: drafted
- claim_id: c8
  rel: incompatible_with
  target: prod:solis-s6-eh1p-h-us
  conditions: 4-pin version supports all Solis models except these
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: tbl=4.r2
    h: dc1eaf71914b
  review: drafted
  review_note: 'support check: partial - The 4-pin version is stated to exclude those models, but the
    statement says the logger as a whole is incompatible, and the USB version is compatible with them.'
- claim_id: c9
  rel: certified_to
  target: std:ce-marking
  conditions: Both 4-pin and USB versions
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: tbl=4.r25
    h: 48fa68c64b5a
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:fcc-equipment-authorization
  conditions: Both 4-pin and USB versions; listed as FCC
  cite:
  - src: src:solis-manual-solis-s1-w4g-st-v3-2-20250806
    loc: tbl=4.r25
    h: 48fa68c64b5a
  review: drafted
---
The S1-W4G-ST is a Solis external data logger stick that sends system data for remote monitoring over Wi-Fi, with cellular as a backup. It is sold in two versions, a 4-pin version and a USB version, and both log data every 5 minutes. The 4-pin version works with every Solis model apart from the S6-EH1P(3.8-11.4)K-H-US, and the USB version works only with that model. When an Export Power Manager is installed, plug the 4-pin logger into the EPM's communication port and not into the inverter. It uses Bluetooth Low Energy 4.2 for local setup, and it is one of the loggers supported for SolisCloud commissioning. It runs on a 5 V DC supply, draws no more than 5 W, has a NEMA 4X enclosure and carries CE and FCC certification. Solis has a knowledge base article on troubleshooting network connection errors on this logger.

<!-- review notes
- sentence 1: support check: partial - Wi-Fi with cellular backup and Solis logger are supported, but the passages do not state that it sends system data for remote monitoring beyond the manual title, which is close enough; the 'stick' form is not explicit.
- sentence 1: review: partial - The passages back a Solis external Wi-Fi and cellular data logger for remote system monitoring with cellular as backup, but the cited text never calls it a 'stick'.
-->
