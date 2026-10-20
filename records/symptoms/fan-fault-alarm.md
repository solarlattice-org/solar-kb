---
id: symptom:fan-fault-alarm
type: Symptom
name: Fan fault alarm
aliases:
- Fan alarm
- ExtFanErr
- fan anomaly
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-temperature-high
  note: Sungrow tells you to check for the 070 fan alarm when the power module (fault 036) or the inverter
    interior (fault 037) runs too hot. If the fan alarm is present, the fix is to replace the fans. This
    links the fan alarm to overheating but does not prove that every fan alarm causes it.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r5
    h: a74a3da25ad0
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=51.r1
    h: fb5c20da466e
  review: drafted
---
The inverter raises a fan alarm when its cooling fan fails. Sungrow reports it as code 070, and CPS and Solectria inverters report it as ExtFanErr. The manuals give three likely causes: the fan is blocked, the fan has reached the end of its service life, or the fan socket connector has poor contact. Start by watching the alarm for a few minutes to see if it clears by itself. Then look for foreign objects on the fan blades and remove any debris. If the alarm stays on, restart the system by switching the external AC disconnect off and on again. If that does not fix it, contact the manufacturer's service team. If the fan does not run properly, shut down and disconnect the inverter, then replace the fan. A fan alarm can go with high power module or internal temperature faults. When those faults appear, check for the fan alarm too, and clean the air ducts and shade the inverter from direct sun.

<!-- review notes
- sentence 6: support check: partial - Faults 036/037 do say to check for the 070 alarm, clean the air ducts and shade the inverter, but the passages do not state that a fan alarm 'can go with' those faults as a co-occurrence; they only list it as a check.
-->
