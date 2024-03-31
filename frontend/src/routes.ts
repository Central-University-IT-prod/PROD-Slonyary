enum paths {
    REGISTRATION = 'registration',
    HOME = 'home',
    POST = 'post'
  }

const NavigatePath = (path:string):string => `/${path}`

export {paths, NavigatePath}