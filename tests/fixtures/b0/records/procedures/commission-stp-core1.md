---
id: proc:commission-stp-core1
type: Procedure
name: Commission an STP CORE1-US
procedure_kind: commission
claims:
  - claim_id: c1
    rel: uses_tool
    target: tool:insulation-tester
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c2
    rel: requires
    target: role:installer
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c3
    rel: applies_to
    target: prod:sma-stp-core1-us
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
  - claim_id: c4
    rel: has_hazard
    target: hazard:dc-arc-flash
    cite: [{src: "src:b0-vendor-manual", loc: "sec=1", h: "a1b2c3d4e5f6"}]
    review: drafted
---

Fixture record for schema 0.5.0 (procedures).
