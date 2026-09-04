# PRINT EXPERIMENT PROTOCOL v1.0

Status: DRAFT
Date: 2026-09-04
Truth level: PROVISIONAL

## Purpose

Physical experiments convert assumptions into measured manufacturing rules. CAPICAPI must prefer its own measured machine data over internet anecdotes.

## Entry Conditions

Do not begin physical testing until:

- Capi v0 has passed digital DFM review.
- Palette is frozen.
- Required filament is purchased.
- Slicer profiles are documented.
- Test record schema is ready.
- Operator agrees to measure real outputs.

## Size And Quality Matrix

Test sizes:

- 40 mm
- 50 mm
- 60 mm

Test layer heights:

- 0.08 mm
- 0.12 mm
- 0.16 mm

Quality judgment must include blind perceived-quality comparison. Do not assume 0.08 mm is the production standard.

## Batching Matrix

After a candidate size/layer combination is promising, test:

- 1 unit
- 5 units
- 10 units
- maximum practical plate

## Required Measurements

Record real values:

- finished product weight
- purge waste
- prime tower material
- failed material
- total filament
- actual print time
- units per printer-hour
- filament cost
- electricity estimate
- operator labor time
- cost per unit
- visible defects
- failure cause

Unknown values are not estimates unless explicitly marked `ESTIMATED`.

## Slicer Estimate Comparison

For every physical test, record:

- slicer estimated time
- actual elapsed print time
- slicer estimated material
- actual measured material
- variance notes

## Blind Quality Comparison

Procedure:

- Label samples with neutral test IDs.
- Hide layer height from reviewers.
- Compare perceived quality, face readability, accessory readability, surface defects, and overall sellability.
- Record reviewer notes separately from measured print metrics.

## Pass Criteria

A manufacturing setting can pass only when:

- support-free print succeeds
- face and core details are readable
- fragile parts survive handling
- actual print time is acceptable relative to perceived quality
- waste data is recorded
- cost inputs are traceable

## Open Risks

- The best-looking sample may be too slow for production.
- The fastest sample may reduce perceived collectible quality.
- Batching may increase failure impact even if it improves throughput.
