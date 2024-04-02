import s from './Channel.module.scss'
import {FC, useState} from "react";
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import {Button} from "@mui/material";
import {Link} from "react-router-dom";
import {NavigatePath, paths} from "../../routes.ts";

type Props = {
  title: string
  subscribers: number
  avatar: string
  posts: {
    pending: number
    moderation: number
  },
}

const Channel: FC<Props> = (props) => {
  const [showPopup, setShowPopup] = useState<boolean>(false)

  return (
    <article className={s.main}>
      <div className={s.avatarContainer}>
        <img src={props.avatar} alt="" className={s.avatar}/>
      </div>
      <div className={s.aboutChannel}>
        <h5 className={s.title}>{props.title}</h5>
        <p className={s.subscribers}>{props.subscribers} Подписчика</p>
      </div>
      <div className={s.posts}>
        <h5 className={s.postTitle}>Посты</h5>
        <div className={s.postStatus}>
          <div className={s.pending}></div>
          <p>Ожидают отправки: {props.posts.pending}</p>
        </div>
        <div className={s.postStatus}>
          <div className={s.moderation}></div>
          <p>На модерации: {props.posts.moderation}</p>
        </div>
      </div>
      <div className={s.actions}>
        <button onClick={() => setShowPopup(show => !show)}>
          <MoreHorizIcon sx={{fontSize: 50}} color='primary'/>
        </button>
        {
          showPopup &&
            <div className={s.popup}>
                <Link to={NavigatePath(paths.CHANNEL_INFO) + '1'}>
                    <Button variant='contained'>Открыть</Button>
                </Link>
                <Button variant='contained'>Удалить</Button>
            </div>
        }
      </div>
    </article>
  )
}

export default Channel
