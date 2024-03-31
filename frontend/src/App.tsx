import { useEffect, useMemo } from 'react'
import './App.css'
import { Outlet } from 'react-router-dom'
import { ThemeProvider, createTheme, Container } from '@mui/material'
import useAppSelector from './hooks/useAppSelector'
import { Navbar } from './modules/Navbar/Navbar.tsx'

function App() {
	const { mode: themeMode } = useAppSelector((state) => state.theme)

	const theme = useMemo(
		() =>
			createTheme({
				palette: {
					mode: themeMode,
					primary: {
						main: '#5578e3'
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
				<Navbar />
				<Container
					maxWidth={'lg'}
					sx={{ marginTop: '20px' }}
					className="App"
					data-theme={themeMode}
				>
					<Outlet />
				</Container>
			</ThemeProvider>
		</div>
	)
}

export default App
