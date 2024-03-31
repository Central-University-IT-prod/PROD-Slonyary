import { useDispatch } from "react-redux"
import {actions as userActions} from '../store/slices/userSlice'
import { useMemo } from "react"
import { bindActionCreators } from "@reduxjs/toolkit"

const rootActions = {
    ...userActions
}

export const useActions = () => {
    const dispatch = useDispatch()

    return useMemo(() => bindActionCreators(rootActions, dispatch), [dispatch])
}