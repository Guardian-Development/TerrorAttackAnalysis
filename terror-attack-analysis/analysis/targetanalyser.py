# a statistical look at the target for attacks.
class TargetAnalyser(object):

    dbaccessor = None

    def getLocationWithKills(self):
        attacks = self.dbaccessor.getAll()
        attackLocation = []

        for attack in attacks:
            formatAttack = {}

            try:
                formatAttack["kills"] = int(attack["kill_count"])
            except Exception as e:
                #kills were 0
                formatAttack["kills"] = 0

            formatAttack["city"] = attack["city"]
            formatAttack["region"] = attack["region_name"]
            formatAttack["year"] = attack["year"]
            formatAttack["description"] = attack["description"]

            try:
                formatAttack["longitude"] = float(attack["longitude"])
                formatAttack["latitude"] = float(attack["latitude"])
            except Exception as e:
                #could not convert lat lng
                continue
            attackLocation.append(formatAttack)

        return attackLocation


    def __init__(self, dbaccessor):
        self.dbaccessor = dbaccessor
