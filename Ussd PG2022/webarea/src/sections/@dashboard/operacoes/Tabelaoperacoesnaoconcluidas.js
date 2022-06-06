import * as React from 'react';
import { useState, useEffect } from 'react';
// import { useHistory } from 'react-router-dom';
// import { baseurl } from "../../lib/settings";

import { DataGrid } from '@mui/x-data-grid';

export default function Tabelaoperacoesnaoconcluidas() {
  // const history = useHistory();
  const [rows, setRows] = useState([]);

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'phone', headerName: 'Celular', width: 130 },
    { field: 'date', headerName: 'Data', width: 140 },
    { field: 'trasantion_type', headerName: 'Operação', width: 370 }
  ];

  // const getConsultas = async () => {
  //   baseurl.get("api/auth/ussd").then((response) => {
  //     setRows(response.data);
  //   });
  // };

  // const TOTAL = requisicoes.length;
  // console.log("Tamanho",TOTAL)

  // useEffect(() => {
  //   getConsultas();
  // }, []);
  return (
    <div style={{ height: 400, width: '100%' }}>
      <h3>Operações não Concluídas</h3>
      <br />
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </div>
  );
}
