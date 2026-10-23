---
id: symptom:dc-contactor-stuck
type: Symptom
name: Contactor fails to open
aliases:
- DC Cont. Err
- BoxQ9NotOpen
- BoxQ2NotOpen
- BoxQ10NotOpen
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Reported as an inverter event or error message: DC Cont. Err on the Yaskawa SGI-XTM (also written
    to the event log), and contactor or tie switch does-not-open events on SMA devices.'
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  - src: src:sma-doc-278742
    loc: tbl=75.r4
    h: 497107d1ffb4
  - src: src:sma-doc-259761
    loc: tbl=71.r4
    h: f6a196b46f00
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=75.r2
    h: 608cf0b645aa
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=74.r7
    h: d302843ca6e7
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=75.r4
    h: 47fd0b479faa
  review: drafted
---
The inverter reports that a contactor was commanded to open but did not open properly. On the Yaskawa SGI-XTM it shows on the user interface as DC Cont. Err and is also written to the event log. SMA equipment reports the same kind of fault as a tie contactor, tie switch or load-shedding contactor that will not open. Some inverters raise a general contactor failure, where the contactor can fail either open or closed. In that case a power cycle is the first step, and technical support is called if the error stays. A contactor that will not open cannot be fixed in the field. The manufacturers say to contact service and have an authorized provider inspect and repair the inverter.

<!-- review notes
- sentence 1: support check: partial - Passages say the contactor failed to open, but none states it was 'commanded' to open; that detail is implied only.
- sentence 4: support check: partial - The AC Contactor Failure row states fail open or closed, power cycle first, then contact Technical Support; 'some inverters' is a generalization, and the row is AC grid contactor specifically.
- sentence 5: support check: partial - Passages say to contact service and have an authorized provider inspect/service, but do not say it cannot be fixed in the field or mention repair explicitly.
-->
