---
id: prod:sma-stp-tl-us
type: Product
name: Sunny Tripower TL-US
aliases:
- STP 20000 TL US
- STP12000-30000TL-US-10
- STP US-10
- Sunny Tripower TL-US-10
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-stptl-10-us-troubleshooting
    loc: sec=front
    h: b6309be603ef
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: sec=front
    h: 8a06f6cda2af
  - src: src:kb-sma-stptl-10-us-commissioning-the-inverter
    loc: sec=front
    h: 53dbfea7ec05
  review: drafted
- claim_id: c2
  rel: implements
  target: func:rapid-shutdown
  note: SMA documents activating a Rapid Shutdown DC discharge function on this family.
  cite:
  - src: src:kb-sma-stptl-10-us-activating-of-the-rapid-shutdown-dc-discharge-function
    loc: sec=front
    h: 2fb826526942
  review: drafted
  review_note: 'support check: partial - The passage is only a title about activating a Rapid Shutdown
    DC discharge function. That implies the function exists, but it doesn''t state outright that the family
    implements PV rapid shutdown.'
- claim_id: c3
  rel: compatible_with
  target: prod:sma-hybrid-controller
  note: The Hybrid Controller datasheet lists STP US-10 among the Sunny Tripower inverters it is compatible
    with.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r12
    h: 827e0069bf51
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2
    h: 3dd628d2646d
  review: drafted
---
The Sunny Tripower TL-US is an SMA family of three-phase string inverters for the US market. Its models are the STP 12000TL-US-10, 15000TL-US-10, 20000TL-US-10, 24000TL-US-10 and 30000TL-US-10. The installation manual has separate technical data sections: one covers the 12000, 15000 and 20000 models, and the other covers the 24000 and 30000 models. SMA documents a Rapid Shutdown DC discharge function that has to be activated on the inverter. SMA service articles cover commissioning, recommissioning, event messages, troubleshooting and checking the PV system for ground faults on this family. The SMA Hybrid Controller datasheet lists the STP US-10 among its compatible Sunny Tripower inverters. Installers returning a defective unit from abroad can look up its customs value for the TL-US-10 models in the SMA Online Service Center.

<!-- review notes
- sentence 1: support check: partial - The five model names are listed, and the family is Sunny Tripower TL-US. The passages don't say it is three-phase, a string inverter, or for the US market (though 'US' is in the name).
- sentence 3: support check: partial - The title shows SMA documents 'Activating of the Rapid Shutdown DC discharge function'. It doesn't explicitly say the function must be activated on the inverter.
-->
