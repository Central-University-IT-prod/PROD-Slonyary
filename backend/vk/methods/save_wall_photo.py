from vk.entities.photo import Photo
from vk.methods.base import VkBaseMethod
from vk.entities.save_wall_photo import SaveWallPhotoInput


# https://dev.vk.com/ru/method/photos.saveWallPhoto
class SaveWallPhoto(VkBaseMethod[SaveWallPhotoInput, list[Photo]]):
    __method__ = "photos.saveWallPhoto"
    __input__ = SaveWallPhotoInput
    __output__ = list[Photo]
