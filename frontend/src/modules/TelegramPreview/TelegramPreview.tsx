import {Dispatch, FC, SetStateAction} from "react";
import {TelegramImagesGrid} from "./TelegramImagesGrid.tsx";
import s from './TelegramPreview.module.scss'
import Tail from "./Tail.tsx";
import {TelegramBg} from "./TelegramBg.tsx";
import CancelIcon from '@mui/icons-material/Cancel';

type Props = {
  htmlText: string,
  images?: string[],
  showFunction: Dispatch<SetStateAction<boolean>>
}

export const TelegramPreview: FC<Props> = (props) => {
  return (
    <aside className={s.main}>
      <div className={s.header}>
        <h5>Предпросмотр</h5>
        <button onClick={() => props.showFunction(false)}><CancelIcon/></button>
      </div>
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
