from pathlib import Path

from src.controllers.basecontrooller import basecomtroller

class DataController(basecomtroller):
    def __init__(self):
        super().__init__()

    def validate(self, project_id: str, file):
        if not project_id.strip():
            raise ValueError("Project ID is required.")     
        if file is None:
            raise ValueError("File is required.")
        extension = Path(file.filename or "").suffix.lower().lstrip(".")
        allowed_extensions = {
            item.lower().lstrip(".")
            for item in self.settings.File_allowed_extensions
        }
        if extension not in allowed_extensions:
            raise ValueError(f"File extension '{extension}' is not allowed.")
        if file.size is None:
            raise ValueError("Unable to determine file size.")
        if file.size > self.settings.file_max_size:
            raise ValueError(f"File size exceeds the maximum limit of {self.settings.file_max_size} bytes.")
        return True

