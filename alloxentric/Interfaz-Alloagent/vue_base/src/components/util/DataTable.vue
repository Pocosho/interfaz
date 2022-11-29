<template>
    <div class="container">
        <v-card-title primary-title>
            <h3> {{ Clients }} Alloagent </h3>
        </v-card-title>

        <v-row class="justify-end my-3 mr-4">
            <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn color="teal lighten-1" dark v-bind="attrs" v-on="on">
                        <v-icon dark>
                            mdi-account-plus
                        </v-icon>
                        Agregar Cliente
                    </v-btn>
                </template>

                <v-card> {{/* Agregar un nuevo cliente */}}
                    <v-card-title>
                        <span class="text-h5">Ingresar nuevo cliente</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field v-model="clientElement" :counter="20"
                                        :rules="[v => !!v || 'Se requiere el cliente', v => !!v || 'Se requiere este campo',
                                        v => (v && v.length <= 20) || 'El cliente no puede tener mas de 20 caracteres']" label="Cliente" 
                                        required>
                                        <v-textarea></v-textarea>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="datosElement" :counter="30"
                                        :rules="[v => !!v || 'Se requiere la base de datos', v => !!v || 'Se requiere este campo',
                                        v => (v && v.length <= 30) || 'La base de datos no puede tener mas de 30 caracteres']" label="Base de datos" required>
                                        <v-textarea></v-textarea>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="serverElement" :counter="30"
                                        :rules="[v => !!v || 'Se requiere la direccion del servidor', v => !!v || 'Se requiere este campo',
                                        v => (v && v.length <= 30) || 'La ruta SFTP no puede tener mas de 30 caracteres']" label="Direccion sftp" required>
                                        <v-textarea></v-textarea>
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-select v-model="transcriptElement" :items="['deepgram',
                                    'transc_1',
                                    'transc_2',
                                    'transc_3']" :rules="[v => !!v || 'Se requiere el tipo de trasncripcion']"
                                        label="Tipo transcripción" required>
                                    </v-select>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="workersElement" :counter="2" :rules="[v => !!v || 'Se requiere la cantidad de workers', v => !!v || 'Se requiere este campo',
                                    v => (v && v.length <= 2) || 'workers no puede tener mas de 2 digitos']"
                                        label="Cantidad de workers" required>
                                        <v-textarea></v-textarea>
                                    </v-text-field>
                                </v-col>

                                <v-checkbox v-model="checkbox"
                                    :rules="[v => !!v || 'Debes aceptar para agregar el cliente!']"
                                    label="Acepto agregar cliente" required></v-checkbox>

                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>

                        <v-btn color="#26c6da" text @click="dialog = false">
                            Cancelar
                        </v-btn>
                        <v-btn color="#26c6da" @click="aggregateItem()">
                            Guardar
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-row>

        {{/* Tabla de Clientes ingresados y editables */}}

        <v-col>
            <v-data-table :headers="header" :items="rows" :search="search" class="elevation-1">
                <template v-slot:item="row">
                    <tr>
                        <td>{{ row.item.Cliente }}</td>
                        <td>{{ row.item.Datos }}</td>
                        <td>{{ row.item.Servidores }}</td>
                        <td>{{ row.item.Transcripcion }}</td>
                        <td>{{ row.item.Workers }}</td>
                        <td>
                            <v-icon small class="mr-2" @click="editItem(row.item)">
                                mdi-pencil
                            </v-icon>
                        </td>
                    </tr>
                </template>
            </v-data-table>
        </v-col>
        <v-dialog v-model="dialogUpdate" max-width="900px" persistent>
            <v-card>
                <v-card-title primary-title>
                    Editar
                </v-card-title>
                <v-col cols="12">
                    <v-text-field v-model="edit_datos" :counter="30" :rules="[v => !!v || 'Se requiere la base de datos', v => !!v || 'Se requiere este campo',
                    v => (v && v.length <= 30) || 'La base de datos no puede tener mas de 30 caracteres']"
                        label="Base de datos" required>
                        <v-textarea></v-textarea>
                    </v-text-field>
                </v-col>
                <v-col cols="12">
                    <v-text-field v-model="edit_server" :counter="30" :rules="[v => !!v || 'Se requiere la direccion del servidor', v => !!v || 'Se requiere este campo',
                    v => (v && v.length <= 30) || 'La ruta SFTP no puede tener mas de 30 caracteres']"
                        label="Direccion sftp" required>
                        <v-textarea></v-textarea>
                    </v-text-field>
                </v-col>
                <v-col cols="12">
                    <v-select v-model="edit_transcript" :items="['deepgram',
                    'transc_1',
                    'transc_2',
                    'transc_3']" :rules="[v => !!v || 'Se requiere el tipo de trasncripcion']"
                        label="Tipo transcripción" required>
                        <v-textarea></v-textarea>
                    </v-select>
                </v-col>
                <v-col cols="12">
                    <v-text-field v-model="edit_workers" :counter="2" :rules="[v => !!v || 'Se requiere la cantidad de workers', v => !!v || 'Se requiere este campo',
                    v => (v && v.length <= 2) || 'workers no puede tener mas de 2 digitos']"
                        label="Cantidad de workers" required>
                        <v-textarea></v-textarea>
                    </v-text-field>
                </v-col>
                <v-card-actions>
                    <v-btn color="#26c6da" text @click="dialogUpdate = false">
                        Cerrar
                    </v-btn>
                    <v-btn color="#26c6da" text :disabled="isLoading" @click="sendEdit()">
                        Guardar
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { IDataTable } from '@/model/main/IDataTable';
import { IHeaderTable } from '@/model/main/IHeaderTable';
import { internet } from '@/utils/Internet';
import Util from '@/utils/Util';
import { ILabels } from '@/model/labels/ILabels';
import axios from 'axios';


