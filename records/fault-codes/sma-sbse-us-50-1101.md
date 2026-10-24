---
id: fc:sma-sbse-us-50-1101
type: FaultCode
name: SMA SBSE-US-50 1101
aliases:
- '1101'
- SMA 1101
- Installation error > Check connection
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '1101'
code_key: '1101'
display_message: Installation error > Check connection
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.18
    h: ebe2ec85401c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h508
    h: a9dee14d1e72
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:neutral-line-abnormal
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.18
    h: ebe2ec85401c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h508
    h: a9dee14d1e72
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h509
    h: e8fb65015461
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.14
    h: 451630c05f83
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h437
    h: a9dee14d1e72
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h438
    h: e8fb65015461
  review: drafted
  review_note: 'support check: partial - Describes a second line conductor connected to N, which is an
    abnormal neutral connection, though not worded as such.'
- claim_id: c3
  rel: indicates
  target: fm:inverter-installation-defect
  note: A line conductor is wired to the neutral terminal.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.18
    h: ebe2ec85401c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h508
    h: a9dee14d1e72
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h509
    h: e8fb65015461
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.14
    h: 451630c05f83
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h437
    h: a9dee14d1e72
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h438
    h: e8fb65015461
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h510
    h: 1a1364f30005
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h439
    h: 1a1364f30005
  review: drafted
  review_note: 'support check: partial - Corrective measure is to connect the neutral conductor to N,
    which is a connection fix but not explicitly a check.'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.18
    h: ebe2ec85401c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h508
    h: a9dee14d1e72
  review: drafted
---
