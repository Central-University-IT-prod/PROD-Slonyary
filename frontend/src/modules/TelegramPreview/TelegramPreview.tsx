import { FC } from 'react'
import { TelegramImagesGrid } from './TelegramImagesGrid.tsx'
import s from './TelegramPreview.module.scss'
import Tail from './Tail.tsx'
import { TelegramBg } from './TelegramBg.tsx'
import useModal from '../../hooks/useModal.ts'
import CloseIcon from '@mui/icons-material/Close'

type Props = {
	htmlText: string
	images?: File[]
}

export const TelegramPreview: FC<{ data: Props }> = ({ data }) => {
	const { htmlText, images } = data
	const { closeOnClickWrapper, setModal } = useModal(
		'',
		`.${s.TelegramPreviewWrapper}`,
		{}
	)

	return (
		<div className={s.TelegramPreviewWrapper} onClick={closeOnClickWrapper}>
			<aside className={s.main}>
				<div className={s.header}>
					<h5>Предпросмотр</h5>
					<button onClick={setModal}>
						<CloseIcon />
					</button>
				</div>
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
		</div>
	)
}
