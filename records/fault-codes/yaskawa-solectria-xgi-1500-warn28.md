---
id: fc:yaskawa-solectria-xgi-1500-warn28
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-28
aliases:
- WARN-28
- warn28
- Yaskawa Solectria WARN-28
- Network Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-28
code_key: warn28
display_message: Network Fault
vendor_severity: Warning
page: 56
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
  cite:
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r2
    h: 3712f730667b
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
  cite:
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: tbl=20
    h: a7be798a92ad
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=17
    h: a7be798a92ad
  review: drafted
- claim_id: c5
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r2
    h: 3712f730667b
  review: drafted
  review_note: 'support check: partial - Network connection failed is a network fault, roughly communication
    loss, but the wording differs.'
- claim_id: c6
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r2
    h: 3712f730667b
  review: drafted
  review_note: 'support check: partial - The row says to check Ethernet connections, but it doesn''t name
    the network cable as the affected component; it also…'
- claim_id: c7
  rel: affects
  target: comp:wifi-module
  note: Antenna mounting orientation is the stated check point.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r2
    h: 3712f730667b
  review: drafted
  review_note: 'support check: partial - The row mentions Wi-Fi antennas being vertically mounted, but
    it does not say the warning affects the Wi-Fi module itself;…'
- claim_id: c8
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: tbl=19.r2
    h: 3712f730667b
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=20.r2
    h: 3712f730667b
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  note: Based on section statement that all warning events cease AC production.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r2
    h: 3712f730667b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: drafted
---
