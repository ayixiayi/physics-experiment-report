# physics-experiment-report

An [OpenCode](https://github.com/nicepkg/opencode) agent skill for generating university physics experiment reports.

## What it does

Generates complete Chinese-language physics experiment reports (上海交通大学 template) from raw experimental data, including:

- Structured report with 实验目的、实验原理、数据处理、误差分析、思考题、总结
- Python plotting code (matplotlib) with scatter+fit overlays, residual analysis
- Linear/polynomial curve fitting with R² and fit equations
- Relative error (Er) calculations with numeric values in report text
- Sensitivity analysis, non-linearity assessment
- Discussion questions answered with physics reasoning

## Supported experiments

- 转动惯量 (Rotational Inertia)
- 波尔共振 (Bohl Resonance) — amplitude-frequency, phase-frequency, damping
- 温度传感器 (Temperature Sensors) — Pt100 & thermocouple comparison
- And other university physics labs (凯特摆, 霍尔传感器, 直流电桥, 落球法, etc.)

## Installation

Copy `SKILL.md` to your OpenCode skills directory:

```bash
cp SKILL.md ~/.config/opencode/skills/physics-experiment-report/SKILL.md
```

Or clone this repo:

```bash
git clone https://github.com/ayixiayi/physics-experiment-report.git ~/.config/opencode/skills/physics-experiment-report
```

## Benchmark results (Iteration 3)

| Config | Pass Rate |
|--------|-----------|
| with_skill | 100.0% |
| without_skill | 96.2% |
| **Delta** | **+3.8%** |

Tested across 3 experiments × 26 assertions.

## License

MIT
