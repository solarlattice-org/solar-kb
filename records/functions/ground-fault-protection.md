---
id: func:ground-fault-protection
type: Function
name: DC ground-fault protection
aliases:
- GFDI
- ground fault detector interrupter
- ground fault detection
- GFP
- ground fault detection and interruption
- GFCI
category: Protection
function_kind: protection
claims:
- claim_id: c1
  rel: requires
  target: func:residual-current-monitoring
  scope:
    products:
    - prod:chint-sch-200-250k-t
    - prod:chint-sch-350ktl
    - prod:yaskawa-solectria-pvi-3800-7600tl
  note: CPS and Solectria string inverters detect DC ground faults using residual current detection, as
    the method required by UL 1741.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: sec=2.8
    h: 7aa93daa11d1
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: sec=2.8
    h: 32d20ea7cd91
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h16
    h: fff667eb17c9
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=2.7
    h: 56a9855b8e71
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h28
    h: 66ae2acc3517
  review: drafted
  review_note: 'support check: partial - Residual current detection is stated for CPS/Solectria inverters,
    but the passages don''t name the CHINT products explicitly, and the ''requires'' wording is that it''s
    part of the UL 1741 method.'
- claim_id: c2
  attr: trip_threshold
  value:
    nominal: 240
    unit: unit:MilliA
  scope:
    products:
    - prod:generac-pv-link
  conditions: Generac PV Link internal GFDI, PV DC ground current; tolerance plus or minus 40 mA
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h32
    h: 2ceb08968699
  review: drafted
- claim_id: c3
  attr: trip_threshold
  value:
    nominal: 4
    unit: unit:A
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  conditions: 'XGI 1500-1MW: current sensor detection makes the DSP trip the breaker; only works when
    the DC input is grounded'
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h43
    h: 96f9b8f91282
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: trip_threshold
  value:
    nominal: 5
    unit: unit:A
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  conditions: 'XGI 1500-1MW: second protection level, where the ground fault circuit breaker trips on
    its own'
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h43
    h: 96f9b8f91282
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: trip_threshold
  value:
    nominal: 1
    unit: unit:A
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-dcg
  conditions: 'XGI 1500-DCG: current sensor detection makes the DSP trip the breaker'
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h41
    h: 55cc38641bd1
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: fig=50
    h: 15be62cdf5fc
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: trip_threshold
  value:
    nominal: 5
    unit: unit:A
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-dcg
  conditions: 'XGI 1500-DCG: second protection level, where the ground fault circuit breaker trips on
    its own'
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h41
    h: 55cc38641bd1
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: fig=50
    h: 15be62cdf5fc
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: trip_threshold
  value:
    nominal: 300
    unit: unit:MilliA
  scope:
    products:
    - prod:yaskawa-solectria-pvi-3800-7600tl
  conditions: Solectria PVI 3800-7600TL GFDI trip limit
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h16
    h: fff667eb17c9
  review: drafted
- claim_id: c8
  attr: trip_threshold
  value:
    max: 1000
    unit: unit:MilliA
  scope:
    products:
    - prod:enphase-m215-m250
  conditions: Original Enphase M215-60-2LL-S22 microinverter, ground fault protection parameter in its
    datasheet table
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=25.r7
    h: 54312bd85a3d
  review: drafted
  review_note: 'support check: partial - Passage gives Max 1000 mA for ground fault protection, but does
    not state it is a trip threshold or DC-specific; ''up to'' fits max.'
---
DC ground-fault protection detects current leaking from the PV DC conductors to ground. When it finds a fault, it alarms and stops the inverter or disconnects it from the grid. NEC 690.41(B)(1) requires the device to detect ground faults in PV DC circuit conductors, including functional grounded conductors, and to be listed for PV ground-fault protection. UL 1741 also requires a DC ground fault detection method. CPS and Solectria string inverters use residual current detection to find leakage current. The Solectria PVI 3800-7600TL trips at 300 mA. The Solectria XGI 1500 central inverters have a GFDI circuit with two levels. The DSP trips the breaker at 4.0 A on the 1MW model or 1.0 A on the DCG model, and the ground fault circuit breaker trips by itself at 5 A. On the XGI 1500-1MW, the GFDI only works when the DC input is grounded. The Generac PV Link has an internal GFDI that trips at 240 mA, plus or minus 40 mA. Ground faults are shown on the PWRcell Inverter control panel. The Fronius Galvo uses its GFDI on negatively grounded arrays and uses insulation monitoring on ungrounded arrays. Power Electronics HEM units combine GFDI with an insulation monitoring device. Enphase M-Series and IQ7-based M215 and M250 microinverters have ground fault protection built in. Their DC circuit is isolated from ground, so they need no grounding electrode conductor. The original M215-60-2LL-S22 is the exception and still needs a GEC.

<!-- review notes
- sentence 7: support check: partial - Galvo GFDI/insulation monitoring behavior is described generically, and the FS-series datasheet lines show GFDI with insulation monitoring, but the passages don't name Fronius Galvo or Power Electronics HEM.
-->
