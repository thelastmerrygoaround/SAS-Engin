from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
import math

app = FastAPI(title="SAS Strategic Intelligence Engine v2.0 (The Architect Omniscience)")

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
# กำหนดประเภทข้อมูลที่เข้มงวดเพื่อป้องกัน Bug เงียบตั้งแต่หน้าประตูบ้าน
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
# 🟠 PART 2: THE QUANTUM CALCULUS CORE (v2.0 OMNISCIENCE LOGIC)
# =====================================================================
class SASLogicCoreV2:
    @staticmethod
    def calculate(raw: SMFFullInputSchema):
        # 0. ดึงข้อมูลแยกกลุ่มตรงตาม Schema ไร้ปัญหาคีย์หลอนพิมพ์ผิด
        w = raw.worlds
        ex = raw.exchange_4g
        syn = raw.standard_line_syntax
        en = raw.energy_iip
        ms = raw.needs_maslow
        cd = raw.conditioning_stack
        id_def = raw.identity_defense
        bf = raw.behavioral_forces

        # 🧠 SIMULATED SEMANTIC LAYER: ประมวลผลน้ำหนักจาก Array ข้อความภาษาไทย (ถ้าส่งข้อมูลมาจะเพิ่มแรงกระเพื่อมระบบ)
        text_weight = 1.0 + (0.05 * (len(w.world_1_objective) + len(w.world_2_subjective) + len(w.world_3_social)))

        # --- LAYER 1: ADVANCED COGNITIVE DISTORTION ---
        # การบิดเบือนสัจจะ (Refraction Index บิดด้วยความแข็งกระด้างของทิฐิ)
        refraction_factor = 1.0 + (w.w2_refraction * 0.12) * (1.0 + (id_def.ditthi_belief_rigidity * 0.08))
        social_interference = w.w3_social_pressure * (1.0 + w.power_relation_asymmetry * 0.15)
        
        # Reality Gap Index (RGI v2.0): ตัวคูณความจริงหลุดลอย
        reality_gap = (refraction_factor * social_interference * text_weight) / (w.w1_obj_count + 1.0)

        # --- LAYER 2: DEEP PSYCHE VISCOSITY & AUTOPILOT ---
        # ความหนืดของจิตวิทยาชั้นลึก (Viscosity บุกคูณด้วยอัตราการกระตุ้นของกิเลสและตัณหา)
        kilesa_amplifier = 1.0 + (cd.kilesa_active_trigger * 0.1)
        asava_force_total = cd.asava_attachment * kilesa_amplifier
        viscosity = (asava_force_total + cd.anusaya_force) / (bf.wisdom_level + 1.0)
        
        # Autopilot Ratio (สัญชาตญาณสัตว์ป่า vs ความตระหนักรู้) ปรับพ่วงแรงผลัก (Craving) และแรงผลักไส (Aversion)
        total_desire_force = cd.craving_intensity + cd.aversion_intensity
        autopilot = (asava_force_total * total_desire_force) / (syn.focus_presence + 1.0)

        # --- LAYER 3: WAVE RESILIENCE & ENERGY DYNAMICS ---
        # คำนวณคลื่นอารมณ์ตกค้าง (Emotional Residue) ผสมความเข้มข้นของพลังงานความเครียด
        emotional_residue = (syn.syntax_amplitude * syn.syntax_freq) * 0.2 * (1.0 + en.intensity * 0.05)
        
        # อัตราการเสื่อมสลายของระบบ (System Decay Rate) เร่งความเร็วด้วยแรงฉุดเฉื่อย (Neutral Drag)
        decay_rate = (emotional_residue + bf.internal_tension + bf.neutral_drag) / (syn.focus_stability + 1.0)

        # --- LAYER 4: IDENTITY DEFENSE & EGO TAX ---
        # ภาษีรักษาหน้าตา (Ego Tax) เพิ่มอัตราคูณหากตัวตนทับซ้อนกับหัวโขนในโลก (Identity Overlap) หรือมีภัยคุกคามตัวตน (ID Threat)
        identity_multiplier = 1.0 + (id_def.identity_overlap * 0.05) + (id_def.id_threat_score * 0.08)
        ego_tax = (id_def.mana_comparison_intensity * w.w3_social_pressure * identity_multiplier) / (bf.wisdom_level + 1.0)
        
        # ความหลอกตัวเองขั้นสูง (Self-Deception Probability Score)
        deception_base = (id_def.belief_attachment * refraction_factor) + (id_def.ego_inflation * 0.5)
        if id_def.atta_defense_active or id_def.defense_mech_id != "None" and id_def.defense_mech_id != "":
            deception_base *= 2.0  # โดนขัดขวางสมบูรณ์แบบคูณสองเท่า!
        
        # --- LAYER 5: MASLOW EQUILIBRIUM & 4G SUSTAINABILITY ---
        # ทฤษฎีความต้องการลำดับขั้น: หากฐานรากสั่นคลอน (Survival ต่ำ) จะเกิดบัฟลบส่งแรงกดดันไปที่ตัวแปรอื่น
        maslow_stability_factor = (ms.survival_safety + ms.self_actualization) / 2.0
        if ms.survival_safety < 4.0:
            maslow_stability_factor *= 0.5  # ระบบเข้าสู่ภาวะขาดแคลนเฉียบพลัน

        # วงจรความยั่งยืน 4G: การแลกเปลี่ยนทรัพยากร (Get/Grow/Give/Gratitude) และแรงยื้อแย่ง (Grab Force)
        lubricated_friction = ex.exchange_friction / (1.0 + (ex.gratitude * 0.6))
        exchange_health = (ex.grow + ex.give) - (ex.get + ex.grab_force * 0.5)
        
        # --- FINAL SYNTHESIS: STRUCTURAL STABILITY SCORE ---
        # การหลอมรวมพารามิเตอร์ non-linear ทั้งหมดเพื่อประเมินความมั่นคงสูงสุดของโครงข่าย
        stability_base = syn.wellbeing_index * 1.5 + (maslow_stability_factor * 0.8) + (en.energy_stability * 0.5)
        tension_impact = (bf.avoidance_force + bf.approach_drive * 0.2 + lubricated_friction) * 0.5
        
        stability = (stability_base / (1.0 + tension_impact)) - (deception_base * 0.15) - (emotional_residue * 0.1) + (exchange_health * 0.1)

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
                "self_deception_score": round(deception_base, 2)
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
        
        # ดึงเพื่อทำรายงานอิงกลุ่มในฐานะตัวแปรอ้างอิง
        ms = raw_dict["needs_maslow"]
        cd = raw_dict["conditioning_stack"]
        id_def = raw_dict["identity_defense"]
        bf = raw_dict["behavioral_forces"]

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
                "Cognitive_Blindspot_Magnitude": round(m['reality_gap'] * (1.0 - (float(bf['wisdom_level'])/10.0)), 2),
                "Active_Kilesa_Type": cd['kilesa_type']
            },
            "Identity_&_Social_Cost": {
                "Image_Maintenance_Tax": f"{round(m['ego_tax'] * 10, 2)}%",
                "Self_Deception_Magnitude": m['self_deception_score'],
                "Active_Defense_Mechanism": id_def['defense_mech_id'] if id_def['defense_mech_id'] else "NONE",
                "Identity_Threat_Exposure": id_def['id_threat_score']
            },
            "Energy_&_Resilience_Dynamics": {
                "Action_Momentum": raw_dict["energy_iip"]['energy_momentum'],
                "Friction_Exchange_Health": m['exchange_health_score'],
                "Dominant_Behavioral_Mode": bf['dominant_mode'],
                "Recovery_Potential": round((float(raw_dict["exchange_4g"]['gratitude']) + float(raw_dict["standard_line_syntax"]['focus_presence'])) / 2.0, 2)
            }
        }

