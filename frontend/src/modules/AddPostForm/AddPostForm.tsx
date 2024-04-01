import React, { FC, useCallback, useMemo, useState } from 'react'
import {
	CompositeDecorator,
	ContentBlock,
	ContentState,
	DraftDecorator,
	DraftEntityMutability,
	DraftEntityType,
	Editor,
	EditorState,
	RichUtils
} from 'draft-js'
import { stateToHTML } from 'draft-js-export-html'
import { Button, CircularProgress, Grid, TextField } from '@mui/material'
import FormatBoldIcon from '@mui/icons-material/FormatBold'
import FormatItalicIcon from '@mui/icons-material/FormatItalic'
import FormatUnderlinedIcon from '@mui/icons-material/FormatUnderlined'
import FormatStrikethroughIcon from '@mui/icons-material/FormatStrikethrough'
import LinkIcon from '@mui/icons-material/Link'
import ImageIcon from '@mui/icons-material/Image'
import './AddPostForm.scss'
import ImageTable from '../ImageTable/ImageTable'
import { getSpellcheckingWords } from './API'
import useModal from '../../hooks/useModal'
import { channelsAPI } from '../../store/services/ChannelService'
import { CheckBox } from '@mui/icons-material'

const AddPostForm: FC = () => {
	const [date, setDate] = useState('')
	const [time, setTime] = useState('00:00')

	const maxLength = 9
	type LinkProps = {
		children: React.ReactNode
		contentState: ContentState
		entityKey: string
	}

	const Link: FC<LinkProps> = ({ contentState, entityKey, children }) => {
		const { url } = contentState.getEntity(entityKey).getData()

		const handlerClick = () => alert(`URL: ${url}`)

		return (
			<a href={url} onClick={handlerClick}>
				{children}
			</a>
		)
	}

	const decorator: DraftDecorator = {
		strategy: findLinkEntities,
		component: Link
	}

	const dec = new CompositeDecorator([decorator])
	const [editorState, setEditorState] = useState<EditorState>(() =>
		EditorState.createEmpty(dec)
	)

	enum InlineStyle {
		BOLD = 'BOLD',
		ITALIC = 'ITALIC',
		UNDERLINE = 'UNDERLINE',
		STRIKE = 'STRIKETHROUGH'
	}

	const handleKeyCommand = (command: string, editorState: EditorState) => {
		const newState = RichUtils.handleKeyCommand(editorState, command)
		if (newState) {
			setEditorState(newState)
			return 'handled'
		}
		return 'not-handled'
	}

	const onBoldClick = () => {
		setEditorState(RichUtils.toggleInlineStyle(editorState, InlineStyle.BOLD))
	}

	const onItalicClick = () => {
		setEditorState(RichUtils.toggleInlineStyle(editorState, InlineStyle.ITALIC))
	}

	const onUnderLineClick = () => {
		setEditorState(
			RichUtils.toggleInlineStyle(editorState, InlineStyle.UNDERLINE)
		)
	}

	const onStrikeClick = () => {
		setEditorState(RichUtils.toggleInlineStyle(editorState, InlineStyle.STRIKE))
	}

	const getText = () => {
		const contentState = editorState.getCurrentContent()
		let html = stateToHTML(contentState)
		const text = contentState.getPlainText()

		let publish_time

		if (!date) {
			publish_time = null
		} else {
			const [day, month, year] = date.split('.')
			const [hours, minut] = time.split(':')
			publish_time = new Date(
				+year,
				+month - 1,
				+day,
				+hours,
				+minut
			).toISOString()
		}

		const formData = new FormData()
		for (let index = 0; index < files.length; index++) {
			const element = files[index]
			formData.append('file', element)
		}

		formData.append('plain_text', text)
		formData.append('html_text', html)
	}

	const addEntity = useCallback(
		(
			entityType: DraftEntityType,
			data: Record<string, string>,
			mutability: DraftEntityMutability
		) => {
			setEditorState((currentState) => {
				const contentState = currentState.getCurrentContent()
				const contentStateWithEntity = contentState.createEntity(
					entityType,
					mutability,
					data
				)
				const entityKey = contentStateWithEntity.getLastCreatedEntityKey()
				const newState = EditorState.set(currentState, {
					currentContent: contentStateWithEntity
				})
				return RichUtils.toggleLink(
					newState,
					newState.getSelection(),
					entityKey
				)
			})
		},
		[]
	)

	const addLink = useCallback(
		(url: string) => addEntity('link', { url }, 'MUTABLE'),
		[addEntity]
	)

	const handlerAddLink = () => {
		const url = prompt('URL:')

		if (!url) return
		addLink(url)
	}
	type TypeFileList = FileList | null

	function findLinkEntities(
		contentBlock: ContentBlock,
		callback: (start: number, end: number) => void,
		contentState: ContentState
	): void {
		contentBlock.findEntityRanges((character) => {
			const entityKey = character.getEntity()
			return (
				entityKey !== null &&
				contentState.getEntity(entityKey).getType() === 'link'
			)
		}, callback)
	}

	const [files, setFiles] = useState<File[]>([])

	const onDragEnter = (e: any) => {
		e.preventDefault()
		e.stopPropagation()
	}

	const filterFiles = (newFiles: TypeFileList): File[] => {
		if (!newFiles) return []

		const res: File[] = [...files]
		for (let index = newFiles.length - 1; index >= 0; index--) {
			const file = newFiles[index]

			if (res.length === maxLength) break

			if ('image/jpeg,image/png'.split(',').includes(file.type)) {
				res.push(file)
			} else {
			}
		}
		return res
	}

	const onDrop = (e: any) => {
		e.preventDefault()
		e.stopPropagation()
		setFiles(filterFiles(e.dataTransfer.files))
	}

	const changeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
		e.preventDefault()
		e.stopPropagation()
		const input = document.querySelector(
			'#upload-postImage'
		) as HTMLInputElement
		setFiles(filterFiles(input.files))
	}

	const deleteMedia = (
		e: React.MouseEvent<HTMLButtonElement>,
		index: number
	) => {
		e.preventDefault()
		e.stopPropagation()

		const arrFiles = [...files]
		arrFiles.splice(index, 1)
		setFiles(arrFiles)
	}

	const [spellcheckingString, setSpellcheckingString] = useState<string>('')
	const [isSpellcheckingLoading, setIsSpellcheckingLoading] =
		useState<boolean>(false)

	const { setModal } = useModal('TELEGRAM-PREVIEW', null, {})

	const spellchecking = async () => {
		setIsSpellcheckingLoading(true)

		const contentState = editorState.getCurrentContent()
		const html = stateToHTML(contentState)
		const words = await getSpellcheckingWords(html)

		let text = html
		let displacement = 0

		for (let index = 0; index < words.length; index++) {
			const element = words[index]
			const { pos, len, s } = element
			const word = s[0].replace(/^,+/, '')

			const leftStr = text.slice(0, pos + displacement)
			const rightStr = text.slice(pos + len + displacement)

			text = leftStr + word + rightStr
			const newDisplacement = word.length - len
			displacement += newDisplacement
		}

		setSpellcheckingString(text)
		setIsSpellcheckingLoading(false)
	}

	const spellcheckingBtnDisabled = useMemo(
		() => editorState.getCurrentContent().getPlainText().trim().length < 2,
		[editorState]
	)

	const { data: channels } = channelsAPI.useGetChannelsQuery(null)
	const [targetChannels, settargetChannels] = useState<
		{ type: string; id: number }[]
	>([])
	const setChannel = (
		e: React.ChangeEvent<HTMLInputElement>,
		channelId: number
	) => {
		console.log(e)
		const newList = targetChannels
		newList.push({ type: 'tg', id: channelId })
	}

	const onDragOver = (e: any) => e.preventDefault()
	return (
		<div className="AddPostForm">
			<ImageTable deleteImage={deleteMedia} files={files} />
			<label
				className="fileInputLabel"
				htmlFor="upload-postImage"
				onDragEnter={onDragEnter}
				onDrop={onDrop}
				onDragOver={onDragOver}
			>
				<ImageIcon />
				<h4>Добавить</h4>
			</label>
			<h2>Текст поста</h2>
			<p>Выделите текст и нажмите на кнопку стиля или ссылки.</p>
			<input
				type="file"
				maxLength={maxLength}
				name="upload-postImage"
				id="upload-postImage"
				style={{ display: 'none' }}
				onChange={changeInput}
				multiple
				hidden
				accept="image/jpeg,image/png"
			/>
			<div className="AddPostForm-buttonGroup">
				<button onClick={onBoldClick}>
					<FormatBoldIcon />
				</button>
				<button onClick={onItalicClick}>
					<FormatItalicIcon />
				</button>
				<button onClick={onUnderLineClick}>
					<FormatUnderlinedIcon />
				</button>
				<button onClick={onStrikeClick}>
					<FormatStrikethroughIcon />
				</button>
				<button onClick={handlerAddLink}>
					<LinkIcon />
				</button>
			</div>
			<div className="AddPost_input">
				<Editor
					editorState={editorState}
					handleKeyCommand={handleKeyCommand}
					onChange={setEditorState}
				/>
			</div>
			<Grid container spacing="10px" sx={{ mt: '10px' }}>
				<Grid item xl={6} lg={6} md={6} sm={6} xs={12}>
					<TextField
						fullWidth
						size="small"
						type="date"
						placeholder="Дата публикации"
						sx={{
							display: 'flex',
							alignItems: 'flex-end'
						}}
					/>
				</Grid>
				<Grid item xl={6} lg={6} md={6} sm={6} xs={12}>
					<TextField
						fullWidth
						size="small"
						placeholder="Время публикации"
						type="time"
						sx={{
							display: 'flex',
							alignItems: 'flex-end'
						}}
					/>
				</Grid>
			</Grid>
			<div className="AddPostForm-btnsbox">
				<Button
					variant="contained"
					onClick={spellchecking}
					disabled={spellcheckingBtnDisabled}
				>
					Проверить орфографию
				</Button>
				<Button
					variant="contained"
					disabled={spellcheckingBtnDisabled}
					onClick={() =>
						setModal({
							htmlText: stateToHTML(editorState.getCurrentContent()),
							images: files
						})
					}
				>
					Показать превью
				</Button>
				<Button variant="contained" onClick={getText}>
					Продолжить
				</Button>
				<Button variant="contained" onClick={getText}>
					Отправить
				</Button>
			</div>
			{spellcheckingString.length ? (
				<div className="AddPostForm-spellchecking-box">
					{isSpellcheckingLoading ? (
						<CircularProgress sx={{ margin: 'auto', display: 'block' }} />
					) : (
						<>
							<h3>Отредактированный текст:</h3>
							<div
								className="AddPostForm-spellchecking"
								dangerouslySetInnerHTML={{ __html: spellcheckingString }}
							></div>
						</>
					)}
				</div>
			) : (
				''
			)}
			<div className="chanelsToPost">
				{channels?.map((channel: ChannelItem) => {
					return (
						<div className="chanelsToPost-item" key={channel.id}>
							<CheckBox onChange={(e: any) => setChannel(e, channel.id)} />
							<img src={channel.url} />
							<h3>{channel.name}</h3>
						</div>
					)
				})}
			</div>
		</div>
	)
}

export default AddPostForm
