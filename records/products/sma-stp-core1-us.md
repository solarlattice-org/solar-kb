---
id: prod:sma-stp-core1-us
type: Product
name: Sunny Tripower CORE1-US
aliases:
- Sunny Tripower CORE 1
- STP CORE 1
- STPCORE 1
- CORE 1 US
- STP xx US 41
- STP xx US 411
- STP 33-US-41
- STP 50-US-41
- STP 62-US-41
- STP 50-US-40
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-stpxx-us-41-firmware-update
    loc: sec=front
    h: 7e55340905f3
  - src: src:kb-sma-stpxx-us-41-troubleshooting
    loc: sec=front
    h: 7e90ac311e57
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=5.r2
    h: a919dade9675
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=5.r2
    h: a919dade9675
  - src: src:sma-sma-stp-33-us-iom
    loc: tbl=5.r2
    h: a919dade9675
  review: drafted
- claim_id: c3
  rel: implements
  target: func:dc-arc-fault-protection
  scope:
    firmware_min: 03.12.21.R
  conditions: Enhanced AFCI event handling on STP 33-US-41, STP 50-US-41 and STP 62-US-41 from firmware
    03.12.21.R
  note: On the older STP 50-US-40 enhanced AFCI event handling is not available; AFCI there results only
    in permanent operation inhibition.
  cite:
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=3
    h: a3b3904be2d2
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: tbl=3.r1
    h: c79ffc6896df
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: sec=h1
    h: bf00f614be88
  review: drafted
  review_note: 'support check: partial - Passages show enhanced AFCI event handling from 03.12.21.R on
    the -41 models and not available on STP 50-US-40 (only AFCI with permanent inhibition), but don''t
    explicitly state the firmware ''min'' scope phrasing beyond the table; core is supported, though ''supports
    DC arc-fault protection'' is implied.'
- claim_id: c4
  rel: implements
  target: func:iv-curve-scan
  scope:
    firmware_min: 03.12.21.R
  conditions: STP 33/50/62-US-41 with firmware 03.12.21.R or later
  note: Listed as not available for the STP 50-US-40.
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: tbl=3
    h: e8e67811d3c1
  review: drafted
---
The Sunny Tripower CORE1-US is an SMA inverter family for the US market, covering the STP 33-US-41, STP 50-US-41 and STP 62-US-41 models plus the earlier STP 50-US-40. Replacement assemblies, such as the communication assembly, come as SMA spare-part sets, and some sets are shared with the Sunny Tripower CORE1.

<!-- review notes
- sentence 1: review: partial - The passages list STP 33/50/62-US-41 and STP 50-US-40 as Sunny Tripower CORE1-US, but they do not say it is for the US market or that STP 50-US-40 is the earlier model.
-->
