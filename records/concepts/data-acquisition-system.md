---
id: concept:data-acquisition-system
type: Concept
name: Data acquisition system
aliases:
- DAS
- data logger
- DAQ
- datalogger
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:monitoring-gateway
  note: In the cited plant, the data acquisition system consists of a datalogger that acquires inverter
    data.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h95
    h: 7ea1f62e1e4d
  - src: src:iea-pvps-t13-19-2021
    loc: sec=4.5
    h: 0f5d2d05af82
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:inverter
  note: The inverter is often the first point of measurement; its data is collected by the data logger.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h95
    h: 7ea1f62e1e4d
  - src: src:iea-pvps-t13-19-2021
    loc: sec=4.5
    h: 0f5d2d05af82
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:scada
  note: SCADA stands for supervisory control and data acquisition.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=4.r11
    h: 108f3e650028
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: tbl=7.r14
    h: 1784ec82ac3e
  - src: src:eq-equip-bess-tesla-powerpack-system-controls-and-communication-manual
    loc: tbl=3.r5
    h: 6caf03738bcf
  review: drafted
- claim_id: c4
  rel: related_to
  target: method:performance-monitoring
  note: Data acquisition supplies performance data for commercial PV monitoring and fault detection.
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-locus-lgate-360
    loc: sec=h1
    h: 29b5007e9ef7
  - src: src:eq-equip-das-alsoenergy-locus-locus-energy-commercial-pv-monitoring
    loc: sec=h13
    h: 29b5007e9ef7
  - src: src:iea-pvps-t13-19-2021
    loc: sec=4.5
    h: 0f5d2d05af82
  review: drafted
  review_note: 'support check: partial - The titles mention performance data acquisition for commercial
    PV, and u27 mentions the data chain for fault detection. None of the passages names performance monitoring,
    and they do not say that DAS data supplies it.'
---
A data acquisition system (DAS) gathers performance data from PV plant equipment, mainly inverters, and usually does this through a data logger. In the usual data chain, the inverter measures DC and AC values and keeps them in internal registers. A data logger then sends them to a database, a vendor portal or a third-party monitoring site. The logger can pass values through unchanged, average a set of samples, or keep one sampled value per interval. So the data in the database may not match what the inverter sent. In one documented plant, the datalogger sampled six inverters every 2 seconds and stored only 10-minute averages. Typical DAS maintenance includes checking power supply voltages and comparing current transducer and sensor readings against calibrated instruments, which shows up sensor calibration errors. DAS plans are often missing or lack detail. If the DAS uses the building IT network, network upgrades or routine IT maintenance can cause connectivity problems. Large central inverters provide a dedicated connection for a third-party DAS. The related term SCADA stands for supervisory control and data acquisition.

<!-- review notes
- sentence 7: support check: partial - The SCADA expansion is supported. The titles of u5 and u6 only name a third-party DAS connection, so they do not say that large central inverters provide a dedicated one.
-->
