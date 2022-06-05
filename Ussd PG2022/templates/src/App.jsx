import React, { useEffect, useState } from 'react';
import {
    TextField, Button, Container,
    Paper, Typography, CircularProgress
} from '@material-ui/core';
import { request } from "./lib/settings";

let randomSession = Math.floor(Math.random() * 1001) + 9999;
function App() {
    const [phone, setPhone] = useState({ session_id: 1235, phone: "", command: "0" });
    const [resultLog, setResultLog] = useState({ title: "", message: "", options: [] });
    const [isLoading, setIsLoading] = useState(false);

    useEffect(init, [])

    async function init() {
        setIsLoading(true);
        randomSession = Math.floor(Math.random() * 1001) + 9999;
        setPhone({ ...phone, session_id: randomSession });
        setIsLoading(false);
    }

    async function processRequest() {
        setIsLoading(true);
        const requestData = await Promise.resolve(request().ussd(phone));
        setPhone({ ...phone, command: "" });
        setResultLog(requestData.data);
        setIsLoading(false);
    }

    if (isLoading)
        return (<div
            style={{
                width: '100%', height: '80vh',
                textAlign: 'center', marginTop: '50vh'
            }}>
            
        </div>)

    return (
        <Container><br />
            <TextField variant="outlined" name="phone" label="Celular"
                value={phone.phone} fullWidth
                onChange={(e) => {
                    setPhone({
                        ...phone,
                        phone: e.target.value.toString()
                    });
                }} /><br />

            <Paper style={{ padding: '10px', marginTop: '10px', }} variant="outlined">
                <Typography style={{ textAlign: 'center' }} variant="button">{resultLog.title}</Typography><br />
                <Typography variant="button">{resultLog.message}</Typography><br />
                {resultLog.options.map(x => (<><Typography
                    style={{ textTransform: 'none' }}
                    variant="button">{x.option}: {x.value}</Typography><br /></>))}
            </Paper><br />
            <TextField variant="outlined" name="commando" value={phone.command} fullWidth
                onChange={(e) => {
                    setPhone({
                        ...phone,
                        command: e.target.value.toString()
                    });
                }} />
                <br/><br/>
            <Button style={{width:'100%'}} color="primary" variant="contained" disabled={!phone.command || !phone.phone} onClick={processRequest}>Enviar</Button>
        </Container>
    )
}

export default App;



const data = {
    "message": "Por favor seleccione uma das opcoes",
    "title": "Menú",
    "options": [
        {
            "option": "1",
            "value": "Informação pessoal"
        },
        {
            "option": "2",
            "value": "Meus terrenos"
        },
        {
            "option": "3",
            "value": "Meus imóveis"
        },
        {
            "option": "4",
            "value": "Minhas Actividades Económicas"
        },
        {
            "option": "5",
            "value": "Impostos/Taxas por pagar"
        },
        {
            "option": "6",
            "value": "Impostos/Taxas pagos parcialmente"
        },
        {
            "option": "7",
            "value": "Impostos/Taxas pagos totalmente"
        },
        {
            "option": "8",
            "value": "Contas para pagamento"
        },
        {
            "option": "9",
            "value": "Prazo de Pagamento"
        },
        {
            "option": "0",
            "value": "Voltar"
        }
    ]
};