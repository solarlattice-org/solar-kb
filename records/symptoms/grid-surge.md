---
id: symptom:grid-surge
type: Symptom
name: Grid surge
claims:
- claim_id: c1
  rel: observed_as
  target: meas:spd-surge-event-record
  note: The Eaton SPD keeps surge logs that can be viewed. It counts low-level surges against a sensitivity
    threshold set through Modbus register 187 (default 25, range 25 to 50).
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=1.r38
    h: b97616ba99bb
  - src: src:eaton-eaton-spd
    loc: tbl=13.r22
    h: d031627bd7e1
  - src: src:eaton-eaton-spd
    loc: tbl=13.r23
    h: 44b636aa87e3
  - src: src:eaton-eaton-spd
    loc: tbl=13.r24
    h: 4e410dd4bfd3
  review: drafted
---
Inverter manuals state their surge withstand for surge category B as standard waveform peak values: 6 kV/0.50 kA for the ring wave and 6 kV/3 kA for the combination wave. When a grid surge is suspected, read the surge protection device's records first. Its surge logs can be viewed and show the recorded events. Some surge protection devices count low-level surges. A sensitivity threshold that can be adjusted locally or over Modbus decides which surges are counted. Some string inverters have a built-in test of the AC surge protection device. It is disabled by default under the IEEE 1547, Rule 21 and ISO-NE grid codes, so confirm it is enabled before relying on it. On some inverters a type 2 surge arrester protects the AC side, alongside the grid monitoring function.

<!-- review notes
- sentence 1: support check: partial - The table gives category B values of 6 kV/0.50 kA (ring) and 6 kV/3 kA (combination), but the passages don't say that inverter manuals state them as the surge withstand.
- sentence 2: support check: partial - The passages only show a table-of-contents entry for viewing surge logs; they don't say to read the SPD records first or what the logs show.
- sentence 3: support check: partial - A sensitivity threshold for the valid low surge count is adjustable on the local display and over Modbus, but the passages never say it decides which surges are counted beyond the threshold description.
- sentence 4: support check: partial - The AC SPD test parameter defaults to Disable under all three grid codes, but the passages don't say the test is built into string inverters or tell the reader to confirm it is enabled.
-->
