def electricityCalc(electricity):
    electricityCO = float(electricity) * 0.04554
    return electricityCO

def naturalGasCalc(natural_gas):
    natural_gasCO = float(natural_gas) * 0.11337931034
    return natural_gasCO

def heatingOilCalc(heating_oil):
    heating_oilCO = float(heating_oil) * 0.0380625
    return heating_oilCO

def milesDrivenCalc(miles_driven):
    miles_drivenCO = float(miles_driven) * 0.0003564
    return miles_drivenCO

def milesFlownCalc(miles_flown):
    miles_flownCO = float(miles_flown) * 0.0002
    return miles_flownCO

def milesTrainCalc(miles_train):
    miles_trainCO = float(miles_train) * 0.000135
    return miles_trainCO

def milesBusCalc(miles_bus):
    miles_busCO = float(miles_bus) * 0.000059
    return miles_busCO

def hotelNightsCalc(hotel_nights):
    hotel_nightsCO = float(hotel_nights) * 0.01513
    return hotel_nightsCO

def FootprintTotal(electricity, natural_gas, heating_oil, miles_driven, miles_flown, miles_train, miles_bus, hotel_nights):
    totalCO = electricityCalc(electricity) + naturalGasCalc(natural_gas) + \
    heatingOilCalc(heating_oil) + milesDrivenCalc(miles_driven) + \
    milesFlownCalc(miles_flown) + milesTrainCalc(miles_train) + \
    milesBusCalc(miles_bus) + hotelNightsCalc(hotel_nights) + 2.545
    return totalCO
