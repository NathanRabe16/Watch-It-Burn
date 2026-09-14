TREE = [
    {"burn_duration": 6, "flammability": {0: 0.0, 1: 0.25, 2: 0.50, 3: 0.75, 4: 1.0}
    , "dryness": 0, "car": "T"}
]

SHRUB = [
    {"burn_duration": 4, "flammability": {0: 0.0, 1: 0.30, 2: 0.60, 3: 0.90, 4: 1.0}
    , "dryness": 0, "car": "S"}
]

GRASS = [
    {"burn_duration": 3, "flammability": {0: 0.0, 1: 0.35, 2: 0.70, 3: 0.95, 4: 1.0}
    , "dryness": 0, "car": "G"}
]

ASHES = [
    {"burn_duration": 0, "flammability": {0: 0.0, 1: 0, 2: 0, 3: 0, 4: 0}
    , "dryness": 0, "car": "A"}
]

WATER = [
    {"burn_duration": 0, "flammability": {0: 0.0, 1: 0, 2: 0, 3: 0, 4: 0}
    , "dryness": 0, "car": "O"}
]

BRIDGE = [
    {"burn_duration": 6, "flammability": {0: 0.0, 1: 0.25, 2: 0.50, 3: 0.75, 4: 1.0}
    , "dryness": 0, "car": "B"}
]

HOUSE = [
    {"burn_duration": 5, "flammability":
    {0: 0.0, 1: 0.25, 2: 0.50, 3: 0.75, 4: 1.0}, "dryness": 0, "car": "H"}
]


STATES = {
    "Tree":     TREE,
    "Shrub":     SHRUB,
    "Grass":    GRASS,
    "Ashes":   ASHES,
    "River":    WATER,
    "Lake":     WATER,
    "Pond":     WATER,
    "Bridge":     BRIDGE,
    "House":     HOUSE
}