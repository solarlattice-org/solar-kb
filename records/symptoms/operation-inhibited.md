---
id: symptom:operation-inhibited
type: Symptom
name: Operation inhibited
aliases:
- Permanent operation inhibition
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: Inverter stops feed-in and stays off until the inhibition is reset manually or the operating mode
    is set back to Start.
  cite:
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h59
    h: 2baabf343bb7
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h97
    h: 2a01965d1910
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h180
    h: 2a01965d1910
  - src: src:sma-kb-event-number-4301
    loc: sec=h1
    h: 9af6ae5c13d3
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h72
    h: c0c528d6a6bd
  - src: src:sma-kb-ereignis-9102
    loc: sec=h1
    h: 4c6511a06635
  review: drafted
  review_note: 'support check: partial - Passages state feed-in stops and manual reset or setting mode
    back to Start is needed, but nothing about AC power falling to zero in daylight or irradiance remaining
    normal.'
- claim_id: c2
  rel: observed_as
  target: meas:inverter-fault-indicator
  note: Red LED lights when the arc fault event triggers and stays red while operation is inhibited.
  cite:
  - src: src:sma-kb-event-number-4301
    loc: sec=h1
    h: 9af6ae5c13d3
  - src: src:sma-kb-sb-us-40-41-and-stp-us-40-41-reset-operation-inhibition-via-the-inverter-user-inter
    loc: sec=h1
    h: 2d907c77d866
  review: drafted
  review_note: 'support check: partial - Red LED illuminates when 4301/4302 triggers and a red LED persists
    until reset, but ''stays red throughout inhibition'' is only implied by the issue description.'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Events 4301/4302 for the arc, 8206/8210 as reminders after about ten minutes if not reset, and
    9102 for permanent inhibition after repeated AFCI trips; shown on the display or user interface depending
    on model.
  cite:
  - src: src:sma-kb-event-number-4301
    loc: sec=h1
    h: 9af6ae5c13d3
  - src: src:sma-kb-stp-us-41-events-8206-8210
    loc: sec=h1
    h: 4223b7d41d2f
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h59
    h: 2baabf343bb7
  - src: src:sma-kb-ereignis-9102
    loc: sec=h1
    h: 4c6511a06635
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:arc-fault-alarm
  note: Inhibition usually follows an arc fault detection by the AFCI.
  cite:
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h59
    h: 2baabf343bb7
  - src: src:sma-kb-stp-us-41-events-8206-8210
    loc: sec=h1
    h: 4223b7d41d2f
  - src: src:sma-kb-ereignis-9102
    loc: sec=h1
    h: 4c6511a06635
  review: drafted
---
Operation inhibition means the inverter has stopped feeding the grid and will stay off until someone resets it by hand. On SMA US inverters it usually follows an arc fault event 4301 or 4302. Events 8206 or 8210 are reminders that the arc fault has not been reset, and they can appear about ten minutes after the original event. You will see a red LED and the event code on the display or user interface, and AC output stays at zero even in full sun. Event 9102, permanent operation inhibition, occurs on some models after repeated trips, such as five AFCI trips in one day. These inverters switch their operating mode to Stop and need it set back to Start. Event 9102 can also follow a short-circuit fault that repeats three times in a row, so check the event history to find which condition triggered the stop. Before you reset, inspect the array and inverter for loose or exposed wires, damaged or mismatched DC connectors, and cracked or scorched modules. Also check rapid shutdown devices for damage and scan for hotspots with a thermal camera. Reset the inhibition only once, after the cause is fixed, because repeated reset commands can damage the inverter. If the arc event comes back, keep troubleshooting.

<!-- review notes
- sentence 3: support check: partial - Red LED and event code on display/UI are stated, but AC output staying at zero in full sun is not explicitly stated, though feed-in stopping is.
-->
