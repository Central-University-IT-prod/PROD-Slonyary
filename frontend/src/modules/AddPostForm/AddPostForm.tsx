import React, { FC, useCallback, useState } from 'react'
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
import { Button, Grid, TextField } from '@mui/material'
import FormatBoldIcon from '@mui/icons-material/FormatBold'
import FormatItalicIcon from '@mui/icons-material/FormatItalic'
import FormatUnderlinedIcon from '@mui/icons-material/FormatUnderlined'
import FormatStrikethroughIcon from '@mui/icons-material/FormatStrikethrough'
import LinkIcon from '@mui/icons-material/Link'
import ImageIcon from '@mui/icons-material/Image'
import './AddPostForm.css'
import ImageTable from '../ImageTable/ImageTable'

function AddPostForm() {
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
		console.log(html, text)
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
		/* Блок в котором производилось последнее изменение */
		contentBlock: ContentBlock,
		/* Функция, которая должна быть вызвана с индексами фрагмента текста */
		callback: (start: number, end: number) => void,
		/* Текущая карта контента */
		contentState: ContentState
	): void {
		/* Для каждого символа в блоке выполняем функцию фильтрации */
		contentBlock.findEntityRanges((character) => {
			/* Получаем ключ Entity */
			const entityKey = character.getEntity()
			/* Проверяем что Entity относится к типу Entity-ссылок */
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
				continue
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
			<Button
				variant="contained"
				sx={{
					mt: '15px',
					ml: 'auto',
					display: 'block',
					fontWeight: 600
				}}
				onClick={getText}
			>
				Отправить
			</Button>
		</div>
	)
}

export default AddPostForm
