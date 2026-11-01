class BayesianMedicalDiagnosis:
    def __init__(self, p_disease, p_pos_given_disease, p_pos_given_no_disease):
        self.p_disease = p_disease
        self.p_no_disease = 1.0 - p_disease
        self.p_pos_given_disease = p_pos_given_disease
        self.p_pos_given_no_disease = p_pos_given_no_disease

    def posterior_disease_given_positive(self):
        p_pos = (self.p_pos_given_disease * self.p_disease) + (self.p_pos_given_no_disease * self.p_no_disease)
        return (self.p_pos_given_disease * self.p_disease) / p_pos


class BayesianAutonomousVehicle:
    def __init__(self, p_obstacle, p_sensor_detect_if_present, p_sensor_false_alarm):
        self.p_obstacle = p_obstacle
        self.p_no_obstacle = 1.0 - p_obstacle
        self.p_detect_present = p_sensor_detect_if_present
        self.p_detect_absent = p_sensor_false_alarm

    def posterior_obstacle_given_detection(self):
        p_detection = (self.p_detect_present * self.p_obstacle) + (self.p_detect_absent * self.p_no_obstacle)
        return (self.p_detect_present * self.p_obstacle) / p_detection


class BayesianSmartManufacturing:
    def __init__(self, p_defect, p_vibration_high_if_defect, p_vibration_high_if_normal):
        self.p_defect = p_defect
        self.p_normal = 1.0 - p_defect
        self.p_vib_defect = p_vibration_high_if_defect
        self.p_vib_normal = p_vibration_high_if_normal

    def posterior_defect_given_high_vibration(self):
        p_high_vib = (self.p_vib_defect * self.p_defect) + (self.p_vib_normal * self.p_normal)
        return (self.p_vib_defect * self.p_defect) / p_high_vib


if __name__ == "__main__":
    medical = BayesianMedicalDiagnosis(p_disease=0.01, p_pos_given_disease=0.95, p_pos_given_no_disease=0.05)
    print("Medical Diagnosis P(Disease | Test+):", round(medical.posterior_disease_given_positive(), 4))

    av = BayesianAutonomousVehicle(p_obstacle=0.05, p_sensor_detect_if_present=0.98, p_sensor_false_alarm=0.02)
    print("Autonomous Vehicle P(Obstacle | Detection):", round(av.posterior_obstacle_given_detection(), 4))

    factory = BayesianSmartManufacturing(p_defect=0.02, p_vibration_high_if_defect=0.90, p_vibration_high_if_normal=0.04)
    print("Smart Manufacturing P(Defect | High Vibration):", round(factory.posterior_defect_given_high_vibration(), 4))
