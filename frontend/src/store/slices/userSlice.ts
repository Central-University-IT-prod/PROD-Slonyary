import { PayloadAction, createSlice } from "@reduxjs/toolkit"

type TypeUser = {
    name: string,
    dateBorn: string | null,
}

const initialState:TypeUser = {
    name: '',
    dateBorn: null
}

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        setUser:(state, action: PayloadAction<TypeUser> ) => {
            console.log(action.payload)
            state = action.payload
            return state
        }
    }
})
export const  {actions,reducer } = userSlice;