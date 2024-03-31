import { useEffect, useMemo } from 'react'
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

	useEffect(() => {
		const body = document.querySelector('body')
		body?.setAttribute('theme', themeMode)
	}, [themeMode])

	return (
		<div className="App">
			<ThemeProvider theme={theme}>
				<Outlet />
			</ThemeProvider>
		</div>
	)
}

export default App
