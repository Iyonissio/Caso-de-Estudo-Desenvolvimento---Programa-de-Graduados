import axios from 'axios';

export function getBaseUrl() {
    if (process.env.NODE_ENV === 'production') {
        return `${window.location.origin}/${window.location.pathname.toString().split('/')[1]}`;
        //return window.location.origin+'/'+survey;
    } else {
        //return 'http://192.168.43.12:8000';
        return 'http://127.0.0.1:8000';
        // return 'http://127.0.0.1:9000';
        //return 'https://atendimento.co.mz';
    }
} 

export const baseUrl = getBaseUrl() + '/api';

export const staticUrl = 'https://dev.atendimento.co.mz';

//export const socketioEndpoint = 'http://atendimento.co.mz:3400';
export const socketioEndpoint = 'http://localhost:3400';



export function request() {
    return {
        ussd: values => axios.post(`${getBaseUrl()}/ussd/ussdapp/json/`, values, {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        }),
    }
}

