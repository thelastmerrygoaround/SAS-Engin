from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import math

app = FastAPI(title="SAS Strategic Intelligence Engine v5.1")

# ปลดล็อค CORS สำหรับการเชื่อมต่อกับ Lovable/Canvas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================================
# 🟢 PART 1: MASTER INPUT SCHEMA (40 SENSORS)
# =====================================================================
class SMFFullInputSchema(BaseModel):
    worlds: Dict
    exchange_4g: Dict
    standard_line_syntax: Dict
    energy_iip: Dict
    needs_maslow: Dict
    conditioning_stack: Dict
    identity_defense: Dict
    behavioral_forces: Dict

# =====================================================================
# 🟠 PART 2: THE DEEP CALCULUS (SAS INTERNAL LOGIC)
# =====================================================================
class SASLogicCore:
    @staticmethod
    def calculate(raw: SMFFullInputSchema):
        # รวบรวมพารามิเตอร์ทั้งหมดเข้าสู่ Flat Map
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
