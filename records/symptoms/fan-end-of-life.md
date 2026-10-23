---
id: symptom:fan-end-of-life
type: Symptom
name: Fan service life reached
aliases:
- Fan Life Reached
- Fan service life has expired
claims:
- claim_id: c1
  rel: observed_as
  target: meas:fan-fail-message
  note: On CPS and Yaskawa PVI string inverters, the external fan error alarm (ExtFanErr) lists an expired
    fan service life as one possible cause. The other listed causes are a blocked fan and poor contact
    at the fan socket connector.
  quote: Cooling fan failure by visual check
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=24.r5
    h: de5bc765d628
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=55.r2
    h: 584b5f831617
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=32.r5
    h: a6f5a7f3b418
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=33.r8
    h: e319683e4bbb
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: tbl=38.r2
    h: 0fce0901dc0c
  review: drafted
---
On SGI-XTM central inverters this symptom shows up as a Fan Life Reached message on the user interface, and it is also written to the event log. In Modbus monitoring it is an informative alarm on bit 11, and the inverter keeps producing AC power while the alarm is active. Even though output continues, the manufacturer recommends a site visit and says to contact Solectria, because the inverter may need work by an authorized service provider. On string inverters, an expired fan service life is one possible cause of the external fan error alarm. The same fan alarm can also come from a blocked fan or poor contact at the fan socket connector, so check for obstructions and reseat the connector before you blame fan age. The fan error is defined as a cooling fan failure found by visual check. One manual advises watching for 5 minutes to see whether the alarm clears by itself.

<!-- review notes
- sentence 1: support check: partial - UI text 'Fan Life Reached' and event log Y are stated, but the passage does not name SGI-XTM central inverters (only Solectria text).
- sentence 2: support check: partial - Bit 11 and AC power produced Yes are stated, and the 'Informative Alarms' heading appears; Modbus context is implied, but it's roughly supported without explicit Modbus mention.
- sentence 5: support check: partial - Other causes are listed, but the advice to check obstructions and reseat the connector before blaming fan age is not stated in the passages.
-->
