---
id: symptom:high-packet-error-rate
type: Symptom
name: High network packet error rate
aliases:
- package error rate
claims:
- claim_id: c1
  rel: observed_as
  target: meas:package-error-rate-high
  note: The SMA inverter interface reports the package error rate as either ok or high; a change of this
    status is flagged as an event.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h217
    h: a1c2873a3c05
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h300
    h: a1c2873a3c05
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:bad-packet-counter-increment
  note: On an SEL meter's Modbus interface, a format error returns Illegal Data Value (03h) and increments
    the Bad Packet Format communication counter.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=293
    h: 85985086a90a
  - src: src:sel-735-im-20250228
    loc: tbl=284.r3
    h: 6484e0987d4f
  - src: src:sel-735-im-20250228
    loc: tbl=288.r3
    h: 6484e0987d4f
  review: drafted
  review_note: 'support check: partial - The passages state a format error returns Illegal Data Value
    (03h) and increments Bad Packet Format, but don''t link it to high network packet error rate.'
- claim_id: c3
  rel: observed_as
  target: meas:network-comm-alert
  note: A monitoring-platform rule in the network communication category flags local network failures
    from common communication problems on devices connected by TCP and RS-485.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=11.r4
    h: 0b0e0447d7ec
  review: drafted
  review_note: 'support check: partial - The rule description is present, but nothing ties it to high
    packet error rate specifically.'
---
The inverter's network interface shows its package error rate as ok or high, and it records an event when that status changes. A high package error rate means the network is overloaded, or the link to the network switch or the DHCP server (router) is impaired. On an Ethernet link, check first that the network cable and connectors are undamaged and correctly plugged in. If the cabling is fine, suspect network overload: increase the data query intervals or reduce the number of devices on the network. On meters that use Modbus, malformed requests return an Illegal Data Value error and increase a Bad Packet Format counter. This counter helps show whether the errors come from packet formatting. Monitoring platforms can also flag local network failures from common communication problems on devices connected by TCP and RS-485.

<!-- review notes
- sentence 1: support check: partial - ok/high status and change notification are stated, but not explicitly that an event is recorded.
- sentence 3: support check: partial - Cable/connector check is listed as a corrective measure, but not stated as 'first'.
- sentence 4: support check: partial - Increasing query intervals and reducing devices are listed, but not framed as following good cabling or as suspecting overload (they are 'if necessary' measures).
- sentence 5: support check: partial - Format error returning Illegal Data Value and incrementing Bad Packet Format is stated, but the 'malformed requests' wording and the diagnostic purpose are not.
-->
