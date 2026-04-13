# Solar Cell I-V Characteristics Experiment Report

## 1. Objective

1. Understand the working principle of solar cells
2. Measure I-V characteristics under different configurations
3. Determine key parameters: Isc, Uoc, Pm, FF, and η

## 2. Principle

A solar cell converts light energy to electrical energy via the photovoltaic effect in a p-n junction. The I-V relationship is described by:

I = Iph - I₀[exp(qU/nkT) - 1] - U/Rsh

Key parameters:
- Short-circuit current Isc: current at U = 0
- Open-circuit voltage Uoc: voltage at I = 0
- Maximum power Pm = max(U × I)
- Fill factor FF = Pm / (Isc × Uoc)
- Efficiency η = Pm / (Pin × A)

## 3. Apparatus

- Solar cell module (4 cells, each ~5.55 cm × 5.95 cm)
- Tungsten-halogen lamp
- Variable load resistance
- Digital voltmeter and ammeter

## 4. Data and Analysis

Cell area: A = 4 × 5.55 × 5.95 = 132.09 cm²

Irradiance: 72 mW/cm² at 80 cm, 131 mW/cm² at 60 cm

### Config 1: 80 cm, Series, 0°

| U/V | 0 | 2.0 | 4.0 | 6.0 | 7.0 | 8.0 | 9.0 | 9.5 | 10.0 | 10.5 | 11.0 | 11.5 | 12.0 | 12.5 | 13.0 | 13.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I/mA | 27.2 | 27.2 | 27.0 | 26.8 | 26.4 | 26.1 | 25.3 | 24.2 | 23.2 | 21.8 | 19.5 | 16.6 | 12.5 | 7.5 | 2.3 | 0 |

Isc = 27.2 mA, Uoc = 13.5 V, Pm = 232.0 mW (at 10.0 V)
FF = 232.0 / (27.2 × 13.5) = 0.632
η = 232.0 / (72 × 132.09) = 2.44%

### Config 2: 60 cm, Parallel, 0°

| U/V | 0 | 0.2 | 0.5 | 0.8 | 1.0 | 1.2 | 1.5 | 1.8 | 2.0 | 2.2 | 2.4 | 2.6 | 2.8 | 3.0 | 3.2 | 3.36 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I/mA | 181.8 | 181.6 | 181.0 | 180.0 | 179.2 | 177.6 | 174.5 | 170.0 | 165.0 | 157.0 | 143.0 | 120.0 | 88.0 | 50.0 | 13.2 | 0 |

Isc = 181.8 mA, Uoc = 3.36 V, Pm = 345.4 mW (at 2.2 V)
FF = 345.4 / (181.8 × 3.36) = 0.565
η = 345.4 / (131 × 132.09) = 2.00%

### Config 3: 60 cm, Series, 30°

| U/V | 0 | 2.0 | 4.0 | 6.0 | 7.0 | 8.0 | 9.0 | 9.5 | 10.0 | 10.5 | 11.0 | 11.5 | 12.0 | 12.5 | 13.0 | 13.46 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I/mA | 38.7 | 38.5 | 38.3 | 37.8 | 37.4 | 36.9 | 35.8 | 34.8 | 33.5 | 31.3 | 28.0 | 23.4 | 17.2 | 9.8 | 2.3 | 0 |

Isc = 38.7 mA, Uoc = 13.46 V, Pm = 328.7 mW (at 10.5 V)
FF = 328.7 / (38.7 × 13.46) = 0.631
η = 328.7 / (131 × cos30° × 132.09) = 2.19%

### Summary Table

| Config | Distance | Topology | Angle | Isc/mA | Uoc/V | Pm/mW | FF | η/% |
|---|---|---|---|---|---|---|---|---|
| 1 | 80 cm | Series | 0° | 27.2 | 13.5 | 232.0 | 0.632 | 2.44 |
| 2 | 60 cm | Parallel | 0° | 181.8 | 3.36 | 345.4 | 0.565 | 2.00 |
| 3 | 60 cm | Series | 30° | 38.7 | 13.46 | 328.7 | 0.631 | 2.19 |

### Comparison

Series connection yields higher voltage (13.5 V) while parallel yields higher current (181.8 mA). The fill factor for series (0.632) is better than parallel (0.565) due to reduced mismatch losses. Increasing the angle of incidence to 30° reduces Isc according to the cosine law.

## 5. Figures

See generated plots:
1. `solar_IV_curves.png` — I-V curves for all three configurations
2. `solar_PV_curves.png` — P-V curves with maximum power points marked

## 6. Discussion

1. The fill factor cannot reach 1 because the exponential I-V characteristic of the p-n junction prevents a rectangular curve shape. Series and shunt resistances further reduce FF.
2. Efficiency can be improved through anti-reflection coatings, optimized junction depth, reduced series resistance, and multi-junction designs.

## 7. Error Analysis

1. Voltmeter/ammeter reading precision (±1 digit)
2. Lamp intensity fluctuation during measurements
3. Temperature rise during extended measurements affects Uoc and Isc
4. Irradiance calibration uncertainty propagates to η

## 8. Conclusion

This experiment characterized solar cell I-V behavior under three configurations. Series connection maximized voltage output, parallel maximized current, and the 30° incidence angle reduced effective irradiance. All configurations showed efficiencies around 2.0-2.4% with fill factors of 0.56-0.63.

## References

1. SJTU Physics Experiment Center, University Physics Experiment Manual
