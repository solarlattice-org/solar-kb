---
id: symptom:low-performance-ratio
type: Symptom
name: Low performance ratio
aliases:
- PR
claims:
- claim_id: c1
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: During grid curtailment the low PR reflects export limits rather than equipment health; inverter
    and tracker availability can look normal.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:performance-ratio-decline
  note: PR plotted over time and against module temperature shows small shifts in system performance and
    long-term degradation.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=1.1
    h: 6ef65608e9f7
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.1.1
    h: d5ee0a10b7d9
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages mention PR over time and long-term degradation, but
    not explicitly a declining PR from AC energy vs POA irradiation as a signature.'
- claim_id: c3
  rel: observed_as
  target: meas:energy-ratio-out-of-range
  note: Daily energy from each inverter or meter is compared with modeled expected energy; the test fails
    when the ratio falls outside its pass band.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=13.r4
    h: 729bb0c18bac
  review: drafted
  review_note: 'support check: partial - Energy ratio test compares daily energy to expected and passes
    between 70-110%, but the passage doesn''t link it to low PR or say ''below expected''; pass band is
    stated.'
- claim_id: c4
  rel: observed_as
  target: meas:performance-index-below-unity
  note: Performance Index alerts trigger on a low ratio of measured to modeled power for meters and inverters.
  cite:
  - src: src:alsoenergy-kb-pv-model-settings
    loc: sec=h11
    h: 52c6aca287c4
  - src: src:alsoenergy-kb-grouping-and-advanced-search
    loc: sec=h1
    h: ad50c4b37958
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - PI alerts trigger on low measured-to-modeled power ratio, but
    ''below unity'' and ''sustained period'' (only time thresholds implied) are not exactly stated.'
- claim_id: c5
  attr: degradation_rate
  value:
    min: 0
    max: 1
    unit: unit:PERCENT-PER-YR
  conditions: Normal expected power-output degradation over time; rates well above this suggest module
    faults such as PID
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.6
    h: 454242c5993b
  review: drafted
---
A low performance ratio means the plant delivers less energy than its irradiance and rated power would predict. It is the main indicator of how efficient and reliable a PV plant is overall. Many things lower PR: module temperature and ventilation, shading or soiling of the modules or the irradiance sensor, cable and inverter losses, mismatch, grid unavailability and ageing. Before treating a low PR as an equipment fault, check for grid curtailment. Curtailment shows up as a flat, controlled output level below what the irradiance supports, while inverters and trackers look fully available. To confirm curtailment, compare plant setpoints, inverter active power limits, dispatch signals, meter output and curtailment flags with the available power estimated from irradiance. On plants that are curtailed often, use curtailment-aware metrics. Otherwise crews may chase equipment problems that are not there. If the plant is not curtailed, trend PR over time and against module temperature. Compare each inverter's energy or power with modeled values to find the underperforming unit. A decline much faster than the usual 0 to 1 percent per year points to module faults such as potential induced degradation. Check for module discoloration, or run low-light voltage tests on site.

<!-- review notes
- sentence 1: support check: partial - PR is described as indicating efficiency and reliability and the ratio of actual to theoretical output, but 'main indicator' is overstated (one of the most important).
-->
