---
id: symptom:generator-out-of-tolerance
type: Symptom
name: Generator voltage or frequency out of tolerance
aliases:
- Voltage of the generator too low
- generator voltage too low
- generator voltage too high
- Generator synchronization error
- Frequency of the generator too high
- external source voltage outside thresholds
- Generator does not synchronize
- external source outside configured range
- Grid fault
- Grid incident
- ExtVtgLoss
- External voltage failure
- ExtVtgRdtErr
- Synchronization not executed
- Generator Meter Out of Bounds
claims:
- claim_id: c1
  rel: observed_as
  target: meas:external-source-out-of-threshold
  note: Off-grid/backup inverter (Sunny Island) logs a grid fault or external voltage failure event when
    the voltage and/or frequency of the generator at the external connection leaves the configured range;
    the external voltage and frequency measured values show the excursion.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h690
    h: 30805d2b1acb
  - src: src:sma-doc-278742
    loc: sec=h772
    h: 0c35cf0fd04c
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=55.r4
    h: 5ef91156cc62
  - src: src:sma-doc-259761
    loc: tbl=59
    h: 6922e0c76236
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=58.r4
    h: 0a30dd18253b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: observed_as
  target: meas:generator-sync-error-event
  note: Synchronization with the generator not successful; Sunny Island events 1615 and 1616 are reported
    when the generator does not synchronize properly.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h825
    h: 0a101064a7b5
  - src: src:sma-doc-259761
    loc: sec=h736
    h: 4951907496f9
  - src: src:sma-kb-rectifying-1615-and-1616-generator-synchronization-issues-in-sunny-island-inverters
    loc: sec=h1
    h: 97871fd2eefd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Sync not successful and 1615/1616 sync errors are stated, but
    the passages don''t state that these are an observation of out-of-tolerance voltage/frequency (only
    that parameters going out of range may result in sync error).'
- claim_id: c3
  rel: observed_as
  target: meas:generator-meter-out-of-bounds-flag
  note: Boolean status register reporting that generator voltage or frequency measurements are out of
    bounds.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=124.r11
    h: ed15a1d25456
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:brief-generator-connection
  note: The inverter connects to the running generator only for a short time, then disconnects; reconnection
    is delayed because connection and disconnection thresholds differ (hysteresis).
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h583
    h: 90446aeb9fde
  - src: src:sma-doc-259761
    loc: sec=h855
    h: 7bfd72b92a8c
  - src: src:sma-doc-259761
    loc: sec=h856
    h: 511b56961bf2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The off-grid or backup inverter reports that the voltage and/or frequency of the generator at its external connection is outside the configured range, logged as a grid fault, grid incident or external voltage failure. Related signs are failed generator synchronization events, a generator meter out-of-bounds flag, or the inverter connecting to the running generator only briefly. Watch the measured external voltage and external frequency values while the system runs to see which limit is crossed and when, especially at the moment of synchronization. A frequent cause is thresholds that are too strict, such as a maximum generator voltage set too low or a minimum generator frequency set too high; set them to match the generator's technical data. If the generator is overloaded, its voltage and frequency sag; reduce or stagger loads and let voltage and frequency return to nominal before expecting reconnection. If synchronization fails, check first that the generator can start and has fuel, that the voltage at the AC2 connection is constant and stable, and that the fuse and circuit breaker are intact. If thresholds are correct and the problem persists, the generator's own regulation may be unsuitable: discontinuous frequency or voltage behavior can make operation with the inverter unstable, so adjust the generator voltage or frequency.

<!-- review notes
- sentence 2: support check: partial - Sync failures, the out-of-bounds flag and brief connection appear in the passages, but none states they are related signs of this condition explicitly.
- sentence 4: support check: partial - Too-strict thresholds (max voltage too low, min frequency too high) causing brief connection and setting to generator data are stated, but 'frequent cause' is not stated.
- sentence 5: support check: partial - Overload remedies (reduce/stagger loads, wait for nominal values) are stated, but the passages do not say voltage and frequency sag under overload.
- sentence 6: support check: partial - Generator start/fuel and stable AC2 voltage are stated, but the fuse and circuit breaker check is stated in a different context (voltage/frequency not within thresholds) and not as a sync-failure first check.
- sentence 7: support check: partial - Discontinuous generator frequency/voltage behavior being unsuitable and adjusting generator voltage/frequency are stated, but the link to thresholds-correct persistence and 'adjust' as the remedy for it is inferred.
- sentence 4: review: partial - The passages state that a maximum voltage set too low or a minimum frequency set too high are too strict and should be set to the generator's data, but they do not call this a frequent cause.
- sentence 7: review: partial - The passages say discontinuous generator behavior is unsuitable and can cause instability, and they list adjusting generator voltage/frequency as a measure, but the condition 'if thresholds are correct and the problem persists' and the link between these points are inferred.
-->
