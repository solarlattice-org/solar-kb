---
id: symptom:invalid-access-code
type: Symptom
name: Invalid access code
aliases:
- SMA Grid Guard code invalid
- Installer code invalid
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA inverters log event 9002, shown as 'SMA Grid Guard code invalid' or 'Installer code invalid',
    when the Grid Guard code entered is wrong. The operating parameters stay locked.
  cite:
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h35
    h: 1d594dc2e48f
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r50
    h: 6a9b8c71bb4f
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h41
    h: 1d594dc2e48f
  - src: src:sma-doc-278742
    loc: tbl=76.r2
    h: ce2ed8a1ddf6
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r2
    h: ac6479fb8aba
  - src: src:sma-doc-259761
    loc: tbl=72.r2
    h: ce2ed8a1ddf6
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r49
    h: 6a9b8c71bb4f
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h50
    h: 3514d406dcf8
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h64
    h: 1d594dc2e48f
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h440
    h: 7ba5aa81e7dc
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h607
    h: 7ba5aa81e7dc
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r52
    h: 6a9b8c71bb4f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h422
    h: 7ba5aa81e7dc
  review: drafted
---
SMA inverters show this event when someone enters a wrong SMA Grid Guard code while trying to change protected settings. Look for event number 9002 in the inverter event log. Depending on the model and manual, it reads either SMA Grid Guard code invalid or Installer code invalid. Because the code was rejected, the operating parameters stay protected and the requested changes are not applied. This is an access problem with the entered code, not a hardware or production fault. To fix it, enter the correct SMA Grid Guard code and then make the parameter change again.

<!-- review notes
- sentence 1: support check: partial - Passages say the event relates to an incorrect Grid Guard code, but don't say it occurs while trying to change protected settings.
- sentence 2: support check: partial - Event 9002 with both message variants is stated, but the passages don't mention the event log or that the wording depends on model/manual.
- sentence 4: support check: partial - Passages show an incorrect code issue with parameters protected, but don't explicitly say it is not a hardware or production fault.
- sentence 5: support check: partial - Corrective measure to enter the correct code is stated, but the follow-up step of making the parameter change again is not.
-->
