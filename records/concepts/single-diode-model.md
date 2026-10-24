---
id: concept:single-diode-model
type: Concept
name: Single-diode model
aliases:
- single diode model
- five-parameter model
- Single Diode PV model
category: Modules
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: tool:pvsyst
  note: The PVsyst module model is based on the single-diode PV model.
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h9
    h: 66236fab93e4
  review: drafted
- claim_id: c2
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack can be set up with a PVsyst or single-diode model, using parameters taken from a PVsyst
    configuration or from module specifications.
  cite:
  - src: src:alsoenergy-kb-pvsyst-or-single-diode-model-configuration-in-powertrack
    loc: sec=front
    h: a22ee30f5c5d
  - src: src:alsoenergy-kb-pvsyst-or-single-diode-model-configuration-in-powertrack
    loc: sec=h1
    h: fa62a42caad1
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:short-circuit-current
  note: Isc is one of the required model parameters.
  cite:
  - src: src:alsoenergy-kb-pvsyst-or-single-diode-model-configuration-in-powertrack
    loc: sec=h1
    h: fa62a42caad1
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:open-circuit-voltage
  note: Voc is one of the required model parameters.
  cite:
  - src: src:alsoenergy-kb-pvsyst-or-single-diode-model-configuration-in-powertrack
    loc: sec=h1
    h: fa62a42caad1
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:double-diode-model
  note: The double-diode model is an alternative solar cell model. Like the single-diode model, it is
    used to produce simulated data for fault detection.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h38
    h: c8d07ea96aab
  - src: src:pv-root-cause-potential-induced-degradation
    loc: fig=4
    h: 532eae3cbaf5
  review: drafted
---
The single-diode model is an equivalent-circuit model of a solar cell or module that is used to calculate how the module behaves electrically. The PVsyst module model is built on the single-diode PV model. To set up the model in a monitoring platform such as PowerTrack, you need the cell technology, Isc, Voc, Impp, Vmpp, the Isc temperature coefficient (muIsc), the shunt and series resistances, and the number of cells in series and in parallel. Cell area, shunt resistance at a given irradiance and the exponential parameters are optional; enter NaN for any value you do not have. You can copy the parameter values straight from a PVsyst configuration or look them up in the module specifications online. Some fault detection systems train on simulated data generated with the single-diode or double-diode solar cell model instead of field data.

<!-- review notes
- sentence 1: support check: partial - Passages show it is a solar cell model used for PV modelling and simulated data, but 'equivalent-circuit' is not stated.
- sentence 6: support check: partial - Passage says some systems use simulated data from single/double diode models, but 'train on' and 'instead of field data' are not stated.
-->
