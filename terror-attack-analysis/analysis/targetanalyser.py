# a statistical look at the target for attacks.
class TargetAnalyser(object):

    dbaccessor = None

    def getLocationWithKills(self):
        attacks = self.dbaccessor.getAll()
        attackLocation = []

        for attack in attacks:
            formatAttack = {}
            formatAttack["kills"] = attack["kill_count"]
            formatAttack["city"] = attack["city"]
            formatAttack["description"] = attack["description"]
            try:
                formatAttack["longitude"] = float(attack["longitude"])
                formatAttack["latitude"] = float(attack["latitude"])
            except Exception as e:
                print("could not add long lat so skipped")
                continue
            attackLocation.append(formatAttack)

        return attackLocation


    def __init__(self, dbaccessor):
        self.dbaccessor = dbaccessor
