# Monitoring Alarm Triage

A utility-scale plant can raise hundreds of alarms a day; the operational
skill is turning that stream into a short, correctly ordered work list.

## Triage order

Safety and equipment-protection alarms come first: ground fault, arc fault,
transformer and switchgear alarms, and repeated inverter protective trips.
Next, availability: whole-inverter or feeder outages, ranked by lost
kilowatts. Then performance: string-level underperformance, tracker
mistracking, sensor disagreement. Communication losses ride last unless they
blind the other categories - a site that has gone dark deserves escalation
because you cannot triage what you cannot see.

## De-duplication and root cause

One physical event fans out into many alarms: a grid disturbance trips every
inverter simultaneously (timestamps within seconds of each other are the
tell); a failed combiner drops several strings that alarm individually.
Group by time correlation and electrical hierarchy before dispatching - the
repair unit is the root cause, not the alarm count.

## Thresholds that stay useful

Static thresholds drift into noise: a fixed "string 10% low" rule fires
constantly in winter mornings and misses summer losses. Better practice is
peer comparison (string versus median of its combiner siblings under equal
conditions) and expected-value models built from weather data, with alarm
thresholds expressed in energy or revenue impact per day. Review alarm
statistics monthly: any rule generating alarms nobody acts on should be
retuned or retired - alarm fatigue is how real faults get missed.
