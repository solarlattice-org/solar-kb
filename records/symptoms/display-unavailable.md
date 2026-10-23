---
id: symptom:display-unavailable
type: Symptom
name: Display unavailable
aliases:
- No display
claims:
- claim_id: c1
  rel: observed_as
  target: meas:blank-inverter-display
  note: 'SMA events 8801 to 8803: the LCD shows no information. Event 8803 means either no display is
    connected or the display connection is defective. The inverter keeps feeding power into the grid.'
  cite:
  - src: src:sma-kb-event-8803
    loc: sec=h1
    h: f5e9d34fdf79
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h248
    h: 07e2f1a8c44d
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h62
    h: 79904b650006
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h63
    h: a4810ceac09c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h417
    h: e02d688c3b88
  review: drafted
---
The inverter's display cannot show any information, and the inverter reports this as a No display event. On SMA Sunny Boy US inverters this appears as event numbers in the range 8801 to 8803. Event 8803 means either no display is connected or the display connection is defective, so the LCD stays blank. The inverter keeps feeding power into the grid, so production data should look normal even though the display is blank. First check whether a display is actually fitted. If none is connected, no further action is needed. If a display is fitted and its connection is defective, replace the display. Owners should contact their installer for further investigation.

<!-- review notes
- sentence 2: support check: partial - Events 8801 to 8803 are 'No display', but the passages don't mention Sunny Boy US specifically.
- sentence 4: support check: partial - Continued feed-in is stated, but 'production data should look normal' is a mild inference not explicitly stated.
-->
