---
id: prod:sma-sunny-island-us
type: Product
name: Sunny Island 4548-US / 6048-US
aliases:
- Sunny Island US
- SI 4548 US
- SI 6048 US
- SI 4548-US-10
- SI 6048-US-10
- SI 4548/6048-US
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-sixx-20-us-commissioning
    loc: sec=front
    h: 0e5700fcb4b6
  - src: src:kb-sma-sixx-20-us-led-signals
    loc: sec=front
    h: 85b2c477ff9f
  review: drafted
- claim_id: c2
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: Maximum efficiency, SI 4548-US-10
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159
    h: 499768f9e93c
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159.r1
    h: fbbba79b245a
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c3
  attr: efficiency
  value:
    nominal: 94.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, SI 4548-US-10
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159
    h: 499768f9e93c
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159.r3
    h: ca0562e71f4f
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c4
  attr: efficiency
  value:
    min: 90
    unit: unit:PERCENT
  conditions: SI 4548-US-10, over 5% Pnom to 120% Pnom
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159
    h: 499768f9e93c
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=159.r2
    h: 17eca6a6e174
  review: drafted
- claim_id: c5
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: Maximum efficiency, SI 6048-US-10
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=163
    h: 4db8cc99f6f1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=163.r1
    h: f207f284e149
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c6
  attr: efficiency
  value:
    nominal: 94
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, SI 6048-US-10
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=163
    h: 4db8cc99f6f1
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: efficiency
  value:
    min: 90
    unit: unit:PERCENT
  conditions: SI 6048-US-10, over 5 to 120% Pnom
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=163
    h: 4db8cc99f6f1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=163.r2
    h: 35a2d6e3b672
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:rs485
  note: Galvanically insulated RS485 communication is optional.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=161.r8
    h: f3af70b11a05
  review: drafted
- claim_id: c9
  rel: requires
  target: prod:sma-multicluster-box
  note: Multicluster Box MCB-12U is needed when clusters are combined into a Multicluster system.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=16.1
    h: adb5b04fd881
  review: drafted
  review_note: 'support check: partial - MCB-12U is required for Multicluster systems, but not for every
    unit; ''requires'' is conditional on multicluster use, which the note captures roughly.'
- claim_id: c10
  rel: compatible_with
  target: arch:battery-inverter-cluster
  note: Each cluster has a master connected to slaves over a communication interface.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=16.1
    h: adb5b04fd881
  review: drafted
  review_note: 'support check: partial - Passage describes clusters with master and slaves, but compatibility
    with a battery inverter cluster architecture is implied rather than stated.'
---
The Sunny Island 4548-US and 6048-US are SMA battery inverters; the operating manual applies to models SI 4548-US-10 and SI 6048-US-10 as of firmware version 7.3. Both models reach a maximum efficiency of 96%, with CEC weighted efficiency of 94.5% for the 4548-US and 94.0% for the 6048-US. Efficiency stays above 90% from 5% to 120% of nominal power. Galvanically insulated RS485 communication is available as an option. Within a cluster, a communication interface links the master unit to the slave units. For more output, up to four clusters can be combined into a Multicluster system. This needs the Multicluster Box MCB-12U and a Multicluster Piggy-Back fitted in the external communication slot.

<!-- review notes
- sentence 6: support check: partial - Up to four clusters, MCB-12U required and MC-PB plugged into external communication slot are stated, but passage doesn't explicitly say the Piggy-Back is required for Multicluster, only how it's installed.
-->
