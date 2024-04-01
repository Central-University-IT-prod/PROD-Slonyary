import AddPostForm from "../../modules/AddPostForm/AddPostForm.tsx";
import s from './AddPostPage.module.scss'
import {useState} from "react";
import bobaImg from "../../assets/imgs/biba.jpg";
import {TelegramPreview} from "../../modules/TelegramPreview/TelegramPreview.tsx";

const AddPostPage = () => {
  const [showPreview, setShowPreview] = useState<boolean>(false)

  return (
    <section className={s.main}>
      <AddPostForm showFunction={setShowPreview}/>
      {
        showPreview &&
          <>
              <div className={s.popup}>
                  <div className={s.background}></div>
                  <TelegramPreview
                      showFunction={setShowPreview}
                      images={[bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg, bobaImg]}
                      htmlText={'ыэвдаьдлтпп фыщжвта фыовтмфытащ тфывтс фыдвл тфыдалсф ыдвс фдывт'}/>
              </div>
          </>
      }
    </section>
  )
}

export default AddPostPage;