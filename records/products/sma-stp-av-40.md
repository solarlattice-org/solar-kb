---
id: prod:sma-stp-av-40
type: Product
name: Sunny Tripower 3.0-10.0-3AV-40
aliases:
- STP 3AV-40
- STPx.x-3AV-40
- STPxx-3AV-40
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-general-commissioning-information-for-sma-sunny-boy-3-0-3-6-4-0-5-0-6-0-sma-sunny-t
    loc: sec=h1
    h: 37cbf913dee8
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Listed under the device category PV inverter.
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3
    h: 63e5d75ca23e
  review: drafted
- claim_id: c3
  rel: lacks
  target: func:system-manager
  note: A device compatibility table marks System Manager Functionality as not available for all STPx.x-3AV-40
    models (firmware 3.10.xx.R listed).
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3.r5
    h: 396e181ff51e
  - src: src:sma-doc-275857
    loc: tbl=3.r4
    h: 1e9b1dad3610
  review: drafted
---
The Sunny Tripower 3.0-10.0-3AV-40 is an SMA family of PV string inverters. The 3.0 to 6.0 models and the 8.0 and 10.0 models have separate manuals. An SMA compatibility table marks these inverters as not offering the system manager function, and it lists firmware 3.10.xx.R for them. The inverter's user interface is not based on ennexOS. A separate SMA compatibility list gives inverter firmware 02.11.09.R as the starting version for this family. Connect and apply both AC and DC before commissioning. With AC alone, you may not be able to log in to the web interface or set parameters.
