---
id: mit:contractual-loss-limit
type: Mitigation
name: Contractual loss tolerance
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Module power loss attributed to light induced degradation (light soaking), general figure
    across technologies
  quote: could potentially entail losses up to 30%
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: drafted
  review_note: 'support check: partial - Passage says LID could entail losses up to 30%, which is an upper
    bound, not a typical value, and it says nothing about contractual tolerance.'
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 10
    max: 30
    unit: unit:PERCENT
  conditions: Amorphous silicon modules, Staebler-Wronski effect, within the first months of outdoor exposure
  note: Crystalline modules show only a few percent loss in the first exposure hours, then regenerate
    over several years; CIS/CIGS may gain instead.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h4
    h: c8bc75bb2d8d
  review: drafted
  review_note: 'support check: partial - Passage gives a-Si up to 10-30% in the first months, crystalline
    few percent, and CIS gains, but ''up to'' is a bound and no contractual tolerance is stated.'
---
This action means accepting a known amount of early module power loss from Light Induced Degradation (LID) and building it into yield and contract assumptions, instead of treating it as a defect. It applies because LID is an initial stabilization loss that appears when modules are first exposed to light, and how large it is depends on the cell technology. Crystalline modules usually lose a few percent in the first hours of exposure and then recover over several years. Amorphous silicon can lose much more in its first months outdoors. In practice, enter an LID percentage as a separate derate in the expected-production model. The model multiplies expected output by one minus that LID value. The tolerance only covers the expected stabilization loss. If early losses are larger than the technology-specific expectation, check them against nameplate with IV curve tracing and flash testing. Choosing low-LID module technologies is a complementary step that keeps the loss you have to accept small. The agreement should state the thresholds and who is responsible for warranty management, so it is clear when a loss goes beyond what was accepted and a claim should be made.

<!-- review notes
- sentence 1: support check: partial - Mitigation says to account for stabilization in yield assumptions, but contract assumptions and 'instead of treating as a defect' are not stated.
- sentence 5: support check: partial - Passages say to verify unexpected early losses with IV and flash testing against nameplate and technology expectations, but 'tolerance only covers expected loss' is not stated explicitly.
- sentence 6: support check: partial - Mitigation lists selecting low-LID technologies, but doesn't explicitly say it keeps the accepted loss small or call it complementary.
- sentence 7: support check: partial - Passage says the agreement should specify warranty management responsibilities and thresholds for acting directly or seeking owner consent, but not thresholds for when a loss exceeds what was accepted or LID specifically.
-->
