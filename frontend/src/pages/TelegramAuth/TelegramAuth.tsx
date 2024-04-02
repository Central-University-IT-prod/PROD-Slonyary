// @ts-ignore
import TelegramLoginButton from 'react-telegram-login'
import {FC} from 'react'
import axios from 'axios'
import {BACKEND_HOST} from '../../constants'
import {useActions} from '../../hooks/useActions'
import './TelegramAuth.scss'

export const TelegramAuth: FC = () => {
  const {setUser} = useActions()
  const handleTelegramResponse = async (response: any) => {
    if (response) {
      setUser(response)

      const res = await axios.post(`http://${BACKEND_HOST}/auth`, {
        ...response
      })

      if (res) {
        localStorage.setItem('accessToken', res.data.token)
      }
    }
  }

  return (
    <div className="TelegramAuth">
      <h4>Зарегистрируйтесь через телеграмм:</h4>
      <TelegramLoginButton
        dataOnauth={handleTelegramResponse}
        botName="StackSMM_Bot"
      />
    </div>
  )
}
