---
id: prod:solis-s6-eh1p-h-us
type: Product
name: Solis S6-EH1P(3.8-11.4)K-H-US
aliases:
- S6-EH1P3.8K-H-US
- S6-EH1P5K-H-US
- S6-EH1P7.6K-H-US
- S6-EH1P9.9K-H-US
- S6-EH1P10K-H-US
- S6-EH1P11.4K-H-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=front
    h: 65d0ffd891c8
  review: drafted
  review_note: 'support check: partial - The passage is only the word ''solis'', which names the manufacturer
    loosely but doesn''t state that this product is made by Solis.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Listed as bi-directional transformerless grid support utility interactive power conversion equipment,
    permanently connected.
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=h295
    h: 7f223e1bec10
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=h302
    h: bfdb64161fcb
  review: drafted
- claim_id: c3
  rel: implements
  target: func:dc-arc-fault-protection
  note: Integrated AFCI listed as Yes for the 3.8, 5, 7.6, 9.9, 10 and 11.4 kW models.
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=24.r24
    h: 9fe41bf4e353
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=18.r24
    h: ea291ef4e968
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=21.r24
    h: 01331fa477ca
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=27.r24
    h: c8b96dc649c0
  review: drafted
  review_note: 'support check: partial - AFCI is listed Yes for 3.8, 5, 7.6, 9.9, 10 and 11.4 kW models,
    but the passages don''t cover the other models, such as 6 and 8 kW.'
- claim_id: c4
  rel: implements
  target: func:ground-fault-protection
  note: Ground fault detection listed as Yes in the technical data tables.
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=18.r22
    h: a51867873d79
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=24.r22
    h: 313fd2091907
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=21.r22
    h: 46a38bb50c53
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=27.r22
    h: 40b39ae6dff4
  review: drafted
- claim_id: c5
  rel: implements
  target: func:reverse-polarity-protection
  note: DC reverse-polarity protection applies to the PV inputs only.
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=18.r25
    h: 85b70a18579a
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=24.r25
    h: a098d9570204
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=27.r25
    h: 373b5578d090
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=21.r25
    h: 802746864b1d
  review: drafted
---
The Solis S6-EH1P(3.8-11.4)K-H-US is a family of single-phase hybrid inverters from Solis. They are transformerless, bi-directional, utility-interactive units with grid support, and they are permanently connected. The certification listing names the 3.8, 5, 7.6, 9.9, 10 and 11.4 kW models, among others. Every model has an integrated AFCI for DC arc-fault protection and has ground fault detection. DC reverse-polarity protection covers the PV inputs only. The technical data refers to a separate compatibility list for the supported rapid shutdown receivers and for the number of batteries per inverter. The family holds a CSA certification under a product class covering power systems equipment certified to U.S. standards. The alarm messages include 12Power-FAULT for a 12 V supply fault, AFCI Check FAULT for an AFCI self-check fault, and DSP-B-FAULT for lost communication between the main and slave DSPs. For each one, the advice is to restart the inverter or contact the installer.

<!-- review notes
- sentence 1: support check: partial - The passages support transformerless, bi-directional, grid support, utility-interactive and permanently connected, but 'single-phase hybrid inverters' is not stated (only the 'EH1P' model name hints at it), and 'solis' alone doesn't establish the maker.
- sentence 3: support check: partial - Evidence covers only the 3.8, 5, 7.6, 9.9, 10 and 11.4 kW models, so 'every model' is overstated, as the 6 and 8 kW models are not covered.
- sentence 1: review: partial - The CSA listing supports bi-directional, transformerless, grid support, utility interactive and permanently connected, but 'single-phase hybrid' is not stated in the passages.
-->
