---
id: meas:soiled-vs-clean-isc-ratio
type: Measurement
name: Soiled vs clean Isc ratio
aliases:
- short-circuit current soiling ratio
- Soiling Ratio
- SR
- Soiling ratio index
- Cleanness Index
- Soiling Factor
- Soiling Loss Factor
signals:
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: use clear-sky, high-irradiance midday periods only
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: back-of-module temperature used to temperature-correct Isc
claims:
- claim_id: c1
  attr: current_drop
  value:
    nominal: 3
    unit: unit:PERCENT
  conditions: Short-circuit current loss under dust-storm soiling, February 2017 event near Évora, Portugal;
    kept small by bypass-diode activation
  note: In the same event the power output fell by 8%, so the Isc ratio underestimated the loss.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=5.3.1
    h: 17978c0f428f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 8
    unit: unit:PERCENT
  conditions: Power output decrease from non-uniform dust-storm soiling, February 2017 event near Évora,
    Portugal, compared with a 3% Isc loss
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=5.3.1
    h: 17978c0f428f
  review: drafted
---
This signature compares the temperature-corrected short-circuit current of a PV device left to soil with that of an identical device that is cleaned regularly and mounted beside it. A ratio of one means the device is clean, and the ratio drops as dirt builds up. The soiling loss is one minus the ratio. The pair can be two reference cells, two modules, or one cell and one module. The reference device should ideally be cleaned every morning, because cleaning it too rarely makes the ratio understate soiling. Take readings in clear sky during the central hours of the day, within about two hours of solar noon for fixed systems, and leave out data from passing clouds. When soiling is uniform, the Isc ratio tracks power loss well. When dirt is uneven, for example built up along the bottom cell row, bypass diodes can switch out soiled cells and power falls much more than Isc. This reading is most often used to measure soiling losses, including dust-storm deposits. For uneven soiling, also log power, or use the power ratio instead. Reference cells may soil differently from array modules if their cover glass is different, and they cannot capture uneven soiling. That makes cell-to-cell setups the least accurate.

<!-- review notes
- sentence 6: support check: partial - Passages say Isc is the common soiling ratio approximation and that power should also be collected or preferred for non-uniform soiling, but 'most often used' for dust-storm deposits specifically is not stated.
- sentence 7: support check: partial - Passages say cell-cell Isc setups are the least accurate (4-7%) because of different cover glass and missed non-uniform soiling, but optical methods are tied for least accurate, so 'the least accurate' omits that.
-->
