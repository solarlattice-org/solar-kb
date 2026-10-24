---
id: fm:internal-connector-unseated
type: FailureMode
name: Internal connector or ribbon cable unseated
aliases:
- ribbon cable not connected
- internal plug connector disconnected
- board loosened by transport
- communication board connection
claims:
- claim_id: c1
  rel: affects
  target: comp:internal-communication-cable
  note: Flat ribbon cables between internal boards, e.g. the BFS board in an inverter or the display connection
    in a surge protector.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  - src: src:sma-kb-stp-us-4x-checking-ribbon-cables-of-the-bfs-for-no-data-or-communications
    loc: sec=h1
    h: deec4a068bd5
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:communication-module
  note: Ribbon cables run between the communication board and other internal assemblies.
  cite:
  - src: src:sma-kb-stp-us-4x-checking-ribbon-cables-of-the-bfs-for-no-data-or-communications
    loc: sec=h1
    h: deec4a068bd5
  - src: src:sma-doc-sb5gcom-stptlee-10-rm-xx-10
    loc: sec=h52
    h: 94e749ab7b25
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:spd-status-led-off
  note: On one phase of the SPD, neither the green LED nor the red LED is lit.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:communication-loss
  note: The inverter user interface does not show instantaneous values properly, or shows no data or communication.
  cite:
  - src: src:sma-kb-stp-us-4x-checking-ribbon-cables-of-the-bfs-for-no-data-or-communications
    loc: sec=h1
    h: deec4a068bd5
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:installation-error
  note: The ribbon cable is not fully connected or is out of line with its connector.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  review: drafted
  review_note: 'support check: partial - u2 gives the cause as the cable not connected properly or misaligned,
    but nothing calls it an installation error.'
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  note: With the unit de-energized, check that each ribbon cable is lined up with its connector and fully
    seated.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  - src: src:sma-kb-stp-us-4x-checking-ribbon-cables-of-the-bfs-for-no-data-or-communications
    loc: sec=h1
    h: deec4a068bd5
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ribbon-cable-reseating
  note: Take the cable out and plug it back in if it is not fully seated.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r11
    h: '175517297533'
  - src: src:sma-kb-stp-us-4x-checking-ribbon-cables-of-the-bfs-for-no-data-or-communications
    loc: sec=h1
    h: deec4a068bd5
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:connector-latch-verification
  note: After inserting the plug, confirm the lock hooks have closed or snapped audibly into place, and
    make sure the cable is not pinched under an assembly or the lid.
  cite:
  - src: src:sma-doc-sb5gcom-stptlee-10-rm-xx-10
    loc: sec=h52
    h: 94e749ab7b25
  - src: src:sma-video-online-training-sunny-island-7-replacement-of-ac-relay-assembly-board-1176112909
    loc: sec=h1
    h: c764e3f4f4b1
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:correct-latch-release
  note: Before unlocking a ribbon plug, check which way its locking tabs press. Pushing them the wrong
    way can break the tabs and damage the cable.
  cite:
  - src: src:sma-doc-stpsxx-20-kp-rm-xx-11
    loc: sec=h59
    h: cab32f399742
  - src: src:sma-doc-stx-20-acrly-rm-xx-11
    loc: sec=h63
    h: 1534eb8bea4d
  - src: src:sma-doc-stx-intfan-rm-xx-11
    loc: sec=h60
    h: 1534eb8bea4d
  review: drafted
  review_note: 'support check: partial - Passages warn about breaking tabs by pressing them the wrong
    way, but do not link this to mitigating an unseated connector.'
---
This fault is an internal ribbon cable or plug connector that is not fully seated or is out of line with its mating connector inside an inverter or surge protector. On a surge protector, it can show as one phase with neither the green nor the red status LED lit. On an inverter, the user interface may not show instantaneous values properly, or may show no data or communication. Disconnect the unit from all voltage sources and wait. Confirm there is no voltage at the AC and DC terminals, then open it and check that the ribbon cables are fully seated. Make sure each cable is lined up with its connector and pushed fully home. Remove and reseat it if needed. When reconnecting, confirm the lock hooks close or click into place, and keep the cable from being pinched under assemblies or the lid. Before unlocking a ribbon plug, check which way its locking tabs press. Pushing them the wrong way can break the tabs and damage the cable.
