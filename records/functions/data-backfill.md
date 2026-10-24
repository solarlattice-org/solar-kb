---
id: func:data-backfill
type: Function
name: Data backfill after communication loss
aliases:
- breakpoint resume
- cached data upload
- data backfill
- Breakpoint Resume Transmission
- Resume Data Transmission
category: Monitoring
function_kind: monitoring
claims:
- claim_id: c1
  rel: requires
  target: tool:solis-soliscloud
  note: Backfilled offline history from Solis stick loggers and data loggers is viewed in SolisCloud after
    the network recovers.
  cite:
  - src: src:kb-solis-44002823125-resume-data-transmission-after-a-disconnected-network-offline
    loc: sec=h5
    h: a1129aa7fe07
  - src: src:kb-solis-44002823125-resume-data-transmission-after-a-disconnected-network-offline
    loc: sec=h4
    h: a4317e389e84
  review: drafted
- claim_id: c2
  rel: subclass_of
  target: func:monitor-key-data
  note: Backfill keeps inverter generation records complete through network outages so that monitoring
    data has no gaps.
  cite:
  - src: src:kb-solis-44002823125-resume-data-transmission-after-a-disconnected-network-offline
    loc: sec=h2
    h: b8f17ad25378
  - src: src:kb-solis-44002823125-resume-data-transmission-after-a-disconnected-network-offline
    loc: sec=h8
    h: b91e165700a1
  review: drafted
---
Data backfill lets a data logger cache inverter data locally while the network is down, then upload the stored history once the connection comes back. On Solis loggers the cached data survives a power failure. After reconnection, real-time data keeps uploading on a parallel thread while the history is backfilled, so live reporting is not held up. Cached records keep their original collection timestamps, so the cloud platform can rebuild the correct time sequence for generation statistics and fault tracing. Solis stick loggers such as the S1-W4G-ST and S2-WL-ST can cache about 30 days of data for one inverter, and the period shrinks as more inverters are connected. The Solis MB-G4-W4 and MB-S4-W4 data loggers can cache about 30 days of data for up to 30 inverters, or about 15 days for 60 inverters. On both logger types, backfill runs at about 3 seconds per data packet, and the history can then be viewed in SolisCloud. On third-party loggers that push data to AlsoEnergy LocusNOC, backfill of an outage period is not guaranteed and depends on the device's storage.

<!-- review notes
- sentence 7: support check: partial - The passage says that depending on device storage data may or may not backfill, but doesn't explicitly say backfill is 'not guaranteed' generally; it's specific to Mocquisuite devices, not all third-party loggers.
-->
