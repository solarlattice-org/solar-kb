---
id: fc:sma-stp-core1-us-7342
type: FaultCode
name: SMA CORE1-US 7342
aliases:
- '7342'
- SMA 7342
- Update Bootloader failed
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7342'
code_key: '7342'
display_message: Update Bootloader failed
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h267
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h268
    h: f30261362a74
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h184
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h185
    h: f30261362a74
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h269
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h270
    h: f30261362a74
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h268
    h: f30261362a74
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h185
    h: f30261362a74
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h270
    h: f30261362a74
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:retry-update
  note: Contact service if the message reappears after retry.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h269
    h: 2b6216ee121d
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h186
    h: 2b6216ee121d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h271
    h: 2b6216ee121d
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h267
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h268
    h: f30261362a74
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h184
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h185
    h: f30261362a74
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h269
    h: 7813c2069e80
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h270
    h: f30261362a74
  review: drafted
---
