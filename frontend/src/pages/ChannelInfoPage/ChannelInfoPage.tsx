import s from './ChannelInfoPage.module.scss'
import bobaImg from '../../assets/imgs/biba.jpg'

const testData = {
  name: 'Название канала',
  link: 'хуйзалупа',
  description: 'ыа флоа фыжвоат щфвыа фыщвтз фвызфыоазшфа фшывмзффл лыь фжывдла дфлвадфыл вадлфыв адлфыва длфвыа дфыва жфывлда фывла фывла ждлфвыао фывоа фывдоа фдылвао фыдлвжао фылова дфылова фыдлвоа дыфлвоа фдылвоа фылодва фылвоа фдывоал дфылвоа фдлвыоа дфловыа фдылвоа дфылвоа фдывлао '
}

const ChannelInfoPage = () => {
  return (
    <section className={s.main}>
      <div className={s.infoContainer}>
        <img src={bobaImg} className={s.avatar} alt=""/>
        <div className={s.infoText}>
          <h3 className={s.channelTitle}>{testData.name}</h3>
          <p className={s.channelLink}>@{testData.link}</p>
          <p className={s.channelDescription}>{testData.description}</p>
        </div>
      </div>
    </section>
  )
}

export default ChannelInfoPage;