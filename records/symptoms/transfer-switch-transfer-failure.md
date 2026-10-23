---
id: symptom:transfer-switch-transfer-failure
type: Symptom
name: Transfer switch transfer failure
aliases:
- TransfNotOpn
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Generac PWRcell wiring error 0X7726 means the inverter ATS did not return to the utility position
    (arm UP); 0X7727 means it did not move to the backup source position (arm DOWN).
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r5
    h: efb1b731f4b0
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r6
    h: 78ba8f6cf7da
  - src: src:sma-doc-259761
    loc: tbl=70.r5
    h: 5d6438cd400a
  - src: src:sma-doc-278742
    loc: tbl=74.r5
    h: 5d6438cd400a
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=65.r1
    h: 2e0a7ce5b630
  review: drafted
---
A transfer failure means the automatic transfer switch did not move to the expected position when the system switched between utility and backup power. On Generac PWRcell inverters it shows up as wiring error 0X7726, where the switch did not return to the utility position with the manual arm UP, or 0X7727, where it did not move to the backup position with the arm DOWN. For 0X7726, first check the wiring to the N terminals of the inverter ATS, the Cat 5 control cable at both ends, and that the factory wiring at the closing coils and relays is tight. For 0X7727, check the wiring to the E terminals and the Cat 5 control cable, and confirm that the inverter AC grid terminals connect on the load side of the inverter ATS. Also confirm that the inverter setting NumTranSwtchs matches the number of transfer switches actually installed. On SMA Sunny Island systems, a transfer relay that does not open is reported as event 7718 or F605. Check that the bypass switch is in the Sunny Island operating position and that AC1 and AC2 are not bridged. Before you work on the utility side of the transfer switch, turn the utility supply off. You can then test switching by simulating a grid failure and watching whether the contactors drop out and pick up as expected.

<!-- review notes
- sentence 5: support check: partial - NumTranSwtchs setting matching installed ATS count is stated, but only in the context of code 0X7721 (ATS detected but not configured), not for the transfer failure codes.
- sentence 6: support check: partial - Event 7718 and F605 and the bypass-switch check are supported, but the AC1/AC2 not-bridged check appears only for 7718, not F605, and F605 is not stated as same event.
-->
