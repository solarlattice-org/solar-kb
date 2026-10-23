---
id: symptom:arc-fault-reset
type: Symptom
name: Arc fault alarm reset
aliases:
- AFDD user reset
- Reset AFD
claims:
- claim_id: c1
  rel: observed_as
  target: meas:arc-fault-reset-event-log
  note: Code W026 (AFDD user reset) is written only to the inverter's event history. No LED shows it,
    and on some UNO-DM models it does not appear on the display. The reset is done by the customer or
    installer, through the webserver, the display or the configuration software.
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=51.r11
    h: 5d75ecc7d08e
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r2
    h: 792bf98c8bad
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r11
    h: 33d87d607835
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r11
    h: 33d87d607835
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=52.r1
    h: 6d0b1668de77
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: tbl=47.r1
    h: 6d0b1668de77
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - W026 is only in event history with no LED and may not show on
    display, and reset is via webserver/display/software, but the ''UNO-DM'' model reference and the event-log
    measurement mapping are not stated in passages.'
- claim_id: c2
  rel: observed_as
  target: meas:afci-self-test-fault
  note: On UNO-DM models, Reset AFD clears E050 and runs the self-test again. If the DC arc is still present,
    the self-test ends with E053 instead of reconnecting.
  cite:
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: sec=h186
    h: c5d423ec1b8d
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: sec=h191
    h: c5d423ec1b8d
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:zero-ac-output
  note: If the inverter does not reconnect after the arc fault is reset, the fault in the PV array is
    still there and needs service.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h152
    h: 2149d6e5f9f2
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=6.4
    h: 0f67995cf961
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Passages say that if the inverter does not reconnect, service
    is needed to repair the array fault, but say nothing about AC output staying at zero with irradiance.'
- claim_id: c4
  rel: observed_as
  target: meas:arc-fault-alarm
  note: A reset follows an arc fault. Before the reset the red GFI LED and the ALARM LED are on and the
    POWER LED is off (Arc Fault pending).
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h152
    h: 2149d6e5f9f2
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: sec=6.4
    h: 0f67995cf961
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=34.r1
    h: aba1c021a0ad
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-quick-installation-guide-reve
    loc: tbl=21
    h: fb1b7b06c08c
  review: drafted
---
This warning records that a customer or installer manually cleared an arc fault error. The manufacturer says it is not an error in itself. It does not light any LED and is kept only in the inverter's event history, so look for it in the event log rather than on the front panel. Depending on the model, the reset is done with a button on the DC wiring box, the internal webserver, the display menu or the configuration software. Each reset means an arc fault came before it. That fault showed as the red GFI and ALARM LEDs on, with POWER off and the inverter disconnected from the grid. If the inverter reconnects normally after the reset, the arc was probably temporary or intermittent. Arcs are more likely in damp conditions and point to insulation breakdown, so still have the PV plant inspected. If the self-test fails again after the reset, or the inverter will not reconnect, the DC arc fault is still present. Lock out the AC and DC disconnects and get service to repair the array. Repeated reset entries in the log are a reason to check DC cables, connectors and module junction boxes for a recurring arc.

<!-- review notes
- sentence 4: support check: partial - Arc fault pending LED pattern and grid disconnection are stated, but 'each reset means an arc fault came before it' is an inference and the LED pattern is from a different model context.
- sentence 7: support check: partial - Passages advise inspecting DC cables, connections and junction boxes after an arc fault, but do not mention repeated reset log entries as a trigger or a recurring arc.
- sentence 4: review: partial - A reset following an arc fault, the LED pattern (POWER off, ALARM and GFI on) and the grid disconnection are all stated, but the LED pattern comes from the PVS-166/175 tables and the sentence applies it to every model's reset.
- sentence 7: review: partial - The passages say to check cables, connections and panel junction boxes after an arc fault, but they never treat repeated reset entries in the log as the trigger or mention a recurring arc.
-->
