---
id: symptom:recovery-after-rain
type: Symptom
name: Recovery after rainfall
claims:
- claim_id: c1
  rel: observed_as
  target: meas:post-rain-production-recovery
  note: With granular dust, irradiance-normalized output falls slowly through dry periods and then recovers
    partly or fully after meaningful rain or washing.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: drafted
  review_note: 'support check: partial - Passages state normalized output declines in dry periods and
    recovers after rain, but say nothing about the specific signals (rain sensor, step up in W, POAI showing
    no matching change).'
---
Irradiance-normalized production falls slowly during dry weather, then comes back partly or fully after a meaningful rain or a wash, and the plant stays online the whole time. This pattern points to granular dust soiling: dust on the glass lets less light through and lowers array current between rain or cleaning events. Fungal or biological soiling looks different. That loss does not recover after rain but does improve after manual cleaning. Check first that the dip is not caused by availability problems, clipping, curtailment or irradiance sensor faults. Then compare the trend with soiling station data, rainfall, cleaning logs and nearby reference blocks. Do not measure dust soiling from one dirty irradiance sensor alone. Sensor drift, poor cleaning practice or a local obstruction can produce a soiling-like signal that does not represent the array. Sources disagree on how much rain it takes to clean modules, and rain may not remove cemented particles, so the recovery can be only partial. Roads, exposed soil, farming, construction, prevailing wind and row edges can make the loss, and the recovery after rain, uneven across the site. Test whether the soiling model reproduces the observed recovery after rain. If it does not, update the local dust build-up and wash-off assumptions before using the model to plan cleaning.

<!-- review notes
- sentence 7: support check: partial - u4 says those factors can make the loss spatially uneven, but doesn't say the recovery after rain is uneven.
-->
