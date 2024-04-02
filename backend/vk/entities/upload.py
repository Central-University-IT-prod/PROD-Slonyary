from vk.entities.base import VkMethodOutputParams


class UploadPhotoInput(VkMethodOutputParams):
    upload_url: str
    filepath: str


class UploadPhotoOutput(VkMethodOutputParams):
    server: int
    photo: str
    hash: str
