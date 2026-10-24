---
id: concept:inverter-cooling
type: Concept
name: Inverter cooling
aliases:
- forced-air cooling
- natural convection cooling
- fan-cooled
- natural convection
- fan-assisted cooling
- controlled forced-air ventilation
- temperature-controlled forced air cooling
- cooling concept
category: Inverters
concept_kind: technology
claims:
- claim_id: c1
  rel: explains
  target: concept:thermal-derating
  note: When cooling cannot remove enough heat, the inverter limits its maximum output power to protect
    semiconductors and other components; a failed fan also curtails output.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=7.1
    h: dccb778213f0
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=7.1
    h: 5f864ecd896b
  review: drafted
- claim_id: c2
  rel: related_to
  target: state:derating
  note: Temperature derating is a protective state, not an error; it can be triggered by ambient temperature
    or internally measured temperatures.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:cooling-fan
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=7.1
    h: dccb778213f0
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=7.1
    h: 5f864ecd896b
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h164
    h: 43fdc21af7d8
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=69.r8
    h: 433c7c29e91e
  - src: src:eq-equip-inverters-delta-m36u-m42u-20190702-m42u-leaflet-old-wb
    loc: tbl=2.r44
    h: 9e729a9cbfd7
  review: drafted
- claim_id: c4
  rel: related_to
  target: comp:heat-sink
  note: In the Sunny Central design, the IGBTs are cooled indirectly through cooling fins that reach into
    the external air channel.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: related_to
  target: fm:fan-failure
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=7.1
    h: dccb778213f0
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=7.1
    h: 5f864ecd896b
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h152
    h: b00a0e7d3b15
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h214
    h: b00a0e7d3b15
  review: drafted
- claim_id: c6
  rel: related_to
  target: fm:inverter-overheating
  note: Incorrect installation that does not leave cooling clearances can cause the inverter to overheat.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: mit:installation-clearance
  note: Leave gaps at both sides and at the top so the inverter can cool properly.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  review: drafted
- claim_id: c8
  rel: related_to
  target: mit:direct-sun-avoidance
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=52.r5
    h: 46c42be6ee70
  review: drafted
- claim_id: c9
  rel: related_to
  target: mit:fan-replacement
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=7.1
    h: dccb778213f0
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=7.1
    h: 5f864ecd896b
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h164
    h: 43fdc21af7d8
  review: drafted
- claim_id: c10
  rel: related_to
  target: mit:clear-ventilation-blockage
  note: If internal overtemperature derating occurs while ambient temperature is not critical, the cooling
    filters may need cleaning.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h164
    h: 43fdc21af7d8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: related_to
  target: meas:inverter-temperature-high
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h164
    h: 43fdc21af7d8
  review: drafted
- claim_id: c12
  rel: related_to
  target: meas:fan-abnormal-noise
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h164
    h: 43fdc21af7d8
  review: drafted
- claim_id: c13
  rel: related_to
  target: stressor:high-altitude
  note: Thinner air at high altitude cools less well, so derating starts earlier and is steeper.
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: drafted
- claim_id: c14
  rel: related_to
  target: stressor:high-temperature
  cite:
  - src: src:sma-video-derating-und-k-hlung-von-sunny-central-wechselrichtern-wbt-4-cooling-derating-909953620
    loc: sec=h1
    h: 29bb5fd6708c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Inverter cooling is the way an inverter gets rid of the heat its power electronics produce while it runs. Datasheets usually list it as one of two methods: natural convection with no fans, or forced air from fans that may be variable speed or temperature controlled. Microinverters and many string inverters use natural convection. Larger string, hybrid and central inverters often use fans that help the convection. Large central inverters can use a sealed internal air loop that passes its heat to a filtered external air stream through an air-to-air heat exchanger. The hottest parts, such as the sine filter choke, are cooled last. If cooling cannot keep up, for example because a fan has failed, a filter is clogged, ambient heat is high or the site is at high altitude, the inverter derates and limits its output to protect its semiconductors. High internal temperature or abnormal fan noise with clean, unblocked vents points to a fan that needs replacing. At installation, leave the required clearances at the sides and top and avoid direct sunlight, or the inverter may overheat.

<!-- review notes
- sentence 3: support check: partial - Natural convection and forced air rows exist, but passages do not state that microinverters and many string inverters use natural convection or that larger ones use fan-assisted convection.
- sentence 5: support check: partial - Fan failure, ambient heat, and altitude are supported, but clogged filter as a cause of derating is only implied as an indicator of cooling not working well.
- sentence 6: support check: partial - Passage says replacement of fans may be necessary in that case, not that it definitely points to a fan needing replacement; hedge is slightly weaker.
-->
