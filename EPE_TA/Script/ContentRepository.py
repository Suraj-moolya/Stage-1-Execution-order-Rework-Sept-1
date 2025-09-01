"""ContentRepository"""
from MapBase import MapBase

class ContentRepository(MapBase):
    """ContentRepository"""

    @property
    def folderstructurecontentrepository(self):
      """folderstructurecontentrepository"""
      return self.get_element("FolderStructure_ContentRepository")
      
    @property
    def nodepropertiescontentrepository(self):
      """nodepropertiescontentrepository"""
      return self.get_element("NodePropertieWindow_EngineeringClient")
      
    @property
    def contentrepositorytextbox(self):
        """contentrepositorytextbox"""
        return self.get_element("CRtextbox_ContentRepository")
