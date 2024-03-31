import PageElement from "../../Ui/PageElement/PageElement";
import biba from "../../assets/imgs/biba.jpg";
import "./Chanel.css";

function Channel() {
  return (
    <PageElement>
      <div className="Chanel">
        <div className="Chanel-image">
          <img src={biba}/>
        </div>
        <div className="Chanel-textContent">
          <div className="textContent-title">
            <h2>Название канала</h2>
          </div>
          <div className="textContent-name">
            <h3>@chanelName</h3>
          </div>
        </div>
        <div className="Chanel-info">
          <div className="info-subsribers"></div>
        </div>
      </div>
    </PageElement>
  );
}

export default Channel;
