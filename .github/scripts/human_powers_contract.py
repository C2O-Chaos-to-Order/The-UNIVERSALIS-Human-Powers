#!/usr/bin/env python3
"""Validate shared Human Powers consent, approval, accessibility and augmentation contracts."""
import copy,json,sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2]
SCHEMA=json.loads((ROOT/"schemas/human-powers/human-authority-contracts.v1.schema.json").read_text())
FIX=json.loads((ROOT/"examples/human_powers/human-authority-contracts.v1.json").read_text())
KEYS={"consent_graph":"consentGraph","consent_label_join":"consentLabelJoin","human_approval_receipt":"humanApprovalReceipt","accessibility_evidence_pack":"accessibilityEvidencePack","sovereignty_profile":"sovereigntyProfile","augmentation_device_profile":"augmentationDeviceProfile","augmentation_action_record":"augmentationActionRecord","consent_revocation_event":"consentRevocationEvent","data_subject_rights_request":"dataSubjectRightsRequest","hardware_control_profile":"hardwareControlProfile","ems_action_record":"emsActionRecord"}
def valid(k,obj):
 s={"$schema":SCHEMA["$schema"],"$ref":"#/$defs/"+KEYS[k],"$defs":SCHEMA["$defs"]}
 Draft202012Validator.check_schema(s); Draft202012Validator(s).validate(obj)
 if k=="human_approval_receipt" and obj.get("fixture_only") and obj.get("signature",{}).get("verified_status")=="verified":
  raise ValueError("fixture-only approval signature cannot be marked verified")
 if k=="ems_action_record" and obj.get("decision")=="allow":
  if obj.get("hardware_interlock_state") not in {"engaged","device-authorized"} or not obj.get("human_approval_ref") or not obj.get("emergency_stop_available"):
   raise ValueError("EMS allow requires a verified hardware-safe state, human approval and available emergency stop")

def expr_ok(expr,active):
 if expr["kind"]=="grant-ref": return expr["grant_ref"] in active
 values=[expr_ok(v,active) for v in expr["children"]]
 return all(values) if expr["kind"]=="all-of" else any(values)
def main():
 for k in KEYS: valid(k,FIX[k])
 assert expr_ok({"kind":"all-of","children":[{"kind":"grant-ref","grant_ref":"g1"},{"kind":"grant-ref","grant_ref":"g2"}]},{"g1","g2"})
 assert not expr_ok({"kind":"all-of","children":[{"kind":"grant-ref","grant_ref":"g1"},{"kind":"grant-ref","grant_ref":"g2"}]},{"g1"})
 assert expr_ok({"kind":"any-of","children":[{"kind":"grant-ref","grant_ref":"g1"},{"kind":"grant-ref","grant_ref":"g2"}]},{"g2"})
 j=FIX["consent_label_join"]; assert set(j["left_restrictions"])|set(j["right_restrictions"])<=set(j["joined_restrictions"])
 assert FIX["human_approval_receipt"]["signature"]["verified_status"]=="not-verified"
 assert FIX["augmentation_action_record"]["decision"]=="deny"
 assert FIX["ems_action_record"]["decision"]=="deny" and FIX["hardware_control_profile"]["hardware_interlock_required"] is True
 neg=[]
 x=copy.deepcopy(FIX); x["consent_label_join"]["joined_restrictions"]=[]; neg.append(("monotonic restriction join","consent_label_join",x))
 x=copy.deepcopy(FIX); x["human_approval_receipt"]["decision"]="maybe"; neg.append(("approval outcome enum","human_approval_receipt",x))
 x=copy.deepcopy(FIX); x["human_approval_receipt"]["signature"]["verified_status"]="verified"; neg.append(("fixture signature must be unverified","human_approval_receipt",x))
 x=copy.deepcopy(FIX); x["accessibility_evidence_pack"]["standard"]="WCAG-2.3"; neg.append(("accessibility standard version","accessibility_evidence_pack",x))
 x=copy.deepcopy(FIX); x["augmentation_device_profile"]["hardware_interlock_required"]=False; neg.append(("hard interlock requirement","augmentation_device_profile",x))
 x=copy.deepcopy(FIX); x["augmentation_action_record"]["emergency_stop_available"]=False; neg.append(("emergency stop requirement","augmentation_action_record",x))
 x=copy.deepcopy(FIX); x["consent_graph"]["grants"][0]["mode"]="unrestricted"; neg.append(("consent grant mode","consent_graph",x))
 x=copy.deepcopy(FIX); x["sovereignty_profile"]["data_control"]["storage_control"]="unknown-value"; neg.append(("data control enum","sovereignty_profile",x))
 x=copy.deepcopy(FIX); x["consent_revocation_event"]["propagation_status"]="done"; neg.append(("revocation state enum","consent_revocation_event",x))
 x=copy.deepcopy(FIX); x["data_subject_rights_request"]["request_type"]="erase-all-now"; neg.append(("data-subject request type","data_subject_rights_request",x))
 x=copy.deepcopy(FIX); x["hardware_control_profile"]["watchdog_required"]=False; neg.append(("watchdog required","hardware_control_profile",x))
 x=copy.deepcopy(FIX); x["ems_action_record"]["emergency_stop_available"]=False; neg.append(("EMS emergency stop","ems_action_record",x))
 x=copy.deepcopy(FIX); x["ems_action_record"]["decision"]="allow"; x["ems_action_record"]["hardware_interlock_state"]="unknown"; neg.append(("EMS allow cannot bypass unknown interlock","ems_action_record",x))
 for label,k,obj in neg:
  try: valid(k,obj)
  except Exception: continue
  raise AssertionError("negative case passed: "+label)
 print(f"PASS: {len(KEYS)} positive contract fixtures, provenance algebra and {len(neg)} negative cases")
 print("LIMIT: no live consent store, identity wallet, signature verification, accessibility audit, legal compliance or device actuation")
if __name__=="__main__":
 try: main()
 except Exception as e: print("FAIL:",e,file=sys.stderr); raise SystemExit(1)
