---
id: method:startup-commissioning-verification
type: DetectionMethod
name: Inverter startup commissioning verification
aliases:
- commissioning checklist
- startup services
- power run
- pre-commissioning
- Pre-Commissioning Checks
- Startup and Verification Test
- Startup Checklist
- Initial verification
- Installer Commissioning Checklist
claims:
- claim_id: c1
  rel: produces
  target: meas:meter-display-mismatch
  note: During CT verification, current on each phase is measured with a clamp meter while all inverters
    are off. The reading is compared with the export power meter value, and the two should match on every
    phase. A mismatch points to a problem with CT orientation or measurement.
  cite:
  - src: src:kb-solis-44002848827-epm-configuration-and-validation-guide
    loc: sec=h17
    h: fb7154fdef50
  review: drafted
  review_note: 'support check: partial - Procedure (inverters off, clamp meter per phase, compare with
    EPM, readings match) is stated, but the passage doesn''t say a mismatch points to CT orientation/measurement
    problems, though that is implied by the step''s purpose.'
---
Startup commissioning verification is the set of checks done when an inverter is first started. For safety, technicians follow the manufacturer's commissioning checklist. IEC 62446-1 describes the commissioning tests and inspection criteria used to confirm that a grid-connected PV system is installed safely and works correctly. The same tests can be repeated later as periodic retests. Some inverters must be commissioned through an installation wizard in their internal web interface. When there are several inverters, each one is commissioned separately. Manufacturer startup services need full DC and AC power at the unit. The AC must come from the utility, not from a generator. Where an export meter is used, the key step is checking CT orientation. With all inverters off, measure each phase with a clamp meter and confirm the reading matches the meter's displayed value. One limit: monitoring portals can show invalid data for the first days after commissioning, which skews long-term data. The fix is to delete those days or move the commissioning date in the portal.

<!-- review notes
- sentence 1: support check: partial - Passages say to follow the checklist for safety during startup, but don't define startup commissioning verification as a set of checks nor name it a manufacturer's checklist explicitly.
- sentence 3: support check: partial - Web UI Installation wizard is required for the inverter described and multiple inverters are commissioned individually, but 'some inverters' generalization is fine; the passages support both, though the individual note is about pre-commissioning.
- sentence 5: support check: partial - CT orientation verification steps are stated, but the 'where an export meter is used' condition is not stated and the meter is called EPM, which is a reasonable equivalent.
- sentence 6: support check: partial - Invalid data in first days after commissioning, skewing long-term data, and fixes of deleting data or changing the commissioning date are stated, but only for SMA Sunny Portal, with a 70-day deletion limit; the move-date fix applies when deletion isn't possible.
-->
