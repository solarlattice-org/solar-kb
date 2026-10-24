---
id: func:pid-recovery
type: Function
name: PID recovery
aliases:
- anti-PID
- PID protection
- PID offset
- PID repair
- PID night recovery
- Integrated PID recovery
category: Protection
function_kind: protection
claims:
- claim_id: c1
  attr: default_value
  value:
    nominal: 500
    unit: unit:V
  scope:
    products:
    - prod:sungrow-sg-cx-us
  conditions: PV string-to-ground voltage once PID recovery is enabled; can be changed in the App
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: sec=h44
    h: c0d03f1c41fe
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: sec=h45
    h: c0d03f1c41fe
  review: drafted
- claim_id: c2
  attr: default_value
  value:
    nominal: 500
    unit: unit:V
  scope:
    products:
    - prod:sungrow-sg250hx
  conditions: PV string-to-ground voltage once PID recovery is enabled
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=h61
    h: 4c06266c0dd2
  review: drafted
- claim_id: c3
  rel: requires
  target: prod:sungrow-emu200
  scope:
    products:
    - prod:sungrow-sg350hx
  note: Anti-PID and PID recovery listed as optional via EMU200 on SG350HX-US
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r14
    h: 79b867c21527
  review: drafted
  review_note: 'support check: partial - Passage shows Anti-PID and PID recovery is optional (EMU200)
    on SG350HX-US, but ''requires'' is stronger than ''optional''.'
- claim_id: c4
  rel: requires
  target: func:night-reactive-power
  scope:
    products:
    - prod:sungrow-sg250hx
  negated: true
  note: PID repair cannot run at the same time as night reactive power generation
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=h61
    h: 4c06266c0dd2
  review: drafted
---
PID recovery fixes potential induced degradation in PV modules. At night, when the array is not producing, the inverter applies a compensating voltage between the PV strings and ground. IEA PVPS reports that recovery works if PID is caught early, but it should be confirmed by monitoring. Advanced PID may take months or years to recover, and replacing the modules may be the better fix. Before enabling PID recovery, check the module manufacturer's required polarity to ground. A wrong voltage scheme can stop the function from working or even damage the modules. The Sungrow inverters report a PID abnormity state if the insulation impedance is abnormal or the function cannot run properly after it is enabled.

<!-- review notes
- sentence 2: support check: partial - Early recovery, monitoring and months/years with replacement are stated, but the passage doesn't attribute it explicitly to IEA PVPS and 'may be the better fix' is softer than 'suggesting in any case replacement'.
-->
