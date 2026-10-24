---
id: prod:sma-sunny-mini-central
type: Product
name: Sunny Mini Central
aliases:
- SMC
- SMC 9000-11000TL-10
- SMC-TL-10
- SMC 9000TL-10
- SMC 7000HV
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-kb-sunny-mini-central-manuals
    loc: sec=h1
    h: fe0a82e371b3
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passage says these are Sunny Mini Central inverters (string inverters)
    but does not explicitly state the class beyond ''inverters''; essentially supported.'
- claim_id: c2
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-change-in-service-concept-for-smc9-11000tl-rp-10
    loc: sec=h1
    h: 42c416c74c8b
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-webbox
  conditions: The Sunny WebBox documentation lists all Sunny Mini Central devices for its SMA-NET protocol
    setting and its SMA-COM interface setting
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25
    h: 628b7b7a4c10
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=24.r1
    h: 0a920c6c756e
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=24
    h: 2b6f22ab4a02
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:sma-net
  conditions: Protocol selected on the Sunny WebBox for Sunny Mini Central devices
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25
    h: 628b7b7a4c10
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: implements
  target: func:phase-balancing
  conditions: SMA Power Balancer, fitted as standard, links 3 Sunny Mini Central units on phases L1, L2
    and L3; deactivated at the factory; modes Fault Guard, Phase Guard, Power Guard, Off
  cite:
  - src: src:sma-kb-configuration-options-sma-power-balancer
    loc: sec=h1
    h: 83dff055fd96
  review: drafted
- claim_id: c6
  rel: requires
  target: role:grid-guard-code-holder
  conditions: Needed to change the PowerBalancer parameter, which can only be set through a communication
    device
  cite:
  - src: src:sma-kb-configuration-options-sma-power-balancer
    loc: sec=h1
    h: 83dff055fd96
  review: drafted
- claim_id: c7
  rel: has_hazard
  target: hazard:electric-shock
  conditions: DC voltage stays in the device unless the strings are disconnected; pulling the ESS handle
    does not de-energize it
  cite:
  - src: src:sma-kb-sunny-mini-central-smc9000tl-10000tl-110000tl-does-not-work-due-to-missing-string-f
    loc: sec=h1
    h: ed36ac947e54
  review: drafted
  review_note: 'support check: partial - Passage says DC voltage is present unless strings are disconnected
    and pulling the ESS handle is insufficient, but does not name electric shock as a hazard.'
- claim_id: c8
  attr: max_count
  value:
    nominal: 3
    unit: unit:NUM
  conditions: Sunny Mini Central inverters per SMA Power Balancer group in a three-phase feed-in system,
    each on a different line conductor
  cite:
  - src: src:sma-kb-configuration-options-sma-power-balancer
    loc: sec=h1
    h: 83dff055fd96
  review: drafted
- claim_id: c9
  attr: max_input_voltage
  value:
    nominal: 700
    unit: unit:V
  conditions: UPV max for SMC9000TL, SMC10000TL and SMC11000TL, from the replacement table
  cite:
  - src: src:sma-kb-change-in-service-concept-for-smc9-11000tl-rp-10
    loc: sec=h1
    h: 42c416c74c8b
  review: drafted
- claim_id: c10
  attr: max_input_current
  value:
    nominal: 28
    unit: unit:A
  conditions: IPV max for SMC9000TL, from the replacement table
  cite:
  - src: src:sma-kb-change-in-service-concept-for-smc9-11000tl-rp-10
    loc: sec=h1
    h: 42c416c74c8b
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions)
- claim_id: c11
  attr: max_input_current
  value:
    nominal: 31
    unit: unit:A
  conditions: IPV max for SMC10000TL, from the replacement table
  cite:
  - src: src:sma-kb-change-in-service-concept-for-smc9-11000tl-rp-10
    loc: sec=h1
    h: 42c416c74c8b
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions)
- claim_id: c12
  attr: max_input_current
  value:
    nominal: 34
    unit: unit:A
  conditions: IPV max for SMC11000TL, from the replacement table
  cite:
  - src: src:sma-kb-change-in-service-concept-for-smc9-11000tl-rp-10
    loc: sec=h1
    h: 42c416c74c8b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
- claim_id: c13
  attr: rated_output_current
  value:
    nominal: 31
    unit: unit:A
  conditions: Maximum output current of the Sunny Mini Central 7000HV
  cite:
  - src: src:sma-doc-275587
    loc: sec=h24
    h: 105cdf06f41f
  review: drafted
  review_note: 'support check: partial - Maximum output current of SMC 7000HV is 31 A, but it is labeled
    maximum, not rated output current.; review: partial - The passage gives 31 A as the maximum output
    current of the SMC 7000HV, but the claim calls it rated output current, which the passage does not
    state.'
---
The Sunny Mini Central (SMC) is a family of older SMA string inverters. It includes the SMC 9000TL-10 to 11000TL-10, the TLRP-10 versions, the 7000HV, the 6000TL to 8000TL and the 4600A to 6000A models. The SMC9000TL, SMC10000TL and SMC11000TL accept up to 700 V DC, with maximum PV input currents of 28 A, 31 A and 34 A. Each connects to a single phase with neutral and protective earth. Every unit has the SMA Power Balancer built in. It links three units on different phases and offers the Fault Guard, Phase Guard, Power Guard and Off modes. It is switched off at the factory, and you need the SMA Grid Guard code to change it. The Sunny WebBox lists all Sunny Mini Central devices as supported, both under its SMA-NET protocol setting and under its SMA-COM interface setting. Known issue: replacement SMC9000TL to 11000TL units ship without string fuses and stay dark until you move the fuses over from the failed unit. If the unit is still dark after that, check the ribbon cable with the strings disconnected. A flashing red LED on the SMC-TL-10 models goes with the display messages Check DC Fuse or Check Varistor. SMA now suggests replacing a failed SMC9-11000TL(-RP)-10 with a Sunny Tripower STPxx-50, and one such unit can often replace three SMCs. For RS485 systems this needs the MD.485-41 module and a minimum firmware version.

<!-- review notes
- sentence 1: support check: partial - Model list is in the passage and they are called past inverters, but 'string inverters' is only a category label and 'older SMA' is implied; 4600A to 6000A fine.
- sentence 2: support check: partial - 700 V and currents are stated, and AC terminal is (3*) 1-N-PE, but 'connects to a single phase' is only implied by 1-N-PE notation.
-->
