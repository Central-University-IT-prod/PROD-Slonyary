import {FC} from 'react'
import s from './Navbar.module.scss'
import {NavLink} from 'react-router-dom'
import {NavigatePath, paths} from '../../routes.ts'
import siteLogoImg from '../../assets/imgs/siteLogo.png'
import useAppSelector from "../../hooks/useAppSelector.ts";
import {useNavigate} from "react-router";

export const Navbar: FC = () => {
  const userData: {
    first_name: string,
    photo_url: string
  } = useAppSelector(state => state.user)
  const navigate = useNavigate()
  if (!userData) navigate(paths.TELEGRAMAUTH)
  return (
    <header className={s.navBar}>
      <div className="container">
        <div className={s.inner}>
          <div className={s.left}>
            <img src={siteLogoImg} alt="" className={s.logo}/>
            <nav className={s.links}>
              <NavLink
                className={({isActive}) =>
                  isActive ? `${s.link} ${s.active}` : s.link
                }
                to={NavigatePath(paths.HOME)}
              >
                Главная
              </NavLink>
              <NavLink
                className={({isActive}) =>
                  isActive ? `${s.link} ${s.active}` : s.link
                }
                to={NavigatePath(paths.CHANNELS)}
              >
                Мои каналы
              </NavLink>
            </nav>
          </div>
          <div className={s.right}>
            <img src={userData.photo_url} alt="" className={s.userLogo}/>
            <span className={s.userName}>{userData.first_name}</span>
          </div>
        </div>
      </div>
    </header>
  )
}
