from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import math

app = FastAPI(title="SAS Strategic Intelligence Engine v2.1 (The Architect Omniscience)")

# ปลดล็อค CORS สำหรับ Lovable / Canvas / หน้าบ้านทั้งหมด
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================================
# 🟢 PART 1: MASTER INPUT SCHEMA (45 ACTIVE SENSORS)
# =====================================================================
class WorldsGroup(BaseModel):
    world_1_objective: List[str]
    world_2_subjective: List[str]
    world_3_social: List[str]
    w1_obj_count: float
    w1_event_id: str
    w2_refraction: float
    w3_social_pressure: float
    power_relation_asymmetry: float

class Exchange4GGroup(BaseModel):
    get: float
    grow: float
    give: float
    gratitude: float
    exchange_friction: float
    grab_force: float

class StandardLineSyntaxGroup(BaseModel):
    wellbeing_index: float
    focus_presence: float
    focus_stability: float
    syntax_amplitude: float
    syntax_freq: float
    syntax_phase: str

class EnergyIIPGroup(BaseModel):
    intensity: float
    momentum: float
    energy_stability: float
    energy_momentum: float

class NeedsMaslowGroup(BaseModel):
    survival_safety: float
    social_esteem: float
    self_actualization: float
    fulfillment_pct: float
    maslow_layer: int

class ConditioningStackGroup(BaseModel):
    asava_attachment: float
    anusaya_force: float
    kilesa_active_trigger: float
    kilesa_type: str
    craving_intensity: float
    aversion_intensity: float

class IdentityDefenseGroup(BaseModel):
    ditthi_belief_rigidity: float
    mana_comparison_intensity: float
    atta_defense_active: bool
    id_threat_score: float
    belief_attachment: float
    ego_inflation: float
    identity_overlap: float
    defense_mech_id: str

class BehavioralForcesGroup(BaseModel):
    approach_drive: float
    avoidance_force: float
    neutral_drag: float
    internal_tension: float
    wisdom_level: float
    dominant_mode: str

class SMFFullInputSchema(BaseModel):
    worlds: WorldsGroup
    exchange_4g: Exchange4GGroup
    standard_line_syntax: StandardLineSyntaxGroup
    energy_iip: EnergyIIPGroup
    needs_maslow: NeedsMaslowGroup
    conditioning_stack: ConditioningStackGroup
    identity_defense: IdentityDefenseGroup
    behavioral_forces: BehavioralForcesGroup

