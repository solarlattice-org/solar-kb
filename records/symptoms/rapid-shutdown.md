---
id: symptom:rapid-shutdown
type: Symptom
name: Rapid shutdown triggered
aliases:
- Rapid Shutdown was triggered
- Rapid Shutdown successful
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-input-voltage-discharged
  note: Event 9035 confirms that the voltage at the DC inputs and the AC output was discharged. The system
    must bring the DC conductors below 30 V within 30 seconds. This is a requirement, not a loss figure.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r3
    h: c0aa437efcaf
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  review: drafted
  review_note: 'support check: partial - Event 9035 discharge confirmation and the <30 V within 30 s requirement
    are stated, but the passages say nothing about the specific signal behaviors (collapse shortly after
    initiation, all MPPT inputs falling simultaneously).'
- claim_id: c2
  rel: observed_as
  target: meas:ac-disconnect-open
  note: The On/Off position of the main PV system AC disconnect shows rapid shutdown status. The Off (Open)
    position means a rapid shutdown has been initiated.
  cite:
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  review: drafted
---
When a Rapid Shutdown is triggered, the inverter reports it as an event and disconnects its AC side, so production stops. A separate success message confirms that the voltage at the DC inputs and the AC output has been discharged. Rapid shutdown is normally started by opening the main PV system AC disconnect, so check first whether that switch is in the Off (Open) position. A grid power failure can also start it: if the grid voltage does not come back within the ride-through time, the inverter disconnects and starts a rapid shutdown. If the shutdown event comes with an error in the Rapid Shutdown system instead, check whether the function is configured wrongly, whether the PV array disconnect switches work, and what their standby voltage is. Enable the function only when PV array disconnect switches are installed, because without them the inverter cannot discharge the DC conductors and may be damaged.
