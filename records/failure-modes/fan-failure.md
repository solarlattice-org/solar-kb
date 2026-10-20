---
id: fm:fan-failure
type: FailureMode
name: Fan failure
aliases:
- ExtFanErr
- Fan Fail
- Cooling fan failure
claims:
- claim_id: c1
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r7
    h: d0b0f2d02d90
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r3
    h: e1cf6ecb59de
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:fan-obstruction
  note: The fan is blocked, for example by foreign objects on the blades.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r8
    h: e319683e4bbb
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:component-aging
  note: The fan has reached the end of its service life.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r8
    h: e319683e4bbb
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:poor-connector-contact
  note: Poor contact at the fan socket connector.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r8
    h: e319683e4bbb
  review: drafted
- claim_id: c6
  rel: leads_to
  target: fm:inverter-overheating
  note: Without working fans the inverter is not cooled properly, and it can derate because of temperature.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r3
    h: e1cf6ecb59de
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:fan-fault-alarm
  note: Shown as ExtFanErr on CPS inverters and as Fan Fail on Solis inverters.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:visual-inspection
  note: Check whether the fan is spinning and whether foreign objects are on the blades.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  review: drafted
  review_note: 'support check: partial - u1 mentions ''by visual check'', u2 says to check for foreign
    objects on the blades, and u9 says to check whether the fan is spinning. The passages do not explicitly
    describe visual inspection as a detection method.'
- claim_id: c9
  rel: detected_by
  target: method:inverter-display-check
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:fan-supply-voltage-check
  note: Measure across the red and black wire pins at the fan connector while the fan is not spinning.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  review: drafted
- claim_id: c11
  rel: distinguished_from
  target: fm:internal-power-supply-fault
  by: method:fan-supply-voltage-check
  note: If the fan is stopped and its supply voltage is below 6 VDC, the fault is inside the inverter
    and the inverter should be replaced. If the voltage is above 6 V, the fan is at fault and should be
    replaced. If the fan spins but the alarm stays on, the sensing circuit is faulty.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  review: drafted
  review_note: 'support check: partial - The voltage thresholds and the sensing circuit case are stated.
    The passages do not mention an ''internal power supply fault'' concept, only replacing the inverter
    when the voltage is low.'
- claim_id: c12
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: Remove foreign objects from the fan blades or clean the fan.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:inverter-restart
  note: Turn the external AC disconnect off and back on to reboot the system.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:fan-replacement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=7.2
    h: 08034ea4d7bf
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Applies when the fan supply voltage is low or the sensing circuit is faulty.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r1
    h: 2884c89a5021
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r1
    h: 2884c89a5021
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=33.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=4.r3
    h: 432cb92c3d99
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=57.r3
    h: 432cb92c3d99
  review: drafted
---
Fan failure means the inverter's cooling fan has stopped working properly. Common causes are a blocked fan, a fan at the end of its service life, or poor contact at the fan socket connector. The inverter shows a fan alarm on its display: ExtFanErr on CPS units or Fan Fail on Solis units. Without working fans the inverter is not cooled properly, which can lead to temperature derating. First, wait about 5 minutes to see if the alarm clears by itself. Then check the fan blades for foreign objects and reboot the inverter using the external AC disconnect. If the alarm stays on while the fan is spinning, the sensing circuit is faulty and the inverter should be replaced. If the fan is not spinning, measure the voltage between the red and black wire pins at the fan connector. Below 6 VDC means the inverter should be replaced. Above 6 V means the fan should be replaced. Before you clean or replace a fan, switch off the grid, the AC power and the DC switch, then wait at least 15 minutes before removing the fan assembly. If none of these steps clears the fault, contact the manufacturer's after-sales service.

<!-- review notes
- sentence 5: support check: partial - The passages say to replace the inverter because the sensing circuit has a problem when the fan is spinning with ExtFanErr displayed. They add a condition that output power is above 50% of rated, which the statement omits.
- sentence 6: support check: partial - The voltage thresholds and replacement actions are stated. The passages add a condition that output power is above 50% of rated, which the statement omits.
-->
