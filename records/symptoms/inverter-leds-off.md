---
id: symptom:inverter-leds-off
type: Symptom
name: Inverter status LEDs off
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-dc-input-voltage
  note: On a Solis inverter an unlit POWER light means no or low DC power. A CPS troubleshooting table
    says to check PV input voltage and polarity when neither the Power LED nor the LCD lights up.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=3
    h: 24edda8a20dd
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=1.r1
    h: 306820081df5
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: On a Solis inverter an unlit OPERATION light means the inverter has stopped producing power.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=3.r4
    h: 230d295b4a21
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=3
    h: 24edda8a20dd
  review: drafted
---
This symptom is an inverter whose status lights stay dark: the Power LED and sometimes also the display. On some inverters an unlit grid status light means the internal power supply is not working, which points to an internal power supply fault. An unlit POWER light can also just mean there is no DC power or too little DC power at the input, so check the PV input voltage first. If the POWER light is lit but the OPERATION light is off, the inverter is getting DC but has stopped producing power. The CPS troubleshooting steps are: open the external AC breaker, switch the DC switch off, then check PV input voltage and polarity. Don't mix up dark LEDs with normal states. On some inverters a blinking or flickering power LED means no production, for example at night or while the inverter is switched off. In normal operation on some central inverters, the Ready, Network and Communications, and Power LEDs are lit and the fault LEDs are off. If those normal LEDs are dark, the inverter needs attention.

<!-- review notes
- sentence 1: support check: partial - The CPS row says the Power LED and LCD don't light, but the 'sometimes also the display' wording is not stated, and the grid-LED row doesn't support the general framing.
- sentence 2: support check: partial - The grid light off is indicated as 'Power supply not working', but 'internal' power supply and 'some inverters' are not explicit, though they are a reasonable reading.
- sentence 6: support check: partial - On SolarEdge, night mode (no production) shows a flickering POWER LED and a blinking POWER LED means AC is connected but not producing, but 'switched off' appears as blinking only for 'Inverter is OFF', and the 'don't mix up with dark LEDs' framing is an interpretation.
- sentence 7: support check: partial - The passages say the three left LEDs are lit and the two right LEDs are off in normal operation, but they say attention is needed when the Maintenance/Power Fault LEDs are lit, not when the normal LEDs are dark.
-->
