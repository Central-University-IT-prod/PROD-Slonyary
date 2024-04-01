from pydantic import BaseModel


class UsersToTgChannelsCreate(BaseModel):
    user_id: int
    tg_channel_id: int
