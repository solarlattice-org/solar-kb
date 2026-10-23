---
id: symptom:calibration-failure
type: Symptom
name: Calibration failure
aliases:
- AC voltage calibration failed
- CalFail
- Calib
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Shown as an inverter event or fault code. Examples: SMA event 9101 (AC voltage calibration failed),
    SMA Sunny Central error 6002 (calibration data cannot be loaded), Sunny Island CalFail and Calib,
    and Yaskawa SGI XTM hardware fault value 8 (current sensor offset calibration failed).'
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h71
    h: 09506f40e943
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h44
    h: 09506f40e943
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h53
    h: 09506f40e943
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h761
    h: 1a37094c7d50
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r1
    h: 1d85123b93a1
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=82.r1
    h: 8853368b185e
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=67.r1
    h: ac8a7b82c6de
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r3
    h: 179e16e05f1a
  review: drafted
---
A calibration failure is reported by the inverter as an event or error code, not seen on the array itself. On SMA string inverters, event 9101 means AC voltage calibration failed, and the manual says only the Service can find the cause. Other forms of the same symptom are calibration data that cannot be loaded or read, and an invalid calibration in the DSP. On Yaskawa central inverters, a hardware fault code flags a failed current sensor offset calibration, which points to the current measurement path. The sources give no field test to find the root cause, so record the exact code and contact the manufacturer's service. If you suspect a revenue meter is out of calibration, compare its readings with other meters on the same line, then contact the meter maker's support, because the meter is calibrated at the factory.

<!-- review notes
- sentence 1: support check: partial - Passages show codes reported by the inverter, but nothing says the failure is not seen on the array itself.
- sentence 2: support check: partial - Event 9101 text and the Service-determined cause are stated, but the passages don't say it applies to SMA string inverters specifically.
- sentence 4: support check: partial - The passage lists a current sensor offset calibration failed fault value, but doesn't say Yaskawa central inverters or that it points to the current measurement path (the latter is inferable).
- sentence 5: support check: partial - All passages say to contact Service, but nothing states that the sources lack a field test or that you should record the exact code.
-->
