import {FC} from 'react'
import Channel from '../../modules/Channel/Channel.tsx'
import {Button} from "@mui/material";
import s from './ChannelPage.module.scss'

export const ChannelPage: FC = () => {
  return (
    <section>
      <div className={s.buttons}>
        <div className="categorieButton">
          <Button sx={{borderRadius: '20px'}} variant="contained">Телеграм</Button>
        </div>
        <a href="https://t.me/StackSMM_Bot?start=add_channel">
          <Button sx={{bgcolor: '#FFB13C'}} variant="contained">Добавить канал</Button>
        </a>
      </div>
      <div>
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
        <Channel
          chanelData={{
            title: 'dima is cool',
            category: 'vk',
            name: '@dima',
            subscribers: 134
          }}
        />
      </div>
    </section>
  )
}
