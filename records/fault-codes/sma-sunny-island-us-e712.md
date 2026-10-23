---
id: fc:sma-sunny-island-us-e712
type: FaultCode
name: SMA SI-US E712
aliases:
- E712
- e712
- SMA E712
- Parameters from MMC/SD memory card loaded
category: Inverters
make: sma
make_name: SMA
model_family: sunny-island-us
family_name: Sunny Island 4548-US / 6048-US
code: E712
code_key: e712
display_message: Parameters from MMC/SD memory card loaded
page: 208
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-doc-si4548-6048-us-be-en-21w
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r8
    h: 8b1fa62be727
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Event row reporting that parameters were loaded from a memory card.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=139.r8
    h: 8b1fa62be727
  review: drafted
---
