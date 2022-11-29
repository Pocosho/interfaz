<template class="content-class"> 

  <v-container fluid> {{/* Contenedor General del Status Cliente */}}

    <template>
      {{ /* Seccion Status cliente */ }}
      <br>
      <h2> {{ Titlestatus }} </h2>
      <br>
    </template>

    <v-container v-if="datoscargados == false"> 
      <div class="text-center">
        <h3> Cargando Datos </h3>
        <v-progress-circular indeterminate color="teal lighten-1"></v-progress-circular>
      </div>
    </v-container>
    
    <v-container v-else-if="datoscargados == true">  
      <v-toolbar dark color="teal lighten-1" class="mb-1">
        <v-toolbar-title class="flex-d justify ml-2 mr-6">Seleccionar Cliente: </v-toolbar-title>
        
        <v-select v-model="cliente_seleccionado" :items="lista_clientes" v-on:change="getData_r" class="align-center mt-3"></v-select>
      </v-toolbar>
      
      <v-data-table :headers="header" :items="rows" class="elevation-1">
        <template v-slot:item="row">
          <tr>
            <td>{{ row.item.Directorio }}</td>
            <td>{{ row.item.Cantidad }}</td>
            <td>{{ row.item.Metadata }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-container>

  </v-container>
</template>



<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>
<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { internet } from '@/utils/Internet';
import axios from "axios";
import { IDataTable, IDataTable2 } from '@/model/main/IDataTable';
import { IHeaderTable2 } from '@/model/main/IHeaderTable';
import { ILabels, ILabels2 } from '@/model/labels/ILabels';

@Component({
  name: 'StatusClients'
})

export default class StatusClients extends Vue {
  public rows: Array<IDataTable2> = [];
  public header: Array<IHeaderTable2<IDataTable2>> = [];
  public isLoading = false;
  public lista_directorios: Array<ILabels2> = [];
  public Titlestatus = this.$t("Main.Titlestatus");
  public SelectClient = this.$t("Main.SelectClient");
  public SelectDictionary = this.$t("Main.SelectDictionary");
  public SearchClients = this.$t("Main.SearchClients");
  public FilterList = this.$t("Main.FilterList");
  public FilterPending = this.$t("Main.FilterPending");
  public FilterProblematic = this.$t("Main.FilterProblematic");
  public clientes: Array<IDataTable2> = [];
  public cliente_seleccionado = 'Duoc';
  public lista_clientes: Array<string> = [];
  public directory_content: Array<string> = [];
  public client_content: Array<string> = [];
  public current_item = { 'Cantidad': '', 'Metadata': '', 'Directarios': '' };
  public datoscargados = false;

  mounted(): void {
    this.getData();
  }
  private getData(): void {
    this.isLoading = true;
    let config = {
      method: 'get',
      url: 'http://127.0.0.1:9090/endpoint4',
      headers: { Authorization: 'Basic ' + btoa('usuario1' + ':' + 'usuario1') }
    };
    axios(config)
      .then((response) => {
        console.log(response.data.lista)
        this.lista_clientes = response.data.lista;

        console.log(this.lista_clientes)
        this.getData_r();
      })
      .catch(console.log)
      .finally(() => {
        this.isLoading = false;
      });
  }

  mounted_r(): void {
    this.getData_r();
  }
  public getData_r() {
    this.isLoading = true;
    this.datoscargados = false;
    let config = {
      valid: true,
      method: 'get',
      url: `http://127.0.0.1:9090/endpoint5?client=${this.cliente_seleccionado}`,
      headers: { 'Authorization': 'Basic ' + btoa('usuario1' + ':' + 'usuario1'), 'Access-Control-Allow-Origin': '*'}
    };
    axios(config)
      .then((response) => {
        const dataTable: Array<IDataTable2> = [];
        if (response.data.client1 == 'False'){
          const row: IDataTable2 = {};
          row['Directorio'] = "No se encontraron datos";
          row['Cantidad'] = "";
          row['Metadata'] = "";
          //console.log(JSON.stringify(item.tunning))
          dataTable.push(row);
        }
        this.lista_directorios = response.data.client1 as Array<ILabels2>;
        for (let item of this.lista_directorios) {
          const row: IDataTable2 = {};
          row['Directorio'] = item.name_directorio;
          row['Cantidad'] = item.cantidad;
          row['Metadata'] = item.metadata;
          //console.log(JSON.stringify(item.tunning))
          dataTable.push(row);
        }
        const header: Array<IHeaderTable2<
          IDataTable2
        >> = Object.keys(dataTable[0]).map(
          (
            key: string
          ): IHeaderTable2<IDataTable> => {
            let text = key;
            switch (key) {
              case 'name_directorio':
                text = "Directorio";
                break;
              case 'cantidad':
                text = "Cantidad";
                break;
              case 'metadata':
                text = "Metadata";
                break;
            }
            return {
              text,
              value: key,
            };
          }
        ) as Array<IHeaderTable2<IDataTable2>>;
        this.rows = dataTable;
        this.header = header;
        this.datoscargados = true;
      })
      .catch(console.log)
      .finally(() => {
        this.isLoading = false;
      });
  }
}
</script>