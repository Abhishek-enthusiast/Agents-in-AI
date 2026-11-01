class MedicalDiagnosisSystem:
    def __init__(self, facts, rules):
        self.facts = facts
        self.rules = rules
   
    # Forward Chaining (Data-Driven Inference)
   
    def forward_chaining(self):
        print("=== Running Forward Chaining ===")
        known_facts = dict(self.facts)
        inferred = True

        while inferred:
            inferred = False
            for rule_id, (condition, outcome_key, outcome_val) in enumerate(self.rules):
                if outcome_key in known_facts and known_facts[outcome_key] == outcome_val:
                    continue
              
                if condition(known_facts):
                    known_facts[outcome_key] = outcome_val
                    print(f"  [Rule Triggered] R{rule_id+1}: Deduced '{outcome_key} = {outcome_val}'")
                    inferred = True
                    break

        print(f"Final Inferred Knowledge Base: {known_facts}\n")
        return known_facts.get("Diagnosis", "Undetermined")

    
    # Backward Chaining (Goal-Driven Inference)
    
    def backward_chaining(self, goal_key, goal_val, visited=None):
        if visited is None:
            visited = set()

        print(f"Checking Goal: {goal_key} == {goal_val}")
        if goal_key in self.facts:
            is_match = self.facts[goal_key] == goal_val
            print(f"  -> Fact exists: {goal_key} = {self.facts[goal_key]} | Match: {is_match}")
            return is_match

        sub_goal_signature = (goal_key, goal_val)
        if sub_goal_signature in visited:
            return False
        visited.add(sub_goal_signature)

        matching_rules = [
            r for r in self.rules if r[1] == goal_key and r[2] == goal_val
        ]

        for rule_id, (condition, _, _) in enumerate(matching_rules):
            print(f"  -> Testing potential rule R{self.rules.index((condition, goal_key, goal_val))+1} to prove '{goal_key} = {goal_val}'")
          
            if condition(self.facts):
                print(f"  -> Goal '{goal_key} = {goal_val}' PROVED by R{self.rules.index((condition, goal_key, goal_val))+1}!")
                return True

        print(f"  -> Goal '{goal_key} = {goal_val}' CANNOT be proved.\n")
        return False

# Execution with Numerical Data

rules = [
    # R1
    (lambda f: f.get("Fever", 0) > 100.0, "Has_High_Fever", True),
    # R2
    (lambda f: f.get("Has_High_Fever", False) and f.get("Cough", False), "Has_Respiratory_Infection", True),
    # R3
    (lambda f: f.get("Has_Respiratory_Infection", False) and f.get("Loss_of_Taste", False), "Diagnosis", "Covid-19"),
    # R4
    (lambda f: f.get("Has_Respiratory_Infection", False) and f.get("Sore_Throat", False), "Diagnosis", "Strep Throat"),
]

patient_facts = {
    "Fever": 102.5,
    "Cough": True,
    "Loss_of_Taste": True,
    "Sore_Throat": False
}

expert_system = MedicalDiagnosisSystem(patient_facts, rules)
# 1. Forward Chaining 
diagnosis_fw = expert_system.forward_chaining()
print(f"Forward Chaining Result: Patient Diagnosis is '{diagnosis_fw}'\n")

# 2. Backward Chaining
print("=== Running Backward Chaining ===")
target_hypothesis = ("Diagnosis", "Covid-19")
is_confirmed = expert_system.backward_chaining(target_hypothesis[0], target_hypothesis[1])
print(f"Backward Chaining Result: Hypothesis '{target_hypothesis[1]}' is {is_confirmed}")
