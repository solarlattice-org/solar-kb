---
id: prod:sma-cluster-controller
type: Product
name: SMA Cluster Controller
aliases:
- Cluster Controller
- CLCON-10
- CLCON-S-10
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-240154
    loc: sec=h2
    h: e3fd64b87ba7
  - src: src:sma-doc-240154
    loc: sec=2.1
    h: 0680c40a8035
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  note: SMA describes both the Cluster Controller and the Data Manager as data loggers.
  cite:
  - src: src:sma-kb-can-i-connect-the-data-manager-to-an-sma-cluster-controller
    loc: sec=h1
    h: 25f63c22afc6
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:speedwire
  note: Sets up the Speedwire network and sends setpoints to inverters over Speedwire.
  cite:
  - src: src:sma-kb-sma-cluster-controller-operating-mode-fallback
    loc: sec=h1
    h: a8418fbbdccb
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:webconnect
  note: Monitors and controls SMA devices that have Speedwire/Webconnect interfaces.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  - src: src:sma-doc-240154
    loc: sec=2.1
    h: 0680c40a8035
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:ftp-push
  note: Can send system data to an FTP server.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  review: drafted
- claim_id: c6
  rel: implements
  target: func:communication-loss-fallback
  note: 'Two fallback types, configured separately: one for a missing or invalid external setpoint, one
    for a Speedwire communication failure between the controller and the inverters.'
  cite:
  - src: src:sma-kb-sma-cluster-controller-operating-mode-fallback
    loc: sec=h1
    h: a8418fbbdccb
  review: drafted
- claim_id: c7
  rel: implements
  target: func:limit-active-power
  note: Applies and reports back active power limitation setpoints from grid operators and from direct
    marketing.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  review: drafted
- claim_id: c8
  rel: implements
  target: func:remote-firmware-update
  note: Updates the controller itself and the inverters. Automatic controller updates come from the SMA
    Update Portal, are checked daily and are installed overnight.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  - src: src:sma-doc-240154
    loc: sec=14.1.1
    h: 9e25a762bc47
  review: drafted
- claim_id: c9
  rel: implements
  target: func:monitor-key-data
  note: Reads out, provides and manages PV system data and reports the system's current total active power.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  review: drafted
- claim_id: c10
  rel: requires
  target: role:grid-guard-code-holder
  conditions: To change fallback settings
  note: Settings must be agreed with the grid operator.
  cite:
  - src: src:sma-kb-sma-cluster-controller-operating-mode-fallback
    loc: sec=h1
    h: a8418fbbdccb
  review: drafted
- claim_id: c11
  rel: incompatible_with
  target: prod:sma-data-manager-m
  conditions: Parallel operation in the same system
  note: SMA says running both data loggers in parallel is not advisable.
  cite:
  - src: src:sma-kb-can-i-connect-the-data-manager-to-an-sma-cluster-controller
    loc: sec=h1
    h: 25f63c22afc6
  review: drafted
  review_note: 'support check: partial - SMA says parallel operation is not advisable, but the passage
    names ''Data Manager'' generally, not Data Manager M, and ''incompatible'' is stronger than ''not
    advisable''.'
- claim_id: c12
  rel: compatible_with
  target: prod:sma-com-gateway
  note: Picks up RS485 inverters through the Com Gateway. Connect the Com Gateway to the controller before
    first commissioning, or wrong time stamps can cause Sunny Portal to discard data.
  cite:
  - src: src:sma-kb-missing-inverters-in-sunny-portal-for-sma-cluster-controller-systems-in-connection
    loc: sec=h1
    h: 63eaea6ce649
  - src: src:sma-kb-sma-com-gateway-manual
    loc: sec=h1
    h: '711e28039588'
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:en-55022
  note: ITE class A device intended for industrial use.
  cite:
  - src: src:sma-doc-240154
    loc: sec=2.1
    h: 0680c40a8035
  review: drafted
  review_note: 'support check: partial - Passage says ITE class A device as per EN 55022 for industrial
    use, but not that it is certified.'
- claim_id: c14
  attr: max_count
  value:
    max: 25
    unit: unit:NUM
  conditions: SMA devices with Speedwire/Webconnect interface monitored; the source gives this figure
    for model CLCON-S-10
  note: The same source also gives 75 for the model it prints as CLCON-S-10, so the model assignment is
    ambiguous.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  - src: src:sma-doc-240154
    loc: sec=2.1
    h: 0680c40a8035
  review: drafted
- claim_id: c15
  attr: max_count
  value:
    max: 75
    unit: unit:NUM
  conditions: SMA devices with Speedwire/Webconnect interface monitored; the source also prints this figure
    for model CLCON-S-10
  note: The source prints both 25 and 75 for CLCON-S-10, so which model gets which figure is ambiguous.
  cite:
  - src: src:sma-doc-240154
    loc: sec=3.1.1
    h: 55ee8325e3f5
  - src: src:sma-doc-240154
    loc: sec=2.1
    h: 0680c40a8035
  review: drafted
---
The SMA Cluster Controller is an indoor-only data logger for monitoring and controlling SMA devices with Speedwire/Webconnect interfaces, in both decentralized PV systems and large PV plants. It builds the Speedwire network, configures device parameters and applies grid operator setpoints for active power limitation and reactive power. It also sends e-mail alarms and pushes data to an FTP server or Sunny Portal. It has fallback modes for a missing or invalid setpoint and for loss of Speedwire communication with the inverters. Changing these settings needs an SMA Grid Guard code and agreement with the grid operator. It can update its own firmware and the inverters' firmware. Automatic updates are downloaded from the SMA Update Portal and installed overnight, and existing settings are kept. SMA advises against running it in parallel with a Data Manager. In plants with Core1 inverters, set up the inverters to match the controller: same firmware and installer password, Webconnect off and automatic time sync off. Known issues: an SD card that is not seated properly causes lost or unapplied settings, and the clock time is lost after more than 14 days out of operation. If the controller shows the wrong number of inverters, check the inverters and network cabling. The inverter wired directly to the controller must be on port X9 or X10. It is the ITE class A device under EN 55022, built for industrial use.
