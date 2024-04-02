import {FC} from 'react'
// @ts-ignore
import s from './PostItem.module.scss'
import {Avatar, AvatarGroup, ImageList, ImageListItem} from '@mui/material'
import {MediaProvider} from '../MediaProvider/MediaProvider'
import MediaView from '../../Ui/MediaView/MediaView'
import {IPostRequest, postsAPI} from "../../store/services/PostsService.ts";

export const PostItem: FC<{
  data: IPostRequest
}> = ({data}) => {
  const [acceptPost, {isLoading, isError, error}] = postsAPI.useAcceptPostMutation()

  const {
    id,
    owner_name: admin,
    status: category,
    publish_time: date,
    html_text: htmlText,
    photos: postImages,
    channels,
    is_owner: isOwner
  } = data
  let rightText
  switch (category) {
    case 'pending':
      rightText = 'Не опубликован'
      break
    case 'published':
      rightText = 'Опубликован'
      break
    case 'moderation':
      rightText = 'На модерации'
  }

  const dateOptions = {
    year: '2-digit',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }

  return (
    <article className={s.post}>
      <div className={s.postInner}>
        <div className={s.postHeader}>
          <div className={s.left}>
            <AvatarGroup max={2}>
              {channels?.map((channel: any, index: number) => (
                <Avatar src={channel.avatar} key={index}>
                  CH
                </Avatar>
              ))}
            </AvatarGroup>
            <div className={s.leftText}>
              <h4>{channels.length === 1 ? channels[0].name : 'В нескольких каналах'}</h4>
              <p>{new Date(date).toLocaleString('ru-RU', dateOptions).replace(',', '')}</p>
            </div>
          </div>
          <div className={s.right}>
            <div className={`${s.publicised} ${s[category]}`}>
              <div></div>
              <span>{rightText}</span>
            </div>
            <p className={s.adminName}>{admin}</p>
          </div>
        </div>
        {postImages.length !== 0 && (
          <ImageList
            sx={{
              width: '100%',
              borderRadius: '20px',
              marginTop: '10px',
              maxWidth: '100%'
            }}
            cols={postImages.length > 3 ? 3 : postImages.length}
          >
            <MediaProvider mediaCount={postImages?.length}>
              {postImages.map((imageSrc, i) => (
                <MediaView index={i} key={i} src={imageSrc.base64}>
                  <ImageListItem key={i}>
                    <img
                      className={`${s.postImage} loaderImg`}
                      src={`data:image/gif;base64,${imageSrc.base64}`}
                      loading="lazy"
                    />
                  </ImageListItem>
                </MediaView>
              ))}
            </MediaProvider>
          </ImageList>
        )}
        <div dangerouslySetInnerHTML={{__html: htmlText}} className={s.postItemTextContant}></div>
      </div>
      {category === 'pending' && (
        <div className={s.bottomButtons}>
          <button className={`${s.leftButton} ${s.grey}`}>Изменить</button>
          <button className={`${s.rightButton} ${s.orange}`}>
            Опубликовать
          </button>
        </div>
      )}
      {category === 'moderation' && isOwner && (
        <div className={s.bottomButtons}>
          <button className={`${s.leftButton} ${s.red}`}>Отклонить</button>
          <button className={`${s.middleButton} ${s.grey}`}>Изменить</button>
          <button onClick={() => {
            console.log('x')
            acceptPost(id)
          }} className={`${s.rightButton} ${s.green}`}>Принять
          </button>
        </div>
      )}
    </article>
  )
}
