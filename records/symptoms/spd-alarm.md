---
id: symptom:spd-alarm
type: Symptom
name: Surge protector alarm
aliases:
- AC-side SPD alarm
- DC-side SPD alarm
- Fault overvoltage protector
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-spd-fault-code
  note: Sungrow reports code 071 for the AC-side SPD and 072 for the DC-side SPD; SMA reports an overvoltage
    protector fault when surge arresters have tripped or are not seated correctly.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r6
    h: ffc90862e4ba
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=52.r7
    h: 8dcb82cff8cf
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h281
    h: 3b4b16a8ddf5
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h198
    h: 3b4b16a8ddf5
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:spd-red-status-led
  note: On the SPD itself, the green LED for a phase or neutral-ground goes out and a red LED comes on,
    which shows protection is compromised or lost.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h51
    h: 3ee4457d2222
  - src: src:eaton-eaton-spd
    loc: tbl=8.r6
    h: 7e445b027d54
  - src: src:eaton-eaton-spd
    loc: tbl=8.r4
    h: 28c46d3ae071
  - src: src:eaton-eaton-spd
    loc: tbl=8.r3
    h: 6ac33fcf20dc
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:spd-surge-event-record
  note: Some SPDs keep a surge counter or log each surge event on screen until an operator acknowledges
    it.
  cite:
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h51
    h: 3ee4457d2222
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h70
    h: 293cadb7a820
  review: drafted
---
The inverter reports this alarm as a fault code: on Sungrow units, 071 means an AC-side SPD alarm and 072 means a DC-side SPD alarm. SMA inverters show an overvoltage protector fault when one or more surge arresters have tripped or are not seated correctly, so check first that every arrester is fully inserted. On the surge protector itself, a green LED that has gone out together with a red LED that is lit, often with an audible alarm, means protection on that phase or on neutral-ground is lost. If a red LED is lit but there is no sound, the alarm was probably silenced, and the fault is still there. The usual cause is a significant surge event, and the fix is to replace the SPD. A surge counter or event log on the device can confirm that a surge happened. A long temporary overvoltage on the grid can also damage the protection. Find and correct the source of the overvoltage before you fit the new SPD. For the Sungrow DC-side alarm, wait for the inverter to return to normal. If it does not, open the AC and DC switches, wait 15 minutes, then close them again to restart.

<!-- review notes
- sentence 2: support check: partial - The SMA fault cause is stated, but the advice to check first that every arrester is fully inserted is not in the passages.
- sentence 4: support check: partial - The passage links red LED with no sound to a silenced alarm after a significant surge, but it does not say outright that the fault is still present; its text is truncated.
- sentence 5: support check: partial - Cause and fix are stated, but the surge counter is not said to confirm that a surge happened; it only counts events.
- sentence 6: support check: partial - Extended TOV as a cause and checking for and correcting TOV sources before replacing the SPD are stated, but 'damage the protection' is only implied by 'compromised or lost'.
-->
