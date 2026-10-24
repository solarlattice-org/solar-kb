---
id: concept:thermal-derating
type: Concept
name: Thermal derating
aliases:
- temperature derating
- output derating at high ambient
- overtemperature derating
- Over-Temperature Derating
- high temperature derating
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: explains
  target: symptom:inverter-power-derating
  note: Adverse environmental conditions such as high ambient temperature are one listed cause of inverter
    power reduction.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=3.7
    h: 905d4a97525a
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=3.7
    h: 822f4c06dd80
  - src: src:eq-equip-inverters-sungrow-sungrow-sg125hv-uen-manual
    loc: sec=h53
    h: f6edd1c7148f
  review: drafted
- claim_id: c2
  rel: related_to
  target: state:derating
  note: Derating is a controlled performance reduction, usually depending on component temperatures, used
    to avoid a full shutdown.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h632
    h: f76b798a6e57
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:inverter-cooling
  note: Derating takes over when the cooling system cannot remove enough heat from internal components.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:inverter-overheating
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=6.r28
    h: 36ac9eb68a94
  - src: src:kb-sungrow-how-to-solve-the-inverter-overtemperature-derating
    loc: sec=h1
    h: 63d12e4af068
  review: drafted
- claim_id: c5
  rel: related_to
  target: stressor:high-temperature
  scope:
    products:
    - prod:chint-sch-350ktl
    - prod:yaskawa-solectria-pvi-20-25tl-480-r
    - prod:chint-sca-50-60ktl
  note: Manuals state output begins to derate when ambient exceeds 45°C (113°F).
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=9.2.3
    h: 2bdbfd303a55
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h178
    h: c28885eae849
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=10.3.1
    h: 1391406b53e3
  - src: src:eq-equip-inverters-sungrow-sungrow-sg125hv-uen-manual
    loc: sec=h53
    h: f6edd1c7148f
  review: drafted
- claim_id: c6
  rel: related_to
  target: stressor:high-altitude
  note: Thinner air cools less well, so maximum output is limited earlier and more steeply at higher sites.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=33.r3
    h: bc3c13e7aad2
  - src: src:eq-equip-inverters-solectria-xgi-1500-xgi-1500-166-manual-rev-p-17-oct-2022
    loc: sec=h138
    h: 95e3472bee58
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h147
    h: 12f53f4c5d91
  review: drafted
- claim_id: c7
  rel: related_to
  target: fm:fan-failure
  note: Fan failure is listed as a derating cause; checking fan operation is a recommended step for overtemperature
    derating.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=3.7
    h: 822f4c06dd80
  - src: src:kb-sungrow-how-to-solve-the-inverter-overtemperature-derating
    loc: sec=h1
    h: 63d12e4af068
  review: drafted
- claim_id: c8
  rel: related_to
  target: mit:clear-ventilation-blockage
  note: Derating from internal overtemperature at non-critical ambient may indicate cooling filters need
    cleaning.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:kb-sungrow-how-to-solve-the-inverter-overtemperature-derating
    loc: sec=h1
    h: 63d12e4af068
  review: drafted
  review_note: 'support check: partial - Transcript says internal overtemperature with normal ambient
    suggests cooling issues and cleaning filters; ''clear ventilation blockage'' is only loosely matched,
    though ventilation check is mentioned.'
- claim_id: c9
  rel: related_to
  target: method:ambient-temperature-check
  cite:
  - src: src:kb-sungrow-how-to-solve-the-inverter-overtemperature-derating
    loc: sec=h1
    h: 63d12e4af068
  review: drafted
- claim_id: c10
  rel: related_to
  target: meas:temperature-derated-output
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h147
    h: b928486f8520
  review: drafted
---
Thermal derating means the inverter lowers its own output power on purpose when ambient or internal temperatures get high. It is a protection feature, not a fault: by limiting maximum output, the inverter keeps sensitive parts such as IGBTs and filter components within safe limits and avoids shutting down completely. Many string inverter manuals state that output starts to derate once ambient temperature passes 45°C (113°F), and each manual gives a derating curve for its model. In one central inverter example, full output holds up to 35 degrees Celsius ambient, and the unit still delivers roughly 90% of rated power up to about 50 degrees before it cuts output sharply. At high altitude the thinner air cools less well, so derating starts earlier; one manual specifies derating above 2000 m. Derating can also be triggered by internal temperature sensors on power stacks and controller boards, not only by ambient temperature. If logs show overtemperature derating while ambient temperature is normal, check the inverter cooling: clean filters, confirm the fans run, and look for poor ventilation or direct sun on the unit.

<!-- review notes
- sentence 3: support check: partial - Three manuals state 45°C/113°F with curves, but 'many string inverter manuals' and each giving a curve is a generalization beyond the sample shown.
-->
