---
id: concept:remote-monitoring
type: Concept
name: Remote monitoring
aliases:
- fleet monitoring
- remote site tracking
category: Monitoring
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: method:performance-monitoring
  note: Remote monitoring lets the operator track system performance and spot underperforming modules
    or strings.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=7.5
    h: e8990b4d5c5b
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:expected-energy-model
  note: On-site weather stations let the system compare output predicted from recent weather with actual
    output.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=7.5
    h: e8990b4d5c5b
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:scada
  note: Cloud-based remote monitoring serves customers who have no SCADA control room of their own.
  cite:
  - src: src:eq-equip-bess-tesla-tesla-powerhub-manual-user
    loc: sec=4.1
    h: a88c8cc913a7
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:tesla-powerhub
  note: Powerhub Plus offers remote monitoring of one site or a fleet through a cloud interface with List,
    Site and Graph views.
  cite:
  - src: src:eq-equip-bess-tesla-tesla-powerhub-manual-user
    loc: sec=4.1
    h: a88c8cc913a7
  review: drafted
- claim_id: c5
  rel: related_to
  target: prod:chint-flexom-gateway
  note: Optional monitoring service that gives the manufacturer remote read/write data access to the inverters.
  cite:
  - src: src:chint-cps-flexom-gateway-user-manual-2025-12-02
    loc: sec=h10
    h: b2396ffb8ea2
  review: drafted
- claim_id: c6
  rel: related_to
  target: func:remote-firmware-update
  note: Monitoring platforms and web-based inverter monitoring can support remote upgrades.
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-locus-energy-commercial-pv-monitoring
    loc: tbl=7.r7
    h: 86cd8d90dc65
  - src: src:eq-equip-inverters-solectria-xgi-1500-fl-xgi1500-01-05-03-2021
    loc: tbl=1.r30
    h: 3ba43de5d699
  review: drafted
  review_note: 'support check: partial - Passages show remote upgrades and remote firmware updates in
    web-based monitoring, but the link to monitoring platforms is only loosely given in table fragments.'
---
Remote monitoring means watching a PV or storage system's performance from off site, usually through a data logger or gateway that sends data to an online platform. Most PV systems come with remote monitoring, and a small weather station is often installed so that output predicted from recent weather can be compared with actual output. If actual output falls below the prediction, that points to a problem. On larger systems the monitoring becomes more complex, because underperforming modules or strings need to be found quickly. Cloud-based interfaces let owners who have no on-site staff and no SCADA control room view real-time and historical data for one site or a whole fleet. Monitoring platforms also support remote troubleshooting of inverters and power optimizers through site lists, alert emails and fleet reports, before anyone is sent to test on site. Some monitoring links give read/write access, so the manufacturer can service the equipment and push firmware updates remotely. Remote access is a security risk, so it should be monitored automatically, encrypted, and routed through managed access points.

<!-- review notes
- sentence 1: support check: partial - Off-site monitoring and cloud platform are supported, but the data logger/gateway mechanism and storage systems are not stated.
- sentence 5: support check: partial - Passages list site list, alert emails, fleet report and monitoring platform troubleshooting, but only as headings, with no explicit statement about remote troubleshooting before on-site testing.
- sentence 6: support check: partial - Read/write access for service is stated for CPS, and remote firmware updates appear in tables, but pushing updates by the manufacturer over such links is not explicit.
- sentence 1: review: partial - Off-site performance monitoring through a cloud platform is supported, but the data logger or gateway mechanism and the explicit mention of storage systems are not in the passages.
-->
