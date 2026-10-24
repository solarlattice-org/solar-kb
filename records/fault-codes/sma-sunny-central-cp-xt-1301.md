---
id: fc:sma-sunny-central-cp-xt-1301
type: FaultCode
name: SMA SC-CP-XT 1301
aliases:
- '1301'
- SMA 1301
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '1301'
code_key: '1301'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-sequence-error
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Covers checking phase position of the AC connection.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:external-fuse-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  review: drafted
  review_note: 'support check: partial - Corrective measure is to make sure all fuses are switched on,
    which is approximately a fuse check but not specifically external.'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r8
    h: 893caf77b61f
  review: drafted
---
