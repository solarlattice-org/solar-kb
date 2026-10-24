---
id: fm:floating-neutral
type: FailureMode
name: Missing or floating neutral
aliases:
- missing neutral
- unreferenced neutral
- neutral not connected
- neutral not referenced to L1 and L2
- neutral connected to high-leg delta inverter
- L-N overvoltage up to 360 V
- floating neutral
- Floating neutral overvoltage
- L or N not connected
- fully-insulated neutral
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:installation-error
  note: Neutral left unconnected where required, or connected where it must not be (240 V high-leg delta).
  cite:
  - src: src:solis-s6-gc-30k-lv-us-30k-high-side-connection
    loc: sec=h3
    h: '831606556e44'
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h510
    h: 1a1364f30005
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h194
    h: 3f7cf298cc7a
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h42
    h: e4a476d7b4af
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h43
    h: 88833a7c906b
  - src: src:solis-s6-gc-30k-lv-us-30k-high-side-connection
    loc: sec=h3
    h: '831606556e44'
  - src: src:solaredge-se-commercial-3ph-inverter-w-synergy-tech-installation-guide-pn-sexxk
    loc: sec=h103
    h: a9e21ed826f8
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:mv-transformer
  note: A wye service transformer with a fully insulated neutral is a prohibited configuration for some
    large inverters.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h42
    h: e4a476d7b4af
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h43
    h: 88833a7c906b
  review: drafted
  review_note: 'support check: partial - Passages state the XGI 1500 inverter cannot operate on wye with
    fully-insulated neutral, but do not mention a medium voltage transformer as such or ''some large inverters''
    generally.'
- claim_id: c4
  rel: presents_as
  target: symptom:grid-connection-failure
  note: Inverter waits for grid voltage and reports an installation failure when L or N is not connected.
  quote: Waiting for grid voltage > Installation failure grid connection > Check grid and fuses
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h194
    h: 3f7cf298cc7a
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:inverter-display-check
  note: The display message reports that L or N is not connected.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h194
    h: 3f7cf298cc7a
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Check that neutral and line conductors are connected to the correct terminals, and check the grid
    and fuses.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h727
    h: 1f6e90b8c2e2
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h510
    h: 1a1364f30005
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h194
    h: 3f7cf298cc7a
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Some inverters have a neutral line setting that must match whether a neutral is actually connected.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=16.r3
    h: 6e25f2b98001
  review: drafted
  review_note: 'support check: partial - A Neutral Line Setting to select whether neutral is connected
    exists, but passage does not say it mitigates a missing/floating neutral or must match wiring.'
- claim_id: c9
  rel: mitigated_by
  target: mit:transformer-configuration-check
  note: Confirm the service transformer winding and neutral arrangement is one the inverter supports.
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h42
    h: e4a476d7b4af
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h43
    h: 88833a7c906b
  - src: src:chint-cps-xfmr-winding-compatibility-rev-2026-03-25
    loc: tbl=1.r1
    h: 00b939985d7f
  - src: src:chint-cps-xfmr-winding-compatibility-rev-2026-03-25
    loc: tbl=1.r2
    h: 4d88cb0108c9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A missing or floating neutral means the neutral conductor is absent or not referenced correctly where the inverter needs it, or it is connected where the inverter needs it left out. In most countries three-phase inverters need a neutral connection, and some high-leg delta setups also require a neutral conductor. Some large inverters cannot run on a wye service whose neutral is fully insulated. Check that the transformer winding type is one the inverter supports. If line or neutral is not connected, the inverter waits for grid voltage and reports an installation failure on the grid connection. The reverse also happens: in 240 V high-leg operation, a neutral connected to the inverter causes wrong measurements. Disconnect that neutral and remove it from the wire box, or tape and secure it if it stays inside. To fix the fault, check that the neutral and line conductors are on the correct terminals, check the grid and the fuses, and make sure the inverter's neutral setting matches the actual wiring.

<!-- review notes
- sentence 1: support check: partial - Both missing neutral and neutral wrongly connected are covered, but 'not referenced correctly' (floating) is only loosely supported, and the definition is synthesized.
- sentence 3: support check: partial - XGI 1500 cannot run on wye with fully-insulated neutral is stated, but 'some large inverters' is generalized and the check advice is not stated.
- sentence 6: support check: partial - Terminal checks and grid/fuse checks are supported, but the neutral setting only appears as a setting description, not as a fix step for this fault.
- c5 dropped at review: The passage says erroneous measurements come from a neutral that IS connected in 240V high-leg operation, which is the opposite of a missing or floating neutral, so it does not support this failure mode presenting as a voltage mismatch.
- sentence 1: review: partial - The passages cover a neutral that is required but not connected, and a neutral that must not be connected in 240V high-leg setups, but 'not referenced correctly' (floating) is not stated.
-->
