---
id: fm:battery-soc-drift
type: FailureMode
name: Battery state-of-charge estimation drift
aliases:
- SOC recalibration
- SOC deviation
- SOC divergence between modules
- 20 percent calibration
- SOC recalibration to 20 %
- cells drifting apart
- state of charge recalibration
- SOC/SOH deviations
- Recalibration to 20%
claims:
- claim_id: c1
  rel: affects
  target: comp:battery-storage
  cite:
  - src: src:sma-doc-260329
    loc: sec=1.2
    h: 0872223561b6
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:poor-battery-maintenance
  note: Named as a cause of frequent recalibrations of SOC to 20%.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r13
    h: 8435e7d4fcf2
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-doc-278742
    loc: tbl=76.r13
    h: 8435e7d4fcf2
  - src: src:sma-kb-sunny-island-is-performing-a-recalibration-of-the-state-of-charge-to-20
    loc: sec=h1
    h: 662215fdd557
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:component-aging
  note: Aged batteries, including batteries whose SOH has fallen below 80%, trigger 20% recalibrations.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r13
    h: 8435e7d4fcf2
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-kb-sunny-island-is-performing-a-recalibration-of-the-state-of-charge-to-20
    loc: sec=h1
    h: 662215fdd557
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h329
    h: a7834373ece7
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:installation-error
  note: For example, a battery that is not connected correctly.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r13
    h: 8435e7d4fcf2
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-kb-sunny-island-is-performing-a-recalibration-of-the-state-of-charge-to-20
    loc: sec=h1
    h: 662215fdd557
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h329
    h: a7834373ece7
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:inverter-settings
  note: Wrong battery parameters, such as battery type or a nominal capacity entered incorrectly, make
    the estimate less accurate.
  cite:
  - src: src:sma-kb-battery-management-of-the-sunny-island-state-of-charge-soc-recalibration
    loc: sec=h1
    h: b3656a110ae7
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-doc-260329
    loc: tbl=1.r1
    h: 77a47a910be0
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h329
    h: a7834373ece7
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:high-battery-cable-resistance
  note: Battery cable resistance that is too high or poor pole connections can trigger a recalibration.
  cite:
  - src: src:sma-kb-battery-management-of-the-sunny-island-state-of-charge-soc-recalibration
    loc: sec=h1
    h: b3656a110ae7
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h329
    h: a7834373ece7
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:electrolyte-concentration-imbalance
  note: Differing acid concentrations in flooded lead-acid batteries.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h329
    h: a7834373ece7
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:current-measurement-inaccuracy
  note: Ampere-hour counting alone is inaccurate because the starting SOC is unknown and the DC current
    measurement is imprecise.
  cite:
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:non-optimal-charging
  cite:
  - src: src:sma-kb-battery-management-of-the-sunny-island-state-of-charge-soc-recalibration
    loc: sec=h1
    h: b3656a110ae7
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:soc-jump
  note: The device flags a 20% recalibration that changed SOC by more than 10% as a battery error (W222).
  cite:
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-doc-278742
    loc: sec=h917
    h: 90e256c25a24
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:soc-recalibration-event
  note: 'Event 9322 / E224: 20% recalibration being performed.'
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r13
    h: 8435e7d4fcf2
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-doc-278742
    loc: tbl=76.r13
    h: 8435e7d4fcf2
  - src: src:sma-kb-sunny-island-is-performing-a-recalibration-of-the-state-of-charge-to-20
    loc: sec=h1
    h: 662215fdd557
  review: drafted
  review_note: 'support check: partial - Event 9322 and E224 are stated for 20% recalibration, but the
    passages do not explicitly link both numbers as one event.'
- claim_id: c12
  rel: presents_as
  target: symptom:battery-error
  cite:
  - src: src:sma-doc-278742
    loc: sec=h917
    h: 90e256c25a24
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:load-shedding
  note: With a newly connected battery, deviations in the SOC estimate during the first two operating
    hours can cause load shedding.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h508
    h: 738bbc6e6968
  - src: src:sma-doc-259761
    loc: sec=h461
    h: 738bbc6e6968
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:soc-error-monitoring
  note: The BatSocErr parameter gives the estimated error of the displayed SOC.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h327
    h: 2e9d5ed84e19
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=60.r4
    h: 4757a32fa6d2
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:battery-capacity-test
  note: The only way to get actual SOC and SOH, but most applications cannot run it in the field.
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
  review_note: 'support check: partial - Capacity tests give actual SOC/SOH and can''t be done in the
    field for most applications, but the passages don''t present it as a detection method.'
- claim_id: c16
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sma-doc-260329
    loc: tbl=1.r1
    h: 77a47a910be0
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:equalization-charge
  note: The SOC error is lowest after a full or equalization charge.
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h620
    h: f3802cb2769a
  - src: src:sma-doc-260329
    loc: sec=h8
    h: 039ffcdcd5a7
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:battery-parameter-check
  note: Check battery type, nominal capacity and the full-charge and equalization-charge settings.
  cite:
  - src: src:sma-kb-battery-management-of-the-sunny-island-state-of-charge-soc-recalibration
    loc: sec=h1
    h: b3656a110ae7
  - src: src:sma-doc-260329
    loc: tbl=1.r1
    h: 77a47a910be0
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:battery-soc-recalibration
  cite:
  - src: src:sma-doc-260329
    loc: sec=h9
    h: 3395a45567d5
  - src: src:sma-kb-battery-management-of-the-sunny-island-state-of-charge-soc-recalibration
    loc: sec=h1
    h: b3656a110ae7
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h327
    h: 2e9d5ed84e19
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:close-monitoring
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-doc-260329
    loc: sec=4
    h: 8ed186212a25
  review: drafted
---
SOC is never measured directly. The battery inverter estimates it from ampere-hour counting, full-charge detection and voltage-based recalibration, so the displayed value can drift away from the real charge. If the battery voltage drops more sharply than expected during discharge, the inverter resets SOC to 20% to protect the battery from deep discharge, and it logs an event when it does. With a healthy battery and correct settings, small SOC jumps are normal. Frequent 20% recalibrations or jumps of more than 10% point to wrong settings, early battery aging or a battery fault. Common causes are poor maintenance, aged batteries, installation errors, a wrongly entered nominal capacity, high battery cable resistance or poor connections. Watch the estimated SOC error value. It is lowest after a full or equalization charge. Check the battery parameters, especially battery type, nominal capacity and the charge settings. Then start an equalization charge, watch how the system responds, and call the inverter service line or battery maker if needed. A new battery reads far off at first and can cause load shedding in its first operating hours. The estimate then gradually settles toward the real values.
