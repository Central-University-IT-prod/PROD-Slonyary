import {FC} from "react";
import s from './TelegramPreview.module.scss'

type Props = {
  images: string[]
}

export const TelegramImagesGrid: FC<Props> = (props) => {
  return (
    <div className={`${s.imagesGrid} ${s['length' + props.images.length]}`}>
      {props.images.map((image, index) => (
        <img key={index} src={image} alt=""/>
      ))}
    </div>
  )
}

