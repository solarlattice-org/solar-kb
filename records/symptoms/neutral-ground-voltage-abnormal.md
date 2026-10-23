---
id: symptom:neutral-ground-voltage-abnormal
type: Symptom
name: Abnormal neutral-to-ground voltage
aliases:
- Zero-to-ground voltage anomaly
- N2PE voltage abnormality
- Abnormal N-G Voltage
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: CPS three-phase string inverters report this as Protect0790, described as a zero-to-ground (N2PE)
    voltage anomaly protection and mapped to Bit15 in the Modbus fault register.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r4
    h: 77a352ec9d2e
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59
    h: c2c3d4a986de
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: tbl=50.r5
    h: c979985c84c5
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=43.r24
    h: d09f1fa0a03b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:spd-red-status-led
  note: An SPD with N-G voltage indicators blinks its red service LED and cycles its audible alarm when
    it detects excessive N-G voltage. This does not happen for transient N-G overvoltages.
  cite:
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h77
    h: a9091451d645
  review: drafted
  review_note: 'review: partial - The red LED blinking and the cycling alarm on excessive N-G voltage
    are stated, but the passage says only the resistor heating and shrink-wrap effect does not occur on
    transient overvoltages, not the LED or alarm.'
- claim_id: c3
  rel: observed_as
  target: meas:high-neutral-ground-voltage
  note: A differential circuit in the SPD measures N-G voltage. A voltmeter reading of zero between N
    and G can be misleading, because the two can sit at the same potential by chance without being bonded.
  cite:
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h77
    h: a9091451d645
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h76
    h: acb8f9e5e8c6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
On CPS three-phase inverters this condition shows up as fault code Protect0790. The manual calls it a zero-to-ground or N2PE voltage anomaly, and it is also flagged as a bit in the Modbus fault register. The manufacturer's first step is to check that the grid connection is good. If the alarm comes back after that, contact after-sales service. The inverter's neutral connection only gives it a measurement reference close to ground potential. A loose neutral wire can make the inverter read the grid voltage wrongly. On site, measure neutral to ground on the AC side along with line to line, line to neutral and line to ground. Only do this with AC on if it is safe. Do not rely on the meter alone: a zero N-G reading can happen by chance. Look to confirm that the neutral-to-ground bond is actually installed. A missing neutral-to-ground bonding jumper at the service entrance or transformer is an installation error. It leaves the system ungrounded, which can push line-to-ground voltages abnormally high and wear out surge protectors over time. Surge protectors that have N-G monitoring blink a red LED and sound an alarm when N-G voltage is excessive, and this needs immediate attention. Do not fit a neutral-to-ground jumper inside the inverter while the neutral conductor is connected, because it can cause damage.

<!-- review notes
- sentence 6: support check: partial - Missing jumper being an installation error, ungrounded system and high L-G voltages leading to SPD failure are stated, but 'service entrance or transformer' location is only partly covered and 'wear out over time' is approximated by 'eventually' chasing until failure.
-->
