---
id: func:residual-current-monitoring
type: Function
name: Residual current monitoring
aliases:
- RCMU
- residual current monitoring unit
- leakage current monitoring
- residual current monitoring device
category: Protection
function_kind: protection
claims:
- claim_id: c1
  attr: trip_threshold
  value:
    nominal: 30
    unit: unit:MilliA
  conditions: Residual current jump at which a transformerless inverter must disconnect from the grid
    at the latest, per IEC 62109-2 as described by SMA
  cite:
  - src: src:sma-doc-237302
    loc: sec=h11
    h: 63b3fad3802c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'review: the compiler-flagged conflict (func:residual-current-monitoring#c2) is a scenario
    difference, resolved at review'
- claim_id: c2
  attr: trip_threshold
  value:
    min: 100
    unit: unit:MilliA
  conditions: Trip rating of an additional external residual-current device, where one is required, for
    SMA Sunny Island / Sunny Boy Storage / Sunny Tripower Smart Energy backup systems
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: sec=h25
    h: 08cf93da565d
  review: disputed
  review_note: 'support check: partial - The passage gives 100 mA or higher for an external RCD, but it
    doesn''t name the specific SMA product families (Sunny Island, Sunny Boy Storage, Sunny Tripower Smart
    Energy) or backup systems.'
  conflicts_with:
  - func:residual-current-monitoring#c1
- claim_id: c3
  attr: trip_threshold
  value:
    min: 100
    unit: unit:MilliA
  scope:
    products:
    - prod:fronius-symo
  conditions: Release current of an additional type B residual current circuit breaker, where required
    by the installation or utility, for Fronius Symo inverters
  cite:
  - src: src:fronius-fronius-symo-advanced-ul-operating-instructions-42-0410-0192
    loc: sec=h198
    h: 00edd59f65fe
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h196
    h: 00edd59f65fe
  review: drafted
---
Residual current monitoring measures the differential current, which is the leakage current plus any residual current, during feed-in, and works out the residual current from that measurement. Fronius describes the unit as watching residual currents between the PV modules and the grid connection, and taking the inverter off the grid when it sees an improper residual current. Under IEC 62109-2, a transformerless inverter must disconnect no later than a 30 mA jump in residual current. SMA states that AC residual currents above 30 mA can be life-threatening. When leakage current is high, the residual current cannot always be calculated accurately, and the errors can shut the inverter down when it should not. If the utility or the installation calls for an extra residual-current device, Fronius specifies a type B breaker with a release current of at least 100 mA. SMA calls for a device that trips at 100 mA or higher. Grid operators may require a residual-current device in their technical connection requirements, but often they only ask for a standard-compliant installation.
