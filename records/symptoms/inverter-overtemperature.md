---
id: symptom:inverter-overtemperature
type: Symptom
name: Inverter overtemperature
aliases:
- TempOver
- Over-temperature protection
- OverTemp
- Overheating (temperature derating)
- Inverter Overheating
- Excessively High Ambient Temperature
- Power Electronics Over Temperature
- Active power limit Temperature
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-temperature-high
  note: The inverter's own temperature reading, or an enclosure sensor added if the inverter does not
    report one, shows overheating. Logging it also lets you judge how well the ventilation works.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h187
    h: 7b8d5092eced
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.10.5
    h: 7a4c1a4979ff
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:temperature-derated-output
  note: CPS SCA36/50/60KTL manuals state output derating starts once ambient temperature passes 45 C.
    SMA flags a temperature power limit after more than 10 minutes of reduced output.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=10.3.1
    h: 1391406b53e3
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=h115
    h: 8bc1b806331d
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h284
    h: 5d84ec3d5090
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h201
    h: 5d84ec3d5090
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: The inverter raises a TempOver or OverTemp protection alarm on its display.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=35.r7
    h: 25366f44879a
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  review: drafted
  review_note: 'support check: partial - TempOver/OverTemp protection alarms are stated, but display or
    indicator light presentation is not explicitly described.'
---
The inverter raises an over-temperature protection alarm when the ambient air or its internal temperature gets too high. In monitoring data, look at the inverter's internal temperature reading next to its output power. Output is reduced, or derated, while the temperature stays high. On CPS SCA36/50/60KTL inverters, output derating begins once ambient temperature goes above 45 C. Common causes are poor inverter installation, a failed cooling fan, dust blocking heat dissipation, or wrong inverter programming. A fan at the end of its service life or a fan plug with a poor connection can also cause overheating. First check that ambient temperature is inside the rated range, that the air inlet, outlet and fan are clear, that installation spacing and location are correct, and that the inverter is not in direct sun. If the alarm does not clear by itself after about 30 minutes of observation, contact the manufacturer's service. Do not mistake this for voltage floor losses, which also show up in hot periods. Those look like underperformance or clipping and are confirmed by reviewing DC voltage, not inverter temperature.

<!-- review notes
- sentence 2: support check: partial - Passages support logging inverter temperature and temperature-related power reduction, but not explicitly comparing the two or derating while temperature stays high.
- sentence 8: support check: partial - Voltage floor losses in hot periods resembling clipping or underperformance, and reviewing DC voltage, are stated, but nothing about not confusing them with overtemperature or not using inverter temperature to confirm.
-->
