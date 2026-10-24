---
id: tool:sel-acselerator-quickset
type: Tool
name: SEL AcSELerator QuickSet
aliases:
- QuickSet
- AcSELerator QuickSet
- SEL-5030
- ACSELERATOR QuickSet SEL-5030 Software
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sel
  note: Listed among SEL trademarks; described as installed SEL software.
  cite:
  - src: src:sel-acselerator-bay-screen-builder-instruction-manual
    loc: tbl=9
    h: 724f5dd22b7d
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: sec=h352
    h: 3abc1c625534
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: uses_protocol
  target: proto:ethernet
  note: Ethernet is one of the links used to send and receive device settings, alongside modem and serial.
  cite:
  - src: src:sel-acselerator-quickset-instruction-manual
    loc: sec=h38
    h: 674a1a110578
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
AcSELerator QuickSet (SEL-5030) is SEL software for communicating with any device SEL supports. It sends and receives device settings over Ethernet, modem or serial links. It can also hold a continuous connection open for human-machine interface (HMI) use. Each device has its own settings driver, for example the drivers for the SEL-735, SEL-710 and SEL-2730M. SEL Compass is a companion program that finds, downloads and installs updates for QuickSet, its drivers and SEL product literature. For a clean reinstall, first remove SEL Compass, the SEL ACSELERATOR Database, QuickSet and the ACSELERATOR Database ODBC Driver. Then download QuickSet again from the SEL website, which only offers the download when you are logged in. Release notes say FTP sessions can run in passive or active mode, and that a fix lets older settings versions be converted to newer ones. QuickSet can also open .evzip event files through its View Event Files with SYNCHROWAVE Event menu option.

<!-- review notes
- sentence 3: support check: partial - Driver titles exist for the three devices, but the passages don't state that each device has its own driver.
- sentence 5: support check: partial - Removal list and login requirement are supported, but the passages give no ordering requirement of 'clean reinstall' beyond Step 1, and 'only offers download when logged in' is roughly stated; the 'clean reinstall' framing is mild inference.
- sentence 6: support check: partial - Passive/Active mode is stated, but release notes say 'allow use of Passive or Active', fine; the conversion fix is stated as addressing an issue; minor wording differences only, though 'can run in' is a slight paraphrase.
-->
