enum paths {
    REGISTRATION = 'registration',
    TELEGRAMAUTH = 'telegramauth',
    HOME = 'home',
    POST = 'post'
  }

const NavigatePath = (path:string):string => `/${path}`

export {paths, NavigatePath}