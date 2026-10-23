---
id: method:dc-injection-measurement
type: DetectionMethod
name: Grid DC component measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:grid-dc-current-high
  note: SMA inverters flag this as event 6 or 601 when the DC share of the grid current exceeds the set
    tripping threshold; the inverter disconnects and reconnects after the grid monitoring time.
  quote: the inverter has detected an excessively high proportion of direct current in the grid current
  cite:
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h6
    h: b24b7952dacf
  - src: src:sma-kb-event-number-6-601
    loc: sec=h1
    h: a9018d679621
  review: drafted
  review_note: 'support check: partial - Events 6/601, excessive DC in grid current, disconnect and reconnect
    after grid monitoring time are stated, but ''exceeds the set tripping threshold'' is only implied
    (threshold mentioned, not explicitly the trigger).'
---
This check looks for a direct current component on the grid connection. It is the follow-up step when an SMA inverter reports too much DC in its grid current. When the inverter detects this condition, it disconnects from the grid for safety. It switches back on by itself after the grid monitoring time set by the country standard. Before measuring, use a communication tool such as Sunny Explorer to read out the country standard, the DC current monitoring trip threshold and the event log. Then check the grid connection for direct current. On single-phase inverters, swapping the phases may be needed. If the event keeps coming back, contact the grid operator. The operator decides whether to fix the grid or to allow a higher monitoring threshold on the inverter. You need an SMA Grid Guard code to change this protection parameter. You can request one through the SMA Online Service Center. Use a measuring device whose range covers the inverter's maximum AC and DC voltage.

<!-- review notes
- sentence 6: support check: partial - A Grid Guard Code is required for changing specific parameters and can be requested via the SMA Online Service Center, but the passage doesn't specifically tie it to this protection parameter.
-->
