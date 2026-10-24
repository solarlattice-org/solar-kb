---
id: fm:afci-nuisance-trip
type: FailureMode
name: Arc fault nuisance trip
aliases:
- false AFCI event
- nuisance trips
- AFCI events with Rapid Shutdown devices
- RSD humming noise during MPPT sweep
- false trips
- AFCI events
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:mlpe-electronic-noise
  note: During the inverter's periodic MPPT sweep (ShadeFix), a rapid shutdown device can be pulled below
    its threshold voltage and its electronics may hum; the inverter can read this noise as an arc.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:inverter-settings
  note: Reported when the ShadeFix MPPT sweep parameter is ON, which is the default on most current SMA
    models.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:rapid-irradiance-change
  note: Fast current changes caused by changing light, combined with a sensitive arc detection circuit,
    can trip the detector when no arc is present.
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
  review_note: 'support check: partial - u2 mentions the arc detection circuit being triggered falsely,
    but no passage names a detection board as the affected component; this is only implied.'
- claim_id: c5
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r21
    h: aa71c3bdef4e
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:rapid-shutdown-device
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
  review_note: 'support check: partial - u1 involves RSD devices as the noise source, but being ''affected''
    by the nuisance trip is not stated.'
- claim_id: c7
  rel: presents_as
  target: symptom:arc-fault-detected
  note: SMA event IDs 4301/4302/8204/8206/8210 are reported, sometimes at random across several inverters.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=4
    h: 121553a4ae2e
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:spurious-fault-event
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:inverter-shutdown
  cite:
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r21
    h: aa71c3bdef4e
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=2.r2
    h: 93b0ffeaef0c
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:operation-inhibited
  note: When AFCI is set with permanent operation inhibition, the inverter waits for a manual reset.
  cite:
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=4
    h: 121553a4ae2e
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=2.r2
    h: 93b0ffeaef0c
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r12
    h: 9d5e8686b009
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:inverter-audible-noise
  note: The humming comes from the rapid shutdown device electronics during the MPPT sweep, not from the
    inverter.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
  review_note: 'support check: partial - u1 says the RSD electronics hum during the sweep and the inverter
    reads it as an AFCI event, but it never lists inverter audible noise as a symptom, and the note that
    the hum is not from the inverter is only implied.'
- claim_id: c12
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:tactile-inspection
  note: Gently tug DC cables at connectors and in the combiner box to find loose terminations or bad crimps.
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
  review_note: 'support check: partial - u2 describes gently tugging DC cables to find loose or badly
    crimped connections, but this finds real faults, not the nuisance trip itself.'
- claim_id: c14
  rel: detected_by
  target: method:insulation-resistance-test
  note: Used on cabling where a hands-on inspection is not possible, such as residential rooftops. It
    does not pinpoint the fault location.
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
  review_note: 'support check: partial - u2 recommends a megohm meter where hands-on inspection is not
    possible and says it does not pinpoint the fault, but it frames this as finding a cabling failure,
    not detecting a nuisance trip.'
- claim_id: c15
  rel: distinguished_from
  target: fm:arc-fault
  by: method:visual-inspection
  note: A real arc leaves evidence such as discolored wiring or racking, melted connectors or insulation,
    and burned junction boxes. A false trip leaves no such damage and no loose or badly crimped connections.
  cite:
  - src: src:solis-service-bulletin-arc-fault-detection-and-troubleshooting
    loc: sec=h2
    h: 8d8ea2c308c7
  review: drafted
  review_note: 'support check: partial - u2 says arcing leaves evidence that a visual inspection finds,
    but it does not state that a false trip leaves none.'
- claim_id: c16
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Set ShadeFix to 'NO' when random AFCI events appear across several inverters at sites with rapid
    shutdown devices.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:firmware-update
  note: The manufacturer said a future firmware release would address the condition.
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:sma-kb-afci-events-in-sites-with-rapid-shut-down-devices
    loc: sec=h1
    h: 7f03da2b22dc
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:latched-fault-reset
  note: Reset only after the array has been inspected.
  cite:
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=4
    h: 121553a4ae2e
  - src: src:kb-sma-stptl-10-us-event-messages
    loc: tbl=1.r21
    h: aa71c3bdef4e
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r12
    h: 9d5e8686b009
  review: drafted
  review_note: 'support check: partial - u9, u13 and u24 support a manual reset of operation inhibition,
    and u2 requires inspecting the site before resetting, but only u2 links reset to nuisance trips and
    it is not in the cited passages for this statement.'
- claim_id: c20
  rel: mitigated_by
  target: mit:close-monitoring
  note: Investigate recurring AFCI events at once. If no cause is found, take the inverter out of service.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h85
    h: 07b9502017da
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h84
    h: b85bcfdc3194
  review: drafted
---
An arc fault nuisance trip happens when the inverter's arc detector reports an arc but no real arc is present in the DC circuit. It can be caused by fast current changes from changing light. At sites with rapid shutdown devices, those devices can also hum during the inverter's MPPT sweep, and the inverter may read that noise as an arc. The inverter logs an arc event, stops feeding the grid, and may stay locked out until someone resets it manually. Never assume a trip is false. Inspect the array before every reset and look for discolored or melted wiring, burned junction boxes, and loose or badly crimped connectors. Where the array cannot be reached, test the cabling with a megohm meter. This finds a fault but does not show where it is. If random arc events affect several inverters at a site with rapid shutdown devices, turning off the ShadeFix sweep can stop the nuisance trips. A firmware update was planned to fix this. If arc events keep recurring, investigate right away. If the cause cannot be found, take the inverter out of service.
