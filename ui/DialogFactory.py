from gameObjects.gameObjectRepository import GameObjectRepository
from ui.qttraderoutecreator import QtTradeRouteCreator
from ui.qtcampaignproperties import QtCampaignProperties
from ui.qtautoconnectionsettings import QtAutoConnectionSettings
from gameObjects.campaign import Campaign

class DialogFactory:
    '''Produces dialog boxes'''
    def __init__(self, repository: GameObjectRepository):
        self.__repository: GameObjectRepository = repository

    def makeTradeRouteCreationDialog(self) -> QtTradeRouteCreator:
        return QtTradeRouteCreator(self.__repository)

    def makeAutoConnectionSettingsDialog(self) -> QtAutoConnectionSettings:
        return QtAutoConnectionSettings(self.__repository)
        
    def makeCampaignPropertiesDialog(self, campaign: Campaign) -> QtCampaignProperties:
        return QtCampaignProperties(campaign)
