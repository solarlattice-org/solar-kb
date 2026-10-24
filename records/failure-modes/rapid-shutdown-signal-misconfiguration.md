---
id: fm:rapid-shutdown-signal-misconfiguration
type: FailureMode
name: Rapid shutdown mode misconfiguration
aliases:
- SunSpec Shutdown not selected
- Rapid Shutdown Mode not set
- keep-alive signal not enabled
- non-approved SunSpec shutdown device
- Rapid shutdown signal misconfiguration
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: The rapid shutdown operating mode is an inverter parameter (On, SunSpec Shutdown, Off, and TS4
    Shutdown on some models).
  cite:
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: sec=h1
    h: 7b6c37b20ba8
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1
    h: 6ac3c561834b
  - src: src:kb-sma-stpxx-us-41-configuring-the-rapid-shutdown-function
    loc: tbl=1
    h: 86d85195c286
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:rapid-shutdown-device
  note: The mode must match the DC disconnection unit fitted to the modules or strings. With TS4-R-F devices,
    SunSpec Shutdown is the required mode.
  cite:
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: sec=h1
    h: 7b6c37b20ba8
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h6
    h: 20f41afb0134
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1.r4
    h: b399418e132b
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:rapid-shutdown-initiator
  note: A separate parameter chooses the initiator, either the AC disconnect or a digital input. If digital
    input is chosen, an initiator must be wired to the GSI input.
  cite:
  - src: src:kb-sma-sbsexx-us-50-parameters-for-rapid-shutdown-function-us
    loc: sec=h1
    h: 7814e82efeb1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=8.8
    h: 5f4090d18a43
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:inverter-settings
  note: Choosing a mode that does not match the installed DC disconnection unit, or leaving the function
    Off when such a unit is present.
  cite:
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: sec=h1
    h: 7b6c37b20ba8
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1
    h: 6ac3c561834b
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1.r4
    h: b399418e132b
  review: drafted
  review_note: 'support check: partial - Modes must match the DC disconnection unit and Off disables the
    function, but the passages don''t explicitly describe mismatch or leaving Off as a misconfiguration.'
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  note: Check the Rapid Shutdown Mode parameter (Operation.RSSOpMode) and the Rapid Shutdown Initiator
    parameter (Operation.RSSInitiator).
  cite:
  - src: src:kb-sma-sbsexx-us-50-parameters-for-rapid-shutdown-function-us
    loc: sec=h1
    h: 7814e82efeb1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=30
    h: f00aac9410b1
  - src: src:kb-sma-sbsexx-us-50-parameters-for-rapid-shutdown-function-us
    loc: tbl=1
    h: 4cb1e58072b1
  review: drafted
  review_note: 'support check: partial - The parameters Operation.RSSOpMode and RSSInitiator are listed,
    but nothing states that reviewing them is a detection method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: 'Set the mode to suit the disconnection unit: On for a separate DC disconnection unit, SunSpec
    Shutdown for SunSpec-compliant devices.'
  cite:
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: sec=h1
    h: 7b6c37b20ba8
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h165
    h: 071194e91e49
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h139
    h: 071194e91e49
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1
    h: 6ac3c561834b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:certified-products
  note: Use rapid shutdown devices that appear on the manufacturer's list of compatible SunSpec-certified
    devices.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h6
    h: 20f41afb0134
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=9.r3
    h: 85de59eb1b35
  review: drafted
  review_note: 'support check: partial - A list of compatible SunSpec rapid shutdown devices exists, but
    passages don''t say using listed devices mitigates mode misconfiguration.'
---
This fault happens when the inverter's rapid shutdown operating mode does not match the DC disconnection equipment installed on the PV modules or strings. If the array has an additional DC disconnection unit, the rapid shutdown function must be enabled, using the mode that fits that unit. Use On for a separate DC disconnection unit between the inverter and the array, and SunSpec Shutdown for devices that follow the SunSpec specification. Off disables the function. On inverters that offer TS4 Shutdown, TS4-R-F devices are not covered by that mode and need SunSpec Shutdown instead. To confirm the fault, read the Rapid Shutdown Mode and Rapid Shutdown Initiator parameters. If the initiator is set to digital input, check that an initiator is actually wired to that input. To fix it, change the parameter to the correct mode, and use only rapid shutdown devices on the manufacturer's compatibility list. With SunSpec rapid shutdown devices installed, I-V curves can show steps and kinks even when the array is healthy, so do not read those features as a module fault.

<!-- review notes
- sentence 1: support check: partial - Mode must be selected in accordance with the disconnection unit used, but passages don't describe a fault occurring on mismatch.
- sentence 5: support check: partial - Parameters and the requirement to connect an initiator to GSI are stated, but not a confirmation procedure for a fault.
- sentence 6: support check: partial - Setting the mode parameter and a compatibility list are mentioned, but not that only listed devices should be used as a fix.
- sentence 1: review: partial - The passages say the mode must be chosen to match the DC disconnection unit, but they never describe a mismatch as a fault that happens.
-->
