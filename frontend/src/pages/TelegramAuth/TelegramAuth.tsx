// @ts-ignore
import TelegramLoginButton from 'react-telegram-login'
import { FC } from 'react'
import axios from 'axios'
import { BACKEND_HOST } from '../../constants'
import { useActions } from '../../hooks/useActions'

export const TelegramAuth: FC = () => {
	const { setUser } = useActions()
	const handleTelegramResponse = async (response: any) => {
		if (response) {
			setUser(response)

			const res = await axios.post(`http://${BACKEND_HOST}/auth`, {
				id: 860014279,
				first_name: 'Стас',
				username: 'strevesuksess',
				photo_url:
					'https://t.me/i/userpic/320/7YeNB5xPCbYNEzk96vXhuwDUpjVeifoP3JxF0zF9MWg.jpg',
				auth_date: 1711962110,
				hash: '6b1fe21be7236d58c69b3211a6bf03a7a7be3fb7393238cad4650a68c8ed3813'
			})
			console.log(res)
			if (res) {
				localStorage.setItem('accessToken', res.data.token)
			}
		}
	}

	return (
		<>
			<TelegramLoginButton
				dataOnauth={handleTelegramResponse}
				botName="StackSMM_Bot"
			/>
		</>
	)
}
