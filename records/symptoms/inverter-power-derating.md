---
id: symptom:inverter-power-derating
type: Symptom
name: Inverter power derating
aliases:
- temperature derating
- power reduction
- Derating running
- Power Derating, Temperature
claims:
- claim_id: c1
  rel: observed_as
  target: meas:temperature-derated-output
  note: The inverter lowers its output, or switches off, to protect its parts from overheating. It may
    not send a status message about it. The manuals give ambient or internal temperature thresholds where
    derating starts (for example 45°C), and one model shuts down at 60°C.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=51.r1
    h: 52f99f2ab326
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r1
    h: 44fc567b4d48
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=24.r8
    h: 50ca486bd754
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=36.r8
    h: 785673ca8918
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=10.3.1
    h: 1391406b53e3
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=13.4
    h: 5061a35f7b2c
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23
    h: ae4d31cce1d2
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:inverter-temperature-high
  note: Temperature-derating event code linked to the inverter's internal operating temperature. If the
    inverter does not report temperature, a sensor in the enclosure can be added to detect overheating.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=23
    h: ae4d31cce1d2
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h187
    h: 7b8d5092eced
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: The inverter limits AC output current, and so derates, when grid voltage is below the rated output
    voltage. With volt-watt enabled it also derates above 106% Un.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=10.3.3
    h: 93b69af74ce8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: observed_as
  target: meas:dc-voltage-outside-mppt-range
  note: Inverters derate linearly when the DC input voltage is outside the rated MPPT window.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: sec=13.5
    h: 5a47aec12cce
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: sec=10.3.4
    h: 57019778a5f9
  review: drafted
---
The inverter delivers less power than it should, or switches off, to protect its internal parts from overheating. Inverters do not always show a derating or power reduction message, so check their behaviour with power versus irradiance curves. Temperature derating usually starts above a set ambient or internal temperature, and output then drops along a fixed curve. Overheating can come from poor installation, fan failure, dust blocking heat dissipation or wrong inverter programming. Derating also happens when the grid voltage is below the rated output voltage, when the DC input voltage is outside the MPPT range, or when a user command asks for it. To find the cause, compare the logged inverter temperature, the grid voltage and the DC input voltage with the times the power was reduced. Check first that all external fans are running and that the ambient temperature is within the normal operating range.

<!-- review notes
- sentence 3: support check: partial - The 45°C onset and linear derating curve are stated, but only for specific models; a general claim of a 'fixed curve' and internal temperature thresholds is not stated.
- sentence 6: support check: partial - Passages describe the derating conditions and that inverter temperature may be logged, but none explicitly recommend comparing logged temperature, grid and DC voltage against derating times.
- sentence 7: support check: partial - Both checks are in the troubleshooting text, but the passage doesn't say they should be done 'first'.
-->
