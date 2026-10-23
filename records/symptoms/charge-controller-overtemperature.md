---
id: symptom:charge-controller-overtemperature
type: Symptom
name: Charge controller overtemperature
aliases:
- Sic1TmpHI
- Sic2TmpHI
- Sic3TmpHI
- Sic4TmpHI
- Overtemperature Sunny Island Charger 1
- Overtemperature Sunny Island Charger 2
- Overtemperature Sunny Island Charger 3
- Overtemperature Sunny Island Charger 4
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Sunny Island shows a level 1 warning per charger: W856 (Sic1TmpHI), W866 (Sic2TmpHI), W876 (Sic3TmpHI),
    W886 (Sic4TmpHI), each described as overtemperature of the matching Sunny Island Charger.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r20
    h: 22318508d624
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=153.r27
    h: 10fd82277cff
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r3
    h: 14100a3d1fb2
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=154.r10
    h: 2e744a077eff
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=78.r5
    h: 75b2d3d25008
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=79.r6
    h: 7b8f75e16756
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=81.r2
    h: 2c3ae1a20500
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=77.r4
    h: 806308158b46
  review: drafted
---
The Sunny Island shows a level 1 warning when one of its connected Sunny Island Charger PV charge controllers reports overtemperature: W856, W866, W876 or W886 for chargers 1 to 4. The manual calls this a device overtemperature of the charge controller, but it says the charger is actually reporting battery overtemperature. For chargers 2, 3 and 4, first check that the Sunny Island Charger is set to the operating mode SMA operation, as described in its installation manual. For charger 1, the manual says to check the charger's DIP switch configuration and to make sure the communication interfaces are correctly inserted in the Sunny Island. In expert mode, each charger's heat sink temperature can be read as a parameter. Use it to see whether the charger itself is running hot. Do not confuse this warning with the matching low-temperature warnings, such as W855 or W865. The manual gives a temperature sensor error or undertemperature as their cause.

<!-- review notes
- sentence 3: support check: partial - The corrective measure to set SMA operation mode is stated for chargers 2-4, but 'first' ordering is not stated (it is the only listed measure).
- sentence 5: support check: partial - Heat sink temperature parameters in expert mode exist for chargers 1, 2, 3 and 4, but the passages don't say to use them to judge whether the charger is running hot.
- sentence 6: support check: partial - W855/865 causes are sensor error or undertemperature as stated, but the passages give no instruction about confusing them with the overtemperature warnings.
-->
