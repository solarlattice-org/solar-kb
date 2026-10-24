---
id: symptom:rcd-nuisance-tripping
type: Symptom
name: Upstream RCD tripping
aliases:
- RCD tripping
- residual-current device trips
- RCD adjustment
- 30 mA residual current
- RCD
- residual-current device
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: When the upstream RCD trips, the inverter is cut off from the grid and stops feeding in. Any other
    loads on the same RCD also lose power.
  cite:
  - src: src:sma-kb-rcd-tripping-with-sunny-tripower-smart-energy-stpxx-0-3se-40
    loc: sec=h1
    h: ffc1b0c17dbb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passage says the inverter is disconnected and stops feeding in,
    but doesn''t mention AC power/voltage signal behavior or that phase voltage is lost; the signal details
    are inferred.'
---
When the RCD between the utility and the inverter trips, the inverter is disconnected from the grid and stops feeding in. Other loads on the same RCD also lose power. In monitoring data this shows up as the inverter's AC output going to zero, with no inverter fault behind it. The RCD sees the inverter's normal leakage current as residual current. So the rated residual current set in the inverter must not be higher than the RCD's rating, and it can be set lower if the RCD trips often. An RCD with a lower rating than the inverter manufacturer specifies can cause false trips, depending on system design. Check the RCD's type and rating against the inverter's datasheet first. A known firmware defect on some SMA Smart Energy inverters caused RCD trips. It affected systems with an RCD rated 100 mA or higher and a connected backup port, and a firmware update fixes it. Also check that fuses and breakers installed in series work together selectively, so that devices further upstream do not trip by mistake. If the trips keep happening, photograph the device that is tripping and send the pictures to the inverter manufacturer's support team.

<!-- review notes
- sentence 2: support check: partial - Disconnection and no feed-in are stated, but nothing about monitoring data or the absence of an inverter fault.
- sentence 4: support check: partial - Passage says a lower-rated RCD risks false tripping depending on system design, but the advice to check RCD type and rating against the datasheet first is not stated (type B compatibility is mentioned only loosely).
- sentence 5: support check: partial - The article describes the 100 mA+ RCD with backup port condition and a firmware update fix, but only for specific firmware versions on the STP Smart Energy; 'some SMA Smart Energy inverters' and calling it a defect is a slight generalization.
- sentence 7: support check: partial - The passage says to send pictures of the tripping device to Solis support if unresolved, but the statement generalizes to any manufacturer and omits the 'if the issue remains unresolved' condition.
- sentence 4: review: partial - The false-tripping risk from a lower-rated RCD, depending on system design, is stated, and the datasheets list RCD type and rating, but no passage advises checking these against the datasheet first.
- sentence 7: review: partial - The passage tells you to send pictures of the tripping device to Solis support if the problem stays unresolved, but the sentence widens this to any inverter manufacturer.
-->
