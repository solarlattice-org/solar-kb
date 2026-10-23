---
id: fc:sma-sbse-us-50-9342
type: FaultCode
name: SMA SBSE-US-50 9342
aliases:
- '9342'
- SMA 9342
- DC connection, polarity reversed > Check connection
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9342'
code_key: '9342'
display_message: DC connection, polarity reversed > Check connection
page: 120
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.76
    h: c3ae73bb0485
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h791
    h: 6e8f4c50da57
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h791
    h: 6e8f4c50da57
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h792
    h: b5bc4ef4be8c
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h792
    h: b5bc4ef4be8c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h793
    h: d6cd763220c1
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Applies to both PV and battery DC conductors.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h793
    h: d6cd763220c1
  review: drafted
---
