---
id: symptom:enclosure-door-open
type: Symptom
name: Enclosure door open
aliases:
- Door Switch Open
- Open Enclosure Door
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA Sunny Central CP-XT reports error 9008 when doors are opened while the inverter is running;
    the listed corrective measure is to contact the SMA Service Line.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r8
    h: c54a837019da
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:door-switch-status-point
  note: Tesla Megapack exposes a DNP3 'Door Switch Open' point that is set when any Megapack door is open
    (the Customer Interface Bay door excluded). Powin HVAC service checks confirm that the door status
    shows correctly as open or closed.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=175.r6
    h: 178f7dda5a06
  - src: src:powin-pom-011-s750-hvac-service-manual-rev-0
    loc: tbl=10.r1
    h: c0a034d73c3e
  review: drafted
---
This symptom means a door on an inverter or equipment enclosure was opened, often while the unit was running. On the SMA Sunny Central CP-XT it shows up as error 9008, which means doors were opened during operation, and SMA advises contacting its Service Line. Battery enclosures such as the Tesla Megapack report it through a door switch point in SCADA when one or more doors are open. Check first that the door status reading is correct when the door is actually open and when it is closed, so you can rule out a faulty door switch or status indication. Before anyone opens an enclosure door, complete the site door access checklist so that site communication and lockout of circuits are done first. The procedures for opening an enclosure door warn of arc flash risk, and some equipment manuals list conditions in which the doors must not be opened at all.

<!-- review notes
- sentence 1: support check: partial - Passages show doors opened during operation (SMA) and Megapack door open, but 'inverter or equipment enclosure, often while running' generalizes; only the SMA case is about running.
- sentence 3: support check: partial - The Megapack Door Switch Open DNP3 point is stated, but 'Battery enclosures such as' generalization and 'SCADA' are not explicitly stated (DNP3 point only).
- sentence 4: support check: partial - The passage says confirm door status displays accurately when open or closed, but the purpose of ruling out a faulty switch and 'check first' are not stated.
- sentence 1: review: partial - The passages back a door being opened on an SMA inverter during operation and on a Megapack, but the 'often while running' frequency and the general 'equipment enclosure' scope are generalizations.
- sentence 4: review: partial - The passage says to confirm the door status displays accurately when open or closed, but it does not give the purpose (ruling out a faulty door switch or indication) or say this is the first check.
-->
