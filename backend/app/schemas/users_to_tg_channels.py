from pydantic import BaseModel


class UsersToTgChannelsCreate(BaseModel):
    user_id: int
    channel_id: int
