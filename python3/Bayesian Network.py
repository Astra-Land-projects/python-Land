# Simple Bayesian Network:
#
# Rain -> WetGrass
#
# P(Rain)
# P(WetGrass | Rain)
# P(WetGrass | NoRain)


P_RAIN = 0.3

P_WET_IF_RAIN = 0.9
P_WET_IF_NO_RAIN = 0.2


def probability_wet_grass():

    return (
        P_WET_IF_RAIN * P_RAIN
        +
        P_WET_IF_NO_RAIN
        * (1 - P_RAIN)
    )


def probability_rain_given_wet():

    p_wet = probability_wet_grass()

    return (
        P_WET_IF_RAIN * P_RAIN
    ) / p_wet


p_wet = probability_wet_grass()

p_rain_given_wet = (
    probability_rain_given_wet()
)


print(
    "P(Wet Grass) =",
    round(p_wet, 4)
)

print(
    "P(Rain | Wet Grass) =",
    round(
        p_rain_given_wet,
        4
    )
)