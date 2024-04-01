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
		admin: 'K1rles',
		postImages: [bibaImg, bibaImg],
		htmlText:
			'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		ownerName: 'xxx',
		category: 'pending'
	},
	{
		channelAvatar: 'x',
		channelName: 'DANO',
		date: '2024-03-31T10:05:03.255Z',
		admin: 'StreveSuksess',
		postImages: [
			'https://img.freepik.com/free-photo/a-painting-of-a-mountain-lake-with-a-mountain-in-the-background_188544-9126.jpg',
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg
		],
		htmlText:
			'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		ownerName: 'xxx',
		category: 'published'
	},
	{
		channelAvatar: 'x',
		channelName: 'ВШЭ',
		date: '2024-03-31T10:05:03.255Z',
		admin: 'Jake Fish',
		postImages: [
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg,
			bibaImg
		],
		htmlText:
			'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto cum illum inventore nam odio quasi!',
		ownerName: 'xxx',
		category: 'moderation'
	}
]

export const Posts: FC = () => {
	const [category, setCategory] = useState<TPostItem['category'] | 'all'>('all')

	return (
		<>
			<Stack
				maxWidth="sm"
				sx={{ mx: 'auto', mt: '15px' }}
				spacing={1}
				direction="row"
			>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('all')}
					variant={category === 'all' ? 'contained' : 'outlined'}
				>
					Все
				</Button>
				<Button
					sx={{ borderRadius: 2 }}
					onClick={() => setCategory('pending')}
					variant={category === 'pending' ? 'contained' : 'outlined'}
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
			<Grid maxWidth="sm" sx={{ mx: 'auto' }} rowSpacing={4} mt={1}>
				{testData
					.filter((post) =>
						category === 'all' ? true : post.category === category
					)
					.map((post, index) => (
						<Grid mt={2} item xs={12} key={index}>
							<PostItem data={post} />
						</Grid>
					))}
			</Grid>
		</>
	)
}
