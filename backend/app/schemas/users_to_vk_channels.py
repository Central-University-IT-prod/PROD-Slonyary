from pydantic import BaseModel


class UsersToVkChannelsCreate(BaseModel):
    user_id: int
    channel_id: int