# =====================================================================
# 🚀 PART 4: THE HYPER-STRATEGIC GAMBIT GENERATOR
# =====================================================================
class StrategicGambitV2:
    @staticmethod
    def get_directive(m, raw_dict):
        # ถอดลอจิกหมากเดินยุทธศาสตร์แบบวิเคราะห์เงื่อนไขซับซ้อนตามแบบคัมภีร์พิชัยสงคราม
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
    # 1. รันเครื่องยนต์คำนวณ Quantum Calculus Core v2.0
    calculation = SASLogicCoreV2.calculate(data)
    
    # 2. ถอดข้อมูลเชิงลึกเป็นรายงานแล็บแบบละเอียดยิบส่งให้หน้าบ้าน
    universal_report = UniversalBridgeV2.build_report(calculation)
    
    # 3. กำหนดคำสั่งหมากเดินยุทธศาสตร์ (Strategic Gambit) 
    directive = StrategicGambitV2.get_directive(calculation['internal_metrics'], calculation['raw_ref'])
    
    return {
        "Status": "Success",
        "Engine_Version": "2.0 (Architect-Omniscience)",
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
        "status": "SAS Master Engine v2.0 is Online", 
        "architecture_mode": "Omniscience",
        "active_sensors": 45
    }
        p = {}
        for group in raw.dict().values():
            p.update(group)

        def get_f(key, default=0.0):
            val = p.get(key, default)
            return float(val) if isinstance(val, (int, float)) else default

        # --- 1. WORLD INTERFERENCE & REFRACTION (M1) ---
        # กฎการซ้อนทับ: W1 ถูกทอนด้วย W2 และบิดด้วย W3
        base_reality = get_f('w1_obj_count')
        refraction_factor = 1 + (get_f('w2_refraction') * 0.15)
        social_interference = get_f('w3_social_pressure') * (1 + get_f('power_relation_asymmetry'))
        
        # Reality Gap Index (RGI)
        reality_gap = (refraction_factor * social_interference) / (base_reality + 1)
        
        # --- 2. DEEP STACK VISCOSITY (M2) ---
        # คำนวณความหนืดของระบบ: (Asava + Anusaya) / Wisdom
        asava = get_f('asava_attachment')
        wisdom = get_f('wisdom_level')
        viscosity = (asava + get_f('anusaya_force')) / (wisdom + 1)
        
        # Autopilot Ratio (สัญชาตญาณ vs สติ)
        autopilot = (asava * get_f('craving_intensity')) / (get_f('focus_presence') + 1)

        # --- 3. WAVE RESILIENCE & RESIDUE (M3) ---
        # คำนวณแรงส่งค้างของอารมณ์ (Residue)
        amplitude = get_f('syntax_amplitude')
        frequency = get_f('syntax_freq')
        emotional_residue = (amplitude * frequency) * 0.2
        
        # System Decay Rate (ความเร็วในการพังทลาย)
        decay_rate = (emotional_residue + get_f('internal_tension')) / (get_f('focus_stability') + 1)

        # --- 4. IDENTITY DEFENSE & EGO TAX (M4) ---
        # Ego Tax: ทรัพยากรที่เสียไปเพื่อรักษาหน้า
        ego_tax = (get_f('mana_comparison_intensity') * get_f('w3_social_pressure')) / (wisdom + 1)
        
        # Self-Deception Index
        deception = (get_f('belief_attachment') * refraction_factor)
        if p.get('atta_defense_active') or p.get('defense_mechanism'):
            deception *= 1.8

        # --- 5. 4G SUSTAINABILITY LOOP ---
        # Gratitude เป็นตัวลดแรงเสียดทาน (Lubricant)
        friction = get_f('friction')
        lubricated_friction = friction / (1 + (get_f('gratitude') * 0.5))
        
        # Stability (หัวใจของเครื่องยนต์)
        # สูตร Non-linear: (Wellbeing / Tension) - (Distortion * Bias)
        stability_base = get_f('wellbeing_index') * 1.2
        tension_impact = (get_f('avoidance_force') + lubricated_friction) * 0.4
        stability = (stability_base / (1 + tension_impact)) - (deception * 0.2) - (emotional_residue * 0.1)

        return {
            "internal_metrics": {
                "stability": round(max(0, min(10, stability)), 2),
                "tension": round(max(0, min(10, get_f('internal_tension') + decay_rate)), 2),
                "reality_gap": round(reality_gap, 2),
                "viscosity": round(viscosity, 2),
                "ego_tax": round(ego_tax, 2),
                "decay_rate": round(decay_rate, 2),
                "autopilot": round(autopilot, 2)
            },
            "raw_ref": p
        }

