---
id: method:grid-relay-self-test
type: DetectionMethod
name: Grid relay pre-connection self-test
aliases:
- relay test
- L-Netz / L-WR / N-Netz / N-WR
- active test before cold start
- relay check before grid connection
- Self-test of the relays
claims:
- claim_id: c1
  rel: produces
  target: meas:grid-relay-self-test-error
  note: 'Reported as messages such as L-Netz, L-WR, N-Netz or N-WR (SMA) or ''Error: Grid relay L1'' (KACO)
    when a grid relay fails to open or close, or sticks, during the pre-connection test.'
  cite:
  - src: src:sma-kb-message-l-netz-l-wr-n-netz-or-n-wr
    loc: sec=h1
    h: b42dc60cdbf6
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c2
  rel: produces
  target: meas:self-test-status-stuck
  note: If the inverter stays in the relay self-test status even with enough DC voltage, the manufacturer
    treats this as a device fault.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r3
    h: 3007b4ba272a
  review: drafted
---
Before it connects to the utility grid, the inverter tests its own grid relays automatically. If a relay has trouble opening or closing, the inverter runs the test again. If the relays still do not work correctly, it stays off the grid for safety reasons. If the disturbance keeps coming back, the inverter goes into permanent operation inhibition. If it stays in the self-test status even with enough DC voltage, that points to a device fault. The test can find a grid-side relay that is stuck, which means the relay is defective. One manufacturer notes that the test does not check whether the relay switches on. Relay test disturbances can also come from incorrect AC installation, so a failed test does not always mean a bad relay. First reset the message. If it comes back, check that L, N and PE are cleanly connected at the inverter and in the sub-distribution, and confirm with a voltage test, especially between N and PE.
