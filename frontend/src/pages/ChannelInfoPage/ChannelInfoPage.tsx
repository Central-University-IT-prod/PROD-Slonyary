import s from './ChannelInfoPage.module.scss'
import bobaImg from '../../assets/imgs/biba.jpg'

const testData = {
  name: 'Название канала',
  link: 'хуйзалупа',
  description: 'ыа флоа фыжвоат щфвыа фыщвтз фвызфыоазшфа фшывмзффл лыь фжывдла дфлвадфыл вадлфыв адлфыва длфвыа дфыва жфывлда фывла фывла ждлфвыао фывоа фывдоа фдылвао фыдлвжао фылова дфылова фыдлвоа дыфлвоа фдылвоа фылодва фылвоа фдывоал дфылвоа фдлвыоа дфловыа фдылвоа дфылвоа фдывлао '
}

const translateStatus = (status: string): string => {
  const russianWords = {
    'owner': 'владелец',
    'moderator': 'модератор',
    'redactor': 'редактор'
  }

  // @ts-ignore
  return status in russianWords ? russianWords[status] : ''
}

const ChannelInfoPage = () => {
  return (
    <section className={s.main}>
      <div className={s.infoContainer}>
        <div className={s.left}>
          <img src={bobaImg} className={s.avatar} alt=""/>
          <div className={s.infoText}>
            <h3 className={s.channelTitle}>{testData.name}</h3>
            <p className={s.channelLink}>@{testData.link}</p>
            <p className={s.channelDescription}>{testData.description}</p>
          </div>
        </div>
        <div className={s.right}>
          <div className={s.members}>
            <h5 className={s.membersTitle}>Участники</h5>
            <div className={s.membersList}>
              {
                [
                  {
                    name: 'JakeFish',
                    id: 131322,
                    status: 'owner'
                  },
                  {
                    name: 'JakeFish',
                    id: 131322,
                    status: 'moderator'
                  },
                  {
                    name: 'JakeFish',
                    id: 131322,
                    status: 'redactor'
                  }
                ].map((user, index) => (
                  <div className={s.user}>
                    <span className={s.number}>{index + 1}.</span>
                    <div className={s.userText}>
                      <h5 className={s.userName}>{user.name}</h5>
                      <p className={s.userStatus + ' ' + s[user.status]}>{translateStatus(user.status)}</p>
                    </div>
                  </div>
                ))
              }
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default ChannelInfoPage;