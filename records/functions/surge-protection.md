---
id: func:surge-protection
type: Function
name: Surge protection
aliases:
- integrated SPD
- surge suppression
- lightning protection
- Surge Protection Device (SPD)
- DC overvoltage surge arresters
- AC overvoltage surge arresters
- Modular Surge Arrester
category: Protection
function_kind: protection
---
Surge protection guards the inverter against voltage spikes and surges. On the PV DC lines these come mainly from lightning, and they can also arrive on the AC grid lines. The protective device either blocks or shorts to ground any voltage above a safe threshold. SolarEdge three phase inverters with Synergy technology have a DC SPD and an AC SPD inside the inverter, and both report surge events and faults to the SolarEdge Monitoring platform. The CPS SCH200K-T-US-480 and SCH250K-T-US-600 use Type II MOV surge protection on both the DC and AC sides. The CPS SCH275KTL-DO/US-800 and SCH350KTL-DO/US-800 have Type II protection on DC and AC. The CSI-50KTL-GS-FL has class II protection on the DC side, and AC class III protection is optional. Every version of the FIMER PVS-60-TL-US has class 2 DC overvoltage surge arresters (PTG PV600-40M2-M), and these parts cannot be replaced. On medium-voltage equipment, Eaton rates an RC snubber with surge suppressor, preceded by a surge arrester where lightning is a concern, as the best protection. The snubber handles high-frequency transients and the arrester handles lightning peaks.

<!-- review notes
- sentence 2: support check: partial - Passages say both SPDs are inside the inverter and report to SolarEdge Monitoring, but do not mention three phase inverters or Synergy technology (only the Synergy manager guide URLs).
- sentence 3: support check: partial - Type II MOV for the 200K/250K models is stated for both sides, and Type II for the 275/350 on DC and AC, but MOV is not stated for those; the statement itself only claims Type II for them, so it is mostly supported; the 'both sides' claims hold.
- sentence 5: support check: partial - Passage supports PTG PV600-40M2-M, class 2, all versions, not replaceable, but the 'every version' applies to PVS-60-TL(-R)-US and the count/model detail is fine; 'cannot be replaced' matches 'not replaceable'. Minor variant naming (-R) is the only gap.
-->
