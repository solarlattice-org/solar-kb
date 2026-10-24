---
id: hazard:dc-arc-flash
type: Hazard
name: DC arc flash
aliases:
- DC arcing
- arc flash
category: Electrical
claims:
- claim_id: c1
  rel: controlled_by
  target: tool:arc-rated-clothing
  note: Arc-rated clothing is the most common, industry-accepted PPE against arc flash; its main purpose
    is to limit burns to a curable level.
  cite:
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: sec=h80
    h: 032cb724d40d
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: proc:arc-flash-hazard-assessment
  note: An incident energy calculation sets the required PPE level and the arc-flash boundary distance.
    NFPA 70E Annex D.5 gives a dc method based on Doan's maximum power transfer approach, for dc systems
    up to 1000 V.
  cite:
  - src: src:trn-safety-epri-dc-arc-flash-on-photovoltaic-equipment
    loc: sec=h18
    h: ddfdc2bab6b6
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: sec=h28
    h: 23c8c5db955a
  - src: src:book-practical-solution-guide-to-arc-flash-hazards-2nd-ed
    loc: sec=h80
    h: 032cb724d40d
  review: drafted
---
A DC arc flash is a sudden high-power discharge between conductors in a PV source circuit. It can release a lot of energy close to a worker. In PV systems it has been studied in combiner boxes and inverter cabinets fed by a live PV array. In those tests the arcs moved around inside the equipment. DC arcs can badly damage a PV system and often start destructive fires. Because they are short-lived, they are hard to detect. DC arc flash is much less understood than AC arc flash. The proposed calculation methods have not been backed by equipment tests and contradict one another. NFPA 70E covers DC arc flash. Its Annex D.5 gives an incident energy method for DC systems up to 1000 V, based on maximum power transfer. Do an arc flash hazard assessment first: the incident energy result sets the PPE level and the arc-flash boundary. PPE that is too heavy or too light both add risk. Limit exposure in three ways: avoid arc flash accidents through correct procedures, proper tools and good maintenance; reduce the arc energy; and wear arc-rated clothing. Arc fault circuit interrupters on individual strings can protect the PV system from DC arc faults.

<!-- review notes
- sentence 1: support check: partial - u7 supports a sudden high-power discharge between two conductors, and u5 says the tests measure the energy a worker could be subjected to near an arc. Nothing states that it releases a lot of energy close to a worker, and the passages do not specifically say 'PV source circuit'.
- sentence 2: support check: partial - The tests in combiner boxes and an inverter cabinet on a live PV source are supported, and the figures show arc movement. u5 poses arc movement only as a research question, and the passages never state the finding that the arcs moved inside the equipment.
- sentence 3: support check: partial - u7 says dc arcs are severely damaging, usually cause destructive fires, and are transient so hard to detect. 'Often' is a reasonable paraphrase of 'usually', but the evidence does not directly say that short-lived arcs are hard to detect for that reason in those words, which is close enough; the main gap is minor.
- sentence 6: support check: partial - u5 says the IE calculation sets the PPE level and boundary, and that overly burdensome and inadequate PPE both carry risk. u33 says the PPE type depends on the assessed hazard. The imperative to do the assessment first is not stated explicitly.
- sentence 7: support check: partial - u30 lists the three ways: avoid accidents via procedures, tools and maintenance, reduce arc energy, and use PPE. The specific 'arc-rated clothing' is only a typical PPE item from u33, not the third method itself.
-->
