import { FC, useState } from 'react'
import { Button, Link, Stack, Typography } from '@mui/material'
import AccessTimeIcon from '@mui/icons-material/AccessTime'
import { getHoursWithMinutes, getMonthName } from '../../utils/utis.ts'
import PageElement from '../../Ui/PageElement/PageElement.tsx'

type Post = {
	name: string
	link: string
	category: 'planned' | 'drafts' | 'published'
	date: string
}

// const testData: Post[] = [
//
// ]

export const Posts: FC = () => {
	const [category, setCategory] = useState<Post['category']>('planned')

	return (
		<>
			<Stack spacing={1} direction="row">
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('planned')}
					variant={category === 'planned' ? 'contained' : 'outlined'}
				>
					Запланированные
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('drafts')}
					variant={category === 'drafts' ? 'contained' : 'outlined'}
				>
					Черновики
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('published')}
					variant={category === 'published' ? 'contained' : 'outlined'}
				>
					Опубликованные
				</Button>
			</Stack>
			<Stack spacing={2}>
				<PageElement>
					<Stack
						direction="row"
						spacing={2}
						sx={{
							minHeight: 100,
							borderRadius: 2,
							transition: 'all .3s'
						}}
					>
						<Stack
							spacing={1}
							alignItems="center"
							justifyContent="center"
							sx={{ minWidth: '100px', height: '100%', padding: 2 }}
						>
							<AccessTimeIcon color="info" fontSize="large" />
							<Typography sx={{ color: '#202020' }} textAlign="center">
								{new Date().getDate()} {getMonthName(new Date().getMonth())}{' '}
								{getHoursWithMinutes(new Date())}
							</Typography>
						</Stack>
						<Stack
							sx={{
								borderLeft: '1px solid #808080',
								padding: 2
							}}
							alignItems="flex-start"
							justifyContent="flex-start"
							spacing={1}
						>
							<Typography sx={{ color: '#202020' }}>
								Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut
								doloribus ducimus facilis fuga fugiat fugit, illum laboriosam
								minima praesentium provident quaerat qui quis tenetur? Beatae
								cumque porro quibusdam voluptatibus voluptatum.
							</Typography>
						</Stack>
						<Stack
							sx={{
								minWidth: '100px',
								marginLeft: 'auto !important',
								borderLeft: '1px solid #808080',
								padding: 2,
								cursor: 'pointer',
								'&:hover': {
									svg: {
										scale: '1.5'
									}
								}
							}}
							alignItems="flex-start"
							justifyContent="flex-start"
							spacing={1}
						>
							<Typography>Каналы:</Typography>
							{['@ssss', '@dddd', '@ffff'].map((channel) => (
								<Link>{channel}</Link>
							))}
						</Stack>
					</Stack>
				</PageElement>
			</Stack>
		</>
	)
}
