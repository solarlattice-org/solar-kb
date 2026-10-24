---
id: func:backup-transfer
type: Function
name: Automatic backup transfer
aliases:
- grid-to-backup transfer
- automatic transfer
- islanding transfer
- switchover
- automatic transfer switch
- automatic transfer switching device
- automatic backup operation
- grid disconnection
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: response_time
  value:
    max: 10
    unit: unit:MilliSEC
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
  conditions: Back-up switch time without an ATR connected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r21
    h: 4c447048f16d
  review: drafted
- claim_id: c2
  attr: response_time
  value:
    max: 300
    unit: unit:MilliSEC
  scope:
    products:
    - prod:solis-rhi-1p-hv-us
  conditions: Back-up switch time with an ATR connected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r21
    h: 4c447048f16d
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 5
    unit: unit:SEC
  conditions: Parameter Operation.BckSwOnDl for automatic backup operation, SMA recommended setting
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=4.1.3
    h: b4e8607e483b
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h82
    h: 1d812b1f2054
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: default_value
  value:
    nominal: 300
    unit: unit:SEC
  conditions: Parameter Operation.BckSwOffDI for automatic backup operation, SMA recommended setting
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=4.1.3
    h: b4e8607e483b
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h82
    h: 1d812b1f2054
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions)
- claim_id: c5
  attr: default_value
  value:
    nominal: 5
    unit: unit:SEC
  conditions: Parameter Operation.BckCbSwDI for automatic backup operation, SMA recommended setting
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=4.1.3
    h: b4e8607e483b
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h82
    h: 1d812b1f2054
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
---
When the grid fails, automatic backup transfer separates the backup grid from the utility grid so that a battery system can keep supplying the loads. In an SMA Sunny Island backup system, loads and PV go unsupplied for roughly five to seven seconds after disconnection. After that the PV system can synchronize to the backup grid and feed in. When the utility grid comes back, the backup system first synchronizes with it, and then the transfer switch reconnects the backup grid. In SMA systems built around Sunny Boy Storage, the SMA Backup Unit Controller inside each transfer switching device operates the contactors as the storage inverter directs. For SMA, the parameter Operation.BckTyp must be set to Automatic backup operation before the device will switch over automatically on grid failure. Its other settings are Off and Backup Secure Operation. The Enphase IQ System Controller acts as the microgrid interconnect device. It detects a grid failure and moves the home from grid power to backup power automatically. For whole-home backup, the IQ System Controller is installed on the line side of main load panels rated up to 200 A. It can also work with a generator, with or without an IQ Battery. The Solis RHI-1P HVES-5G hybrid inverter lists a backup switch time under 10 ms without an ATR and under 300 ms with an ATR connected.
