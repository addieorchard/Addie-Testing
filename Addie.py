
data = [
    {"farm_id": "F001", "crop": "Wheat", "year": 2022, "yield_tonnes": 3.2},
    {"farm_id": "F001", "crop": "Wheat", "year": 2023, "yield_tonnes": 3.6},
    {"farm_id": "F002", "crop": "Corn",  "year": 2022, "yield_tonnes": 5.1},
    {"farm_id": "F002", "crop": "Corn",  "year": 2023, "yield_tonnes": 4.9},
    {"farm_id": "F003", "crop": "Wheat", "year": 2023, "yield_tonnes": 2.8},
    {"farm_id": "F003", "crop": "Soy",   "year": 2022, "yield_tonnes": 3.9},
    {"farm_id": "F003", "crop": "Soy",   "year": 2023, "yield_tonnes": 4.2},
]


class CropYieldAnalyzer:
    def __init__(self, data):
        self.data = data

    def average_yield_by_crop(self, crop_name):
        total = 0
        count = 0

        for record in self.data:
            if record["crop"] == crop_name:
                total += record["yield_tonnes"]
                count += 1
            
        if count == 0:
            return None

        return total / count

analyze = CropYieldAnalyzer(data)
print(analyze.average_yield_by_crop("Wheat"))
