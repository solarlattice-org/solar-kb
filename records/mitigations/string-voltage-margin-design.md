---
id: mit:string-voltage-margin-design
type: Mitigation
name: String voltage margin design
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average summer 2025 energy loss from inverter voltage flooring at a 100 MW California PV
    plant, before any mitigation
  note: This is the loss the mitigation addresses. The source credits voltage or setting adjustments,
    not string redesign specifically, with recovering a large share of it.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
String voltage margin design means sizing PV strings so the array voltage stays inside the inverter's DC input window, at both low and high module temperatures. It addresses inverter voltage floor losses, where array Vmp drops below the inverter's minimum DC input voltage and the inverter has to run above the maximum power point. Hot weather is the main risk on the low side, because module voltage falls as cell temperature rises. Cold weather is the risk on the high side, because string voltage rises and can damage the inverter. For manual sizing, apply the NEC 690.7 temperature factors or the module maker's temperature coefficient, and check that string voltage at the minimum design temperature stays below the inverter limit. The supplier's online string sizing tool can be used instead. In the field, measure each string's open-circuit voltage. If it is close to the inverter's maximum accepted value, check the string length. The source lists string redesign as a change for future designs only. For existing plants it names transformer tap adjustment, inverter parameter changes and a revised voltage control strategy. Check any change with the inverter supplier and the plant electrical engineer. Afterwards, compare the recovered operation with IV-derived Vmp and Pmp, and confirm that reactive power obligations are still met.

<!-- review notes
- sentence 1: support check: partial - Passages mention preserving low- and high-temperature voltage margin and keeping string voltage under limit at minimum temperature, but don't define the term as sizing within the DC window at both extremes.
- sentence 4: support check: partial - Passages say to follow NEC 690.7 factors or manufacturer coefficient so voltage is below 600 V at minimum temperature, and mention Solectria's tool; the limit is a specific 600 V for that inverter, and the tool is Solectria's rather than generic supplier.
- sentence 6: support check: partial - Passage lists string design changes as 'future' and lists the other actions, but doesn't explicitly say they are for existing plants.
-->
