import { FC, useState } from 'react'
import { Button, Grid, Stack } from '@mui/material'
import { PostItem } from '../../../modules/PostItem/PostItem.tsx'
import { TPostItem } from '../../../models/PostsModels.ts'
import bibaImg from '../../../assets/imgs/biba.jpg'

const testData: TPostItem[] = [
	{
		channelAvatar: 'x',
		channelName: 'PROD',
		date: '2024-03-31T10:05:03.255Z',
		publicised: true,
		admin: 'K1rles',
		postImages: [bibaImg, bibaImg],
		postText: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		category: 'planned'
	},
	{
		channelAvatar: 'x',
		channelName: 'DANO',
		date: '2024-03-31T10:05:03.255Z',
		publicised: false,
		admin: 'StreveSuksess',
		postImages: ['https://img.freepik.com/free-photo/a-painting-of-a-mountain-lake-with-a-mountain-in-the-background_188544-9126.jpg', bibaImg, bibaImg, bibaImg, bibaImg, bibaImg],
		postText: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		category: 'published'
	},
	{
		channelAvatar: 'x',
		channelName: 'ВШЭ',
		date: '2024-03-31T10:05:03.255Z',
		publicised: false,
		admin: 'Jake Fish',
		postImages: [bibaImg, bibaImg, bibaImg, bibaImg, bibaImg, bibaImg, bibaImg, bibaImg],
		postText: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		category: 'moderation'
	}
]


export const Posts: FC = () => {
	const [category, setCategory] = useState<TPostItem['category'] | 'all'>('all')

	return (
		<>
			<Stack spacing={1} direction='row'>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('all')}
					variant={category === 'all' ? 'contained' : 'outlined'}
				>
					Все
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('planned')}
					variant={category === 'planned' ? 'contained' : 'outlined'}
				>
					Запланированные
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('moderation')}
					variant={category === 'moderation' ? 'contained' : 'outlined'}
				>
					На модерации
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('published')}
					variant={category === 'published' ? 'contained' : 'outlined'}
				>
					Опубликованные
				</Button>
			</Stack>
			<Grid container rowSpacing={4} mt={1} spacing={2}>
				{testData
					.filter(post => category === 'all' ? true : post.category === category)
					.map((post, index) => <Grid item xs={12} sm={6} key={index}><PostItem {...post} /></Grid>)}
			</Grid>
		</>
	)
}
