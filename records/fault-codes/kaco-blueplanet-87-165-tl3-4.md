---
id: fc:kaco-blueplanet-87-165-tl3-4
type: FaultCode
name: KACO new energy blueplanet TL3 4
aliases:
- '4'
- KACO new energy 4
- Feed in at max. MPP
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '4'
code_key: '4'
display_message: Feed in at max. MPP
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
  review_note: 'support check: partial - It is a status message (feed-in at max MPP), implying informational,
    but not explicitly classed.'
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  note: Normal MPP feed-in; investigate the plant only if feed-in is low.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Normal MPP feed-in and investigate only if insufficient power
    is stated; ''no production effect'' is implied but not explicit.'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
  review_note: 'support check: partial - Checks relate to strings/tracker and the array, but the code
    affecting the PV array is only loosely implied.'
- claim_id: c5
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
  review_note: 'support check: partial - Only checking for DC polarity reversal is mentioned, not a polarity
    measurement method per se.'
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r2
    h: 41289483e81c
  review: drafted
---
