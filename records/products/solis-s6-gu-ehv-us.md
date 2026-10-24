---
id: prod:solis-s6-gu-ehv-us
type: Product
name: Solis S6-GU(250-350)K-EHV-US
aliases:
- S6-GU250K-EHV-US
- S6-GU300K-EHV-US
- S6-GU350K-EHV-US
- S6-250K-EHV-US
- S6-300K-EHV-US
- S6-350K-EHV-US
- S6-GU250K-EHV-US-M12
- S6-GU300K-EHV-US-M12
- S6-GU350K-EHV-US-M12
- S6-GU350K-EHV-US-M16
- S6-250K-EHV-US-M12
- S6-300K-EHV-US-M12
- S6-350K-EHV-US-M12
- S6-350K-EHV-US-M16
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=front
    h: 65d0ffd891c8
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=h186
    h: 15151cd5ed78
  review: drafted
  review_note: 'support check: partial - Evidence shows a ''solis'' label and a certification listing
    with S6-GU models, but doesn''t explicitly state Solis makes them (weakly implied by the name).'
- claim_id: c2
  rel: implements
  target: func:dc-arc-fault-protection
  note: Integrated AFCI listed as YES for each model in the datasheet tables.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r20
    h: 076a45a2637f
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r20
    h: 4f1be8eb99b2
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r20
    h: 0e83d5616989
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r20
    h: f5685915b0e2
  review: drafted
- claim_id: c3
  rel: implements
  target: func:pid-recovery
  note: Integrated PID recovery listed as YES.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r21
    h: 13ec3ed015e1
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r21
    h: 53e4871f537c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r21
    h: eddf8df54faa
  review: drafted
  review_note: 'support check: partial - PID recovery YES for 250, 300, 350-M12 but the M16 model is not
    shown.'
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r37
    h: 70e7513567ac
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r37
    h: 9a4438cfabbf
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r37
    h: a04e3732f7a2
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r37
    h: 41bb0053b781
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:power-line-communication
  note: PLC is listed as an optional communication connection.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r37
    h: 70e7513567ac
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r37
    h: 9a4438cfabbf
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r37
    h: a04e3732f7a2
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r37
    h: 41bb0053b781
  review: drafted
- claim_id: c6
  rel: implements
  target: func:demand-response-modes
  note: The alarm table includes a DRM LINK Fail alarm; the DRM link signal is expected to be normally
    closed.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=15.r7
    h: d4b37f841572
  review: drafted
  review_note: 'support check: partial - The DRM LINK Fail alarm implies DRM support, but no passage explicitly
    states DRM mode support.'
- claim_id: c7
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, stated for 250K-M12, 300K-M12, 350K-M12 and 350K-M16 models
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r1
    h: abb47294867d
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r1
    h: a9c170e36ab7
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r1
    h: 88298515934a
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r1
    h: 2cc4600ebf09
  review: drafted
- claim_id: c8
  attr: rated_output_current
  value:
    nominal: 240.6
    unit: unit:A
  conditions: S6-250K-EHV-US-M12 rated output current
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r13
    h: c4a124be0979
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 251
    unit: unit:A
  conditions: S6-300K-EHV-US-M12 rated output current
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r13
    h: 80fe073e79b0
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 252.6
    unit: unit:A
  conditions: S6-350K-EHV-US-M12 rated output current
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r13
    h: 9c0816cd2581
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions)
- claim_id: c11
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency, S6-300K-EHV-US-M12
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r16
    h: a47e0bad5d3b
  review: drafted
- claim_id: c12
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC efficiency, stated for 250K-M12, 300K-M12, 350K-M12 and 350K-M16 models
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r18
    h: 416d784b5831
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r18
    h: ec595391bea5
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r18
    h: dbc5102a6392
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r18
    h: 5a46cc931ad5
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: efficiency
  value:
    nominal: 98.9
    unit: unit:PERCENT
  conditions: Maximum efficiency, stated for 250K-M12, 300K-M12, 350K-M12 and 350K-M16 models
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r17
    h: 4de86e59a856
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r17
    h: a97374436b5e
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r17
    h: 16e3ef7b64f3
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r17
    h: 86a1026690e7
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions)
- claim_id: c14
  attr: operating_temperature
  value:
    min: -30
    max: 60
    unit: unit:DEG_C
  conditions: Operating ambient temperature range, stated for 250K-M12, 300K-M12, 350K-M12 and 350K-M16
    models
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=19.r26
    h: 89dc7b0a3fba
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=17.r26
    h: 2e308e157aa6
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=16.r26
    h: 74e08337500b
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=18.r26
    h: 43727cb5300d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The Solis S6-GU(250-350)K-EHV-US is a family of three-phase string inverters made by Solis, with four models: 250K-M12, 300K-M12, 350K-M12 and 350K-M16. The certification listing describes them as transformerless, grid-support, utility-interactive PV inverters that are permanently connected. Every model accepts up to 1500 V DC. The 350K-M12 is rated at 1080 V DC and operates from 480 to 1500 V. Rated output current is 240.6 A on the 250K, 251 A on the 300K and 252.6 A on the 350K-M12. The 300K is rated for a 60 Hz grid. Efficiency is listed as 98.9% maximum and 98.5% CEC. The permitted ambient temperature range is -30 to +60 °C. Integrated AFCI (DC arc-fault protection) and PID recovery are built in. Communication is over RS-485, and PLC is available as an option. A DRM LINK Fail alarm points to a fault on the DRM link. To fix it, restart the inverter, check the DRM cables inside and outside the unit, and confirm the signal is normally closed.

<!-- review notes
- sentence 1: support check: partial - The four models are listed, but 'three-phase string inverters' and Solis as maker are not explicitly stated beyond the name.
- sentence 6: support check: partial - AFCI is YES for all four models, but PID recovery evidence omits the M16 model.
- sentence 1: review: partial - The four model names and the Solis brand are in the passages, but nothing quoted calls them three-phase string inverters.
-->
