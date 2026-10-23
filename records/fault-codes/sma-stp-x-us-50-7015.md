---
id: fc:sma-stp-x-us-50-7015
type: FaultCode
name: SMA STP-X-US 7015
aliases:
- '7015'
- SMA 7015
- Fault sensor interior temperature
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '7015'
code_key: '7015'
display_message: Fault sensor interior temperature
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h568
    h: 43c32662cf90
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h684
    h: 43c32662cf90
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h685
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h568
    h: 43c32662cf90
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h569
    h: b75389760f61
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h685
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h569
    h: b75389760f61
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h685
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h569
    h: b75389760f61
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h685
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h569
    h: b75389760f61
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h685
    h: b75389760f61
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h686
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h569
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h570
    h: 417f2f122215
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.54
    h: c8f78c265f7d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h686
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.41
    h: feff490af79f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h570
    h: 417f2f122215
  review: drafted
---
