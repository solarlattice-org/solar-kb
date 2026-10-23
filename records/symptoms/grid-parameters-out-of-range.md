---
id: symptom:grid-parameters-out-of-range
type: Symptom
name: Grid parameters out of range
aliases:
- Grid Fail
- W003
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: W003 is raised when, during normal operation, grid voltage goes beyond operator-set limits, including
    unstable voltage that is too low or too high.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: An unstable grid frequency is one trigger for W003. Other vendors report a separate fault for
    abnormal grid frequency.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r2
    h: 22c6c28d3439
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=35.r2
    h: 2814ecbc7c19
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:zero-ac-grid-voltage
  note: When grid voltage is absent, the inverter changes to Missing Grid. While Missing Grid is shown,
    the alarm contact stays at rest.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h226
    h: 2fd670a1318a
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=h167
    h: ffc2bb62205a
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:grid-voltage-rise-with-power
  note: If the voltage rises while the inverter is connected, the line or grid impedance is high.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=50.r1
    h: 095289612c19
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:ten-minute-average-overvoltage
  note: 'This is the related E036 condition: grid voltage averaged over 10 minutes is outside the permitted
    range. The inverter limits power first and disconnects if the voltage does not settle.'
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:overvoltage-power-derating
  note: The inverter reduces output automatically when grid voltage is too high or too low.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=56.r3
    h: e0c1ecd44612
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h57
    h: 0984ac48be5b
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: sec=h44
    h: e9fe29d4a796
  review: drafted
---
The inverter reports a grid warning, for example W003 Grid Fail with a yellow LED, when grid voltage or frequency goes beyond the limits set by the operator during normal operation. Possible triggers are an absent grid voltage, after which the inverter shows Missing Grid, an unstable voltage that is too low or too high, or an unstable grid frequency. The alarm relay switches while W003 to W007 are present and resets when the signal ends, because checking the grid is normal operation and not an alarm state. Check the grid voltage first at the inverter and then at the supply point. If it is absent at both, the problem is on the grid side. If the voltage rises only while the inverter is exporting, or is high at the supply, the line or grid impedance is high. Ask the utility to adjust the voltage, and change inverter limits only with their approval and with customer assistance. If the voltage at the supply point is much lower than at the inverter, the line between the inverter and the contactor needs attention. If voltage stays high, the inverter may first reduce output power and later disconnect if a 10-minute average stays out of range. Check whether the protection settings suit the selected grid standard.

<!-- review notes
- sentence 4: support check: partial - The passages say to check at the inverter and then at the supply point if absent, but they do not say that absence at both means the problem is on the grid side.
- sentence 5: support check: partial - High impedance and asking the operator to adjust voltage are stated, but 'utility' is not named, and 'only while exporting' is a stronger reading than 'tends to rise when connected'.
- sentence 7: support check: partial - Power limiting then disconnection on a 10-minute average is stated, but checking protection settings against the grid standard is only loosely supported (the standard-dependent U< and U> values, and the Sungrow protection-parameter check for underfrequency).
-->
