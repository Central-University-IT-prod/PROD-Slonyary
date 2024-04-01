import { FC } from 'react'
import { TelegramImagesGrid } from './TelegramImagesGrid.tsx'
import s from './TelegramPreview.module.scss'
import Tail from './Tail.tsx'
import { TelegramBg } from './TelegramBg.tsx'

type Props = {
	htmlText: string
	images?: string[]
}

export const TelegramPreview: FC<Props> = ({ htmlText, images }) => {
	return (
		<aside className={s.main}>
			<h5>Предпросмотр</h5>
			<div className={s.telegramMessage}>
				{images && <TelegramImagesGrid images={images} />}
				<div
					dangerouslySetInnerHTML={{ __html: htmlText }}
					className={s.textContainer}
				></div>
				<Tail className={s.tail} />
			</div>
			<TelegramBg className={s.background} />
		</aside>
	)
}
