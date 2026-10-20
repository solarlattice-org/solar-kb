---
id: method:energy-ratio-analysis
type: DetectionMethod
name: Energy ratio analysis
claims:
- claim_id: c1
  rel: produces
  target: meas:energy-ratio-gradual-decline
  note: Soiling loss is flagged by pattern matching on the energy ratio as a slow loss over several days;
    typically 5 or more days of data are needed and spans shorter than 4 days are not detected. Loss size
    comes from the slope, the gap between ideal and daily average energy ratio, and actual production.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: drafted
  review_note: 'support check: partial - Soiling pattern matching on energy ratio, 5+ days, <4 days undetected,
    and loss-size basis are stated, but the specific signals (no matching irradiance drop, module temperature
    input, daily AC energy falling) are only loosely supported and ''gradual decline'' is described as
    gradual performance loss.'
- claim_id: c2
  rel: produces
  target: meas:energy-ratio-out-of-range
  note: Daily energy of each inverter and production meter is compared with expected energy from a full
    PV model; the check passes when produced energy is between 70% and 110% of expected. The test is disabled
    by snow.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=13.r4
    h: 729bb0c18bac
  review: drafted
---
Energy ratio analysis compares the energy a system actually produced each day with the energy a PV model expects from measured irradiance and module temperature. The ratio can be calculated separately for each inverter and each production meter, and a daily check passes when output stays within a set band around the expected energy. Results depend on a well-tuned PV model and accurate irradiance and temperature data, and the check is switched off when snow is present. Soiling losses show up as a slow drop in the energy ratio over several days, which a pattern-matching routine picks up. Usually five or more days of data are needed to detect a soiling event, and spans shorter than four days are not detected. Soiling loss can be measured against an ideal ratio of 1.0 for a model tuned to a clean system, or counted from zero at the start of each soiling event. A simpler monthly version, the insolation-adjusted estimated energy ratio, divides the ratio of measured to estimated AC energy by the ratio of measured to estimated insolation.

<!-- review notes
- sentence 7: support check: partial - The IEER formula and monthly nature are stated, but 'simpler version' of the energy ratio is not stated (simplicity is mentioned), and 'ratio of measured to estimated' matches the formula.
-->
