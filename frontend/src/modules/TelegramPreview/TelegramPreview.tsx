import {FC} from "react";
import {TelegramImagesGrid} from "./TelegramImagesGrid.tsx";
import s from './TelegramPreview.module.scss'
import Tail from "./Tail.tsx";
import {TelegramBg} from "./TelegramBg.tsx";

type Props = {
  htmlText: string,
  images?: string[]
}

export const TelegramPreview: FC<Props> = (props) => {
  return (
    <aside className={s.main}>
      <h5>Предпросмотр</h5>
      <div className={s.telegramMessage}>
        {props.images &&
            <TelegramImagesGrid images={props.images}/>
        }
        <div dangerouslySetInnerHTML={{__html: props.htmlText}} className={s.textContainer}></div>
        <Tail className={s.tail}/>
      </div>
      <TelegramBg className={s.background}/>
    </aside>
  )

};
