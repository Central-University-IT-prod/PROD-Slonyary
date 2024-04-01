import { createBrowserRouter } from 'react-router-dom'
import { paths } from './routes'
import App from './App'
<<<<<<< Updated upstream
import PostPage from './pages/PostPage/PostPage.tsx'
import { TelegramAuth } from './pages/TelegramAuth/TelegramAuth.tsx'
import { ChannelPage } from './pages/ChannelPage/ChannelPage.tsx'
import AddPostPage from './pages/AddPostPage/AddPostPage.tsx'

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
				path: paths.ADD_POST,
				element: <AddPostPage />
			},
			{
				path: paths.CHANNELS,
				element: <ChannelPage />
			},
			{
				path: paths.POSTS,
				element: <PostPage />
			}
		]
	}
=======
import HomePage from './pages/HomePage.tsx'
import PostPage from './pages/PostPage/PostPage.tsx'
import {TelegramAuth} from './pages/TelegramAuth/TelegramAuth.tsx'
import {ChannelPage} from './pages/ChannelPage/ChannelPage.tsx'
import AddPostPage from "./pages/AddPostPage/AddPostPage.tsx";
import ChannelInfoPage from "./pages/ChannelInfoPage/ChannelInfoPage.tsx";

export const router = createBrowserRouter([
  {
    element: <App/>,
    path: '/',
    children: [
      {
        path: paths.TELEGRAMAUTH,
        element: <TelegramAuth/>
      },
      {
        path: paths.ADD_POST,
        element: <AddPostPage/>
      },
      {
        path: paths.CHANNELS,
        element: <ChannelPage/>
      },
      {
        path: paths.HOME,
        element: <HomePage/>
      },
      {
        path: paths.POSTS,
        element: <PostPage/>
      },
      {
        path: paths.CHANNEL_INFO,
        element: <ChannelInfoPage/>
      }
    ]
  }
>>>>>>> Stashed changes
])
