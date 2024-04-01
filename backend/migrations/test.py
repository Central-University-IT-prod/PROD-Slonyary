import sqlalchemy as sa

from shared.database.models import (
    Post,
    PostsToTgChannels,
    TgChannel,
    User,
    UsersToTgChannels,
)
from shared.database.session import db_session_manager


async def test() -> None:

    async with db_session_manager() as session:
        k1rles = User(
            telegram_id=11111,
            username="K11111rLes",
            name="Кирилл",
        )
        jakefish = User(
            telegram_id=22222,
            username="jakeFish22222",
            name="Инсаф",
        )
        session.add(k1rles)
        session.add(jakefish)
        await session.commit()

        channel = TgChannel(
            channel_id=1234567890,
            owner_id=k1rles.id,
            username="testChannel",
            title="testChannel",
            photo_url="https://url.com",
        )
        s_channel = TgChannel(
            channel_id=987654321,
            owner_id=jakefish.id,
            username="sChannel",
            title="sChannel",
            photo_url="http://example.com",
        )
        session.add(channel)
        session.add(s_channel)
        await session.flush()

        user_to_channel = UsersToTgChannels(
            user_id=k1rles.id,
            channel_id=channel.id,
        )
        user_to_s_channel = UsersToTgChannels(
            user_id=jakefish.id,
            channel_id=s_channel.id,
        )
        session.add(user_to_channel)
        session.add(user_to_s_channel)
        await session.flush()

        post = Post(
            owner_id=k1rles.id,
            html_text="<h>Привет</h>",
            plain_text="Привет",
        )
        s_post = Post(
            owner_id=jakefish.id,
            html_text="<h>Странно</h>",
            plain_text="Странно",
        )
        session.add(post)
        session.add(s_post)
        await session.flush()

        post_to_channel = PostsToTgChannels(post_id=post.id, channel_id=channel.id)
        s_post_to_channel = PostsToTgChannels(
            post_id=s_post.id, channel_id=s_channel.id
        )
        session.add(post_to_channel)
        session.add(s_post_to_channel)
        await session.flush()

        invite = UsersToTgChannels(
            user_id=jakefish.id,
            channel_id=channel.id,
        )
        session.add(invite)
        await session.flush()

        await session.commit()


async def test_query() -> None:
    await test()
    user_id = 2
    query = sa.select(Post).where(
        Post.id.in_(
            sa.select(PostsToTgChannels.post_id).where(
                PostsToTgChannels.channel_id.in_(
                    sa.select(TgChannel.id).where(
                        sa.or_(
                            TgChannel.id.in_(
                                sa.select(UsersToTgChannels.channel_id).where(
                                    UsersToTgChannels.user_id == user_id
                                )
                            ),
                            TgChannel.owner_id == user_id,
                        )
                    )
                )
            )
        )
    )
    async with db_session_manager() as session:
        posts = await session.scalars(query)
        print(*list(posts), "\n", sep="\n")

        query = sa.select(User).where(User.id == 2)
        user = await session.scalar(query)
        for tg_ch in user.tg_channels:
            tg_ch: TgChannel
            for post in tg_ch.posts:
                post: Post
                print(post)
