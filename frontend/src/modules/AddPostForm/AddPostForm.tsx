import { useCallback, useState } from 'react'
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
import './AddPostForm.css'

function AddPostForm() {
	type LinkProps = {
		children: React.ReactNode
		contentState: ContentState
		entityKey: string
	}

	const Link: React.FC<LinkProps> = ({ contentState, entityKey, children }) => {
		/* Получаем url с помощью уникального ключа Entity */
		const { url } = contentState.getEntity(entityKey).getData()

		const handlerClick = () => {
			alert(`URL: ${url}`)
		}

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
				/* Получаем текущий контент */
				const contentState = currentState.getCurrentContent()
				/* Создаем Entity с данными */
				const contentStateWithEntity = contentState.createEntity(
					entityType,
					mutability,
					data
				)
				/* Получаем уникальный ключ Entity */
				const entityKey = contentStateWithEntity.getLastCreatedEntityKey()
				/* Обьединяем текущее состояние с новым */
				const newState = EditorState.set(currentState, {
					currentContent: contentStateWithEntity
				})
				/* Вставляем ссылку в указанное место */
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
		(url: string) => {
			addEntity('link', { url }, 'MUTABLE')
		},
		[addEntity]
	)

	const handlerAddLink = () => {
		const url = prompt('URL:')

		if (url) {
			addLink(url)
		}
	}

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

	return (
		<div className="AddPostForm">
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
					<FormatStrikethroughIcon />
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
