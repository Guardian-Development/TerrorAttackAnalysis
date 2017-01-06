
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
    description,
    targetId,
    targetDescription,
    numberKilled,
    weapon):

    return {
        "_id" : eventId,
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
        "description" : description,
        "target_id" : targetId,
        "target_description" : targetDescription,
        "kill_count" : numberKilled,
        "weapon" : weapon
    }
