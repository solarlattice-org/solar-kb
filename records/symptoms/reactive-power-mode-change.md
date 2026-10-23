---
id: symptom:reactive-power-mode-change
type: Symptom
name: Reactive power mode change
aliases:
- Reactive power mode changed
- Q-mode Change
claims:
- claim_id: c1
  rel: observed_as
  target: meas:reactive-power-mode-event-log
  note: 'FIMER/ABB code W022: recorded only in the inverter''s event history. No LED lights for it, and
    on some UNO-DM models it does not appear on the display.'
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r8
    h: 3735cef94281
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r8
    h: 20d1f512c6e3
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r7
    h: 7e769a00aaf0
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r8
    h: 20d1f512c6e3
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=46.r8
    h: 3cdae2f5a508
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=51.r8
    h: 3cdae2f5a508
  review: drafted
---
This message appears when someone changes the way the inverter manages reactive power. FIMER and ABB string inverters log it as warning code W022. The change is made by the customer or installer through the internal webserver, the Web User Interface, the display or the advanced configuration software, depending on the model. The manuals say it is not an error. The inverter only stores it in its event history, and no LED lights for it. On some UNO-DM models the code is not shown on the display, so look for it in the event log. If the entry is unexpected, check the reactive power control settings, such as Cosphi(P), Q Set, Cosphi Set and Q(V). Do not change these settings unless the grid operator asks for it. Some inverters can also switch to a reactive power mode chosen by the grid operator when the setpoint is lost, for example after a communication failure with the plant controller.

<!-- review notes
- sentence 1: support check: partial - W022 reactive power mode changed is supported, but 'FIMER and ABB string inverters' brand attribution is not stated in the passages.
- sentence 4: support check: partial - The passages say W022 is 'not visualised on display' with an asterisk, but do not name UNO-DM models; the event history is stated as where it's saved.
- sentence 5: support check: partial - Passage lists the settings and says not to change them unless the grid operator requests, but does not say to check them when the entry is unexpected.
- sentence 6: support check: partial - Passage says the grid operator can request switching to a specified mode when the setpoint is absent, but doesn't say 'some inverters' or that the inverter switches automatically.
-->
