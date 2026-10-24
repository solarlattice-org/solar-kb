---
id: prod:sma-speedwire-webconnect-module
type: Product
name: SMA Speedwire/Webconnect data module
aliases:
- SWDM
- Speedwire-Webconnect Piggyback
- SWPB-US-10
- SWDM-10
- SMA Webconnect Data Module
- Speedwire/Webconnect Piggy-Back
- SMA Speedwire data module
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:communication-module
  note: Retrofit data module for SMA inverters that lack an integrated Speedwire interface.
  cite:
  - src: src:sma-doc-278405
    loc: sec=6.1
    h: 16eceeabe346
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-279088
    loc: tbl=6.r5
    h: e889a676f653
  - src: src:sma-doc-279088
    loc: tbl=6
    h: a21a5c491599
  review: drafted
  review_note: 'support check: partial - The passages give the module''s designation as ''SMA Speedwire/Webconnect
    Data Module'', so the SMA name is there. They never say SMA makes it.'
- claim_id: c3
  rel: uses_protocol
  target: proto:speedwire
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  - src: src:sma-kb-swpb-us-10-firmware-update-via-sunny-explorer-for-the-piggyback-in-the-sb-us-12-tl1
    loc: sec=h1
    h: 431ceed535b1
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:webconnect
  note: Webconnect sends data straight from the inverters of a small system to Sunny Portal without any
    extra communication device.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-doc-262660
    loc: sec=h20
    h: a90c0c39a652
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:ethernet
  note: Ethernet-based, 10/100 Mbit; RJ45 connection; CAT5E/CAT6 cable with 568B wire order.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-stp-tl-us
  note: Fitted as standard with an RJ45 connection.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=34.r7
    h: 7ca6211d826b
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=106.r2
    h: 077b71411cb3
  review: drafted
  review_note: 'support check: partial - u3 and u19 show the Webconnect data module with an RJ45 connection
    as standard. They do not say which inverter is meant, and u8 says only ''the inverter''.'
- claim_id: c7
  rel: compatible_with
  target: prod:sma-sb-tl-us-22
  note: SWDM installed in SB-US-TL22; the open port of the SWDM can take one inverter fitted with a piggyback
    card as a daisy chain.
  cite:
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:sma-cluster-controller
  conditions: Large-scale plants send data to Sunny Portal through the Cluster Controller; the output
    of a piggyback star network's Ethernet switch can feed a Cluster Controller.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:sma-sb-us-12
  scope:
    regions:
    - region:us
    firmware_min: BFR/SRR=2.00
  conditions: SWPB-US-10 piggyback in SB5000US-12 through SB8000US-12; minimum firmware is printed on
    the EPROM chip.
  cite:
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
  review_note: 'support check: partial - u23 gives a minimum of BFR/SRR=2.00 for the SB5000US-12 to SB8000US-12
    series with the SWPB-US-10 piggyback. The passages do not say this applies to the SWDM module itself,
    and they do not state a US region scope.'
- claim_id: c10
  rel: incompatible_with
  target: prod:sma-sb-us-12
  scope:
    firmware_max: BFR/SRR=1.12
  conditions: SB5000US-12 through SB8000US-12 with firmware below the required BFR/SRR=2.00; the source's
    example is BFR/SRR=1.12, which will not work.
  cite:
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:sma-sb-5000us-8000us
  scope:
    regions:
    - region:us
    firmware_min: BFR/SRR=1.12
  conditions: SWPB-US-10 piggyback in SB5000US through SB8000US.
  cite:
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  review: drafted
  review_note: 'support check: partial - u23 says the SB5000US to SB8000US series needs a minimum BFR/SRR
    of 1.12 for the SWPB-US-10 piggyback. The passages do not mention a US region scope or the SWDM module
    itself.; review: partial - The passage confirms that SB5000US through SB8000US work with the SWPB-US-10
    piggyback only with firmware BFR/SRR of at least 1.12; that firmware condition is left out, and the
    passage treats the piggyback as separate from the Speedwire-Webconnect Data Module (SWDM)…'
- claim_id: c12
  rel: requires
  target: tool:sma-sunny-explorer
  conditions: The first time an SWPB-US-10 piggyback is installed, its default firmware must be updated
    over Speedwire with Sunny Explorer before it can communicate or report to Sunny Portal.
  cite:
  - src: src:sma-kb-swpb-us-10-firmware-update-via-sunny-explorer-for-the-piggyback-in-the-sb-us-12-tl1
    loc: sec=h1
    h: 431ceed535b1
  review: drafted
- claim_id: c13
  rel: requires
  target: role:qualified-person
  conditions: Installing, wiring and updating the piggyback means opening the lower lid of the de-energized
    inverter; only electrically qualified persons may do this.
  cite:
  - src: src:sma-kb-swpb-us-10-piggyback-troubleshooting-for-installation-and-wiring-issues
    loc: sec=h1
    h: 609fc7eda3ba
  - src: src:sma-kb-swpb-us-10-firmware-update-via-sunny-explorer-for-the-piggyback-in-the-sb-us-12-tl1
    loc: sec=h1
    h: 431ceed535b1
  review: drafted
- claim_id: c14
  attr: max_count
  value:
    max: 4
    unit: unit:NUM
  conditions: Inverters per Sunny Portal system using the Webconnect function
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h60
    h: 4f16663e94bf
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h665
    h: 9c02105ab357
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h335
    h: 59f3729d0203
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
The SMA Speedwire/Webconnect data module is an SMA communication module. It adds an Ethernet-based Speedwire interface to SMA inverters that do not have one built in. Speedwire/Webconnect runs 10/100 Mbit data transfer to Sunny Explorer. Through the Webconnect function, a small system can report straight to Sunny Portal for up to 4 inverters. Larger plants report through the SMA Cluster Controller. The Sunny Tripower TL-US has the Webconnect data module with an RJ45 connection as standard. The Sunny Island uses its own Speedwire data module, which Sunny Explorer shows as a protocol converter. The SWPB-US-10 piggyback version mounts on the communication board of SB-US-12 and SB-US-TL12 inverters. Before you buy one, read the BFR/SRR stamp on the inverter's EPROM chip to confirm the minimum firmware: 1.12 for SB5000US to SB8000US and 2.00 for SB5000US-12 to SB8000US-12. Piggyback cards cannot be daisy-chained. Wire each inverter in a star pattern to its own Ethernet switch port using CAT5E or CAT6 cable with 568B wire order, and keep communication cables at least 2 inches from AC cables. A newly installed piggyback must get a firmware update over Speedwire with Sunny Explorer before it can communicate. Afterwards, a flashing amber LED means it is wired correctly, and a solid green LED means it has a good internet connection. On the Sunny Island, warning 848 PhsMtrComFail (communication with the SMA Energy Meter failed) calls for checking the data cables and installing the current firmware on the Speedwire data module.

<!-- review notes
- sentence 1: support check: partial - u1 says the module is for inverters without an integrated Speedwire interface, and u8 says Speedwire is Ethernet-based. The passages do not say outright that the module adds the interface, and they do not call it an SMA communication module.
- sentence 3: support check: partial - u3 supports the RJ45-as-standard part, though it does not name the Sunny Tripower TL-US. u10 and u26 show the Sunny Island Speedwire data module displayed as a protocol converter in firmware components, which the passages do not tie to Sunny Explorer.
- sentence 4: support check: partial - u23 supports the minimum firmware values and the BFR/SRR check before purchase. It also supports mounting on the Communication Board of SB-US-12 and SB-US-TL12 inverters. It does not say the 1.12 and 2.00 values come from reading the stamp on the EPROM chip for those exact series.
-->