# =====================================================================
# 🔵 PART 3: UNIVERSAL SEMANTIC BRIDGE (DATA EXPANSION)
# =====================================================================
class UniversalBridge:
    @staticmethod
    def build_report(calc_results):
        m = calc_results["internal_metrics"]
        p = calc_results["raw_ref"]
        
        return {
            "System_Vitality_Profile": {
                "Structural_Stability_Score": m['stability'],
                "Internal_Friction_Level": m['tension'],
                "System_Degradation_Velocity": m['decay_rate'],
                "Homeostasis_Adherence": p.get('wellbeing_index')
            },
            "Cognitive_Distortion_Diagnostics": {
                "Reality_Refraction_Index": m['reality_gap'],
                "Subconscious_Inertia": m['viscosity'],
                "Autopilot_Dominance_Rate": f"{round(m['autopilot'] * 10, 2)}%",
                "Cognitive_Blindspot_Magnitude": round(m['reality_gap'] * (1 - (float(p.get('wisdom_level', 0))/10)), 2)
            },
            "Identity_&_Social_Cost": {
                "Image_Maintenance_Tax": f"{round(m['ego_tax'] * 10, 2)}%",
                "Self_Deception_Probability": "High" if p.get('belief_attachment', 0) > 7 else "Normal",
                "Social_Validation_Dependency": round(float(p.get('mana_comparison_intensity', 0)) * (float(p.get('w3_social_pressure', 0))/10), 2)
            },
            "Energy_&_Resilience": {
                "Action_Momentum": p.get('energy_momentum'),
                "Emotional_Turbulence_Impact": p.get('syntax_amplitude'),
                "Recovery_Potential": round((float(p.get('gratitude', 0)) + float(p.get('focus_presence', 0))) / 2, 2)
            }
        }

