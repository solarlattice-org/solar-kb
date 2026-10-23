---
id: comp:ac-disconnect
type: Component
name: AC disconnection unit
aliases:
- AC switch
- AC breaker
- AC disconnect Switch
- Load rated AC switch
---
The AC disconnection unit separates the inverter's AC output from the medium voltage transformer or grid; it can be opened by hand and in central inverters it also opens automatically when residual current is detected. It is a separate part from the AC contactor, which handles routine automatic disconnection between inverter and transformer. On SMA Sunny Central inverters the ABB unit has three handle positions: on means closed, the central position means it tripped and is open, and off means open. SMA reports event 7706 when the unit is open or has tripped and event 7707 when its switching status is faulty; in both cases the fix is to contact SMA service. On Huawei string inverters an AC switch left off or an open AC circuit raises the Grid Loss alarm 2032, so check that the AC cable is connected and the switch is ON. Yaskawa Solectria central inverters can be fitted with a shunt trip, where a remote 24 V DC signal energizes a solenoid that opens the AC breaker; after a trip the handle must be turned to OFF before the breaker can be reset by hand. If the 24 V signal is applied to the shunt trip terminals without the option installed, the inverter stops producing power, and a shunt trip event may only appear in the log after the inverter is powered again. Smaller string inverters use a built-in, lockable, load-rated AC switch to disconnect the AC output.

<!-- review notes
- sentence 5: support check: partial - Alarm 2032 Grid Loss lists a disconnected AC circuit or AC switch off as causes and the check measure, but it also arises from grid outage, and 'string inverters' is not stated.
- sentence 7: support check: partial - Inverter stopping when 24 V is applied without the option is stated, but the log note refers to an actual shunt trip event, not specifically the no-option case.
- sentence 8: support check: partial - A built-in lockable AC disconnect switch and load-rated AC switch appear, but 'smaller string inverters' as a general class is not stated.
- sentence 1: review: partial - The passages back manual disconnection and automatic opening on residual current between inverter and MV transformer, but 'or grid' and the claim that this applies to central inverters in general are not stated (the source covers only the SMA Sunny…
- sentence 7: review: partial - The passage states that applying 24V without the option installed stops power production, but its log note is about a real shunt trip event (the inverter loses power), not the case where the option is missing.
-->
