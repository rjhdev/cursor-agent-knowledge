# Google Site Reliability Engineering Book

Reference catalog for [*Site Reliability Engineering: How Google Runs Production Systems*](https://sre.google/sre-book/table-of-contents/) (O'Reilly, 2017). Use this file to locate the right chapter when working on reliability, operations, incident response, or production engineering tasks.

Published by Google under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Full text is free online at [sre.google/sre-book](https://sre.google/sre-book/table-of-contents/).

## Key facts

- SRE applies software engineering to operations problems; reliability is a feature, not an afterthought
- The book replaces the traditional dev/ops split with shared ownership of production systems
- Part II (Principles) covers foundational concepts: risk, SLOs, toil, monitoring, automation, release engineering, simplicity
- Part III (Practices) covers day-to-day operations: alerting, on-call, incidents, postmortems, testing, and system design patterns
- Part IV (Management) covers team structure, interrupts, operational overload, and SRE engagement models
- Appendices include availability math, production best practices, and example incident/postmortem/launch templates
- "Hope is not a strategy" — systems require deliberate design and operation at scale
- Error budgets connect reliability targets (SLOs) to release velocity; they balance innovation against stability
- Toil is manual, repetitive, automatable work that scales linearly with service growth and should be eliminated
- Postmortem culture treats failures as learning opportunities; blameless analysis is a core SRE practice

## When to read which chapter

| Task or question | Start here |
|----------------|------------|
| Define reliability targets, SLIs, SLOs, error budgets | [Ch. 4 — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) |
| Reduce manual ops work | [Ch. 5 — Eliminating Toil](https://sre.google/sre-book/eliminating-toil/) |
| Design monitoring and alerting | [Ch. 6 — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/), [Ch. 10 — Practical Alerting](https://sre.google/sre-book/practical-alerting/) |
| On-call, incidents, postmortems | [Ch. 11–16](https://sre.google/sre-book/being-on-call/) |
| Cascading failures, overload, load balancing | [Ch. 19–22](https://sre.google/sre-book/load-balancing-frontend/) |
| Launch coordination | [Ch. 27](https://sre.google/sre-book/reliable-product-launches/), [Appendix E — Launch Checklist](https://sre.google/sre-book/launch-checklist/) |
| SRE team onboarding and engagement | [Ch. 28–32](https://sre.google/sre-book/accelerating-sre-on-call/) |
| Availability calculations | [Appendix A — Availability Table](https://sre.google/sre-book/availability-table/) |

## Table of contents

### Front matter

| Section | URL |
|---------|-----|
| Foreword | https://sre.google/sre-book/foreword/ |
| Preface | https://sre.google/sre-book/preface/ |

### Part I — Introduction

| Ch. | Title | URL |
|-----|-------|-----|
| 1 | Introduction | https://sre.google/sre-book/introduction/ |
| 2 | The Production Environment at Google, from the Viewpoint of an SRE | https://sre.google/sre-book/production-environment/ |

### Part II — Principles

| Ch. | Title | URL |
|-----|-------|-----|
| 3 | Embracing Risk | https://sre.google/sre-book/embracing-risk/ |
| 4 | Service Level Objectives | https://sre.google/sre-book/service-level-objectives/ |
| 5 | Eliminating Toil | https://sre.google/sre-book/eliminating-toil/ |
| 6 | Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ |
| 7 | The Evolution of Automation at Google | https://sre.google/sre-book/automation-at-google/ |
| 8 | Release Engineering | https://sre.google/sre-book/release-engineering/ |
| 9 | Simplicity | https://sre.google/sre-book/simplicity/ |

### Part III — Practices

| Ch. | Title | URL |
|-----|-------|-----|
| 10 | Practical Alerting | https://sre.google/sre-book/practical-alerting/ |
| 11 | Being On-Call | https://sre.google/sre-book/being-on-call/ |
| 12 | Effective Troubleshooting | https://sre.google/sre-book/effective-troubleshooting/ |
| 13 | Emergency Response | https://sre.google/sre-book/emergency-response/ |
| 14 | Managing Incidents | https://sre.google/sre-book/managing-incidents/ |
| 15 | Postmortem Culture: Learning from Failure | https://sre.google/sre-book/postmortem-culture/ |
| 16 | Tracking Outages | https://sre.google/sre-book/tracking-outages/ |
| 17 | Testing for Reliability | https://sre.google/sre-book/testing-reliability/ |
| 18 | Software Engineering in SRE | https://sre.google/sre-book/software-engineering-in-sre/ |
| 19 | Load Balancing at the Frontend | https://sre.google/sre-book/load-balancing-frontend/ |
| 20 | Load Balancing in the Datacenter | https://sre.google/sre-book/load-balancing-datacenter/ |
| 21 | Handling Overload | https://sre.google/sre-book/handling-overload/ |
| 22 | Addressing Cascading Failures | https://sre.google/sre-book/addressing-cascading-failures/ |
| 23 | Managing Critical State: Distributed Consensus for Reliability | https://sre.google/sre-book/managing-critical-state/ |
| 24 | Distributed Periodic Scheduling with Cron | https://sre.google/sre-book/distributed-periodic-scheduling/ |
| 25 | Data Processing Pipelines | https://sre.google/sre-book/data-processing-pipelines/ |
| 26 | Data Integrity: What You Read Is What You Wrote | https://sre.google/sre-book/data-integrity/ |
| 27 | Reliable Product Launches at Scale | https://sre.google/sre-book/reliable-product-launches/ |

### Part IV — Management

| Ch. | Title | URL |
|-----|-------|-----|
| 28 | Accelerating SREs to On-Call and Beyond | https://sre.google/sre-book/accelerating-sre-on-call/ |
| 29 | Dealing with Interrupts | https://sre.google/sre-book/dealing-with-interrupts/ |
| 30 | Embedding an SRE to Recover from Operational Overload | https://sre.google/sre-book/operational-overload/ |
| 31 | Communication and Collaboration in SRE | https://sre.google/sre-book/communication-and-collaboration/ |
| 32 | The Evolving SRE Engagement Model | https://sre.google/sre-book/evolving-sre-engagement-model/ |

### Part V — Conclusions

| Ch. | Title | URL |
|-----|-------|-----|
| 33 | Lessons Learned from Other Industries | https://sre.google/sre-book/lessons-learned/ |
| 34 | Conclusion | https://sre.google/sre-book/conclusion/ |

### Appendices

| Appendix | Title | URL |
|----------|-------|-----|
| A | Availability Table | https://sre.google/sre-book/availability-table/ |
| B | A Collection of Best Practices for Production Services | https://sre.google/sre-book/service-best-practices/ |
| C | Example Incident State Document | https://sre.google/sre-book/incident-document/ |
| D | Example Postmortem | https://sre.google/sre-book/example-postmortem/ |
| E | Launch Coordination Checklist | https://sre.google/sre-book/launch-checklist/ |
| F | Example Production Meeting Minutes | https://sre.google/sre-book/production-meeting/ |

### Back matter

| Section | URL |
|---------|-----|
| Bibliography | https://sre.google/sre-book/bibliography/ |

## Common issues

- **Need SLO guidance but only have the TOC** → Fetch [Ch. 4](https://sre.google/sre-book/service-level-objectives/) for SLI/SLO/error-budget definitions and examples
- **Incident response playbook missing** → Use [Ch. 13–15](https://sre.google/sre-book/emergency-response/) plus [Appendix C](https://sre.google/sre-book/incident-document/) and [Appendix D](https://sre.google/sre-book/example-postmortem/) as templates
- **Alert fatigue** → [Ch. 10](https://sre.google/sre-book/practical-alerting/) covers actionable alerting; pair with [Ch. 6](https://sre.google/sre-book/monitoring-distributed-systems/) on monitoring philosophy
- **Service degrading under load** → [Ch. 21–22](https://sre.google/sre-book/handling-overload/) on overload and cascading failures
- **Ops team overwhelmed** → [Ch. 5](https://sre.google/sre-book/eliminating-toil/) on toil and [Ch. 30](https://sre.google/sre-book/operational-overload/) on operational overload recovery

## References

- [Table of Contents](https://sre.google/sre-book/table-of-contents/) — canonical index for all chapters
- [Google SRE books hub](https://sre.google/books/) — also includes *The Site Reliability Workbook* and *Building Secure and Reliable Systems*
- O'Reilly Media, 2017 — print edition
