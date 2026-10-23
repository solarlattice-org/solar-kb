---
id: symptom:manual-grid-disconnect
type: Symptom
name: Manual grid disconnection
aliases:
- Manual grid disconnection release
- Manual network disconnect release
- GdManOff
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: After the manual disconnection procedure started from the multi-function buttons, the device is
    reported as disconnected from the grid. While it stays disconnected, AC output should read zero.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=49.r4
    h: cdc6ba054c3c
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=49.r5
    h: bc425c0c0c9f
  review: drafted
  review_note: 'support check: partial - Passages say the device is disconnected from the grid after the
    procedure, but zero AC power/current and staying zero until reconnection are not stated (only implied).'
---
The procedure starts when the right-hand function button is pressed. Afterwards the unit reports that it is disconnected from the grid. SMA battery inverters log a similar operator action as an event, 'Manual grid disconnection release' or 'Manual network disconnect release'. On Sunny Island units it appears as GdManOff, 'Manual grid release'. Do not confuse it with automatic disconnections. Grid protection trips the inverter after a set delay when voltage or frequency goes outside limits, and some inverters drop off the grid on a schedule to run an insulation test.

<!-- review notes
- sentence 1: support check: partial - Passages show the button press commences the procedure and the device is then disconnected, but one passage says a brief press (<1 sec) and another a >5 sec press, so the unqualified statement omits the press duration.
- sentence 2: support check: partial - Event 1614 'Manual grid disconnection release' / 'Manual network disconnect release' and GdManOff 'Manual grid release' are in the passages, but the Sunny Island/SMA battery inverter attribution and the 'similar operator action' framing aren't stated.
-->
