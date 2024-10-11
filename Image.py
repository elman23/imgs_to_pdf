class Image:
    file_name: str
    orientation: str

    def __init__(self, file_name: str, orientation: str = "portrait") -> None:
        self.file_name = file_name
        self.orientation = str(orientation)
