import {createBrowserRouter} from 'react-router-dom'
import {paths} from './routes'
import App from './App'
import PostPage from './pages/PostPage/PostPage.tsx'
import {TelegramAuth} from './pages/TelegramAuth/TelegramAuth.tsx'
import {ChannelPage} from './pages/ChannelPage/ChannelPage.tsx'
import AddPostPage from './pages/AddPostPage/AddPostPage.tsx'
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
        path: paths.CHANNEL_INFO,
        element: <ChannelInfoPage/>
      },
      {
        path: paths.HOME,
        element: <PostPage/>
      }
    ]
  }
])
