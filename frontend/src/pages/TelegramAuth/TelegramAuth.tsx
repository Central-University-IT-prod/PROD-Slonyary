// @ts-ignore
import TelegramLoginButton from 'react-telegram-login'
import { FC } from 'react'


export const TelegramAuth: FC = () => {
	const handleTelegramResponse = (response: any) => {
		console.log(response)
	}

	return <TelegramLoginButton dataOnauth={handleTelegramResponse} botName='StackSMM_Bot' />
}
