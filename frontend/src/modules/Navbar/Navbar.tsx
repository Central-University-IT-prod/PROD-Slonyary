import {FC} from 'react'
import s from './Navbar.module.scss'
import {NavLink} from 'react-router-dom'
import {NavigatePath, paths} from '../../routes.ts'
import bibaImg from '../../assets/imgs/biba.jpg'
import siteLogoImg from '../../assets/imgs/siteLogo.png'

export const Navbar: FC = () => {
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
            <img src={bibaImg} alt="" className={s.userLogo}/>
            <span className={s.userName}>User</span>
          </div>
        </div>
      </div>
    </header>
  )
}
