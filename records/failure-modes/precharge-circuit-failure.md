---
id: fm:precharge-circuit-failure
type: FailureMode
name: Precharge circuit failure
aliases:
- Event 6456
- Error 6456
- Precharging Circuit Defective
claims:
- claim_id: c1
  rel: affects
  target: comp:precharge-circuit
  note: SMA Sunny Central event 6456 reports the DC link pre-charging circuit as defective.
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: Reported for Sunny Central central inverters (SC-XXX-CP-10, SC-XXX-JP, SC CP XT).
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: drafted
  review_note: 'support check: partial - The passages name the Sunny Central and list SC-XXX-CP-10 and
    SC-XXX-JP, but SC CP XT is not mentioned.'
- claim_id: c3
  rel: presents_as
  target: symptom:ac-voltage-mismatch
  note: In the data log, the frequency of the AC voltage metering does not match the grid AC voltage.
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: detected_by
  target: method:fuse-check
  note: Check the pre-charging input fuses and the pre-charging feedback signal at SC20CONT terminals
    X14-8 and X14-9.
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  note: First check whether the inverter has the Q at night function and whether the QoDEna parameter
    is enabled.
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact SMA Service if the fuses and feedback check out OK, or straight away according to the
    operating manual.
  cite:
  - src: src:sma-kb-error-message-6456-precharging-circuit-defective
    loc: sec=h1
    h: ec77417e5497
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
On SMA Sunny Central inverters, event 6456 means the circuit that pre-charges the DC link is defective. In the data log it can show up as a mismatch: the frequency of the AC voltage metering does not match the grid AC voltage. The manual lists the inverter behavior for this event as W. First check whether the inverter has the Q at night function and whether the QoDEna parameter is enabled. Next, check the pre-charging input fuses and the pre-charging feedback signal at SC20CONT terminals X14-8 and X14-9. If those checks find nothing wrong, contact SMA Service.

<!-- review notes
- sentence 4: support check: partial - u1 asks about the Q at night function and QoDEna, but its flow is garbled (a 'No' branch asks about QoDEna), so 'first check whether it has the function and whether QoDEna is enabled' is only roughly stated.
-->
