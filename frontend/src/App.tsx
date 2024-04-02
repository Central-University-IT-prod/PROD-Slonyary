import {useEffect, useMemo} from 'react'
import './App.css'
import {Outlet} from 'react-router-dom'
import {createTheme, ThemeProvider} from '@mui/material'
import useAppSelector from './hooks/useAppSelector'
import {Navbar} from './modules/Navbar/Navbar.tsx'
import MediaSlider from './modules/MediaSlider/MediaSlider.tsx'
import axios from 'axios'
import {BACKEND_HOST} from './constants.ts'
import {TelegramPreview} from './modules/TelegramPreview/TelegramPreview.tsx'
import {useActions} from './hooks/useActions.ts'
import {ToastContainer} from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const {mode: themeMode} = useAppSelector((state) => state.theme)
  const {type, data} = useAppSelector((state) => state.modal)
  const {setUser} = useActions()

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

  useEffect(() => {
    axios.get(`http://${BACKEND_HOST}/ping`)
    const data = localStorage.getItem('userData')
    if (data) {
      setUser(JSON.parse(data))
    }
  }, [])

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Navbar/>
        <div className="container">
          <Outlet/>
          {type === 'MEDIA-SLIDER-MODAL' && <MediaSlider data={data}/>}
          {type === 'TELEGRAM-PREVIEW' && <TelegramPreview data={data}/>}
        </div>
      </ThemeProvider>
      <ToastContainer
        position="top-center"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
    </div>
  )
}

export default App