# =====================================================================
# 🚀 PART 4: THE STRATEGIC GAMBIT GENERATOR
# =====================================================================
class StrategicGambit:
    @staticmethod
    def get_directive(m, p):
        # ค้นหาจุดคันโยก (Leverage Points)
        if m['stability'] < 4.0:
            return "หมากเดิน: CRISIS RESET - หยุดทุกการตัดสินใจ และลด Tension ใน World 2 ทันที"
        elif m['ego_tax'] > 6.0:
            return "หมากเดิน: EGO STRIP - ยอมเสียหน้าใน World 3 เพื่อกู้คืนทรัพยากรใน World 1"
        elif m['viscosity'] > 7.0:
            return "หมากเดิน: PATTERN BREAK - จงใจทำสิ่งที่ฝืนความเคยชินเดิมเพื่อทำลายลูป Autopilot"
        elif m['reality_gap'] > 5.0:
            return "หมากเดิน: REALITY ANCHOR - เลิกฟังความเห็นคนอื่น แล้วกลับมาไล่เช็คตัวเลขจริงใน W1"
        else:
            return "หมากเดิน: EXPANSION - ระบบเสถียร พร้อมสำหรับการรุกคืบในเชิงยุทธศาสตร์"

# =====================================================================
# 📡 PART 5: ENDPOINTS
# =====================================================================
@app.post("/analyze")
async def main_analysis_endpoint(data: SMFFullInputSchema):
    # 1. รันเครื่องยนต์ SAS Logic
    calculation = SASLogicCore.calculate(data)
    
    # 2. แตกข้อมูลเป็น Universal Report (ตรวจเลือดละเอียดยิบ)
    universal_report = UniversalBridge.build_report(calculation)
    
    # 3. สร้างคำสั่งหมากเดิน (Gambit)
    directive = StrategicGambit.get_directive(calculation['internal_metrics'], calculation['raw_ref'])
    
    return {
        "Status": "Success",
        "Engine_Version": "5.1 (Master)",
        "Strategic_Verdict": {
            "Stability_Status": "SAFE" if calculation['internal_metrics']['stability'] > 7 else "WARNING" if calculation['internal_metrics']['stability'] > 4 else "CRITICAL",
            "Next_Gambit": directive
        },
        "Comprehensive_Lab_Report": universal_report,
        "Raw_Sensor_Echo": data.dict()
    }

@app.get("/")
async def root():
    return {"status": "SAS Master Engine is Online", "power": "100% Potency"}
