
def buildAttack(
    eventId,
    year,
    month,
    day,
    countryId,
    countryName,
    regionId,
    regionName,
    state,
    city,
    latitude,
    longitude,
    description):

    return {
        "event_id" : eventId,
        "year" : year,
        "month" : month,
        "day" : day,
        "country_id" : countryId,
        "country_name" : countryName,
        "region_id" : regionId,
        "region_name" : regionName,
        "state" : state,
        "city" : city,
        "latitude" : latitude,
        "longitude" : longitude,
        "description" : description
    }
