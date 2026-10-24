---
id: prog:sunspec-certification
type: Program
name: SunSpec certification
aliases:
- SunSpec certified
- SunSpec Modbus certification
- SunSpec rapid shutdown certification
category: Certification
program_kind: certification
claims:
- claim_id: c1
  rel: issued_by
  target: org:sunspec
  note: Devices are labelled SunSpec certified; the SunSpec Alliance publishes the normative interoperability
    specifications that conformance is checked against.
  cite:
  - src: src:sma-kb-installation-of-sunspec-certified-shutdown-receiver
    loc: sec=h1
    h: 0a53013adbc9
  - src: src:test-cx-manuals-sunspec-commissioning-for-pv-performance
    loc: sec=h7
    h: 137dce698dee
  review: drafted
  review_note: 'support check: partial - u11 says SunSpec Alliance publishes normative interoperability
    specs, but nothing states that the Alliance issues the certification or that devices are labelled
    certified by it (only that products are ''SunSpec certified'').'
- claim_id: c2
  rel: applies_to
  target: prod:jms-f-rapid-shutdown-device
  note: SMA calls the JMS-F a SunSpec Certified Rapid Shutdown Device.
  cite:
  - src: src:sma-kb-installation-of-sunspec-certified-shutdown-receiver
    loc: sec=h1
    h: 0a53013adbc9
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:tigo-ts4
  note: The TS4-R-F line is an SMA-compatible rapid shutdown receiver that is SunSpec certified.
  cite:
  - src: src:sma-kb-installation-of-sunspec-certified-shutdown-receiver
    loc: sec=h1
    h: 0a53013adbc9
  review: drafted
---
SunSpec certification shows that a device conforms to a SunSpec interoperability specification. The best-known example is rapid shutdown equipment that responds to the SunSpec shutdown signal. SunSpec interoperability specifications are normative documents, so a product has to conform to them to support interoperability. Each specification moves through draft, test, approved and superseded stages. SMA publishes a technical information document that lists which of its inverters are approved for use with SunSpec Certified rapid shutdown devices. Check it before pairing an inverter with shutdown hardware. SMA names the JMS-F devices and the Tigo TS4-R-F receiver line as SunSpec certified rapid shutdown equipment that works with its inverters. On SMA inverters, set the rapid shutdown mode to SunSpec Shutdown when you use a PV array disconnect switch under the SunSpec interoperability specification.

<!-- review notes
- sentence 1: support check: partial - Passages show SunSpec certified rapid shutdown devices and SunSpec interoperability specs, but don't explicitly say certification shows conformance or that this is the best-known example.
- sentence 3: support check: partial - The titles show an SMA technical information document giving an overview of approved inverters with SunSpec Certified RSDs, but the advice to check it before pairing is not in the passages.
-->
