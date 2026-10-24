---
id: fm:rapid-shutdown-device-failure
type: FailureMode
name: Rapid shutdown device failure
aliases:
- defective RSD
- MLPE stuck in bypass mode
- JMS-F device no longer producing reference voltage
- failed or bypassed MLPE
- RSD not activating
- RSD failure
- TS4 communicating but not producing
- Failed or Bypassed MLPE Devices
- stuck in bypass mode
- defective device
claims:
- claim_id: c1
  rel: affects
  target: comp:rapid-shutdown-device
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:rapid-shutdown-failure
  note: Devices do not activate when grid power is removed.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:low-shutdown-string-voltage
  note: In the shutdown state, string voltage reads below the expected per-device reference voltage times
    the number of devices.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  - src: src:sma-kb-faq-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: bf1044cdf7d2
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:low-string-operating-voltage
  note: The safety voltage can be correct while the operating Vmp is low, which points to an RSD stuck
    in bypass mode or underperforming.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:mlpe-detection-failure
  note: TS4-R devices not communicating after detection, or communicating but not producing.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Abnormal heat signatures from RSDs; heat alone does not confirm failure.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:installation-error
  note: Connecting the device to a panel that is already wired into a string may permanently damage it.
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:electrical-overstress
  note: Overvoltage damage when assemblies are strung before each panel has its device attached.
  cite:
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:poor-connector-contact
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
  review_note: 'support check: partial - u1 mentions inspecting for damage or poor contact and overheating
    from poor connections, but does not clearly state poor connector contact causes RSD failure.'
- claim_id: c10
  rel: detected_by
  target: method:mlpe-safety-voltage-check
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  - src: src:sma-kb-faq-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: bf1044cdf7d2
  - src: src:sma-kb-creating-a-string-with-jms-f-rapid-shutdown-devices
    loc: sec=h1
    h: fbb01e1f0330
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Vmp check across string terminals while the system is running.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:fault-localization
  note: Halve the string, or isolate single assemblies, until the faulty device is found.
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c13
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  review: drafted
  review_note: 'support check: partial - u1 offers thermal imaging as optional diagnostic helpful for
    identifying faults, but says heat alone does not confirm failure, so detection is only suggestive.'
- claim_id: c15
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:known-good-swap-test
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c17
  rel: distinguished_from
  target: fm:rapid-shutdown-signal-misconfiguration
  by: method:inverter-settings-review
  note: Before blaming a device, confirm that the inverter rapid shutdown mode is set to SunSpec Shutdown.
    If the setting is correct and the voltage is still low, suspect the device.
  cite:
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  - src: src:sma-kb-faq-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: bf1044cdf7d2
  review: drafted
  review_note: 'support check: partial - u2 says to confirm SunSpec Shutdown setting first, but the passages
    don''t frame it as a differentiator or give the ''setting correct and voltage still low'' logic explicitly.'
- claim_id: c18
  rel: mitigated_by
  target: mit:mlpe-replacement
  cite:
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:warranty-claim
  cite:
  - src: src:sma-kb-advanced-troubleshooting-steps-for-jms-f-sunspec-rapid-shutdown-devices
    loc: sec=h1
    h: 9f825260fb2d
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-kb-troubleshooting-failed-or-bypassed-mlpe-devices-ts4-f-jmthy
    loc: sec=h1
    h: 0f68753f778a
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:assembly-voltage-verification
  cite:
  - src: src:sma-kb-installing-the-jms-f-rapid-shutdown-device-to-your-pv-panel
    loc: sec=h1
    h: 2efbe57cbd0a
  - src: src:sma-kb-creating-a-string-with-jms-f-rapid-shutdown-devices
    loc: sec=h1
    h: fbb01e1f0330
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c22
  rel: mitigated_by
  target: mit:proper-installation
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:wireless-range-extension
  cite:
  - src: src:sma-kb-troubleshooting-steps-for-tigo-ts4-r-rapid-shutdown-devices
    loc: sec=h1
    h: 93a1d9e35f6f
  review: drafted
---
A rapid shutdown device fails when a module-level unit stops working or gets stuck in bypass. The string then loses its correct shutdown voltage, its operating voltage, or both. Typical signs are devices that do not activate when grid power is cut, low string voltage, string mismatches, or units that communicate but do not produce. To check, switch AC off and measure the string in its shutdown state. Expect about 0.6 V per TS4-F unit or about 1 V per JMS-F unit. Then measure Vmp with the system running, because a device stuck in bypass can show a correct safety voltage but a low Vmp. Before suspecting the hardware, confirm that the inverter rapid shutdown mode is set to SunSpec Shutdown. To find the bad unit, keep splitting the string in half or isolate single panel assemblies. Check connectors and housings for heat damage. Use a swap with a known-good device or thermal imaging to back up the result. Photograph the serial number of the faulty device, open a case with the manufacturer, and replace it under warranty. To prevent this, attach each device to its panel before stringing, and check the voltage of each assembly before connecting it into a string.

<!-- review notes
- sentence 3: support check: partial - u1 and u9 give 0.6V per TS4-F and ~1V per JMS-F (u1 says 1V to 2V); the 'about 1 V' is loosely supported and the range is omitted.
-->
