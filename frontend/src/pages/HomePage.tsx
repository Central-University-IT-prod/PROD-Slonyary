import {TelegramPreview} from "../modules/TelegramPreview/TelegramPreview.tsx";
import bobaImg from '../assets/imgs/biba.jpg'

function HomePage() {
  return (
    <>
      <TelegramPreview
        images={[bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg]}
        htmlText={'ыэвдаьдлтпп фыщжвта фыовтмфытащ тфывтс фыдвл тфыдалсф ыдвс фдывт'}/>
    </>
  )
}

export default HomePage
