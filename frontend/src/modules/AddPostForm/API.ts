import axios from "axios";

export const getSpellcheckingWords = async (html:string) => {
    try {
        const res = await axios.get(`https://speller.yandex.net/services/spellservice.json/checkText`, {params:{text: html, format: 'html'}});
        return res?.data
    } catch (error) {
        return null;
    }
}