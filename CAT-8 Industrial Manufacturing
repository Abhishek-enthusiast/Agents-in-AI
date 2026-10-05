class IndustrialManufacturingKBS:
    def __init__(self, telemetry, rules):
        self.telemetry = dict(telemetry)
        self.rules = rules

    def forward_chaining(self):
        known_facts = dict(self.telemetry)
        inferred = True

        while inferred:
            inferred = False
            for rule_id, (condition, key, val) in enumerate(self.rules):
                if key in known_facts and known_facts[key] == val:
                    continue

                if condition(known_facts):
                    known_facts[key] = val
                    inferred = True
                    break

        return known_facts, known_facts.get("Maintenance_Alert", "Normal Operation")

    def backward_chaining(self, goal_key, goal_val, visited=None):
        if visited is None:
            visited = set()

        if goal_key in self.telemetry:
            return self.telemetry[goal_key] == goal_val

        sub_goal = (goal_key, goal_val)
        if sub_goal in visited:
            return False
        visited.add(sub_goal)

        matching_rules = [
            r for r in self.rules if r[1] == goal_key and r[2] == goal_val
        ]

        for condition, _, _ in matching_rules:
            if condition(self.telemetry):
                return True

        return False


rules = [
    (lambda f: f.get("spindle_vibration_mm_s", 0) > 4.5 and f.get("operating_temp_c", 0) > 85.0, "Bearing_Wear", "Critical"),
    (lambda f: f.get("coolant_pressure_bar", 99.0) < 2.0, "Cooling_Efficiency", "Degraded"),
    (lambda f: f.get("Bearing_Wear") == "Critical" and f.get("Cooling_Efficiency") == "Degraded", "Maintenance_Alert", "Immediate Shutdown Required"),
    (lambda f: f.get("Bearing_Wear") == "Critical" and f.get("Cooling_Efficiency") != "Degraded", "Maintenance_Alert", "Schedule Maintenance")
]

machine_telemetry = {
    "spindle_vibration_mm_s": 5.8,
    "operating_temp_c": 92.0,
    "operating_hours": 1200,
    "coolant_pressure_bar": 1.2
}

factory_kbs = IndustrialManufacturingKBS(machine_telemetry, rules)

# 1. Forward Chaining
derived_state, action = factory_kbs.forward_chaining()

# 2. Backward Chaining
is_shutdown_justified = factory_kbs.backward_chaining("Maintenance_Alert", "Immediate Shutdown Required")
