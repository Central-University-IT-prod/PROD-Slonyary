// @ts-ignore

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
import { Button, CircularProgress } from '@mui/material'
import FormatBoldIcon from '@mui/icons-material/FormatBold'
import FormatItalicIcon from '@mui/icons-material/FormatItalic'
import FormatUnderlinedIcon from '@mui/icons-material/FormatUnderlined'
import FormatStrikethroughIcon from '@mui/icons-material/FormatStrikethrough'
import LinkIcon from '@mui/icons-material/Link'
import './AddPostForm.scss'
import { getSpellcheckingWords } from '../AddPostForm/API'

const AddPostForm: FC = () => {
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

	const getText = async () => {
		//const contentState = editorState.getCurrentContent()
		//let html = stateToHTML(contentState)
		//const text = contentState.getPlainText()
		//const data = {
		//	plain_text: text,
		//	html_text: html
		//}
		//const t = await addMessages(data, formData)
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

	const [spellcheckingString, setSpellcheckingString] = useState<string>('')
	const [isSpellcheckingLoading, setIsSpellcheckingLoading] =
		useState<boolean>(false)

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

	const mainBtn = useMemo(
		() => editorState.getCurrentContent().getPlainText().trim().length > 0,
		[editorState]
	)

	return (
		<div className="AddPostForm">
			<h2>Текст поста</h2>
			<p>Выделите текст и нажмите на кнопку стиля или ссылки.</p>
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
			<div className="AddPostForm-btnsbox">
				<Button variant="contained" onClick={spellchecking} disabled={mainBtn}>
					Проверить орфографию
				</Button>
				<Button
					variant="contained"
					disabled={mainBtn}
					className="main-btn"
					onClick={getText}
				>
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
		</div>
	)
}

export default AddPostForm
