---
id: prod:solis-rai-48es-5g
type: Product
name: Solis RAI-48ES-5G AC-coupled inverter
aliases:
- RAI-3K-48ES-5G
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:kb-solis-44002382799-rai-3k-48es-5g-how-to-enable-charging-times
    loc: sec=front
    h: 7ee37efc3873
  - src: src:kb-solis-44002485763-procedure-for-local-hmi-dsp-update
    loc: sec=h1
    h: 7bf9db597d18
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: arch:ac-coupled-storage
  note: Listed among RAI / S5 AC-coupled inverters; a CT on the 2-pin CT port measures the power of an
    external PV inverter.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
  review_note: 'support check: partial - The guide says RAI/S5 AC-coupled inverters use a 2-pin CT port
    CT to measure external PV inverter power, and lists RAI-3K-48ES-5G for that CT (UK only). It never
    calls the RAI-3K-48ES-5G itself AC-coupled.'
- claim_id: c3
  rel: compatible_with
  target: prod:eastron-sdm120ctm
  note: Single-phase meter with external CT, used for hybrid control logic, export limitation and consumption
    monitoring.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:eastron-esct-ta16
  note: The ESCT-TA16 100A/100mA CT used with the Eastron SDM120CTM single-phase meter.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:acrel-acr10r-16dte
  note: Single-phase meter with an external 40 mA secondary CT (XH-SCT-T16/120).
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:acrel-acr10r-16dte4
  note: Three-phase meter. A single-phase inverter connects on phase A of the meter.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:acrel-xh-sct-t16-120
  note: 120A:40mA CT used together with Acrel meters.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c8
  rel: implements
  target: func:export-limitation
  note: Needs a compatible external meter or CT.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
  review_note: 'support check: partial - The compatible meters are described as providing export power
    limitation and RAI-3K-48ES-5G is listed with them. The guide doesn''t state the RAI itself implements
    export limitation, but the external meter/CT need is supported.'
- claim_id: c9
  rel: implements
  target: func:consumption-metering
  note: Needs a compatible external meter or CT.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
  review_note: 'support check: partial - The compatible meters and CTs give consumption monitoring and
    the RAI is listed with them. The guide doesn''t state outright that the RAI supports consumption metering.'
- claim_id: c10
  rel: implements
  target: func:scheduling
  note: A Solis KB article describes how to enable charging times on this inverter.
  cite:
  - src: src:kb-solis-44002382799-rai-3k-48es-5g-how-to-enable-charging-times
    loc: sec=front
    h: 7ee37efc3873
  review: drafted
  review_note: 'support check: partial - Only the article title is shown, "how to enable charging times"
    for RAI-3K-48ES-5G, with no body text. That implies charging time scheduling but does not state scheduling
    of power values and modes.'
- claim_id: c11
  rel: requires
  target: tool:solis-firmware-update-stick
  note: Needed for local DSP and HMI updates through the 4-pin green COM port. Solis sends update sticks
    only to installers. The HMI firmware file is named HMI.bin only.
  cite:
  - src: src:kb-solis-44002485763-procedure-for-local-hmi-dsp-update
    loc: sec=h1
    h: 7bf9db597d18
  review: drafted
  review_note: 'support check: partial - u28 covers the update stick, 4-pin green port, installer-only
    sticks and HMI.bin only for RAI-3K-48ES-5G. It says the stick is needed for local updates but doesn''t
    say the inverter "requires" it as such.'
---
The Solis RAI-48ES-5G, printed as RAI-3K-48ES-5G, is a Solis AC-coupled storage inverter. In an AC-coupled system, a CT on its 2-pin CT port measures the output of an existing external PV inverter. The Yuanxing CTSA016 clamp that does this is for UK inverters only. Compatible metering includes the Eastron SDM120CTM meter with an ESCT-TA16 CT, and the Acrel ACR10R-16DTE or ACR10R-16DTE4 meters with the XH-SCT-T16/120 CT. These give hybrid control logic, export power limitation and consumption monitoring. Solis says it cannot support systems that use a meter or CT not on its compatibility list. Check the list before installing. Charging times can be enabled under the Advanced Settings menu. Local DSP and HMI firmware updates use the Solis update stick in the 4-pin green COM port. The HMI file must be named HMI.bin. Do the DSP update before the HMI update.

<!-- review notes
- sentence 1: support check: partial - u3 lists RAI-3K-48ES-5G as a hybrid inverter and says RAI/S5 AC-coupled inverters use the 2-pin CT port to measure external PV power. It doesn't explicitly call this model an AC-coupled storage inverter, and u1 shows only a title.
- sentence 3: support check: partial - The SDM120CTM with ESCT-TA16 100A/100mA, and the Acrel ACR10R16DTE/DTE4 with XH-SCT-T16/120, are listed with hybrid control, export limitation and consumption monitoring. The ACR10R16DTE4 entry doesn't name the CT explicitly, though the CT entry covers both Acrel meters.
- sentence 5: support check: partial - u1 shows only the title and the kb_folder "Advanced Settings", with no body text. That suggests but doesn't state the menu location for enabling charging times.
- sentence 6: support check: partial - u28 supports the update tool in the 4-pin green port, HMI.bin only for RAI-3K-48ES-5G, and doing DSP before HMI. DSP before HMI is only a recommendation, not a requirement.
-->
