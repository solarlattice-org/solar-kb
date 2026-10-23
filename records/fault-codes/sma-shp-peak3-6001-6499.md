---
id: fc:sma-shp-peak3-6001-6499
type: FaultCode
name: SMA PEAK3-US 6001-6499
aliases:
- 6001-6499
- SMA 6001-6499
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: 6001-6499
code_key: 6001-6499
code_from: 6001
code_to: 6499
display_message: Self-diagnosis > Interference device
page: 63
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.12
    h: afc088b83c4e
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h334
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.40
    h: 5708ca34d693
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h616
    h: 75f49e9e17fb
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.24
    h: 4f81ecd9e884
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h485
    h: 75f49e9e17fb
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.12
    h: afc088b83c4e
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h334
    h: 75f49e9e17fb
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.40
    h: 5708ca34d693
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h618
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.24
    h: 4f81ecd9e884
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h487
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.12
    h: afc088b83c4e
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h336
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.40
    h: 5708ca34d693
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h617
    h: cca77e1e7cd3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.24
    h: 4f81ecd9e884
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h486
    h: cca77e1e7cd3
  review: drafted
  review_note: 'support check: partial - Cause must be determined by Service implies device problem, but
    fault vs warning classification isn''t explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.40
    h: 5708ca34d693
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h617
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h618
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.24
    h: 4f81ecd9e884
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h486
    h: cca77e1e7cd3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h487
    h: 417f2f122215
  review: drafted
---
