import AddPostForm from '../../modules/AddPostForm/AddPostForm.tsx'
import s from './AddPostPage.module.scss'
import { TelegramPreview } from '../../modules/TelegramPreview/TelegramPreview.tsx'

const AddPostPage = () => {
	return (
		<section className={s.main}>
			<AddPostForm />
			{false && (
				<>
					<div className={s.popup}>
						<div className={s.background}></div>
						<TelegramPreview
							htmlText={
								'ыэвдаьдлтпп фыщжвта фыовтмфытащ тфывтс фыдвл тфыдалсф ыдвс фдывт'
							}
						/>
					</div>
				</>
			)}
		</section>
	)
}

export default AddPostPage
