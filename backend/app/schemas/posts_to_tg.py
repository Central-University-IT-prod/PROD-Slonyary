from pydantic import BaseModel


class PostsToTgChannelsCreate(BaseModel):
    post_id: int
    channel_id: int
