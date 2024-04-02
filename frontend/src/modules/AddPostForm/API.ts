import axios from "axios";
import { BACKEND_HOST } from "../../constants";

export const getSpellcheckingWords = async (html:string) => {
    try {
        const res = await axios.get(`https://speller.yandex.net/services/spellservice.json/checkText`, {params:{text: html, format: 'html'}});
        return res?.data
    } catch (error) {
        return null;
    }
}

export const addMessages = async (data:any, images:FormData) => {
    try {
        const response = await axios.post(`http://${BACKEND_HOST}/posts`, data, {
            headers: {
                'token': localStorage.getItem('accessToken')
            }
        })
        await axios.post(`http://${BACKEND_HOST}/posts`, images, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'token': localStorage.getItem('accessToken')
            }
        })
        console.log(response)
        return response;
    } catch (error) {
        console.log(error)
        return error;
    }
}