import biba from '../../assets/imgs/biba.jpg'
import './Chanel.scss'
import { Button } from '@mui/material'

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

function Channel({ chanelData }: IProps) {
	const { title, subscribers } = chanelData

	return (
		<div className="Chanel">
			<div className="Chanel-box">
				<div className="Chanel-mainContant">
					<div className="Chanel-image">
						<img alt={'img'} src={biba} />
					</div>
					<div className="Chanel-textContent">
						<h2 className="textContent-title">{title}</h2>
						<h4 className="info-subscribers">{subscribers} подписчика</h4>
					</div>
				</div>
				<div className="Chanel-manageBtns">
					<Button
						sx={{ borderRadius: '20px' }}
						className="open-btn"
						variant="contained"
					>
						Открыть
					</Button>
				</div>
			</div>
		</div>
	)
}

export default Channel