# =====================================================================
# 🟠 PART 2: THE QUANTUM CALCULUS CORE (v2.1 LOGIC)
# =====================================================================
class SASLogicCoreV2:
    @staticmethod
    def calculate(raw: SMFFullInputSchema):
        w = raw.worlds
        ex = raw.exchange_4g
        syn = raw.standard_line_syntax
        en = raw.energy_iip
        ms = raw.needs_maslow
        cd = raw.conditioning_stack
        id_def = raw.identity_defense
        bf = raw.behavioral_forces

        # SIMULATED SEMANTIC LAYER
        text_weight = 1.0 + (0.05 * (len(w.world_1_objective) + len(w.world_2_subjective) + len(w.world_3_social)))

        # --- LAYER 1: ADVANCED COGNITIVE DISTORTION ---
        refraction_factor = 1.0 + (w.w2_refraction * 0.12) * (1.0 + (id_def.ditthi_belief_rigidity * 0.08))
        social_interference = w.w3_social_pressure * (1.0 + w.power_relation_asymmetry * 0.15)
        reality_gap = (refraction_factor * social_interference * text_weight) / (w.w1_obj_count + 1.0)

        # --- LAYER 2: DEEP PSYCHE VISCOSITY & AUTOPILOT ---
        kilesa_amplifier = 1.0 + (cd.kilesa_active_trigger * 0.1)
        asava_force_total = cd.asava_attachment * kilesa_amplifier
        viscosity = (asava_force_total + cd.anusaya_force) / (bf.wisdom_level + 1.0)
        
        total_desire_force = cd.craving_intensity + cd.aversion_intensity
        autopilot = (asava_force_total * total_desire_force) / (syn.focus_presence + 1.0)

        # --- LAYER 3: WAVE RESILIENCE & ENERGY DYNAMICS ---
        emotional_residue = (syn.syntax_amplitude * syn.syntax_freq) * 0.2 * (1.0 + en.intensity * 0.05)
        decay_rate = (emotional_residue + bf.internal_tension + bf.neutral_drag) / (syn.focus_stability + 1.0)

        # --- LAYER 4: IDENTITY DEFENSE & EGO TAX ---
        identity_multiplier = 1.0 + (id_def.identity_overlap * 0.05) + (id_def.id_threat_score * 0.08)
        ego_tax = (id_def.mana_comparison_intensity * w.w3_social_pressure * identity_multiplier) / (bf.wisdom_level + 1.0)
        
        deception_base = (id_def.belief_attachment * refraction_factor) + (id_def.ego_inflation * 0.5)
        if id_def.atta_defense_active or (id_def.defense_mech_id != "None" and id_def.defense_mech_id != ""):
            deception_base *= 2.0
        
        # --- LAYER 5: MASLOW EQUILIBRIUM & 4G SUSTAINABILITY ---
        maslow_stability_factor = (ms.survival_safety + ms.self_actualization) / 2.0
        if ms.survival_safety < 4.0:
            maslow_stability_factor *= 0.5

        lubricated_friction = ex.exchange_friction / (1.0 + (ex.gratitude * 0.6))
        exchange_health = (ex.grow + ex.give) - (ex.get + ex.grab_force * 0.5)
        
        # --- FINAL SYNTHESIS ---
        stability_base = syn.wellbeing_index * 1.5 + (maslow_stability_factor * 0.8) + (en.energy_stability * 0.5)
        tension_impact = (bf.avoidance_force + bf.approach_drive * 0.2 + lubricated_friction) * 0.5
        stability = (stability_base / (1.0 + tension_impact)) - (deception_base * 0.15) - (emotional_residue * 0.1) + (exchange_health * 0.1)

        # 🧠 LOCALIZATION MAP: แปลงคำศัพท์เชิงทฤษฎีให้เป็นมิตรกับผู้ใช้งานทั่วไป
        kilesa_map = {"Lobha": "Desire / Attachment", "Dosa": "Resistance / Anger", "Moha": "Confusion / Inattention"}
        defense_map = {"ISOLATION": "Social Detachment", "DENIAL": "Refusing Reality", "PROJECTION": "Blaming External Factors", "RATIONALIZATION": "Over-thinking"}
        mode_map = {"FIGHT": "Active Response", "FLIGHT": "Defensive Retreat", "FREEZE": "Stagnant Holding", "FAWN": "People Pleasing"}

        user_friendly_driver = kilesa_map.get(cd.kilesa_type, cd.kilesa_type if cd.kilesa_type else "Balanced State")
        user_friendly_shield = defense_map.get(id_def.defense_mech_id.upper(), id_def.defense_mech_id if id_def.defense_mech_id else "No Shield Active")
        user_friendly_persona = mode_map.get(bf.dominant_mode.upper(), bf.dominant_mode if bf.dominant_mode else "Adaptive Observation")

        return {
            "internal_metrics": {
                "stability": round(max(0.0, min(10.0, stability)), 2),
                "tension": round(max(0.0, min(10.0, bf.internal_tension + decay_rate)), 2),
                "reality_gap": round(max(0.0, reality_gap), 2),
                "viscosity": round(max(0.0, viscosity), 2),
                "ego_tax": round(max(0.0, ego_tax), 2),
                "decay_rate": round(max(0.0, decay_rate), 2),
                "autopilot": round(max(0.0, autopilot), 2),
                "exchange_health_score": round(exchange_health, 2),
                "self_deception_score": round(deception_base, 2),
                "subconscious_driver": user_friendly_driver,
                "ego_shield": user_friendly_shield,
                "action_persona": user_friendly_persona
            },
            "raw_ref": raw.dict()
        }

# =====================================================================
# 🔵 PART 3: UNIVERSAL SEMANTIC BRIDGE V2 (COMPREHENSIVE TRANSLATION)
# =====================================================================
class UniversalBridgeV2:
    @staticmethod
    def build_report(calc_results):
        m = calc_results["internal_metrics"]
        raw_dict = calc_results["raw_ref"]
        ms = raw_dict["needs_maslow"]
        id_def = raw_dict["identity_defense"]

        return {
            "System_Vitality_Profile": {
                "Structural_Stability_Score": m['stability'],
                "Internal_Friction_Level": m['tension'],
                "System_Degradation_Velocity": m['decay_rate'],
                "Homeostasis_Adherence": raw_dict["standard_line_syntax"]['wellbeing_index'],
                "Maslow_Hierarchy_Layer": ms['maslow_layer'],
                "Needs_Fulfillment_Percentage": f"{ms['fulfillment_pct'] * 10 if ms['fulfillment_pct'] <= 10 else ms['fulfillment_pct']}%"
            },
            "Cognitive_Distortion_Diagnostics": {
                "Reality_Refraction_Index": m['reality_gap'],
                "Subconscious_Inertia": m['viscosity'],
                "Autopilot_Dominance_Rate": f"{round(m['autopilot'] * 10, 2)}%",
                "Cognitive_Blindspot_Magnitude": round(m['reality_gap'] * (1.0 - (float(raw_dict["behavioral_forces"]['wisdom_level'])/10.0)), 2),
                "Subconscious_Driver": m['subconscious_driver']  # ✨ เปลี่ยนคีย์จาก Active_Kilesa_Type เป็นมิตรกับยูสเซอร์
            },
            "Identity_&_Social_Cost": {
                "Image_Maintenance_Tax": f"{round(m['ego_tax'] * 10, 2)}%",
                "Self_Deception_Magnitude": m['self_deception_score'],
                "Ego_Shield": m['ego_shield'],  # ✨ เปลี่ยนคีย์จาก Active_Defense_Mechanism
                "Identity_Threat_Exposure": id_def['id_threat_score']
            },
            "Energy_&_Resilience_Dynamics": {
                "Action_Momentum": raw_dict["energy_iip"]['energy_momentum'],
                "Friction_Exchange_Health": m['exchange_health_score'],
                "Action_Persona": m['action_persona'],  # ✨ เปลี่ยนคีย์จาก Dominant_Behavioral_Mode
                "Recovery_Potential": round((float(raw_dict["exchange_4g"]['gratitude']) + float(raw_dict["standard_line_syntax"]['focus_presence'])) / 2.0, 2)
            }
        }

