from vk.methods.base import VkBaseMethod
from vk.entities.get_wall_upload_server import (
    GetWallUploadServerOutput,
    GetWallUploadServerInput,
)


# https://dev.vk.com/ru/method/photos.getWallUploadServer
class GetWallUploadServer(
    VkBaseMethod[
        GetWallUploadServerInput,
        GetWallUploadServerOutput,
    ]
):
    __method__ = "photos.getWallUploadServer"
    __input__ = GetWallUploadServerInput
    __output__ = GetWallUploadServerOutput
