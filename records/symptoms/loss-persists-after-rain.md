---
id: symptom:loss-persists-after-rain
type: Symptom
name: Loss persists after rainfall
claims:
- claim_id: c1
  rel: observed_as
  target: meas:no-recovery-after-rain
  note: Weather-normalized production deficit stays after rain events; with fungal bio-soiling only manual
    cleaning recovers it.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:post-cleaning-production-step
  note: A repeatable step-up in normalized production after manual cleaning, where rain had not restored
    expected output, is the key evidence for biological soiling.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent fungal bio-soiling losses at solar farms in North Carolina (humid subtropical
    U.S.), recovered only by manual cleaning, from 2024 field work
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: drafted
  review_note: 'support check: partial - 5-11% persistent losses in North Carolina recovered only by manual
    cleaning are stated, but ''typical'' is not used; they are reported losses.'
---
This symptom is a weather-normalized production deficit that stays in place after rain instead of recovering, as ordinary dust soiling normally does. Its main known cause is widespread fungal soiling: biofilms and other persistent biological deposits on the module glass that rain does not wash off but manual cleaning removes. It is easy to mistake for ordinary dust, pollen or a weather-normalization error. Granular dust soiling usually recovers partly or fully after enough rain, so the lack of recovery after rain is the key difference. Some particles can become cemented to the glass, and rain may not remove them either. In that case active cleaning is needed. Check first by comparing rain events and cleaning logs with SCADA, irradiance and weather-normalized production. Look for a repeatable step-up after cleaning where rain did not bring output back. Confirm biofilm with a close visual inspection or handheld microscopy. Check several areas of the array, because biological deposits can be patchy. Where this loss is confirmed, add cleaning to the maintenance plan and base forecasts on cleaning results, not on the assumption that rain resets the loss.

<!-- review notes
- sentence 4: support check: partial - u10 mentions the argument that rain doesn't remove cemented particles and active cleaning becomes necessary, but only as one side of a debate, not a firm statement.
-->
