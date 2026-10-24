---
id: prod:sma-sbse-us-50
type: Product
name: Sunny Boy Smart Energy US-50
aliases:
- Sunny Boy Smart Energy US
- SBSE US 50
- SBSExx US 50
- Sunny Boy Smart Energy
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-sbsexx-us-50-firmware-update
    loc: sec=front
    h: d091b3faf8d8
  - src: src:kb-sma-sbsexx-us-50-commissioning
    loc: sec=front
    h: a9095e2f50d8
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Single-phase transformerless hybrid inverter with battery connection; 3 PV inputs on 3.8-7.7 kW
    models, 4 on 9.6 and 11.5 kW models.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=2.1
    h: d076b5a3943d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=7.r2
    h: 66a276cf7fec
  review: drafted
- claim_id: c3
  rel: implements
  target: func:backup-power
  scope:
    applications:
    - backup
  note: 'SMA Backup Secure: a manual secure power supply function that feeds selected loads through an
    inverter-connected socket from battery and PV during an outage.'
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=2.1
    h: d076b5a3943d
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: arch:ac-coupled-storage
  note: Can convert AC from additional PV inverters in the system into DC to charge the battery.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=2.1
    h: d076b5a3943d
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: arch:hybrid-inverter-system
  note: Can work as a hybrid inverter, a PV-only inverter or a battery inverter.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=2.1
    h: d076b5a3943d
  review: drafted
- claim_id: c6
  rel: implements
  target: func:system-manager
  scope:
    firmware_min: 3.08.11.R
  conditions: SBSE3.8 to SBSE11.5-US-50 models from firmware version 3.08.11.R
  cite:
  - src: src:sma-doc-275857
    loc: tbl=5.r3
    h: fbcfe3f98d3e
  review: drafted
- claim_id: c7
  rel: requires
  target: role:qualified-person
  conditions: Doing a firmware update through the SMA 360° app
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h367
    h: a7f8ea7ceff3
  review: drafted
  review_note: 'support check: partial - The passage is headed ''Qualified person'' and says a firmware
    update can be done via the app. It does not explicitly state that a qualified person is required,
    though the heading implies it.'
---
The Sunny Boy Smart Energy US-50 is an SMA family of single-phase, transformerless hybrid inverters with a battery connection, sold as the SBSE3.8, 4.8, 5.8, 7.7, 9.6 and 11.5-US-50 models. The four smaller models have 3 PV inputs and the 9.6 and 11.5 models have 4 PV inputs. The unit can work as a hybrid inverter, a PV-only inverter or a battery inverter. It can also take AC from other PV inverters on site and use it to charge the battery. SMA Backup Secure is a manual backup function: during a grid outage it powers selected loads from the battery and PV through a socket connected to the inverter. From firmware 3.08.11.R the inverter supports System Manager functionality. A qualified person can update the firmware through the SMA 360° app, either before configuration or during operation. The firmware can also be updated manually through the user interface. The inverter is for stationary indoor or outdoor installation only. It must be used only with PV modules and cables approved under local electrical standards and the National Electrical Code.

<!-- review notes
- sentence 6: support check: partial - The SMA 360° app update, before configuration or during operation, is stated. For the manual update through the user interface, the evidence has only a page title, and it does not say who performs it.
-->
