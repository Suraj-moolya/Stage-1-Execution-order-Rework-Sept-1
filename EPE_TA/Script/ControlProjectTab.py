"""ControlProjectTab"""
from MapBase import MapBase

class ControlProjectTab(MapBase):
    """ControlProjectTab"""
    
    @property
    def renamefbdsectionwhilecreation(self):
      """renamefbdsectionwhilecreation"""
      return self.get_element("RenameFBDsection_ProjectExplorerTab")
  
      
    @property
    def selectpathoffbdpopup(self):
      """selectpathoffbdpopup"""
      return self.get_element("Pathsfbd_ProjectExplorerTab")