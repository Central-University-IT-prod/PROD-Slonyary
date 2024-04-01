enum paths {
  REGISTRATION = 'registration',
  TELEGRAMAUTH = 'telegramauth',
  HOME = 'home',
  POSTS = 'posts',
  CHANNELS = "channels",
  ADD_POST = "addpost",
}

const NavigatePath = (path: string): string => `/${path}`

export {paths, NavigatePath}