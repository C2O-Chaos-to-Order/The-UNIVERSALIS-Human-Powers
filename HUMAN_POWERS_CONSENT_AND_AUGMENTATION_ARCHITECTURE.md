# Human Powers Consent, Oversight and Augmentation Toolchain — UNIVERSALIS

**Owner:** The UNIVERSALIS Human Powers repository  
**Boundary:** Public, open, local-first, independently operated  
**Status:** Portable contract foundation; external integrations and physical-device adapters remain candidates  
**Taxonomy:** Existing `Human_Powers.md` H-P-01–H-P-12 remains canonical and unchanged

## Architectural position

Human authority is an external, first-class boundary. A human's consent, refusal, withdrawal, rights, accessibility needs and ability to override are not inferred from an agent's reasoning or software capability declaration. Human powers include informational, computational, physical, resource, economic, organizational, institutional, social, creative, protective, delegated and self-governance dimensions. The existing taxonomy remains the concept source of truth.

## Open candidate inventory

### Human-in-the-loop and oversight
Magentic-UI; hitl-mcp-server; clarify-mcp; mcp-feedback-enhanced; human-in-the-loop-mcp; gotoHuman; ReadyAgents Core; SemaClaw; AG2; Open Computer Agent v2.0.

### Consent, sovereignty and privacy
agentgov; consent-mcp; consentgraph; levain; @at1c/sdk; @weave_protocol/domere; SovereignOS; CapAuth; Anuma; doxx.net; RAI Manifesto / Digital DNA. No central UNIVERSALIS consent authority is required.

### Accessibility and inclusion
a11y-toolkit; mcp-axe; @webability/mcp; playwright-accessibility-mcp-server; axe-scanner-mcp; Morae. The earlier Human Capabilities source described 32 a11y-toolkit tools while this source says 31. Preserve this source/version discrepancy; tool count is not acceptance evidence.

### Human augmentation
OpenExo; CEINMS-RT; Human Operator; body-powered supernumerary robotic finger. These are hardware, control and human-interface candidates, not software authority systems. No live actuation or medical/rehabilitation claim is established by a schema.

All named third-party projects remain candidates until canonical identity, license, maintainer, version, security, accessibility, privacy and reproducibility checks are complete.

## Shared portable contracts

- Consent graph and grant records using opaque subject and principal references.
- Consent-label join algebra: combining restrictions cannot reduce the restrictions of either input.
- Provenance expression using all-of / any-of branches, so withdrawal and correction propagation can be independently evaluated without exporting a private consent store.
- Human-approval receipt bound to one approver, requesting agent, action, target, purpose, scope, evidence, time window, nonce, signature and trust reference.
- Accessibility evidence pack with WCAG 2.2 criterion-level evidence, assessment method, limitations and human review/countersign state.
- Sovereignty profile using a portable credential or native record with subject-controlled data preferences and export/revocation references.
- Augmentation device/action evidence records linked to a device-specific safety case, calibration, hardware interlock, emergency-stop test, wearer consent and action-specific approval.

The shared contracts use opaque references and hashes. They do not publish human names, private consent-store contents, personal data, C2O signing keys or C2O authority tokens.

## Consent and approval semantics

- Human-originated consent is explicit, purpose-bound, action-bound, resource-bound, time-bound and revocable.
- Delegated authority is non-amplifying: an agent cannot grant more scope than the human granted.
- Restrictions compose monotonically; the v1 example uses set union of restriction labels.
- Provenance `all-of` requires every parent grant; `any-of` requires at least one valid alternative. Revocation requires dependent decisions to be recomputed against that expression.
- Veto wins: any applicable prohibition or denial blocks the action.
- Approval is action-specific and expires; a prior approval does not authorize a different action or changed target.
- A signature proves integrity and signer possession only. It does not prove understanding, voluntariness, or legal sufficiency.

## Accessibility and augmentation boundaries

Automated scanners cover only testable subsets of accessibility criteria. A passing automated scan is not a WCAG conformance determination. Human review, assistive-technology testing and representative user testing remain necessary. Evidence packs record methods, criteria, results, limitations and reviewer state instead of asserting blanket compliance.

Physical augmentation records are evidence contracts only. They require a validated device-specific safety case, calibration, hardware interlock, tested emergency stop, wearer consent and human operator oversight. A software policy must never override a hardware safety interlock. This repository does not command, test, prescribe or validate a live exoskeleton, EMS system, wearable robot or assistive device.

## Current implementation and limits

The shared schemas, synthetic fixtures and semantic checks provide a basic portable record model. They do not deploy a consent service, identity wallet, signing service, DSAR service, accessibility auditor, device driver or augmentation control loop. Signature verification, proof of understanding, revocation propagation service and actual device safety validation remain outstanding.

## Source verification and caveats

- AT1C current public repository states its SDK uses ML-DSA-65 and has retired Ed25519; receipt verification must be algorithm-agile and pin exact verifier policy: https://github.com/at1c-protocol/at1c-protocol-official
- WCAG 2.2 is the accessibility evaluation reference; automated reports alone do not establish conformance.
- The number of a11y-toolkit MCP tools differs across the supplied inventory versions (31 vs 32); do not present either count as verified until a specific release is pinned and inspected.
