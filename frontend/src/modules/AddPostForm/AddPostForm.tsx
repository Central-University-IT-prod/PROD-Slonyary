import { useState } from "react";
import { Editor, EditorState, RichUtils } from "draft-js";
import { stateToHTML } from "draft-js-export-html";
import { Button, ButtonGroup, Grid, TextField } from "@mui/material";
import FormatBoldIcon from "@mui/icons-material/FormatBold";
import FormatItalicIcon from "@mui/icons-material/FormatItalic";
import FormatUnderlinedIcon from "@mui/icons-material/FormatUnderlined";
import PageElement from "../../Ui/PageElement/PageElement";
import FormatStrikethroughIcon from "@mui/icons-material/FormatStrikethrough";
import "./AddPostForm.css";

function AddPostForm() {
	const [editorState, setEditorState] = useState<EditorState>(() =>
		EditorState.createEmpty()
	);

	enum InlineStyle {
		BOLD = "BOLD",
		ITALIC = "ITALIC",
		UNDERLINE = "UNDERLINE",
		STRIKE = "STRIKETHROUGH",
	}

	const handleKeyCommand = (command: string, editorState: EditorState) => {
		const newState = RichUtils.handleKeyCommand(editorState, command);
		if (newState) {
			setEditorState(newState);
			return "handled";
		}
		return "not-handled";
	};

	const onBoldClick = () => {
		setEditorState(
			RichUtils.toggleInlineStyle(editorState, InlineStyle.BOLD)
		);
	};

	const onItalicClick = () => {
		setEditorState(
			RichUtils.toggleInlineStyle(editorState, InlineStyle.ITALIC)
		);
	};

	const onUnderLineClick = () => {
		setEditorState(
			RichUtils.toggleInlineStyle(editorState, InlineStyle.UNDERLINE)
		);
	};

	const onStrikeClick = () => {
		setEditorState(
			RichUtils.toggleInlineStyle(editorState, InlineStyle.STRIKE)
		);
	};

	const getText = () => {
		const contentState = editorState.getCurrentContent();
		let html = stateToHTML(contentState);
		const text = contentState.getPlainText();
		console.log(html, text);
	};

	return (
		<PageElement>
			<ButtonGroup
				sx={{ justifyContent: "center", display: "flex" }}
				variant="outlined"
				aria-label="Basic button group"
			>
				<Button onClick={onBoldClick}>
					<FormatBoldIcon />
				</Button>
				<Button onClick={onItalicClick}>
					<FormatItalicIcon />
				</Button>
				<Button onClick={onUnderLineClick}>
					<FormatUnderlinedIcon />
				</Button>
				<Button onClick={onStrikeClick}>
					<FormatStrikethroughIcon />
				</Button>
			</ButtonGroup>

			<div className="AddPost_input">
				<Editor
					editorState={editorState}
					handleKeyCommand={handleKeyCommand}
					onChange={setEditorState}
				/>
			</div>
			<Grid container spacing="10px" sx={{ mt: "10px" }}>
				<Grid item xl={6} lg={6} md={6} sm={6} xs={12}>
					<TextField
						fullWidth
						size="small"
						placeholder="Дата публикации"
						sx={{
							display: "flex",
							alignItems: "flex-end",
						}}
					/>
				</Grid>
				<Grid item xl={6} lg={6} md={6} sm={6} xs={12}>
					<TextField
						fullWidth
						size="small"
						placeholder="Время публикации"
						sx={{
							display: "flex",
							alignItems: "flex-end",
						}}
					/>
				</Grid>
			</Grid>

			<Button
				variant="contained"
				sx={{
					mt: "15px",
					ml: "auto",
					display: "block",
					fontWeight: 600,
				}}
				onClick={getText}
			>
				Отправить
			</Button>
		</PageElement>
	);
}

export default AddPostForm;
