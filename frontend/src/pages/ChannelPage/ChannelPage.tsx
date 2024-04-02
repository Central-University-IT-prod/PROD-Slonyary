import {FC} from 'react'
import Channel from '../../modules/Channel/Channel.tsx'
import {Button} from '@mui/material'
import s from './ChannelPage.module.scss'
import {channelsAPI} from "../../store/services/ChannelService.ts";

export const ChannelPage: FC = () => {
  const {data: channels} = channelsAPI.useGetChannelsQuery(null)

  return (
    <section>
      <div className={s.buttons}>
        <div className="categorieButton">
          <Button sx={{borderRadius: '20px'}} variant="contained">
            Телеграм
          </Button>
        </div>
        <a href="https://t.me/StackSMM_Bot?start=add_channel">
          <Button sx={{bgcolor: '#FFB13C'}} variant="contained">
            Добавить канал
          </Button>
        </a>
      </div>
      <div>
        {channels && channels.map(channel => <Channel
          title={channel.name}
          subscribers={channel.subscribers}
          avatar={channel.photo_url}
          posts={{
            pending: 24,
            moderation: 23
          }}
          id={channel.id}
        />)}
      </div>
    </section>
  )
}
