---
id: func:communication-loss-fallback
type: Function
name: Communication-loss fallback
aliases:
- fallback mode
- reversion
- heartbeat timeout
- setpoint timeout
- Fallback
- Fallback Behavior
- fallback plan
- system fallback
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: role:grid-guard-code-holder
  note: An SMA Grid Guard code is needed to change fallback settings on the Cluster Controller and the
    superordinate fallback on the Inverter Manager.
  cite:
  - src: src:sma-kb-sma-cluster-controller-operating-mode-fallback
    loc: sec=h1
    h: a8418fbbdccb
  - src: src:sma-doc-278879
    loc: sec=5.2.6
    h: 9f7e6e82c227
  review: drafted
- claim_id: c2
  rel: requires
  target: tool:sma-lcs-tool
  scope:
    products:
    - prod:sma-inverter-manager
  note: The superordinate system fallback between the SMA Inverter Manager and a higher-level controller
    can only be configured with the LCS-Tool.
  cite:
  - src: src:sma-doc-278879
    loc: sec=5.2.6
    h: 9f7e6e82c227
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: sec=6.6
    h: d97262135449
  review: drafted
- claim_id: c3
  rel: requires
  target: role:installer-access-level
  scope:
    products:
    - prod:sma-inverter-manager
  note: The Inverter Manager system fallback is set under the Installer user group.
  cite:
  - src: src:sma-doc-278879
    loc: sec=5.2.6
    h: 9f7e6e82c227
  review: drafted
- claim_id: c4
  rel: part_of
  target: func:export-limitation
  note: In FIMER inverters the fallback plan belongs to the export limitation control and is triggered
    when communication with the export meter is lost.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h31
    h: 07524ffc6b81
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  review: drafted
- claim_id: c5
  rel: requires
  target: tool:fimer-installer-app
  note: The FIMER export limitation fallback plan is enabled and configured in the Installer for solar
    inverters app.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h31
    h: 07524ffc6b81
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  attr: setting_range
  value:
    min: 20
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sunny-tripower-core2
  conditions: Waiting time before fallback takes effect when communication between SMA Data Manager and
    Sunny Tripower CORE2 fails; at least 20 s must be set
  cite:
  - src: src:sma-kb-zero-feed-in-power-with-sunny-tripower-stp110-60-core2
    loc: sec=h1
    h: 5a8fe0a4eb3f
  review: drafted
---
Communication-loss fallback puts inverters into a defined feed-in state when control communication fails or setpoints stop arriving. After an adjustable timeout, the inverter either keeps the last values it received or applies preset fallback values. The SMA Cluster Controller supports two fallback types, and each is configured separately. One covers a missing or invalid external setpoint. The other covers failure of Speedwire communication between the controller and the inverters. The Speedwire fallback cannot be configured on inverters with a Speedwire Webconnect Piggy-Back. It is designed for inverters with the Speedwire/Webconnect data module and for Sunny Boy Smart Energy. Inverters controlled by the SMA Inverter Manager switch to their fallback state when communication is interrupted, and they report status events 2055 and 2056. Fallback is set up through the grid code file or the LCS-Tool. The system-level fallback toward a SCADA or power plant controller needs the LCS-Tool and a Grid Guard code. On the Sunny Tripower CORE2 you set a waiting time of at least 20 seconds and a fallback value. A fallback value of 0 percent still lets about 1 to 2 kW feed in, and fallback cannot be set to disconnect from the grid. SMA states that the activation and configuration of fallback must be agreed with the grid operator.
