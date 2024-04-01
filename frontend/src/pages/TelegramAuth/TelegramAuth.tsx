// @ts-ignore
import TelegramLoginButton from 'react-telegram-login'
import { FC } from 'react'
import axios from 'axios'
import { BACKEND_HOST } from '../../constants'
import { useActions } from '../../hooks/useActions'

export const TelegramAuth: FC = () => {
	const { setUser } = useActions()
	const handleTelegramResponse = async (response: any) => {
		console.log(response)
		const user = response?.user
		if (user) {
			setUser(user)
		}

		const res = await axios.post(`http://${BACKEND_HOST}/api/auth`, {
			body: user
		})
		console.log(res)
		if (res) {
			localStorage.setItem('accessToken', res.data.token)
		}
	}

	return (
		<TelegramLoginButton
			dataOnauth={handleTelegramResponse}
			botName="StackSMM_Bot"
		/>
	)
}
