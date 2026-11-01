class TriangularMF:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_membership(self, x):
        if x <= self.a or x >= self.c:
            return 0.0
        if x == self.b:
            return 1.0
        if self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        return (self.c - x) / (self.c - self.b)


class FuzzyMedicalSystem:
    def __init__(self):
        self.fever_low = TriangularMF(36.0, 37.0, 38.0)
        self.fever_high = TriangularMF(37.5, 39.0, 41.0)
        self.cough_mild = TriangularMF(0.0, 2.0, 5.0)
        self.cough_severe = TriangularMF(4.0, 8.0, 10.0)

    def infer_risk(self, temp, cough_severity):
        mu_fever_high = self.fever_high.get_membership(temp)
        mu_cough_severe = self.cough_severe.get_membership(cough_severity)
        high_risk_degree = max(mu_fever_high, mu_cough_severe)
        
        mu_fever_low = self.fever_low.get_membership(temp)
        mu_cough_mild = self.cough_mild.get_membership(cough_severity)
        low_risk_degree = min(mu_fever_low, mu_cough_mild)

        numerator = (low_risk_degree * 20.0) + (high_risk_degree * 80.0)
        denominator = low_risk_degree + high_risk_degree + 1e-9
        return numerator / denominator


class FuzzyEVSystem:
    def __init__(self):
        self.dist_close = TriangularMF(0.0, 2.0, 10.0)
        self.dist_far = TriangularMF(8.0, 20.0, 50.0)
        self.speed_slow = TriangularMF(0.0, 20.0, 40.0)
        self.speed_fast = TriangularMF(30.0, 70.0, 100.0)

    def infer_brake(self, distance, speed):
        mu_dist_close = self.dist_close.get_membership(distance)
        mu_speed_fast = self.speed_fast.get_membership(speed)
        hard_brake_degree = min(mu_dist_close, mu_speed_fast)

        mu_dist_far = self.dist_far.get_membership(distance)
        mu_speed_slow = self.speed_slow.get_membership(speed)
        light_brake_degree = min(mu_dist_far, mu_speed_slow)

        numerator = (light_brake_degree * 20.0) + (hard_brake_degree * 90.0)
        denominator = light_brake_degree + hard_brake_degree + 1e-9
        return numerator / denominator


class FuzzyManufacturingSystem:
    def __init__(self):
        self.temp_normal = TriangularMF(20.0, 40.0, 60.0)
        self.temp_hot = TriangularMF(55.0, 75.0, 95.0)
        self.vib_low = TriangularMF(0.0, 1.0, 3.0)
        self.vib_high = TriangularMF(2.5, 5.0, 8.0)

    def infer_maintenance_urgency(self, temperature, vibration):
        mu_temp_hot = self.temp_hot.get_membership(temperature)
        mu_vib_high = self.vib_high.get_membership(vibration)
        urgent_degree = max(mu_temp_hot, mu_vib_high)

        mu_temp_normal = self.temp_normal.get_membership(temperature)
        mu_vib_low = self.vib_low.get_membership(vibration)
        routine_degree = min(mu_temp_normal, mu_vib_low)

        numerator = (routine_degree * 10.0) + (urgent_degree * 85.0)
        denominator = routine_degree + urgent_degree + 1e-9
        return numerator / denominator


if __name__ == "__main__":
    fuzzy_med = FuzzyMedicalSystem()
    print("Medical Risk Score (Temp: 38.5C, Cough: 7):", round(fuzzy_med.infer_risk(38.5, 7.0), 2))

    fuzzy_ev = FuzzyEVSystem()
    print("EV Brake Intensity (Dist: 5m, Speed: 60km/h):", round(fuzzy_ev.infer_brake(5.0, 60.0), 2))

    fuzzy_mfg = FuzzyManufacturingSystem()
    print("Smart Manufacturing Maintenance Urgency (Temp: 70C, Vib: 4.0):", round(fuzzy_mfg.infer_maintenance_urgency(70.0, 4.0), 2))
