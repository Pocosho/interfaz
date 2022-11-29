<template class="content-class">
  <v-container>
    {{ /* Seccion ReportedeCargas */ }}
    <h3>Reportes de Cargas</h3>
    <br />
    <v-row cols="12" md="6" class="d-flex justify-space-around">
      <template>
        <div class="text--primary">
          {{ /* reporte general por dia*/ }}
          <v-card class="mx-auto pa-10">
            <template v-if="$vuetify.breakpoint.mdAndUp">
              <v-toolbar dark color="teal lighten-1" class="mb-1">
                <template>
                  Reporte general por dia

                  <v-spacer></v-spacer>

                  <v-text-field v-model="search" clearable flat solo-inverted hide-details
                    prepend-inner-icon="mdi-magnify" label="Buscar"></v-text-field>
                </template>
              </v-toolbar>

              <v-toolbar>
                <v-col cols="12" sm="6" md="4" class="my-5">
                  <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date"
                    transition="scale-transition" offset-y min-width="auto">
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field v-model="date" label="Selecionar fecha" prepend-icon="mdi-calendar" readonly
                        v-bind="attrs" v-on="on" class="flex-d mt-8 " min-width="auto"></v-text-field>
                    </template> {{/* DataPicker Reporte de cargas */}}
                    <v-date-picker v-model="date" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="menu = false">
                        Cancel
                      </v-btn>
                      <v-btn text color="primary" @click="$refs.menu.save(date); filtrodate();">
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
              </v-toolbar>
              {{/* tabla */}}
              <v-col>
                <v-data-table :headers="header" :items="rows" :search="search" class="elevation-1">
                  <template v-slot:item="row">
                    <tr>
                      <td>{{ row.item.Ultimo_registro }}</td>
                      <td>{{ row.item.Ultimo_analisis }}</td>
                      <td>{{ row.item.Idioma }}</td>
                    </tr>
                  </template>
                </v-data-table>
              </v-col>
            </template>
          </v-card>

          <div class="my-6"></div>

          {{ /* reporte general por dia*/ }}
          <v-card class="mx-auto pa-6" height="auto" width="700">
            <template v-if="$vuetify.breakpoint.mdAndUp">
              <v-toolbar dark color="teal lighten-1" class="mb-1">
                <template>
                  Reporte de la fecha:

                  <v-spacer></v-spacer>

                  <v-text-field v-model="search" clearable flat solo-inverted hide-details
                    prepend-inner-icon="mdi-magnify" label="Buscar"></v-text-field>
                </template>
              </v-toolbar>
            </template>
          </v-card>
        </div>
      </template>
    </v-row>
  </v-container>
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
  name: 'AppReporteCargas'
})

export default class AppReporteCargas {
  public rows: Array<IDataTable> = [];
  public header: Array<IHeaderTable<IDataTable>> = [];
  public isLoading = false;
  public data: Array<ILabels> = [];
  public search: any;
  public selected: any;
  public $vuetify: any;
  public menu: any;
  public date: any;
  public datos: any


  mounted(): void {
    this.getData();
  }
  private getData(): void {
    this.isLoading = true;
    let config = {
      valid: true,
      method: 'get',
      url: 'http://127.0.0.1:9090/model3',
      headers: { Authorization: 'Basic ' + btoa('usuario1' + ':' + 'usuario1') }
    };
    //se debe cambiar las variables a trabajar en el datatable para poder trabajar con la variable informe 
    axios(config)
      .then((response) => {
        this.data = response.data as Array<ILabels>;
        this.datos = response.data
        const dataTable: Array<IDataTable> = [];
        for (let item of this.data) {
          // console.log(item);
          const row: IDataTable = {};
          row['Ultimo_registro'] = item.ultimo_registro;
          row['Ultimo_analisis'] = item.ultimo_analisis;
          row['Idioma'] = item.idioma;
          //console.log(JSON.stringify(item.tunning))
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
              case 'ultimo_registro':
                text = "Ultimo_registro";
                break;
              case 'idioma':
                text = "Idioma";
                break;
              case 'ultimo_analisis':
                text = "Ultimo_analisis";
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

  public filtrodate() {
    let fechas = this.date.split('-')
    let fechaBuscar = fechas[2]+'/'+fechas[1]+'/'+fechas[0]
    let Array=this.datos.filter(datos => datos.ultimo_registro === fechaBuscar)
    const dataTable: Array<IDataTable> = [];
        for (let item of Array) {
          // console.log(item);
          const row: IDataTable = {};
          row['Ultimo_registro'] = item.ultimo_registro;
          row['Ultimo_analisis'] = item.ultimo_analisis;
          row['Idioma'] = item.idioma;
          //console.log(JSON.stringify(item.tunning))
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
              case 'ultimo_registro':
                text = "Ultimo_registro";
                break;
              case 'idioma':
                text = "Idioma";
                break;
              case 'ultimo_analisis':
                text = "Ultimo_analisis";
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

  }




}
</script>