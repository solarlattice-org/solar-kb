---
id: fm:voltage-sensor-fault
type: FailureMode
name: Voltage measurement sensor fault
aliases:
- Vsense Error
- Vsense Err
- DC voltage measurement deviation
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r1
    h: 785d03abb123
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=18.r7
    h: 9a224b5dfec7
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: affects
  target: comp:voltage-sensor
  note: Sources describe an internal voltage sensing circuit or the sensor used to measure DC voltage
    inside the inverter.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r1
    h: 785d03abb123
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=18.r7
    h: 9a224b5dfec7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: presents_as
  target: symptom:measurement-signal-error
  note: Reported by the inverter as a sensor error when measuring DC voltage, or as a deviation in DC
    or grid voltage measurement.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r1
    h: 785d03abb123
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: detected_by
  target: method:inverter-display-check
  note: The Yaskawa SGI-XTM shows the Vsense Error text on its UI and records it in the event log.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: All sources say to contact the manufacturer's service line; an authorized service provider may
    need to service the inverter.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r1
    h: 785d03abb123
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r11
    h: 251d0aca9ea4
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=18.r7
    h: 9a224b5dfec7
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  note: One Yaskawa manual says to switch DC and AC off and then restart the inverter before getting service.
  cite:
  - src: src:yaskawa-sgi-500xt-iom-docr-070254-b
    loc: tbl=18.r7
    h: 9a224b5dfec7
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This fault means the inverter's internal voltage sensing circuit, or the sensor that measures DC voltage, has failed. SMA Sunny Central CP XT inverters report it as error 6427 or 6441, which mean a sensor error in DC voltage measurement. Yaskawa Solectria SGI-XTM inverters show Vsense Error on the user interface and record it in the event log. Other SMA inverters report a related measurement error when the DC or grid voltage reading deviates. On Yaskawa units, switch DC and AC off and restart the inverter. If the fault returns, turn the inverter off. This is an internal hardware fault, so contact the manufacturer's service line. An authorized service provider may need to inspect and service the inverter.

<!-- review notes
- sentence 2: support check: partial - Errors 6427 and 6441 are sensor errors in DC voltage measurement, but the passages never name the Sunny Central CP XT model.
- sentence 3: support check: partial - Vsense Error on the UI and Event Log Y are stated, but the passages don't name the SGI-XTM model.
- sentence 5: support check: partial - u5 gives the off/restart step, but 'if the fault returns, turn the inverter off' is only loosely implied by the second action column.
- sentence 6: support check: partial - Contact service and possible authorized-provider servicing are stated, but 'internal hardware fault' is only implied via internal failure of the sensing circuit.
-->
