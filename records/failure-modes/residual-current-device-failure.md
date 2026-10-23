---
id: fm:residual-current-device-failure
type: FailureMode
name: Residual current device failure
aliases:
- AFI module fault
- RCD
- residual current breaker
claims:
- claim_id: c1
  rel: affects
  target: comp:residual-current-device
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  - src: src:sma-sc-wa-en-31
    loc: sec=6.2
    h: 6c6a213ef52b
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: tbl=24.r1
    h: 473b0dc9debd
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: detected_by
  target: method:inverter-display-check
  note: The fault is shown as a status message on the inverter web interface.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: detected_by
  target: method:rcd-function-test
  note: Pressing the device's test button simulates a fault; afterwards check whether voltage is still
    present downstream.
  cite:
  - src: src:sma-sc-wa-en-31
    loc: sec=6.2
    h: 6c6a213ef52b
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: tbl=24.r1
    h: 473b0dc9debd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: If voltage is still present at the output after the test button is pressed, rewire the residual-current
    device correctly and switch it back on.
  cite:
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: tbl=24.r1
    h: 473b0dc9debd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: If an external residual-current device trips frequently, set the inverter's rated residual current
    lower so the inverter disconnects first.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=8.12
    h: 18f0a2f177b5
  review: drafted
  review_note: 'support check: partial - Lowering the inverter value when the device trips frequently
    is stated, but the passage doesn''t call this a mitigation of device failure. It also describes the
    inverter disconnecting to prevent incorrect tripping, not ''first'' as such.; review: partial - Setting
    the inverter value lower when the RCD trips frequently, so that the inverter disconnects and prevents
    incorrect tripping, is stated; but that is nuisance tripping, not a failure of the device, so calling
    it a mitigation of device failure…'
- claim_id: c6
  rel: caused_by
  target: fm:leakage-current
  note: When leakage currents are high, the residual current cannot always be calculated accurately, and
    the calculation errors can cause unwanted inverter shutdowns.
  cite:
  - src: src:sma-doc-237302
    loc: sec=h11
    h: 63b3fad3802c
  review: drafted
  review_note: 'support check: partial - High leakage currents causing calculation errors and unwanted
    inverter shutdown are stated, but the passage says nothing about a residual current device failure.;
    review: partial - Unsupported is too harsh. The passage says high leakage currents keep the RCMU (the
    inverter''s residual-current monitoring unit) from calculating residual current accurately, and that
    these errors can cause an undesired inverter shutdown. That is leakage current causing the residual-current…'
- claim_id: c7
  rel: distinguished_from
  target: fm:insulation-loss
  by: method:insulation-resistance-test
  note: A genuine residual-current trip usually comes from faulty earth cabling or low insulation resistance,
    which an insulation test confirms. A fault in the device itself is reported as a separate module-fault
    status.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=42.r1
    h: 53a521edab18
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: drafted
  review_note: 'support check: partial - The residual current shutdown, with faulty earth cabling and
    an insulation resistance measurement, and the separate AFI module fault are stated. The passages do
    not say that an insulation test tells the two apart.; review: partial - The passages separate the
    residual-current shutdown (faulty earth cabling or low insulation, check by measuring insulation resistance)
    from a distinct AFI module fault status, but never say the insulation test is how the two are told
    apart.'
---
This failure means the residual current device itself is faulty, rather than a real residual current being present. Check the device with its test button: pressing it simulates a fault, so the output should then be dead. If voltage is still present after pressing the test button, wire the device correctly and switch it back on. Do not confuse it with a real residual current shutdown, which is usually caused by faulty earth cabling, often shows up during rain, and is confirmed by an insulation resistance measurement. High leakage currents can upset the residual current calculation and cause unwanted shutdowns. If an external device trips often, set the inverter's rated residual current lower.

<!-- review notes
- sentence 1: support check: partial - The AFI module fault row says a fault occurred in the breaker, which is consistent with the device itself being faulty. The passages don't explicitly contrast it with a real residual current.
- sentence 2: support check: partial - The test button simulating a fault is stated, and u13 checks for voltage at X3. The passages don't explicitly say the output should be dead, though that is implied.
- sentence 4: support check: partial - Faulty earth cabling, rainfall and an insulation measurement are stated for the real residual current shutdown. The passages don't explicitly say not to confuse it with the module fault.
- sentence 1: review: partial - The passages say the residual current breaker itself has a fault (and a test button can simulate failure), but they never contrast this with a real residual current being present.
-->
