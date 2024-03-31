enum paths {
    REGISTRATION = 'registration',
    HOME = 'home',
  }

const NavigatePath = (path:string):string => `/${path}`

export {paths, NavigatePath}