---
id: symptom:arc-fault-detected
type: Symptom
name: Arc fault detected
aliases:
- ARC Protect
- ARC-FAULT
- Electric arc detected
- DC series arc fault
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: The LCD shows the arc fault message. On FIMER units the error code can be read through the internal
    web server.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h120
    h: 96e96d3db561
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.8
    h: 067a93ba212d
  - src: src:yaskawa-solectria-pvi-36tl
    loc: fig=131
    h: edb18b4cf3a2
  - src: src:yaskawa-solectria-pvi-36tl
    loc: tbl=36.r6
    h: b6a836ab9105
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=27
    h: d30e74190b7e
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: The inverter shuts down or stops feeding in, and stays off until the arc fault is cleared manually
    or operation inhibition is reset.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h120
    h: 96e96d3db561
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=4.4.8
    h: 067a93ba212d
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  - src: src:kb-sma-sbx1spus40-event-messages
    loc: tbl=1.r17
    h: ec4414cba702
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=27
    h: d30e74190b7e
  - src: src:kb-sma-sbsexx-us-50-manual-restart-after-electric-arc
    loc: sec=h1
    h: 056aee0429a1
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h72
    h: 609b66a0a612
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: observed_as
  target: meas:visible-burn-marks
  note: Arcing can leave discolored wiring or racking, melted connectors or insulation, and burned module
    junction boxes.
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
---
The inverter's arc fault detector picks up the electrical noise of a DC series arc. The inverter then shuts down and shows a message such as Arc Fault Detected, ARC Protect or Electric arc detected. In monitoring data, AC output stops and feed-in does not restart until the fault is cleared manually or operation inhibition is reset. A real arc fault usually comes from damaged, pinched or abraded conductors, loose or separated connections, poor crimps, cracked or corroded solder joints, degraded junction boxes or rodent damage. Look for evidence of arcing: discolored wiring or racking, melted connectors or insulation, and burned junction boxes. Gently tug on DC cables and connectors to find loose terminations, including factory crimps on the modules. False trips can happen when light changes cause rapid current swings, but the site must still be inspected before every reset. If no array or wiring damage is found, suspect a failed arc detection board. Check that the logic connector to the arc board is secure, then run the arc fault self-test. If the alarm comes back, replace the arc board or wiring box. Some inverters report which string group detected the arc, which narrows the search to the strings on those inputs.

<!-- review notes
- sentence 6: support check: partial - Check logic connector, run self-test, and replace arc board or wiring box if alarm recurs are stated, but 'if no array or wiring damage is found, suspect a failed arc board' is only loosely implied (u23 says if no issues found contact service).
-->
