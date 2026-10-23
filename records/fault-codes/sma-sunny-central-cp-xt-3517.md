---
id: fc:sma-sunny-central-cp-xt-3517
type: FaultCode
name: SMA SC-CP-XT 3517
aliases:
- '3517'
- SMA 3517
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3517'
code_key: '3517'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r9
    h: 3b647f7c40b9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status message while insulation measurement runs.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r9
    h: 3b647f7c40b9
  review: drafted
  review_note: 'support check: partial - It is a status message about insulation measuring, but the row
    shows behavior W (warning), not informational.'
---
