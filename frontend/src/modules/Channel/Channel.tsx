import biba from '../../assets/imgs/biba.jpg'
import './Chanel.css'

type TypeChanel = {
  title: string
  name: string
  subscribers: number
  category: string
  //img: string
}

interface IProps {
  chanelData: TypeChanel
}

function Channel({chanelData}: IProps) {
  const {title, subscribers} = chanelData

  return (
    <div className="Chanel">
      <div className="Chanel-box">
        <div className="Chanel-mainContant">
          <div className="Chanel-image">
            <img alt={'img'} src={biba}/>
          </div>
          <div className="Chanel-textContent">
            <div className="textContent-title">
              <h2>{title}</h2>
            </div>
            <div className="info-subsribers">
              <h4>{subscribers} подписчика</h4>
            </div>
          </div>
        </div>
        <div className="Chanel-manageBtns">
          <button className="open-btn">Открыть</button>
        </div>
      </div>
    </div>
  )
}

export default Channel
