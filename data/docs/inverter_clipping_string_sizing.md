# Inverter Clipping and DC/AC Ratio

## What clipping is

Most plants are built with more DC module capacity than inverter AC rating -
DC/AC ratios of 1.1 to 1.4 are typical. When the array's available DC power
exceeds the inverter's AC limit, the inverter operates off the maximum power
point and "clips" output at its rating. In monitoring data this appears as a
flat-topped power curve on clear days around solar noon.

## Deliberate vs problematic clipping

Some clipping is an economic optimum: it costs a small percentage of summer
noon energy while allowing more generation in mornings, evenings, and winter.
Expected clipping loss should be modelled at design time; measured clipping
matching the model is not a fault.

Problematic clipping appears when the flat top starts lower than the inverter
rating - that is derating, not design clipping. Common causes: high ambient
temperature triggering thermal derating (check cooling), grid voltage near
limits forcing the inverter to curtail, or an incorrectly configured export
limit. Distinguish by comparing the clip level with the inverter's rated AC
output and its event log.

## Interaction with fault detection

Clipping confuses naive ML fault detectors because power stops tracking
irradiance for hours at a time. Either include the inverter AC limit as a
model feature, cap the model's target at the plant's AC rating, or exclude
clipped periods from residual-based fault scoring. A fault detector that
flags every sunny noon as anomalous has almost certainly not accounted
for clipping.
