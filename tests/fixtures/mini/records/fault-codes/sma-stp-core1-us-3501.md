---
id: fc:sma-stp-core1-us-3501
type: FaultCode
name: SMA CORE1-US 3501
aliases: ['3501', SMA 3501, Insulation failure > Check PV array]
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3501'
code_key: '3501'
display_message: Insulation failure > Check PV array
page: 51
status: active
claims:
  - claim_id: c1
    rel: defined_in
    target: src:sma-core1-manual
    cite: [{src: "src:sma-core1-manual", loc: "sec=h12", h: "4d5e6f708192"}]
    review: drafted
  - claim_id: c2
    rel: reports
    target: symptom:low-insulation-resistance
    cite: [{src: "src:sma-core1-manual", loc: "sec=h12", h: "4d5e6f708192"}]
    review: drafted
  - claim_id: c3
    rel: has_event_class
    target: ec:fault
    cite: [{src: "src:sma-core1-manual", loc: "sec=h12", h: "4d5e6f708192"}]
    review: drafted
  - claim_id: c4
    rel: has_production_effect
    target: ec:trip
    cite: [{src: "src:sma-core1-manual", loc: "sec=h12", h: "4d5e6f708192"}]
    review: drafted
---
