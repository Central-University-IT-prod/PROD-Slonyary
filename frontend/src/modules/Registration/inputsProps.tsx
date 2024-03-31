import { InputAdornment, TextFieldPropsSizeOverrides } from "@mui/material";

type TypeInputs = {
	name: TextFieldPropsSizeOverrides;
	dateBorn: TextFieldPropsSizeOverrides;
	email: TextFieldPropsSizeOverrides;
};

export const inputsProps: TypeInputs = {
	name: {
		size: "small",
		fullWidth: true,
		InputProps: {
			startAdornment: (
				<InputAdornment position="end" sx={{ marginRight: 1 }}>
					I am
				</InputAdornment>
			),
		},
	},
	dateBorn: {
		fullWidth: true,
		size: "small",
		type: "date",
	},
	email: {
		fullWidth: true,
		size: "small",
		type: "email",
		placeholder: "email",
	},
};
