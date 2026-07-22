from pathlib import Path
from app.models.framework import Framework
from app.services.file_loader import FileLoader

       

class FrameworkLoader:

    @staticmethod
    def load(path: str | Path) -> Framework:
        data = FileLoader.load_yaml(path)

        return Framework.model_validate(data)
        

        


        

   
       



    