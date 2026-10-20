---
id: stressor:high-system-voltage
type: Stressor
name: High voltage to ground
aliases:
- module-to-ground voltage
- high voltage stress
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 41
    unit: unit:PERCENT
  conditions: Average performance loss reported for a 10.7 MW plant in Spain affected by PID, cited by
    Libby et al.
  note: This loss comes from PID, which is driven by voltage to ground. It is one plant's figure, not
    a general rate.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  review: drafted
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 20
    unit: unit:PERCENT
  conditions: Yield losses seen in past cases of PID within one year, caused by high voltage stress with
    respect to ground
  quote: Yield losses of 20 percent and more within 1 year were observed in the past.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
---
The voltage between a module's cells and its grounded frame grows as more modules are wired in series in a string. This voltage to ground drives leakage currents through the front glass and encapsulant, which causes Potential Induced Degradation (PID) and can sharply cut module and string power. In the shunting form of PID, sodium ions move from the glass into the cell and create shunts. In the polarization form, negative surface charges build up on the cell. Modules with p-type cells degrade in strings at negative polarity, and modules with n-type cells degrade in strings at positive polarity. Damage is worst in modules near one end of the string and in cells close to the frame. Exposure has grown because maximum system voltage has risen from 600 V to 1500 V. Transformerless inverters also often prevent grounding either end of the string. Heat, humidity, rain, condensation and soiling all speed up the damage, because they raise leakage current. To reduce the stress, use system grounding or offset strategies, choose PID-resistant modules, clean off conductive soiling, and consider qualified regeneration where appropriate.

<!-- review notes
- sentence 2: support check: partial - The passages support leakage currents through the front glass and encapsulant causing PID-s and large power loss. They do not tie that mechanism to voltage-to-ground-driven PID in general: PID-p is attributed to surface charge build-up, not leakage current.
- sentence 5: support check: partial - u14 gives the rise from 600 V to 1500 V and says transformerless power conditioners often prevent grounding either end of the string. It does not say explicitly that exposure has grown because of the voltage rise, though it implies higher voltage burdens.
- sentence 6: support check: partial - The passages list temperature, humidity, rain, condensation and soiling as accelerating factors. u14 says temperature, humidity and glass surface conductivity all lead to higher leakage current, but rain, condensation and soiling are not explicitly tied to leakage current.
-->
