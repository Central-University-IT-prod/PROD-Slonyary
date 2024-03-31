import { FC } from 'react'
import { Posts } from './pages/Posts/Posts.tsx'
import { Container } from '@mui/material'

const App: FC = () => {

  return (
    <Container maxWidth="lg">
      <Posts />
    </Container>
  )
}

export default App
