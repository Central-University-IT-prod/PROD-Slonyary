enum paths {
    REGISTRATION = 'registration',
    TELEGRAMAUTH = 'telegramauth',
    HOME = 'home',
    POSTS = 'posts',
    CHANELS = "chanels"
  }

const NavigatePath = (path:string):string => `/${path}`

export {paths, NavigatePath}