# =====================================================================
# 🚀 PART 4: THE HYPER-STRATEGIC GAMBIT GENERATOR
# =====================================================================
class StrategicGambitV2:
    @staticmethod
    def get_directive(m, raw_dict):
        ms = raw_dict["needs_maslow"]
        id_def = raw_dict["identity_defense"]

        if ms['survival_safety'] < 4.0:
            return "หมากเดิน: BASELINE REDOUBT - ทรัพยากรพื้นฐานวิกฤต! จงตัดขาดโลกภายนอก (W3) แล้วถอยกลับไปรักษาความปลอดภัยทางกายภาพและจิตใจเป็นอันดับแรก"
        if m['stability'] < 3.5:
            return "หมากเดิน: OVERDRIVE CRISIS RESET - ระบบเสี่ยงพังทลายในระดับโครงสร้าง สั่งปิดกลไกตอบสนองทั้งหมด ตัดกระแสขับเคลื่อน (Drive) ล้างกระดานอารมณ์ทันที"
        if id_def['id_threat_score'] > 7.0 or m['ego_tax'] > 6.5:
            return "หมากเดิน: ASYMMETRIC DECOUPLING - กำลังติดกับดักการเปรียบเทียบและอัตตาคุกคาม จงถอดหน้ากากใน W3 และสลายภาพลักษณ์ทิ้งเพื่อหยุดการไหลออกของพลังงาน"
        if m['viscosity'] > 7.5:
            return "หมากเดิน: COGNITIVE SHOCKWAVE - ความหนืดในตะกอนจิตใต้สำนึกสูงเกินไป จงทำพฤติกรรมที่หักล้างสัญชาตญาณเดิมอย่างรุนแรง (Pattern Breaker)"
        if m['reality_gap'] > 6.0:
            return "หมากเดิน: EMPIRICAL ANCHOR - ความจริงวิบัติตกแต่งสูงเกินไป หยุดประมวลผลความรู้สึก (W2) และความคิดเห็นสังคม เลิกเดา แล้วกลับไปวัดผลตัวเลขเชิงประจักษ์ใน W1 เท่านั้น"
        if m['exchange_health_score'] < -3.0:
            return "หมากเดิน: METABOLIC PURGE - วงจรการแลกเปลี่ยนเสียสมดุลเนื่องจากการ 'ขอกลืนกินและยื้อแย่ง' สูงเกินไป ให้เปลี่ยนโหมดเป็นผู้ให้ชั่วคราวเพื่อลดแรงเสียดทาน"

        return "หมากเดิน: TOTAL EXPANSION OMNI - ระบบอยู่ในเสถียรภาพระดับควอนตัม ไร้แรงเสียดทาน ขยายขอบเขตอิทธิพลเชิงยุทธศาสตร์และโจมตีกระดานเป้าหมายได้เต็มกำลัง"

# =====================================================================
# 📡 PART 5: ENDPOINTS
# =====================================================================
@app.post("/analyze")
async def main_analysis_endpoint(data: SMFFullInputSchema):
    calculation = SASLogicCoreV2.calculate(data)
    universal_report = UniversalBridgeV2.build_report(calculation)
    directive = StrategicGambitV2.get_directive(calculation['internal_metrics'], calculation['raw_ref'])
    
    return {
        "Status": "Success",
        "Engine_Version": "2.1 (Architect-Omniscience-UX)",
        "Strategic_Verdict": {
            "Stability_Status": "🎯 PERFECT EQUILIBRIUM" if calculation['internal_metrics']['stability'] > 8.0 else "✅ SAFE" if calculation['internal_metrics']['stability'] > 6.0 else "⚠️ WARNING" if calculation['internal_metrics']['stability'] > 4.0 else "🚨 CRITICAL VULNERABILITY",
            "Next_Gambit": directive
        },
        "Comprehensive_Lab_Report": universal_report,
        "Raw_Sensor_Echo": data.dict()
    }

@app.get("/")
async def root():
    return {
        "status": "SAS Master Engine v2.1 is Online", 
        "architecture_mode": "Omniscience-UX",
        "active_sensors": 45
    }

