from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

# 1. สร้าง App (ประตูบ้าน)
app = FastAPI()

# =====================================================================
# 🟢 PART 1: SMF PARAMETER ONTOLOGY
# =====================================================================

class BaseParam(BaseModel):
    evidence: Optional[str] = Field(default=None, description="Exact quote as proof.")
    confidence: float = Field(default=1.0, description="0.0-1.0 confidence level.")

class Layer1To3Worlds(BaseModel):
    world_1_objective: List[str] = Field(description="Verifiable facts, resources, money, time constraints.")
    world_2_subjective: List[str] = Field(description="Internal perceptions, specific emotions, mental state.")
    world_3_social: List[str] = Field(description="Roles, power dynamics, group expectations, reputation risk.")
    power_relation_asymmetry: float = Field(default=0.0, description="Power balance (0=Equal, 10=Oppressed).")

class LayerConditioning(BaseModel):
    asava_reservoir: float = Field(description="Deep habitual patterns / Addictions / Past conditioning.")
    anusaya_latent_bias: float = Field(description="Hidden tendencies / Biases that are not yet active.")
    kilesa_active_trigger: float = Field(description="Current activated emotional state (Craving/Aversion).")

class LayerIdentityDefense(BaseModel):
    ditthi_belief_rigidity: float = Field(description="Strength of fixed mindsets/theories.")
    mana_comparison_intensity: float = Field(description="Level of social comparison or ego-status concern.")
    atta_defense_active: bool = Field(default=False, description="Is the system currently protecting self-image?")

class LayerMaslow(BaseModel):
    survival_safety: float = Field(description="Physiological & Safety satisfaction.")
    social_esteem: float = Field(description="Belonging & Status satisfaction.")
    self_actualization: float = Field(description="Growth & Fulfillment.")

class LayerStandardLine(BaseModel):
    wellbeing_index: float = Field(description="Average of Happiness, Enjoyment, Relaxation, Fulfillment.")
    focus_presence: float = Field(description="Focus state: ability to remain in the present without escape.")

class LayerSystemDynamics(BaseModel):
    exchange_balance_4g: float = Field(description="Balance of Get/Grow vs Give/Gratitude (-10 to +10).")
    energy_momentum: float = Field(description="Energy intensity and direction (IIP Model).")
    avoidance_force: float = Field(description="Push force: Flight/Escape intensity.")
    approach_drive: float = Field(description="Pull force: Fight/Engagement intensity.")

class SMFFullEngineSchema(BaseModel):
    worlds: Layer1To3Worlds
    conditioning: LayerConditioning
    identity: LayerIdentityDefense
    needs: LayerMaslow
    equilibrium: LayerStandardLine
    dynamics: LayerSystemDynamics

# =====================================================================
# 🟠 PART 2: THE INTERCONNECTED LOGIC (SAS Engine 5.1)
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
# 🔵 PART 3: UNIVERSAL CONNECTOR
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
    # 1. คำนวณค่าทางตัวเลข
    calculation = SASLogicProcessor.process(data)
    # 2. แปลงผลเป็น Insight ที่มนุษย์เข้าใจ (ผ่าน Bridge)
    insight = UniversalBridge.export_insight(data, calculation)
    return insight

@app.get("/")
async def root():
    return {"status": "SMF Engine is Online", "version": "5.1"}


