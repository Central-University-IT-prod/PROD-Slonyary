import { FC } from 'react'
import bibaImg from '../../assets/imgs/biba.jpg'
import s from './PostItem.module.scss'
import { TPostItem } from '../../models/PostsModels.ts'
import { ImageList, ImageListItem } from '@mui/material'
import { MediaProvider } from '../MediaProvider/MediaProvider.tsx'
import MediaView from '../../Ui/MediaView/MediaView.tsx'

export const PostItem: FC<TPostItem> = (props) => {
	const mainEditor = true
	let rightText
	switch (props.category) {
		case 'pending':
			rightText = 'Не опубликован'
			break
		case 'published':
			rightText = 'Опубликован'
			break
		case 'moderation':
			rightText = 'На модерации'
	}

	return (
		<article className={s.post}>
			<div className={s.postInner}>
				<div className={s.postHeader}>
					<div className={s.left}>
						<img src={bibaImg} alt="Аватарка канала" className={s.avatar} />
						<div className={s.leftText}>
							<h4>{props.channelName}</h4>
							<p>{new Date(props.date).toDateString()}</p>
						</div>
					</div>
					<div className={s.right}>
						<div className={`${s.publicised} ${s[props.category]}`}>
							<div></div>
							<span>{rightText}</span>
						</div>
						<p className={s.adminName}>{props.admin}</p>
					</div>
				</div>
				{!!props.postImages?.length && (
					<ImageList
						sx={{ width: '100%', borderRadius: '40px', marginTop: '10px' }}
						cols={props.postImages.length > 3 ? 3 : props.postImages.length}
					>
						<MediaProvider mediaCount={props.postImages?.length}>
							{props.postImages.map((src, i) => (
								<ImageListItem key={i}>
									<MediaView index={i} key={i} src={src}>
										<img className={s.postImage} src={src} loading="lazy" />
									</MediaView>
								</ImageListItem>
							))}
						</MediaProvider>
					</ImageList>
				)}
				{props.htmlText ? (
					props.htmlText
				) : (
					<p className={s.postText}>{props.plainText}</p>
				)}
			</div>
			{props.category === 'pending' && (
				<div className={s.bottomButtons}>
					<button className={`${s.leftButton} ${s.grey}`}>Изменить</button>
					<button className={`${s.rightButton} ${s.orange}`}>
						Опубликовать
					</button>
				</div>
			)}
			{props.category === 'moderation' && mainEditor && (
				<div className={s.bottomButtons}>
					<button className={`${s.leftButton} ${s.red}`}>Отклонить</button>
					<button className={`${s.middleButton} ${s.grey}`}>Изменить</button>
					<button className={`${s.rightButton} ${s.green}`}>Принять</button>
				</div>
			)}
		</article>
	)
}
