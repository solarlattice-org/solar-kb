---
id: role:utility-approval
type: Role
name: Utility approver
aliases:
- grid operator approval
- network operator approval
- responsible grid operator
- electrical network operator
category: Roles
role_kind: role
---
The utility approver is the responsible grid operator, and it must agree before anyone changes an inverter's grid-relevant parameters. If an inverter often logs event 501 (grid frequency out of range, inverter disconnected), first check how often the frequency fluctuates. Then ask the grid operator for approval to change the operating parameters. The grid operator only gives approval. Once it agrees, the parameter changes themselves are discussed with the manufacturer's Service team. On SMA equipment, the personal SMA Grid Guard code is also required before grid-related parameters can be changed. This code is separate from the utility's approval. Enphase microinverters must not be connected to the grid or have their AC circuits energized until installation is finished and the electrical network operator has approved. Some Solis settings are reserved for grid operators. Do not change them unless you are specifically told to.

<!-- review notes
- sentence 4: support check: partial - Passages show the Grid Guard code is needed for utility-grid-related parameters, but don't state it is separate from utility approval, though both are listed as requirements.
-->
