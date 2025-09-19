import pandas as pd

predictions = pd.read_csv("./predictions.csv", sep=";")


types = [
    "NaturalPark",
    "NationalPark",
    "Tower",
    "Basilica",
    "RomanesqueChurch",
    "NaturalArea",
    "UndergroundChurch",
    "Cave",
    "SeaCave",
    "UndergroundOilMill",
    "EntertainmentBusiness",
    "Church",
    "Museum",
    "OrthodoxWorship",
    "Ravine",
    "EcoMuseum",
    "Lake",
    "WWFOasis",
    "MarineReserve",
    "Convent",
    "ArecheologicalPark",
    "Amphitheater",
    "Garden",
    "Library",
    "Trullo",
    "Reserve",
    "Synagogue",
    "Port",
    "Mill",
    "Beach",
    "Mosque",
    "Worship",
    "Landing",
    "Farmhouse",
    "HistoricTheater",
    "Castle",
    "HistoricPalace"
]

mask1 = predictions['s'].str.contains('generic_review') & (predictions['p'] == 'hasRating')
mask2 = (predictions['p'] == 'type') & (predictions['o'].isin(types))
mask3 = predictions['p'] == 'hasDayOfWeek'

predictions = predictions[mask1 | mask2 | mask3]