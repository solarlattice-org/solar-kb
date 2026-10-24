---
id: prod:solis-s6-eh2p-l-us
type: Product
name: Solis S6-EH2P(9.6-16)K-SV-YD-L-US
aliases:
- S6-EH2P9.6K03-SV-YD-L-US
- S6-EH2P10K03-SV-YD-L-US
- S6-EH2P11.4K03-SV-YD-L-US
- S6-EH2P12K03-SV-YD-L-US
- S6-EH2P14K03-SV-YD-L-US
- S6-EH2P16K03-SV-YD-L-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=front
    h: 65d0ffd891c8
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 9.6
    unit: unit:KiloW
  conditions: Nameplate rating, 9.6 kW model; also the maximum AC output to grid and backup combined
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5.r1
    h: 4a07641050df
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions)
- claim_id: c3
  attr: rated_power
  value:
    nominal: 11.4
    unit: unit:KiloW
  conditions: Nameplate rating, 11.4 kW model; also the maximum AC output to grid and backup combined
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5.r2
    h: a4b0283c6f16
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 12
    unit: unit:KiloW
  conditions: Nameplate rating, 12 kW model; also the maximum AC output to grid and backup combined
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions)
- claim_id: c5
  attr: rated_power
  value:
    nominal: 14
    unit: unit:KiloW
  conditions: Nameplate rating, 14 kW model; also the maximum AC output to grid and backup combined
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: rated_power
  value:
    nominal: 16
    unit: unit:KiloW
  conditions: Nameplate rating, 16 kW model; also the maximum AC output to grid and backup combined
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5.r5
    h: 99e9d09c38c3
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  rel: implements
  target: func:backup-power
  note: Datasheet table gives a maximum AC output power shared by the grid and backup ports.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=5
    h: d985f1a307e3
  review: drafted
  review_note: 'support check: partial - Table shows AC output power to both grid and backup, implying
    backup output, but backup power function isn''t explicitly stated.'
- claim_id: c8
  rel: implements
  target: func:dc-arc-fault-protection
  note: An AFCI self-test runs; a failed test shows the AFCI-Check message.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r4
    h: 2083a226e468
  review: drafted
- claim_id: c9
  rel: implements
  target: func:dc-injection-limitation
  note: DCInj-FAULT is raised when the DC component of the output current goes over the limit.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r1
    h: 69c05042a23a
  review: drafted
---
The Solis S6-EH2P(9.6-16)K-SV-YD-L-US is a Solis inverter family. The applicable models listed are the 9.6, 11.4, 12, 14 and 16 kW versions. Each model's nameplate rating is also its maximum AC output power, shared between the grid and backup ports. According to the datasheet table, the inverter can carry two times its rated power for 10 seconds. The inverter runs an AFCI self-test. If the test fails it shows AFCI-Check, and the first step is to restart the system and see whether the fault comes back. DCInj-FAULT means the DC component of the output current is over the limit. Check the grid and the AC cable connections, then restart. BatName-FAIL means the battery brand selected does not match the battery actually installed. 12Power-FAULT is a 12 V undervoltage failure, so check the grounding and look for wires leaking current to ground. The manual includes an SGS certificate of compliance, number SGSNA/25/GZ/00140.

<!-- review notes
- sentence 3: support check: partial - The table fragment says 2 times rated power, 10 s, but the context (carrying/overload, which parameter) is only fragmentary.
- sentence 6: support check: partial - BatName-FAIL is supported, but 12Power-FAULT is stated as 12V undervoltage with leakage/grounding check, which matches; however 'wrong battery brand selection' vs 'battery model selection' is slightly different wording only, so core fits with minor paraphrase.
-->
