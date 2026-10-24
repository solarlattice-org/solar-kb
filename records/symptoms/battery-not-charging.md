---
id: symptom:battery-not-charging
type: Symptom
name: Battery not charging
aliases:
- Batteries not Being Charged
- battery will not recharge in backup mode
- battery is not charged
- Batteries not charging or discharging
- Not charging or discharging
claims:
- claim_id: c1
  rel: observed_as
  target: meas:reduced-battery-charge-current
  note: Charging power can stay below the maximum when ambient temperature is too high or too low, when
    a lithium-ion battery's BMS limits it, or when AC/DC charging current limit parameters are reached.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h985
    h: 32a04faf0161
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=14.2.9
    h: aabc484ce239
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:soc-below-full-after-full-charge
  note: High load demand before the full charge finished can keep the battery from reaching full SOC;
    a longer full charge time setting may help.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h979
    h: 2a543f30380c
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:battery-voltage-low
  note: Cable voltage drop from too small a battery cable cross-section, especially on long runs, can
    leave the charging voltage at the battery below the intended value.
  cite:
  - src: src:sma-doc-260329
    loc: tbl=1.r3
    h: 7d523bce0c0f
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:battery-soc-reading-low
  note: On Solis hybrid inverters, setting Charging from Grid to Not Allow can disturb force-charging
    logic and lead to a fully discharged battery.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: sec=h122
    h: 0e405355cdba
  review: drafted
---
The battery in a hybrid or battery-inverter system does not charge, or charges at less than the expected power. Check the charging power and the battery state of charge first, then compare the battery's current state with what you expect and look for the cause of any difference. Charging below full power can come from ambient temperature that is too high or too low, from the lithium-ion battery management system limiting the charge, or from the inverter's set AC and DC charging current limits. On Enphase systems, check the production and consumption meter setup first, because disabled or wrongly configured meters stop the batteries from charging or discharging. Check the operating settings: some modes only charge when there is enough PV power, and blocking grid charging can leave the battery fully discharged. If the SOC stays below full after a full charge, high load demand during charging may be the cause, so consider a longer full charge time. Also check that the battery cables are thick enough, since voltage drop on long thin cables lowers the charging voltage at the battery, and check that the system is not too small to supply enough charging energy. Overcurrent events during charging point to a problem in the external battery management system, so refer to the battery manufacturer's documentation.

<!-- review notes
- sentence 2: support check: partial - Comparing the current state with the expected state is stated, but checking charging power and SOC first is only loosely implied by a display label.
- sentence 8: support check: partial - Two passages say to fix the cause in the external BMS per the manufacturer's documentation, but the event 9392 passage only says the Service determines the cause and to contact the manufacturer, so the blanket claim for overcurrent events is stronger.
-->