@Component({
    name: 'DataTable'
})
export default class DataTable extends Vue {
    public rows: Array<IDataTable> = [];
    public header: Array<IHeaderTable<IDataTable>> = [];
    public isLoading = false;
    public data: Array<ILabels> = [];
    public dialog = false;
    public clientElement = "";
    public datosElement = "";
    public serverElement = "";
    public transcriptElement = "";
    public workersElement = "";
    public dialogUpdate = false;
    public edit_client = "";
    public edit_datos = "";
    public edit_server = "";
    public edit_transcript = "";
    public edit_workers = "";
    public clientRules = "";
    public datosRules = "";
    public sftpRules = "";
    public workersRules = "";
    public transcript: "";
    public search: "";
    public valid: "";
    public current_item = { 'Cliente': '', 'Datos': '', 'Servidores': '', 'Transcripcion': '', 'Workers': '' };
    public Clients = this.$t("Main.Clients");
    public AddClientButton = this.$t("Main.AddClientButton");
    public checkbox;
    public verificarFormu = true;

    mounted(): void {
        this.getData();
    }
    private getData(): void {
        this.isLoading = true;
        let config = {
            valid: true,
            method: 'get',
            url: 'http://127.0.0.1:9090/model1',
            headers: { Authorization: 'Basic ' + btoa('usuario1' + ':' + 'usuario1') }
        };
        axios(config)
            .then((response) => {
                this.data = response.data as Array<ILabels>;
                const dataTable: Array<IDataTable> = [];
                for (let item of this.data) {
                    // console.log(item);
                    const row: IDataTable = {};
                    row['Cliente'] = item.client;
                    row['Datos'] = item.db_client;
                    row['Servidores'] = item.sftp_client;
                    row['Transcripcion'] = item.transcript;
                    row['Workers'] = item.workers;
                    row['Acciones'] = item.actions;
                    console.log(JSON.stringify(item.tunning))
                    dataTable.push(row);
                }
                const header: Array<IHeaderTable<
                    IDataTable
                >> = Object.keys(dataTable[0]).map(
                    (
                        key: string
                    ): IHeaderTable<IDataTable> => {
                        let text = key;
                        switch (key) {
                            case 'client':
                                text = "Cliente";
                                break;
                            case 'db_client':
                                text = "Datos";
                                break;
                            case 'sftp_client':
                                text = "Servidores";
                                break;
                            case 'transcript':
                                text = "Transcripcion";
                                break;
                            case 'workers':
                                text = "Workers";
                                break;
                        }
                        return {
                            text,
                            value: key,
                        };
                    }
                ) as Array<IHeaderTable<IDataTable>>;
                this.rows = dataTable;
                this.header = header;
            })
            .catch(console.log)
            .finally(() => {
                this.isLoading = false;
            });
    }

    public editItem(item: ILabels) {
        let db_client = item.Datos;
        let sftp_client = item.Servidores;
        let transcript = item.Transcripcion;
        let workers = item.Workers;
        this.edit_datos = db_client;
        this.edit_server = sftp_client;
        this.edit_transcript = transcript;
        this.edit_workers = workers;
        this.dialogUpdate = true;
        this.current_item = item;
    }
    public sendEdit() {
        let cliente = this.current_item.Cliente;
        let dt = JSON.stringify({
            'client': cliente,
            'db_client': this.edit_datos,
            'sftp_client': this.edit_server,
            'transcript': this.edit_transcript,
            'workers': this.edit_workers
        })
        let config = {
            method: 'post',
            url: 'http://127.0.0.1:9090/model1',
            data: dt,
            headers: {
                Authorization: 'Basic ' + btoa('usuario1' + ':' + 'usuario1'),
                'Content-Type': 'application/json'
            }
        };
        axios(config)
            .then(response => {
                this.getData();
                this.dialogUpdate = false;
            })
    }
    public aggregateItem() {
        let client = this.clientElement;
        let db_client = this.datosElement;
        let sftp_client = this.serverElement;
        let transcript = this.transcriptElement;
        let workers = this.workersElement;
        let config = {
            method: 'put',
            url: 'http://127.0.0.1:9090/model1',
            params: {
                'client': client, 'db_client': db_client, 'sftp_client': sftp_client,
                'transcript': transcript, 'workers': workers
            },
            search: '',
            headers: { Authorization: 'Basic ' + btoa('usuario1' + ':' + 'usuario1') }
        };
        axios(config)
            .then(response => {
                this.dialog = false;
                this.clientElement = "";
                this.datosElement = "";
                this.serverElement = "";
                this.transcriptElement = "";
                this.workersElement = "";
                this.getData();
            })

    }

    
}
</script>