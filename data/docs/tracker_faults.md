# Solar Tracker Faults

Single-axis trackers raise energy yield 15-25% over fixed tilt but add
moving parts - motors, gearboxes, controllers, and position sensors - each
a new failure mode.

## Failure modes and signatures

A stalled tracker leaves its row at a fixed angle: output matches the fleet
at one moment of the day and diverges either side of it, producing a
distinctive skewed daily profile compared with neighbouring rows. A tracker
stuck flat loses morning and evening energy but looks normal at noon.
Controller communication loss may leave rows in their overnight stow
position - near-total loss that is obvious - or silently freeze tracking
mid-morning, which is subtler.

Position-sensor drift causes systematic mistracking: the row follows the sun
with a constant angular offset, costing a few percent continuously - hard to
see on any single day, visible when comparing row-level energy over weeks.

Backtracking misconfiguration (the algorithm that tilts rows to avoid
row-to-row shading at low sun) causes morning/evening losses across the
whole field that can be mistaken for soiling.

## Wind stow and weather response

Trackers protect themselves by stowing flat in high wind. Frequent stow
events appear as sudden fleet-wide flattening of output uncorrelated with
irradiance. Verify anemometer calibration if stow frequency seems high -
a failed wind sensor that reads high wastes energy in false stows; one that
reads low risks structural damage.

## Maintenance

Exercise rows through full range during commissioning and annually,
grease per schedule, verify row-position telemetry against a physical
inclinometer sample, and trend motor currents - rising drive current
precedes mechanical seizure.
