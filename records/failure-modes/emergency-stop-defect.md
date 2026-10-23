---
id: fm:emergency-stop-defect
type: FailureMode
name: Emergency stop circuit defect
aliases:
- Defective fast stop
claims:
- claim_id: c1
  rel: affects
  target: comp:emergency-stop
  note: SMA Sunny Central CP-XT error 9019 reports a defective fast stop.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r11
    h: 7d76c721dadc
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39
    h: 763d9267b674
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: presents_as
  target: symptom:emergency-stop-triggered
  note: The inverter can show an emergency stop status when the button was not pressed. The manual lists
    an internal inverter fault as the other possible cause.
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=23
    h: 70ec326e8f54
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:emergency-stop-function-test
  note: Operate each emergency switch, both on the cabinet and external ones. In normal operation both
    signal lights on the emergency stop relay should be lit, and they should go off when a switch or door
    contact is opened. In Team configurations the relay must switch in every cabinet.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=h79
    h: 1111c4350569
  - src: src:sma-sc-wa-en-31
    loc: sec=h78
    h: 056c2ff6c6f8
  - src: src:sma-sc-wa-en-31
    loc: sec=h77
    h: db5684d202c6
  - src: src:sma-sc-wa-en-31
    loc: sec=h83
    h: 7414a16d90c5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  note: When output is abnormal, check what state the emergency stop button is in.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: sec=11.2
    h: ad4454644a7d
  review: drafted
  review_note: 'review: partial - The Sungrow passage says to check the state of the emergency stop button
    when power output is abnormal, but that is a check on whether the button is engaged, not a stated
    way to detect a defect in the circuit.'
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: For error 9019, the corrective measure is to check the fast stop cabling.
  quote: Check the fast stop cabling.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r11
    h: 7d76c721dadc
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39
    h: 763d9267b674
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact after-sales service if the emergency stop status remains after the button has been reset.
  cite:
  - src: src:chint-cps-100kw-legacy-user-manual
    loc: tbl=23
    h: 70ec326e8f54
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This failure is a defect in the emergency stop circuit, also called the fast stop. On SMA Sunny Central CP-XT inverters it is reported as error 9019. The inverter can show an emergency stop status even when no one has pressed the button, and an internal inverter fault is one listed cause. Before going further, check that the emergency stop button really is released. For error 9019, the manual says to check the fast stop cabling. Test each emergency switch, on the cabinet and outside it. With the circuit healthy, both signal lights on the emergency stop relay should be lit, and they should go off when a switch is operated. In plants where several inverters run in a Team configuration, the emergency stop relay must switch in every cabinet. If the stop status is still there after the button is reset, contact the manufacturer's service center.

<!-- review notes
- sentence 1: support check: partial - Error 9019 is 'Defective fast stop', but the passages do not say that 'fast stop' is another name for the emergency stop circuit, and 'CP-XT' is not mentioned.
- sentence 1: review: partial - Error 9019 'Defective fast stop' is stated, but the passages never say that fast stop is another name for the emergency stop circuit, and CP-XT appears only in the source id.
-->
