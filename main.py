from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <--- เพิ่มบรรทัดนี้
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# =====================================================================
# 🔓 ส่วนที่เพิ่มเข้าไปเพื่อแก้ "Failed to fetch" (CORS)
# =====================================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # อนุญาตทุกเว็บไซต์ให้เชื่อมต่อ (เหมาะสำหรับช่วงพัฒนา)
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก Method (GET, POST, etc.)
    allow_headers=["*"],  # อนุญาตทุก Header
)

# =====================================================================
# 🟢 PART 1: SMF PARAMETER ONTOLOGY (เหมือนเดิม)
# =====================================================================
class Layer1To3Worlds(BaseModel):
    world_1_objective: List[str]
    world_2_subjective: List[str]
    world_3_social: List[str]
    power_relation_asymmetry: float

class LayerConditioning(BaseModel):
    asava_reservoir: float
    anusaya_latent_bias: float
    kilesa_active_trigger: float

class LayerIdentityDefense(BaseModel):
    ditthi_belief_rigidity: float
    mana_comparison_intensity: float
    atta_defense_active: bool

class LayerMaslow(BaseModel):
    survival_safety: float
    social_esteem: float
    self_actualization: float

class LayerStandardLine(BaseModel):
    wellbeing_index: float
    focus_presence: float

class LayerSystemDynamics(BaseModel):
    exchange_balance_4g: float
    energy_momentum: float
    avoidance_force: float
    approach_drive: float

class SMFFullEngineSchema(BaseModel):
    worlds: Layer1To3Worlds
    conditioning: LayerConditioning
    identity: LayerIdentityDefense
    needs: LayerMaslow
    equilibrium: LayerStandardLine
    dynamics: LayerSystemDynamics

# =====================================================================
# 🟠 PART 2: THE INTERCONNECTED LOGIC (เหมือนเดิม)
# =====================================================================
class SASLogicProcessor:
    @staticmethod
    def process(data: SMFFullEngineSchema) -> dict:
        distortion = (data.conditioning.asava_reservoir * 0.4) + \
                     (data.conditioning.anusaya_latent_bias * 0.3) + \
                     (1.5 if data.identity.atta_defense_active else 0)
        
        needs_pressure = 10.0 - data.needs.survival_safety
        social_pressure = data.worlds.power_relation_asymmetry
        tension = (data.dynamics.avoidance_force + social_pressure + needs_pressure) / 3.0
        
        stability = data.equilibrium.wellbeing_index - (distortion * 0.5) - (abs(data.dynamics.approach_drive - data.dynamics.avoidance_force) * 0.3)
        
        if stability < 4.0: status = "CRITICAL: Collapsing"
        elif tension > 7.0: status = "HIGH FRICTION: Distorted"
        else: status = "BALANCED: Standard Line"

        return {
            "Stability_Index": round(max(0.0, min(10.0, stability)), 2),
            "Tension_Level": round(max(0.0, min(10.0, tension)), 2),
            "Distortion_Score": round(distortion, 2),
            "Behavioral_Status": status,
            "Energy_Momentum_Vector": data.dynamics.energy_momentum
        }

# =====================================================================
# 🔵 PART 3: UNIVERSAL CONNECTOR (เหมือนเดิม)
# =====================================================================
class UniversalBridge:
    @staticmethod
    def export_insight(raw: SMFFullEngineSchema, calc: dict) -> dict:
        return {
            "Reality_Gap": {
                "World_1_Facts": raw.worlds.world_1_objective,
                "Refraction_Level": calc["Distortion_Score"]
            },
            "Internal_Engine": {
                "Stability": calc["Stability_Index"],
                "Stress_Pressure": calc["Tension_Level"],
                "Identity_Shield": "ON" if raw.identity.atta_defense_active else "OFF"
            },
            "Strategic_Signal": {
                "Status": calc["Behavioral_Status"],
                "Recommendation_Vector": "Focus on Stability" if calc["Stability_Index"] < 5 else "Focus on Growth"
            }
        }

# =====================================================================
# 🚀 PART 4: THE ENDPOINTS
# =====================================================================
@app.post("/analyze")
async def analyze_smf(data: SMFFullEngineSchema):
    calculation = SASLogicProcessor.process(data)
    insight = UniversalBridge.export_insight(data, calculation)
    return insight

@app.get("/")
async def root():
    return {"status": "SMF Engine is Online", "version": "5.1"}
