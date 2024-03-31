import { createBrowserRouter } from 'react-router-dom'
import { paths } from './routes'
import App from './App'
import RegistrationPage from './pages/RegistrationPage'
import HomePage from './pages/HomePage'
import PostPage from './pages/PostPage'

export const router = createBrowserRouter([
	{
		element: <App />,
		path: '/',
		children: [
			{
				path: paths.REGISTRATION,
				element: <RegistrationPage />
			},
			{
				path: paths.HOME,
				element: <HomePage />
			},
			{
				path: paths.POST,
				element: <PostPage />
			}
		]
	}
])
