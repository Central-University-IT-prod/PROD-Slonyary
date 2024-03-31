import { FC } from 'react'
import s from './Navbar.module.scss'
import { NavLink } from 'react-router-dom'
import { NavigatePath, paths } from '../../routes.ts'
import bibaImg from '../../assets/imgs/biba.jpg'
import siteLogoImg from '../../assets/imgs/siteLogo.png'
import { Container } from '@mui/material'

export const Navbar: FC = () => {
	return (
		<nav className={s.navBar}>
			<Container maxWidth={'lg'} sx={{ padding: '15px 20px 15px 15px' }}>
				<div className={s.inner}>
					<div className={s.left}>
						<img src={siteLogoImg} alt="" className={s.logo} />
						<div className={s.links}>
							<NavLink
								className={({ isActive }) =>
									isActive ? `${s.link} ${s.active}` : s.link
								}
								to={NavigatePath(paths.HOME)}
							>
								Главная
							</NavLink>
							<NavLink
								className={({ isActive }) =>
									isActive ? `${s.link} ${s.active}` : s.link
								}
								to={NavigatePath(paths.CHANNELS)}
							>
								Мои каналы
							</NavLink>
							<NavLink
								className={({ isActive }) =>
									isActive ? `${s.link} ${s.active}` : s.link
								}
								to={NavigatePath(paths.POSTS)}
							>
								Мои посты
							</NavLink>
						</div>
					</div>
					<div className={s.right}>
						<img src={bibaImg} alt="" className={s.userLogo} />
						<span className={s.userName}>User</span>
					</div>
				</div>
			</Container>
		</nav>
	)
}
