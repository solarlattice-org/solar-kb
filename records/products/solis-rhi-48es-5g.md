---
id: prod:solis-rhi-48es-5g
type: Product
name: Solis RHI-48ES-5G hybrid
aliases:
- RHI-48ES-5G
- RHI-3K-48ES-5G
- RHI-K-48ES-5G
- Solis Single Phase Hybrid inverter
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:kb-solis-44002492947-rhi-3-6-k-48es-5g-and-s5-eh1p-3-6-k-self-use-setup
    loc: sec=front
    h: f0fdd1c1925d
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=front
    h: 45b6ab0b365d
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Described as a single-phase hybrid inverter.
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:hybrid-inverter-system
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  review: drafted
- claim_id: c4
  rel: implements
  target: func:self-consumption-optimization
  scope:
    applications:
    - self-consumption
  note: Self-use storage mode, described as the most common configuration.
  cite:
  - src: src:kb-solis-44002492947-rhi-3-6-k-48es-5g-and-s5-eh1p-3-6-k-self-use-setup
    loc: sec=h1
    h: e7a8d245db57
  review: drafted
- claim_id: c5
  rel: implements
  target: func:battery-grid-charging
  note: Grid charging can be enabled during self-use setup.
  cite:
  - src: src:kb-solis-44002492947-rhi-3-6-k-48es-5g-and-s5-eh1p-3-6-k-self-use-setup
    loc: sec=h1
    h: e7a8d245db57
  review: drafted
- claim_id: c6
  rel: implements
  target: func:backup-power
  note: Setup guidance says to disable backup if it is not used.
  cite:
  - src: src:kb-solis-44002492947-rhi-3-6-k-48es-5g-and-s5-eh1p-3-6-k-self-use-setup
    loc: sec=h1
    h: e7a8d245db57
  review: drafted
  review_note: 'support check: partial - The passage only says to disable backup if it is not in use,
    which implies backup exists but does not state backup power support outright.'
- claim_id: c7
  rel: implements
  target: func:export-limitation
  conditions: With a compatible Solis-listed meter installed
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c8
  rel: implements
  target: func:consumption-metering
  conditions: With a compatible Solis-listed meter or CT installed
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c9
  rel: compatible_with
  target: prod:puredrive-battery
  note: Installation video shows the inverter with three Puredrive batteries.
  cite:
  - src: src:kb-solis-44002492966-solis-hybrid-inverter-s5-eh1p-3-6-k-l-or-rhi-3-6-k-48es-5g-and-puredr
    loc: sec=h1
    h: 02c41dbcacd2
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:eastron-sdm120ctm
  note: Single-phase meter for hybrid control logic, export limiting and consumption monitoring.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:eastron-esct-ta16
  note: ESCT-TA16 100A/100mA CT used together with the Eastron SDM120CTM meter.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:eastron-sdm630
  note: SDM630MCT 40mA three-phase variant; the single-phase inverter connects on phase L1.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: prod:acrel-acr10r-16dte
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c14
  rel: compatible_with
  target: prod:acrel-acr10r-16dte4
  note: Three-phase meter; the inverter connects on phase A.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c15
  rel: compatible_with
  target: prod:acrel-xh-sct-t16-120
  note: CT used with Acrel meters.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c16
  rel: requires
  target: tool:solis-firmware-update-stick
  conditions: Local DSP or HMI firmware update through the 4-pin green COM port
  cite:
  - src: src:kb-solis-44002485763-procedure-for-local-hmi-dsp-update
    loc: sec=h1
    h: 7bf9db597d18
  review: drafted
- claim_id: c17
  rel: requires
  target: role:installer
  conditions: Solis sends update sticks only to installers, not to system owners
  cite:
  - src: src:kb-solis-44002485763-procedure-for-local-hmi-dsp-update
    loc: sec=h1
    h: 7bf9db597d18
  review: drafted
  review_note: 'support check: partial - Update sticks are sent only to installers, but the passage does
    not say the model requires an installer role.'
---
The Solis RHI-(3-6)K-48ES-5G is a single-phase hybrid inverter family made by Solis. Its most common setup is self-use storage mode. In that mode you can turn on grid charging, and you should turn off backup if the site does not use it. It has been installed with Puredrive batteries, using three Puredrive units in the example installation. For hybrid control, export limiting and consumption monitoring, use only meters and CTs on Solis's list: the Eastron SDM120CTM with an ESCT-TA16 CT, the Eastron SDM630MCT, or the Acrel ACR10R-16DTE and ACR10R-16DTE4 with XH-SCT-T16/120 CTs. Solis will not support a site that uses a meter or CT that is not on its list. Local DSP and HMI firmware updates are done with the Solis update stick in the green 4-pin COM port. The HMI file for this family is named HMI_WIFI.bin. Before a local update, unplug the communication cables and set the inverter address to 1. Solis sends update sticks only to installers.

<!-- review notes
- sentence 4: support check: partial - The listed meters and CTs match, but the guide also lists others (such as SDM630MCT with other CTs and the Solis CT) and the statement narrows the list.
-->
