import { createBrowserRouter } from 'react-router-dom'
import { paths } from './routes'
import App from './App'
import RegistrationPage from './pages/RegistrationPage'
import PostPage from './pages/PostPage/PostPage.tsx'
import { TelegramAuth } from './pages/TelegramAuth/TelegramAuth.tsx'
import { ChannelPage } from './pages/ChannelPage/ChannelPage.tsx'
import HomePage from './pages/HomePage.tsx'

export const router = createBrowserRouter([
	{
		element: <App />,
		path: '/',
		children: [
			{
				path: paths.TELEGRAMAUTH,
				element: <TelegramAuth />
			},
			{
				path: paths.REGISTRATION,
				element: <RegistrationPage />
			},
			{
				path: paths.CHANNELS,
				element: <ChannelPage />
			},
			{
				path: paths.HOME,
				element: <HomePage />
			},
			{
				path: paths.POSTS,
				element: <PostPage />
			}
		]
	}
])
