import { FC, useState } from 'react'
import { Button, Grid } from '@mui/material'
import { PostItem } from '../../../modules/PostItem/PostItem.tsx'
import { TPostItem } from '../../../models/PostsModels.ts'
import './Posts.scss'
import { postsAPI } from '../../../store/services/PostsService.ts'
import { Loading } from '../../../modules/Loading/Loading.tsx'

export const Posts: FC = () => {
	const [category, setCategory] = useState<TPostItem['category'] | 'all'>('all')
	const {
		data: posts,
		isLoading,
		refetch
	} = postsAPI.useFetchAllPostsQuery(null)

	if (isLoading) return <Loading />
	if (!posts) return <p>ну пиздец</p>
	return (
		<>
			<div className="status-filter">
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
			</div>
			{posts && (
				<Grid
					maxWidth="sm"
					sx={{ mx: 'auto', pb: '20px' }}
					rowSpacing={4}
					mt={1}
				>
					{posts
						.filter((post) =>
							category === 'all' ? true : post.status === category
						)
						.map((post, index: number) => (
							<Grid mt={2} item xs={12} key={index}>
								<PostItem data={post} refetch={refetch} />
							</Grid>
						))}
				</Grid>
			)}
		</>
	)
}
