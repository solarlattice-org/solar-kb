---
id: symptom:inverter-shutdown
type: Symptom
name: Inverter shutdown
aliases:
- Automatic shutdown
- Key-shutdown
- Rapid Shutdown
- Not operating
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-power-at-irradiance
  note: In the fault state the inverter stops operating and opens its AC relay. Automatic shutdown also
    happens when the grid fails or the ambient temperature is out of range, even when PV input is available.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=36
    h: a8727ce09c50
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=5.2
    h: 6b85a3d0c0b9
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=6.2
    h: a23f18f42f30
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: sec=6.7
    h: 297ee1f2537c
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: The inverter logs an insulation or ground fault. Production does not resume until the installer
    corrects the fault. This tends to appear after rain or with morning dew.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=21.r1
    h: 1cbe041ab521
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h131
    h: '6465313e8638'
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h178
    h: 280ff65da917
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h261
    h: 280ff65da917
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:ac-power-step-drop
  note: A Rapid Shutdown event or a fault disconnects the AC side, so output drops abruptly.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=36
    h: a8727ce09c50
  review: drafted
---
An inverter shutdown means the inverter stops converting power and feeding the grid. In the fault state it also opens its AC relay and displays the fault information. Inverters shut down on their own when PV voltage and power fall below the set values, when the AC grid fails, or when the ambient temperature is outside its normal range. Before treating a shutdown as a defect, rule out intended stops. These include a manual OFF or shutdown command from the display or app, a triggered Rapid Shutdown, and a power limit set to zero. Loss of electrical insulation is a likely cause when the shutdown happens after rain or with morning dew and the inverter logs a low insulation or ground fault. After an insulation or grounding fault, the installer has to correct the fault before the inverter will produce power again. The fault can be confirmed by measuring the insulation resistance under dry or wet conditions. Inverter overheating is more likely when the ambient temperature is high, a fan is blocked, or there is not enough airflow around the inverter. Inverter temperature readings help pick out this cause. When an inverter has stopped operating completely, restart it first. Then check components and connections with IR thermography and Voc measurements, replace defective or abnormally hot parts, and update the software.

<!-- review notes
- sentence 3: support check: partial - Manual shutdown and Rapid Shutdown are covered, and a switch for stopping at 0% power limit exists, but the passages do not state the advice to rule out these intended stops before treating a shutdown as a defect.
- sentence 7: support check: partial - The passage lists restart, IRT/VOC checks, replacing defective or abnormally hot parts and software update, but does not state the ordering (restart first, then check) as a sequence.
-->
