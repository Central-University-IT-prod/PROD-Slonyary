import { FC, useEffect } from 'react'
import Channel from '../../modules/Channel/Channel.tsx'
import { Button } from '@mui/material'
import s from './ChannelPage.module.scss'
import { channelsAPI } from '../../store/services/ChannelService.ts'

export const ChannelPage: FC = () => {
	const { data } = channelsAPI.useGetChannelsQuery(null)

	useEffect(() => {
		console.log(data)
	}, [data])

	return (
		<section>
			<div className={s.buttons}>
				<div className="categorieButton">
					<Button sx={{ borderRadius: '20px' }} variant="contained">
						Телеграм
					</Button>
				</div>
				<a href="https://t.me/StackSMM_Bot?start=add_channel">
					<Button sx={{ bgcolor: '#FFB13C' }} variant="contained">
						Добавить канал
					</Button>
				</a>
			</div>
			<div>
				<Channel
					title="Name channel"
					subscribers={233}
					avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw4UeEjjERyEVTOIaXIKHlj7snPZAKulH5-z1Kau1lsw&s"
					posts={{
						pending: 24,
						moderation: 23
					}}
				/>
			</div>
		</section>
	)
}
