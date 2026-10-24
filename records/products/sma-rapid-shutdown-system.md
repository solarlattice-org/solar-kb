---
id: prod:sma-rapid-shutdown-system
type: Product
name: SMA Rapid Shutdown System
aliases:
- RSS-US-IA
- PVRSS
- PV Rapid Shutdown System
category: MLPE
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  review: drafted
  review_note: 'support check: partial - Passages describe an SMA inverter-based rapid shutdown system
    (SMA 360° app, SMA Rapid Shutdown Initiator) but never state that the system is made by SMA explicitly;
    implied only.'
- claim_id: c2
  rel: implements
  target: func:rapid-shutdown
  note: A complete system is the SMA inverter (listed as PV Rapid Shutdown Equipment), PV array disconnect
    switches and a rapid shutdown initiator; it must bring DC conductors below 30 V within 30 seconds.
  cite:
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:sunspec-rapid-shutdown-signal
  note: The inverter sends a SunSpec permission-to-operate signal over the DC input conductors and stops
    it when rapid shutdown is initiated.
  cite:
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  review: drafted
- claim_id: c4
  rel: requires
  target: role:qualified-person
  note: Connecting the external SMA Rapid Shutdown Initiator RSI-US-50 is a task for a qualified person.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h197
    h: 2164977aaec7
  review: drafted
  review_note: 'support check: partial - u25 is headed QUALIFIED PERSON and covers connecting the RSI-US-50,
    but the passage doesn''t explicitly say it requires a qualified person beyond the heading.'
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sbse-us-50
  note: Rapid Shutdown function enabled by default on this inverter.
  cite:
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=4.4.11
    h: 651fa43381de
  - src: src:kb-sma-sbsexx-us-50-sm-rapid-shutdown-initiator
    loc: tbl=1
    h: 3f6455b58cd5
  review: drafted
  review_note: 'support check: partial - u16 links RSI-US-50 to Sunny Boy Smart Energy, but the default-enabled
    note appears in u24/u26 whose applicability to SBSE US-50 isn''t stated in the passages.'
- claim_id: c6
  rel: compatible_with
  target: prod:sma-stp-core1-us
  note: Rapid Shutdown function disabled by default.
  cite:
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  - src: src:kb-sma-stpxx-us-41-configuring-the-rapid-shutdown-function
    loc: sec=front
    h: a658b65c6f8a
  review: drafted
  review_note: 'support check: partial - Disabled-by-default is stated in u2/u34, and u7 is a Sunny Tripower
    CORE1-US configuration article, but u2/u34 don''t name the product explicitly.'
- claim_id: c7
  rel: compatible_with
  target: prod:sma-sb-us-41
  cite:
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: sec=front
    h: 07476a4e5bca
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: tbl=19.r3
    h: cbb2f6177c5f
  - src: src:kb-sma-sbx1xpus41-configuring-the-rapid-shutdown-function
    loc: tbl=1.r3
    h: d0088ff9ec26
  review: drafted
  review_note: 'support check: partial - u4 is a Sunny Boy 3.0-7.7-US-41 configuring-rapid-shutdown article
    title, implying compatibility, but no content states it.'
- claim_id: c8
  rel: compatible_with
  target: prod:sma-stp-tl-us
  note: DC-side discharge is off by default and must be activated manually after commissioning.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h63
    h: 01288b4fa6a7
  review: drafted
  review_note: 'support check: partial - u29 states DC discharge off by default and must be activated
    manually, but doesn''t name Sunny Tripower TL-US or explicitly state compatibility.'
- claim_id: c9
  rel: compatible_with
  target: prod:jms-f-rapid-shutdown-device
  note: SMA-compatible SunSpec certified rapid shutdown receiver mounted on each module frame.
  cite:
  - src: src:sma-kb-jms-f-sunspec-certified-rapid-shutdown-device-installation
    loc: sec=h1
    h: 8e81e8fbd970
  - src: src:sma-kb-installing-the-jms-f-rapid-shutdown-device-to-your-pv-panel
    loc: sec=h1
    h: 2efbe57cbd0a
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:sma-rapid-shutdown-initiator-rsi-us-50
  scope:
    products:
    - prod:sma-sbse-us-50
  cite:
  - src: src:kb-sma-sbsexx-us-50-sm-rapid-shutdown-initiator
    loc: tbl=1
    h: 3f6455b58cd5
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h197
    h: 2164977aaec7
  review: drafted
- claim_id: c11
  attr: max_count
  value:
    max: 3
    unit: unit:NUM
  scope:
    products:
    - prod:sma-sbse-us-50
  conditions: Inverters connectable to one SMA Rapid Shutdown Initiator RSI-US-50 using the adapter matched
    to the Sunny Boy Smart Energy
  cite:
  - src: src:kb-sma-sbsexx-us-50-sm-rapid-shutdown-initiator
    loc: tbl=1
    h: 3f6455b58cd5
  review: drafted
---
The SMA Rapid Shutdown System is a complete PV rapid shutdown setup. It is made up of an SMA inverter, PV module or array disconnect switches, and a rapid shutdown initiator. Together they must bring the DC conductors below 30 V within 30 seconds. The inverter on its own is listed as PV Rapid Shutdown Equipment under UL 1741 and does not perform every function of a complete system. The installer is responsible for making sure the finished system meets NEC rapid shutdown requirements. Rapid shutdown starts when the inverter loses AC grid voltage, for example when the main PV AC disconnect is opened. That disconnect must be readily accessible and marked, and its Off position shows that a shutdown has been initiated. With SunSpec-compliant module switches, the inverter sends a permission-to-operate signal over the DC conductors and stops sending it during a shutdown. Every module connected to the inverter must then have a SunSpec-compliant switch. The switches must disconnect the array within 15 seconds. The sum of switch standby voltages in a string must stay below 30 V, and newer manuals add a lower limit of 3.6 V. The recommended total string cable length is 300 m (1000 ft) on Sunny Tripower models and 160 m (520 ft) on Sunny Boy Smart Energy. On Sunny Boy Smart Energy, the initiator can be the AC disconnect or a device wired to the GSI digital input, such as the SMA Rapid Shutdown Initiator RSI-US-50, which can serve up to 3 inverters. SMA supports JMS-F SunSpec certified rapid shutdown devices. Each one should measure about 1 Vdc before it is connected into a string.

<!-- review notes
- sentence 4: support check: partial - Signal, stop on shutdown and 15 s disconnect are stated, but 'every module must have a SunSpec switch' is stated as needed for proper function, fine; however the 15 s applies to all disconnect switches rather than only SunSpec ones, a minor qualifier.
- sentence 5: support check: partial - The <30 V, >3.6 V in newer manual, 300 m and 160 m are stated, but the 160 m passage (u24) is for a different inverter (PV or hybrid) and Sunny Boy Smart Energy is not named there; u26 attributes it to the SBSE section only implicitly, and u26's 3.6 V/160 m is shown while u30 shows 300 m with 3.6 V too, so 'Sunny Tripower' attribution is unstated.
- sentence 6: support check: partial - RSI-US-50 up to 3 inverters and a GSI digital input initiator option are stated, but 'AC disconnect' as an SBSE initiator option and the RSI wired to the GSI are only loosely supported.
-->
