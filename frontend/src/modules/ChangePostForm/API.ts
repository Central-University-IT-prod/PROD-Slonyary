import axios from "axios";
import { BACKEND_HOST } from "../../constants";

export const changeMessage = async (id:string, data:any) => {
    try {
        const response = await axios.post(`http://${BACKEND_HOST}/posts/${id}`, data, {
            headers: {
                'token': localStorage.getItem('accessToken')
            }
        })
        return response.data;
    } catch (error) {
        console.log(error)
        return error;
    }
}