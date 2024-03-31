from vk.entities.upload import UploadPhotoInput, UploadPhotoOutput
from vk.methods.base import VkApiResponse, VkBaseMethod


class UploadPhoto(VkBaseMethod[UploadPhotoInput, UploadPhotoOutput]):
    __input__ = UploadPhotoInput
    __output__ = UploadPhotoOutput
    __method__ = None

    async def __call__(
        self,
        params: UploadPhotoInput,
    ) -> VkApiResponse[UploadPhotoOutput]:
        filepath = params.filepath
        with open(filepath, "rb") as f:
            files = {"file": (filepath, f)}
            resp = await self.client.post(params.upload_url, files=files)
            return await self.check_response({"response": resp.json()})
