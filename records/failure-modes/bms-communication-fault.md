---
id: fm:bms-communication-fault
type: FailureMode
name: Inverter-BMS communication fault
aliases:
- CAN COM Fail
- Battery communication error
- CAN interface defect
- BMS communication fault
- CAN interface fails to detect the battery
- COM connector disconnected
- CAN-BUS-Lose
- faulty CAN bus termination
- CAN Fail
- BMS CAN communication fault
- Battery system communication error
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:poor-connector-contact
  note: A loose or badly seated communication cable between inverter and battery can drop the link.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  - src: src:kb-sungrow-how-to-troubleshoot-ec714-bms-communication-fault
    loc: sec=h1
    h: 475873edd6aa
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:communication-bus-fault
  note: A faulty termination on the battery-inverter communication cable is listed as a possible cause.
  cite:
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:installation-error
  note: Wrong wiring of the battery-inverter communication.
  cite:
  - src: src:kb-sungrow-how-to-troubleshoot-ec714-bms-communication-fault
    loc: sec=h1
    h: 475873edd6aa
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:unsuitable-communication-cable
  note: Cable not meeting the manual's requirements, missing cores, or no shielding layer.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  review: drafted
- claim_id: c5
  rel: caused_by
  target: fm:inadequate-earthing
  note: Incorrect grounding of the inverter or battery system.
  cite:
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c6
  rel: caused_by
  target: fm:firmware-defect
  note: Inverter software version not up to date.
  cite:
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:signal-cable-emi
  note: Serious interference on the CAN link.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  review: drafted
  review_note: 'support check: partial - u1 mentions serious interference only as a hardware problem to
    check; it does not say the interference is on the signal cable.'
- claim_id: c8
  rel: caused_by
  target: stressor:battery-switched-off
  note: Battery not powered on or not switched on correctly.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h352
    h: fa95d55eedef
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=h352
    h: fa95d55eedef
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:inverter-settings
  note: Wrong battery model configured on the inverter.
  cite:
  - src: src:solis-solis-kb-s6-bus-check-troubleshooting
    loc: sec=h5
    h: 19991408763b
  - src: src:kb-solis-44002527013-s6-eh3p-5-10-k-h-eu-bms-bus-testing
    loc: sec=h1
    h: 53cfcd3eb62a
  review: drafted
  review_note: 'support check: partial - u14 says to verify the correct battery model is configured when
    alarms appear, but it does not state a wrong model as a cause of the fault.'
- claim_id: c10
  rel: affects
  target: comp:battery-storage
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c11
  rel: affects
  target: comp:inverter
  note: A defect in the inverter's CAN interface on the battery interface module is one possible cause.
  cite:
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  review: drafted
- claim_id: c12
  rel: affects
  target: comp:communication-cable
  cite:
  - src: src:kb-sungrow-how-to-troubleshoot-ec714-bms-communication-fault
    loc: sec=h1
    h: 475873edd6aa
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:communication-loss
  note: CAN communication between inverter and battery is lost.
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: sec=h352
    h: fa95d55eedef
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=h352
    h: fa95d55eedef
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:battery-not-detected
  note: The CAN interface does not detect the connected batteries or backup box; a No Battery alarm may
    appear.
  cite:
  - src: src:solis-solis-kb-s6-bus-check-troubleshooting
    loc: sec=h5
    h: 19991408763b
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:battery-can-interface-test
  note: Loopback test with a test cable; success rate 100 means the inverter's CAN inputs work and the
    fault lies elsewhere.
  cite:
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=7
    h: edeb28b371f9
  - src: src:sma-doc-sbsx-x-10-can-sg-en-10
    loc: sec=3
    h: 09dacb162cca
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:communication-bus-voltage-test
  note: Multimeter check of CAN H and CAN L against ground on the inverter side.
  cite:
  - src: src:solis-solis-kb-s6-bus-check-troubleshooting
    loc: sec=h1
    h: 5ebb90784532
  - src: src:kb-solis-44002527013-s6-eh3p-5-10-k-h-eu-bms-bus-testing
    loc: sec=h1
    h: 53cfcd3eb62a
  review: drafted
- claim_id: c17
  rel: detected_by
  target: method:communication-test
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
  review_note: 'support check: partial - u33 says to perform a communication test via the user interface
    as a corrective measure, but it does not clearly state this as detecting the fault.'
- claim_id: c18
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=62
    h: 60eac848d32b
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=62.r6
    h: af1b9f4fd00a
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  - src: src:kb-sungrow-how-to-troubleshoot-ec714-bms-communication-fault
    loc: sec=h1
    h: 475873edd6aa
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:battery-connection-check
  cite:
  - src: src:solis-solis-kb-s6-bus-check-troubleshooting
    loc: sec=h4
    h: 4634327bc280
  - src: src:kb-solis-44002527013-s6-eh3p-5-10-k-h-eu-bms-bus-testing
    loc: sec=h1
    h: 53cfcd3eb62a
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h393
    h: fa95d55eedef
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:battery-parameter-check
  note: Confirm the correct battery model and communication pins are configured.
  cite:
  - src: src:solis-solis-kb-s6-bus-check-troubleshooting
    loc: sec=h5
    h: 19991408763b
  - src: src:kb-solis-44002527013-s6-eh3p-5-10-k-h-eu-bms-bus-testing
    loc: sec=h1
    h: 53cfcd3eb62a
  review: drafted
  review_note: 'support check: partial - u14 gives the model and pin check, but it only partly covers
    ''communication pins configured''.'
- claim_id: c22
  rel: mitigated_by
  target: mit:communication-bus-termination
  note: Use at least Cat 5e twisted pair, respect maximum length, strip properly, use shielded cabling.
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  - src: src:kb-solis-44002781192-full-alarm-code-maintenance-overview
    loc: sec=h11
    h: ee2da61a2b27
  review: drafted
  review_note: 'support check: partial - u24 lists firmware compatibility among the checks and u35 says
    to update firmware if necessary, but neither says an update resolves the fault.'
- claim_id: c25
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  review: drafted
- claim_id: c26
  rel: mitigated_by
  target: mit:battery-interface-module-replacement
  note: Needed when the CAN functional test shows success rate 0.
  cite:
  - src: src:sma-kb-functional-test-of-can-interface-of-the-sunny-boy-storage
    loc: sec=h1
    h: b20d3ee6952a
  review: drafted
- claim_id: c27
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kb-solis-44002518993-s6-hybrid-series-parallel-function-setup-guide
    loc: tbl=1.r12
    h: f40be2333f68
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h76
    h: 98737cac3bc3
  review: drafted
---
This fault means the inverter has lost CAN communication with the battery management system. It shows up as a CAN Fail, CAN COM Fail or battery communication error alarm, sometimes with a No Battery alarm or a red LED on the inverter. Common causes are a loose or wrongly wired communication cable, an unsuitable or unshielded cable, faulty bus termination, poor grounding, outdated inverter software, or a battery that is switched off. First check that the battery is on, that the cable is seated and wired correctly, and that the correct battery model is set on the inverter. If the alarm stays, measure the CAN H and CAN L voltages against ground at the inverter, or run the manufacturer's CAN interface loopback test. If the loopback test passes, the inverter is not the cause and the fault lies elsewhere in the installation; if it fails, the battery interface module must be replaced through service. Restart the inverter and contact the manufacturer if the fault persists.
