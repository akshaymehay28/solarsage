# Long-Term Degradation Mechanisms: LID, LETID and Ageing

Crystalline silicon modules typically degrade 0.4-0.7% per year; warranties
commonly guarantee 80-87% of nameplate after 25-30 years. Understanding which
mechanism is active matters because some are recoverable and some are not.

## Light-induced degradation (LID)

Classic LID affects boron-doped p-type silicon: boron-oxygen complexes form
under initial light exposure and reduce carrier lifetime. It causes a 1-3%
power drop in the first days to weeks of operation, then stabilises.
Commissioning tests done before stabilisation will overstate later "losses" -
baseline after the LID settles.

## LeTID (light and elevated temperature induced degradation)

LeTID affects PERC cells and progresses over months to years at operating
temperatures, with losses that can reach 3-6% before a slow recovery phase.
It shows up in fleet data as multi-year degradation faster than warranty
curves, especially in hot climates. Modern cell processes mitigate it;
suspected LeTID should be confirmed with lab flash-testing of sample modules.

## Other mechanisms

Solder-joint fatigue from daily thermal cycling raises series resistance,
visible as fill-factor decline in IV traces. Metallisation corrosion,
accelerated by moisture ingress and encapsulant breakdown, does the same.
Glass anti-reflective coating degradation reduces current slightly. Junction
box adhesive failures can admit water, causing abrupt failures late in life.

## Separating degradation from other losses

Degradation is slow, monotonic, and does not recover after rain or cleaning.
Trend the temperature-corrected performance ratio over years; a step change
is a fault, an accelerating drift in a PERC fleet suggests LeTID, and a
steady 0.5%/year is normal ageing.
