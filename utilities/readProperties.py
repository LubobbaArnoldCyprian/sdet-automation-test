import configparser

config = configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
config.read(".//Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getArtsCraftsAssertions():
        artsAssertion = config.get('common info', 'assertArtsCrafts')
        return artsAssertion

    @staticmethod
    def getBeadingJewelryAssertions():
        beadingAssertion = config.get('common info', 'assertBeadingJewelry')
        return beadingAssertion

    @staticmethod
    def getCraftSewingAssertions():
        craftAssertion = config.get('common info', 'assertCraftsSewing')
        return craftAssertion
