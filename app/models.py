class InsuranceRating:
    @staticmethod
    def calculate_premium(age, vehicle_value, mileage):
        base_premium = 500
        age_factor = max(1, (30 - age) / 10)
        value_factor = vehicle_value / 50000
        mileage_factor = mileage / 10000
        
        premium = base_premium * age_factor * value_factor * mileage_factor
        return round(premium, 2)