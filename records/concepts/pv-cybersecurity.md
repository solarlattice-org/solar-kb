---
id: concept:pv-cybersecurity
type: Concept
name: Cybersecurity of PV systems
aliases:
- cybersecurity
- defense-in-depth
- port forwarding risk
- cyber security
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:monitoring-gateway
  note: As a minimum, data loggers should not be reachable directly from the internet, or should at least
    sit behind a firewall.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=9.9
    h: 41a24fc00085
  review: drafted
- claim_id: c2
  rel: related_to
  target: proto:modbus
  note: SMA warns against port forwarding on the Modbus ports in use. An enabled Modbus interface can
    let unauthorized users manipulate data or devices.
  cite:
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=h26
    h: 1a15355fd878
  - src: src:eq-equip-inverters-sma-data-manager-m-manual-edmm-10-be-en-17
    loc: sec=h37
    h: 1a15355fd878
  - src: src:sma-doc-259761
    loc: sec=h529
    h: 39f05a575c95
  - src: src:eq-equip-inverters-sma-data-manager-m-edmm-10-be-en-23
    loc: sec=h32
    h: 4c56313b07a0
  - src: src:eq-equip-inverters-sma-data-manager-m-edmm-10-is-xx-16
    loc: sec=h30
    h: 4c56313b07a0
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:remote-maintenance
  note: Limit remote access to the use cases that need it, and provide it only through a VPN.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.9
    h: 89e38f107a98
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=h26
    h: 1a15355fd878
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=9.9
    h: 41a24fc00085
  - src: src:sma-doc-259761
    loc: sec=h529
    h: 39f05a575c95
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: related_to
  target: mit:firmware-update
  note: Vulnerability management includes keeping device firmware and software up to date.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.9
    h: 89e38f107a98
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=9.9
    h: 41a24fc00085
  review: drafted
- claim_id: c5
  rel: related_to
  target: role:read-only-user
  note: Separate the roles where possible, for example read-only users and administration access.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.9
    h: 89e38f107a98
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=9.9
    h: 41a24fc00085
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: related_to
  target: role:administrator
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=9.9
    h: 89e38f107a98
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=9.9
    h: 41a24fc00085
  review: drafted
- claim_id: c7
  rel: related_to
  target: symptom:unauthorized-access-attempt
  note: Once connected to the internet, unauthorized users may access and manipulate PV system data.
  cite:
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=h26
    h: 1a15355fd878
  - src: src:eq-equip-inverters-sma-data-manager-m-manual-edmm-10-be-en-17
    loc: sec=h37
    h: 1a15355fd878
  - src: src:eq-equip-inverters-sma-data-manager-m-edmm-10-be-en-23
    loc: sec=h32
    h: 4c56313b07a0
  review: drafted
- claim_id: c8
  rel: related_to
  target: comp:battery-storage
  note: Industrial battery systems are critical to grid reliability. Balance-of-plant cyber assets that
    are misconfigured can introduce vulnerabilities.
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: sec=5
    h: ef04d52b8f0a
  review: drafted
---
Cybersecurity covers the technologies, processes and controls that protect systems, networks and data from cyber-attacks. PV plants carry real cyber risk because their inverters, power plant controllers and monitoring systems are connected to the internet so operators can watch them and send remote commands. Once PV equipment is online, unauthorized users may be able to access and manipulate system data or devices. This applies especially when a Modbus interface is enabled. Basic measures are a firewall, closing network ports that are not needed, no port forwarding, remote access only through a VPN, and network segmentation. Guidelines also call for changing factory default passwords, using a different password for each plant, separating read-only and administrator roles, keeping firmware current, and avoiding wireless access unless it is needed. Best practice is to begin with a risk assessment and run a cybersecurity management system on a plan-do-check-act cycle. Countermeasures are mapped onto zones and conduits of the system architecture, an approach in line with the defense-in-depth principle. Data loggers should not be directly reachable from the internet, and control commands should go to the control device over a secure VPN. Two-factor authentication adds further protection. Battery storage owners have similar duties: balance-of-plant equipment that is misconfigured on the network can become a source of vulnerabilities.

<!-- review notes
- sentence 6: support check: partial - Risk assessment, PDCA CSMS, and zones and conduits are stated, but the defense-in-depth link is not stated in the passages (u25 is only a control name with no explanation).
- sentence 8: support check: partial - Misconfigured balance-of-plant assets as a vulnerability source is stated, but 'owners' having 'similar duties' is a loose paraphrase (passage says all parties involved must take steps).
-->
