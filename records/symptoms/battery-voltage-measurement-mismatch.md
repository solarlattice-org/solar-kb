---
id: symptom:battery-voltage-measurement-mismatch
type: Symptom
name: Battery voltage measurement mismatch
aliases:
- Deviation in battery voltage
- Failed plausibility check
- inverter vs BMS battery voltage deviation
- Event 9306
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-bms-battery-voltage-deviation
  note: 'The inverter compares the battery voltage it measures with the value the BMS reports and flags
    a failed plausibility check when the two differ too much. In the field, compare the displayed (communicated)
    value with a meter reading at the battery: a gap above 1.5% points to the inverter''s voltage measurement,
    a gap below 1.5% points to the battery.'
  quote: When comparing the measured battery voltages between inverter and battery management system (BMS),
    an excessive deviation was observed.
  cite:
  - src: src:sma-kb-event-9306-with-sb3600se-10-or-sb5000se-10
    loc: sec=h1
    h: 203da3a4c8d0
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Reported as event 9306 on SMA SB3600SE-10 and SB5000SE-10 inverters.
  cite:
  - src: src:sma-kb-event-9306-with-sb3600se-10-or-sb5000se-10
    loc: sec=h1
    h: 203da3a4c8d0
  review: drafted
---
The inverter flags this when the battery voltage it measures itself differs too much from the voltage reported by the battery management system (BMS). On SMA SB3600SE-10 and SB5000SE-10 inverters it appears as event 9306, a failed plausibility check. First, measure the battery voltage directly with a meter and compare it with the value shown through communication. If the two values differ by more than 1.5%, the inverter's voltage measurement is faulty and the inverter should be replaced. If they differ by less than 1.5%, the battery is the likely cause and should be replaced. Before contacting SMA Service, note the inverter type and serial number, the event number, the battery pack serial number, how long the error has lasted, whether it is sporadic or continuous, and any other error messages. For battery error messages in general, check that the message is plausible before you replace the battery.

<!-- review notes
- sentence 3: support check: partial - Passage says to measure battery voltage and compare with the displayed communicated value, but does not say 'directly with a meter'; this is a minor detail.
-->
