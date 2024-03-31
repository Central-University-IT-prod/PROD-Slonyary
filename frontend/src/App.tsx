import { useMemo } from 'react'
import './App.css'
import { Outlet } from 'react-router-dom'
import { ThemeProvider, createTheme } from '@mui/material'
import useAppSelector from './hooks/useAppSelector'

function App() {
	const { mode: themeMode } = useAppSelector((state) => state.theme)

	const theme = useMemo(
		() =>
			createTheme({
				palette: {
					mode: themeMode,
					primary: {
						main: '#ffdd2d'
					}
				}
			}),
		[themeMode]
	)
	return (
		<div className="App" data-theme={themeMode}>
			<ThemeProvider theme={theme}>
				<Outlet />
			</ThemeProvider>
		</div>
	)
}

export default App
