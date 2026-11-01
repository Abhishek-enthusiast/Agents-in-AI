class AutonomousVehicleKBS:
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

        return known_facts, known_facts.get("Action", "Maintain Speed")

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
    (lambda f: f.get("obstacle_distance", 999) < (f.get("vehicle_speed", 0) * 0.3), "Collision_Risk", "Critical"),
    (lambda f: f.get("Collision_Risk") == "Critical", "Action", "Emergency Brake"),
    (lambda f: f.get("traffic_light") == "red" and f.get("vehicle_speed", 0) > 0, "Action", "Stop at Intersection")
]

sensor_data = {
    "obstacle_distance": 12.0,
    "vehicle_speed": 50.0,
    "traffic_light": "green"
}

av_system = AutonomousVehicleKBS(sensor_data, rules)

# 1. Forward Chaining
derived_state, action = av_system.forward_chaining()

# 2. Backward Chaining
is_emergency_brake_justified = av_system.backward_chaining("Action", "Emergency Brake")
