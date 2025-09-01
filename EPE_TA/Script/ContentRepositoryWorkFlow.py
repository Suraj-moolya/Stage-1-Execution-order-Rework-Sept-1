"""ContentRepositoryWorkFlow"""  

import Applicationutility
import Contentrepositoryutility
import Engineeringclientutility


class ContentRepositoryWorkFlow:
    """ContentRepositoryWorkFlow"""

    def expandnodecontentrepository(self,identifiers):
      """expandnodecontentrepository"""
      try:
          Contentrepositoryutility.Expand_nodes_ContentRepository(identifiers)
      except Exception as ex:
          raise Exception(ex) from ex
          
    def selectfolderscontentrepository(self,param):
      """selectmultiplefolders"""
      try:
          Contentrepositoryutility.Select_multiple_folders(param)
      except Exception as ex:
          raise Exception(ex) from ex
          
    def verifyfolderscontentrepository(self,param):
      """verifySelectmultiplefolders"""
      try:
          Contentrepositoryutility.verify_Select_multiple_folders_EC(param)
      except Exception as ex:
          raise Exception(ex) from ex
          
          
    def propertywindowcontentrepository(self):
          """propertywindow"""
          try:
              Contentrepositoryutility.Property_Window()
          except Exception as ex:
              raise Exception(ex) from ex  
