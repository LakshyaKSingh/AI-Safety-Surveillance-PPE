AI-Based Safety Surveillance Vision Model

Context-Aware PPE Compliance with Identity Binding

1. Project Overview

This project presents a prototype AI-based safety surveillance system designed to monitor Personal Protective Equipment (PPE) compliance on construction and industrial sites.

Unlike conventional CCTV or single-frame PPE detection systems, this solution focuses on:

Continuous worker tracking

Context-aware safety enforcement

Violation duration reasoning

Employee-level accountability through QR-based identity binding

The system is designed as a foundation prototype, with scope for further enhancement, optimization, and large-scale deployment.

2. Problem Being Addressed

Manual safety monitoring on worksites is:

Reactive and inconsistent

Difficult to scale across large areas

Lacking in worker-level accountability

Existing AI solutions often detect PPE visually but fail to:

Track violations over time

Identify the responsible employee

Generate audit-ready evidence

This project addresses these gaps through AI vision + rule-based reasoning + identity binding.

3. Approach Summary

The system follows a pipeline-based approach:

Video Input

Recorded CCTV or site footage (prototype stage)

Worker Detection & Tracking

Detects workers and assigns persistent tracking IDs across frames

Identity Binding (Entry Point)

QR code on helmet scanned at entry gate

Employee ID mapped to tracking ID for the shift

PPE Detection

Detects required PPE such as helmet, vest, gloves, goggles, boots

Harness compliance enforced via context rules

Context-Aware Safety Rules

PPE requirements vary by work zone (general, height, machinery)

Violation Reasoning

Violations evaluated based on duration, not single frames

Severity classified to reduce false alerts

Outputs

Annotated video

Violation snapshots

Compliance logs and summaries

4. Project Structure
ppe_safety_surveillance/
│
├── data/
│   ├── videos/          # Input videos
│   └── logs/            # Generated violation logs
│
├── models/
│   └── ppe_yolo.pt      # Trained / placeholder PPE model
│
├── src/
│   ├── detector.py     # Person & PPE detection
│   ├── zones.py        # Zone definitions
│   ├── violation.py    # Violation duration logic
│   ├── qr_bind.py      # QR-based employee ID binding (planned)
│   └── main.py         # Main pipeline runner
│
├── requirements.txt
└── README.md


The codebase is modular by design, allowing each component to be improved independently.

5. Setup Instructions
Prerequisites

Python 3.8+

pip package manager

Installation
git clone https://github.com/<your-username>/AI-Safety-Surveillance-PPE
cd AI-Safety-Surveillance-PPE
pip install -r requirements.txt

Required Libraries

Ultralytics (YOLO)

OpenCV

NumPy

Pandas

6. Usage Guidelines

Place a sample video inside:

data/videos/input.mp4


Run the prototype:

cd src
python main.py


The system will:

Detect and track workers

Simulate PPE violation timing

Display annotated video output

Prepare structured logs (prototype stage)

7. Current Prototype Capabilities

✅ Worker detection and multi-frame tracking
✅ Violation duration tracking
✅ Context-aware enforcement logic (zone-based)
✅ Structured system architecture

8. Features Under Development

The following components are planned and partially implemented, and will be extended further:

Full PPE multi-class detection tuning

Robust QR-based employee ID binding at entry gates

Automated violation snapshot capture

Role-based compliance reports (Supervisor / Manager / HR)

Performance optimization for edge deployment

This prototype serves as a proof of concept for the complete system.

9. Ethical & Privacy Considerations

No facial recognition is used

Identity binding is performed only via QR codes at controlled entry points

Data access is intended to be role-based and compliance-focused

10. Conclusion

This project demonstrates a practical, industry-aligned approach to AI-based safety surveillance by moving beyond basic detection toward accountability, context awareness, and actionable intelligence.

The current implementation represents a foundation prototype, designed to be further developed into a scalable, production-grade safety enforcement system.