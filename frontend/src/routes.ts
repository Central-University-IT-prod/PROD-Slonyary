enum paths {
  TELEGRAMAUTH = 'telegramauth',
  HOME = '',
  POSTS = 'posts',
  CHANNELS = "channels",
  ADD_POST = "addpost",
  CHANNEL_INFO = "channelinfo",
}

const NavigatePath = (path: string): string => `/${path}`

export {paths, NavigatePath}