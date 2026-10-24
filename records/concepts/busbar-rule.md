---
id: concept:busbar-rule
type: Concept
name: 120% busbar rule
aliases:
- 120% rule
- busbar rating
- busbar overload
- 120% of busbar rule
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: arch:load-side-connection
  note: The busbar rating methods apply to connections made on the load side of the service disconnecting
    means.
  cite:
  - src: src:std-standards-nec-2017-nec2017-705
    loc: sec=h9
    h: 6de44b94103f
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:ampacity
  note: The limit is set as a percentage of the busbar ampacity.
  cite:
  - src: src:std-standards-nec-2020-nec-2020-705
    loc: sec=h25
    h: c63742cb1b49
  - src: src:std-standards-nec-2017-nec2017-705
    loc: sec=h9
    h: 6de44b94103f
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h159
    h: 9edad9ff2e02
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:overcurrent-protection
  note: The rating of the overcurrent device protecting the busbar is part of the sum.
  cite:
  - src: src:std-standards-nec-2020-nec-2020-705
    loc: sec=h25
    h: c63742cb1b49
  - src: src:std-standards-nec-2017-nec2017-705
    loc: sec=h9
    h: 6de44b94103f
  review: drafted
- claim_id: c4
  rel: related_to
  target: arch:supply-side-connection
  note: A line side tap is listed as an option when the 120% rule does not leave enough room for the solar
    breaker.
  cite:
  - src: src:se-academy-solaredge-pcs-certification-na-technical-02-solaredge-nexis-pcs-training
    loc: sec=h2
    h: 304eea485e46
  review: drafted
---
The 120% busbar rule is an NEC method for load-side PV connections. It adds 125 percent of the source output circuit current to the rating of the breaker protecting the busbar, and that sum may reach up to 120 percent of the busbar ampacity. It only applies when the utility and the inverter feed the busbar from opposite ends, the busbar serves loads, and the busbar is sized for those loads under Article 220. A permanent warning label must be placed next to the back-fed breaker telling people not to relocate it. Moving that breaker could load the busbar beyond its rating. For example, a 200 A busbar fed by a 200 A main breaker allows an inverter output current of up to 32 A. In field terms, the maximum solar breaker is the busbar rating times 1.2 minus the main breaker rating, and the solar breaker itself is sized at 1.25 times the inverter's maximum continuous current. If that is not enough, the options are derating the main breaker, a line side tap, or a main panel upgrade. A Temporary Interim Amendment, carried into the 2017 NEC, lets the same 120 percent limit apply to a PV breaker at either end of a center-fed panelboard in a dwelling. Other busbar methods include the 100 percent sum rule, the sum-of-breakers rule used for AC combiner panels, and designs done under engineering supervision.

<!-- review notes
- sentence 2: support check: partial - Opposite-end sources, loads on the busbar and Article 220 sizing are stated, but 'only applies' is too strong: the center-fed dwelling provision also applies the 120% limit, and the source is 'a primary source', not strictly the utility.
- sentence 5: support check: partial - Formulas and derate MCB/line side tap/MPU options are on the slide, but 'MPU' is not spelled out as a main panel upgrade in the passage.
- sentence 7: support check: partial - The sum-of-breakers (AC combiner) and engineering-supervision methods are stated, and method (a) is the sum with the 100% busbar ampacity limit, but it is not called a '100 percent sum rule'.
-->
