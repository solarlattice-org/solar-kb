---
id: prod:enphase-iq-system-controller
type: Product
name: Enphase IQ System Controller
aliases:
- Enpower
- IQ System Controller
- IQ System Controller 2
- IQ System Controller 3
- IQ System Controller 3G
- IQ System Controller 3 INT
- EP200G101-M240US00
- EP200G101-M240US01
- EP200G-SC2-RSD-KIT
category: Protection and BOS
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:transfer-switch-controller
  note: Provides microgrid interconnect device (MID) functionality.
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r2
    h: 34320f0a03a6
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r2
    h: a056ccd7f647
  review: drafted
- claim_id: c2
  rel: implements
  target: func:backup-transfer
  note: Detects grid failure and moves the home from grid power to backup power automatically.
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r2
    h: 34320f0a03a6
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r2
    h: a056ccd7f647
  review: drafted
- claim_id: c3
  rel: implements
  target: func:generator-support
  note: Generator input circuit on IQ System Controller 2; on the 3G the third DER port supports generator
    integration.
  cite:
  - src: src:enphase-enphase-troubleshooting-energy-systems-with-iq-battery-5p
    loc: sec=h9
    h: a1f63938aa25
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:enphase-iq8
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:enphase-iq-gateway
  note: Gateway communicates with the controller; a wireless communications kit at 2.4 GHz enables direct
    communication.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: arch:split-phase-120-240v
  scope:
    applications:
    - backup
  note: A neutral-forming transformer enables 120/240 V operation in backup mode.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c7
  rel: requires
  target: func:rapid-shutdown
  scope:
    products:
    - prod:enphase-iq8
  conditions: Systems with IQ8 Microinverters and an IQ System Controller 2 must use a Rapid Shutdown
    switch.
  cite:
  - src: src:enphase-enphase-critical-updates-and-best-practices-installing-and-commissioning
    loc: sec=h15
    h: 5c4ee2e6de95
  review: drafted
---
The Enphase IQ System Controller, previously called Enpower, is a smart switch that ties the home to grid power, IQ Battery storage and solar PV. It works as a microgrid interconnect device: when the grid fails it detects the outage and moves the home to backup power automatically. The family includes the original unit, IQ System Controller 2, 3, 3G and 3M, and each version has its own SKU. On the IQ System Controller 3 the third DER port takes extra PV and IQ Battery 5P. On the 3G that port takes a generator instead. IQ System Controller 2 has PV, storage and generator input circuits, plus a neutral-forming transformer for 120/240 V operation in backup. You can install several controllers on one site, but only in parallel, never in series, and each one needs its own Enlighten site ID. Known troubleshooting topics include the controller not reporting, rapid shutdown issues and power cycling.
