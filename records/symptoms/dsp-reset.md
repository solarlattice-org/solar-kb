---
id: symptom:dsp-reset
type: Symptom
name: Signal processor reset
aliases:
- DSP reset
- RsDsp
- RsDspSlv1
- RsDspSlv2
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'On Sunny Island devices the reset shows as an event code: F702 for the device at L1 (master),
    and W791, W792 or W793 for slaves 1, 2 or 3.'
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r25
    h: c026f33e7fc1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r26
    h: 88c96cde3448
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r27
    h: 253a272f03ed
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=150.r1
    h: d69f6e4ce3fd
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=66.r1
    h: 70b113593b5b
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=71.r7
    h: f356e9811906
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=71.r8
    h: 65656442ecb4
  review: drafted
---
A signal processor reset is reported by SMA Sunny Island battery inverters when the device detects that a digital signal processor (DSP) has restarted. If the reset happens in the device at L1 (the master), it is logged as error F702 (RsDsp) at level 5. If it happens in a slave device, it is logged as a level 1 warning: W791 for slave 1, W792 for slave 2 and W793 for slave 3. Check the code first to see which device in the cluster reset, the master or a particular slave. A separate warning, W705, means the watchdog of the master's signal processor has tripped. Check whether it was logged too. The manual's only corrective action for these events is to contact SMA Service.

<!-- review notes
- sentence 4: support check: partial - Passages show codes distinguish master vs slaves, but nothing instructs checking the code first; that is an inferred recommendation.
- sentence 5: support check: partial - W705 watchdog of master's signal processor is stated, but the advice to check whether it was also logged is not in the passages.
-->
