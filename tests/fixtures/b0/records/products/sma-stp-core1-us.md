---
id: prod:sma-stp-core1-us
type: Product
name: SMA Sunny Tripower CORE1-US
make: sma
product_level: family
claims:
  - claim_id: c1
    rel: instance_of
    target: comp:string-inverter
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c2
    rel: manufactured_by
    target: org:sma
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c3
    rel: implements
    target: func:rapid-shutdown
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c4
    rel: uses_protocol
    target: proto:modbus-tcp
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c5
    rel: exposes
    target: reg:sma-stp-core1-us-30513
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c6
    rel: has_hazard
    target: hazard:dc-arc-flash
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c7
    rel: compatible_with
    target: arch:ac-coupled-storage
    negated: true
    scope:
      applications: [backup]
      regions: [region:us]
      firmware_min: 3.12.20.R
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
---

Fixture record for schema 0.5.0 (products).
