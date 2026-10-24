---
id: func:insulation-monitoring
type: Function
name: Insulation monitoring
aliases:
- IMI
- insulation monitoring interrupter
- Riso check
- isolation resistance measurement
- Isolation Monitor Interrupter
- isolation monitor interruptor
- Insulation resistance detection
- insulation resistance monitoring
- Insulation Monitor/Interruption
category: Protection
function_kind: protection
claims:
- claim_id: c1
  rel: subclass_of
  target: func:ground-fault-protection
  note: SMA and Sungrow datasheets list insulation monitoring under ground-fault monitoring.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=33.r6
    h: 3313e831e5f8
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=49.r7
    h: 39b8e8759578
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=57.r6
    h: fb224e5c3e9a
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=69.r1
    h: 2d0f3a07b010
  review: drafted
---
Insulation monitoring checks the resistance between the PV positive or negative pole and ground, and the inverter disconnects from the grid if either DC conductor is shorted to ground, for example because of poorly insulated cables or faulty modules. Low insulation resistance can defeat direct and indirect contact protection, and the resulting ground fault current can cause fire, equipment damage or injury. Fronius says UL 1741 and the National Electrical Code require this safety function. Insulation monitoring or insulation resistance detection is listed for the Huawei SUN2000-25KTL-US, SUN2000-30KTL-US and SUN2000-45KTL-US-HV-D0, the Fronius Primo 208-240 models, and the CPS SCA36-60KTL-DO/US-480 inverters. SMA datasheets give an Riso limit for each model, for example Riso > 417 kΩ for the STP 12000TL-US-10 and Riso > 150 kΩ for the STP 33-US-41.
