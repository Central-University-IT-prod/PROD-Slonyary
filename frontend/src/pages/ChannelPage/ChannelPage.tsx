// @ts-ignore
import {FC} from 'react'
import Channel from '../../modules/Channel/Channel.tsx'
import {Button} from '@mui/material'
import s from './ChannelPage.module.scss'
import {channelsAPI} from '../../store/services/ChannelService.ts'
import {Loading} from "../../modules/Loading/Loading.tsx";

export const ChannelPage: FC = () => {
  const {data: channels, isLoading} = channelsAPI.useGetChannelsQuery(null)

  if (isLoading) return <Loading/>
  return (
    <section>
      <div className={s.buttons}>
        <div className="categorieButton">
          <Button sx={{borderRadius: '20px'}} variant="contained">
            Телеграм
          </Button>
        </div>
        <a href="https://t.me/StackSMM_Bot?start=add_channel">
          <Button sx={{borderRadius: '20px', bgcolor: '#FFB13C'}} variant="contained">
            Добавить канал
          </Button>
        </a>
      </div>
      <div>
        {channels &&
          channels.map((channel: any) => (
            <Channel
              title={channel.name}
              subscribers={channel.subscribers}
              avatar={channel.photo_url}
              posts={{
                pending: channel.on_pending,
                moderation: channel.on_moderation
              }}
              id={channel.id}
            />
          ))}
      </div>
    </section>
  )
}
