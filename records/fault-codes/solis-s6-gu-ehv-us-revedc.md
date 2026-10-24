---
id: fc:solis-s6-gu-ehv-us-revedc
type: FaultCode
name: Solis S6-GU Reve-DC
aliases:
- Reve-DC
- revedc
- Solis Reve-DC
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: Reve-DC
code_key: revedc
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r6
    h: 07ff73591f84
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r6
    h: 07ff73591f84
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:unbalanced-mppt-connection
  note: 'Alternative cause: strings with differing module counts on the inputs.'
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r6
    h: 07ff73591f84
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r6
    h: 07ff73591f84
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r6
    h: 07ff73591f84
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r6
    h: 07ff73591f84
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only at night with string current below 0.5 A and DC switches off.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r6
    h: 07ff73591f84
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r6
    h: 07ff73591f84
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r10
    h: 8b1a0c30407d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when polarity is correct but module counts differ between strings.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=14.r6
    h: 07ff73591f84
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r6
    h: 07ff73591f84
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:solis-s6-gu-ehv-us
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=12.r6
    h: 1bc234caf689
  review: drafted
---
