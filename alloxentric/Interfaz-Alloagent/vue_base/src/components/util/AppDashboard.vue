<template class="content-class">
  <v-container fluid>

    {{ /* Seccion Dashboard */ }}
    <template>
      <h2 class="md-3"> Dashboard </h2>
      <br>
    </template>

    <v-row cols="12" md="6" class="d-flex justify-space-around">

      {{ /* Dashboard Servicios */ }}
      <v-card class="mx-auto" height="auto" width="500">
        {{/* Titulo de Servicios y Cantidad de activos */}}
        <v-list-item two-line>
          <v-list-item-content>
            <div class="d-flex justify-space-around mb-6">
              <v-list-item-title class="text-h5 font-weight-black"> {{ TitleServices }} </v-list-item-title>
              <v-list-item-subtitle class="d-flex justify-center"> 2/3 {{ Servicesup }} </v-list-item-subtitle>
            </div>

          </v-list-item-content>
        </v-list-item>

        <v-card-text> {{/* Carta contenedora Servicios */}}
          <v-row algin="center"> {{/* Orden y disposicion botones */}}
            <v-col class="text-h2" cols="12">
              {{/* Boton STT */}}

              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="red lighten-1" dark width="100%" v-bind="attrs" v-on="on">
                    STT
                  </v-btn>

                </template>


                <template v-slot:default="dialog"> {{/* Boton de estado STT*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusServiceSTT }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <div class="text-center my-3">
                      <h3> Intentando establecer conexión </h3>
                      <v-progress-circular class="mt-2" indeterminate color="teal lighten-1"></v-progress-circular>
                    </div>

                    {{/*Botones Cancelar y Levantar servicio*/}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>


                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>


              {{/* Boton Separación de voz */}}

              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="teal lighten-1" dark width="100%" v-bind="attrs" v-on="on">
                    {{ TitleSeparation }} {{/* Etiqueta de texto I18 (EN/ES) */}}
                  </v-btn>

                </template>


                <template v-slot:default="dialog"> {{/* Boton de estado Separacion de voz*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusVoiceSeparation }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <v-card-text>
                      <v-alert outlined class="mt-8" color="green">
                        <div class="text-h6">
                          Servicio separador de voz
                        </div>
                        <div>SERVICIO CONECTADO, 0 WARNINGS, 0 ERRORES</div>
                      </v-alert>
                    </v-card-text>


                    {{/*Botones Cancelar y Levantar servicio*/}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>


                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>

              {{/* Boton Perfilamiento de voz */}}
              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="teal lighten-1" dark width="100%" v-bind="attrs" v-on="on">
                    {{ TitleProfiling }} {{/* Etiqueta de texto I18 (EN/ES) */}}
                  </v-btn>

                </template>

                <template v-slot:default="dialog"> {{/* Boton de estado Perfilamiento de voz*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusVoiceProfiling }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <v-card-text>
                      <v-alert outlined class="mt-8" color="green">
                        <div class="text-h6">
                          Servicio perfilamiento de audio
                        </div>
                        <div>SERVICIO CONECTADO, 0 WARNINGS, 0 ERRORES</div>
                      </v-alert>
                    </v-card-text>

                    {{/*Botones Cancelar y Levantar servicio*/}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>


                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>
            </v-col>

          </v-row>
        </v-card-text>
      </v-card>



      {{ /* Dashboard Servidores */ }}

      <v-card class="mx-auto" height="auto" width="500">
        {{/* Titulo de Servidores y Cantidad de activos */}}
        <v-list-item two-line>
          <v-list-item-content>
            <div class="d-flex justify-space-around mb-6">
              <v-list-item-title class="text-h5 font-weight-black"> {{ Servers }} </v-list-item-title>
              <v-list-item-subtitle class="d-flex justify-center"> 2/3 {{ Servers }} UP </v-list-item-subtitle>
            </div>

          </v-list-item-content>
        </v-list-item>

        <v-card-text> {{/* Carta contenedora Servidores */}}
          <v-row algin="center"> {{/* Orden y disposicion botones */}}
            <v-col class="text-h2" cols="12">
              {{/* Boton SFTP */}}

              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="teal lighten-1" dark width="100%" v-bind="attrs" v-on="on">
                    SFTP
                  </v-btn>

                </template>


                <template v-slot:default="dialog"> {{/* Boton de estado SFTP*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusServerSFTP }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <v-card-text>
                      <v-alert outlined class="mt-8" color="green">
                        <div class="text-h6">
                          Servidor SFTP
                        </div>
                        <div>SERVIDOR SFTP CONECTADO, 0 WARNINGS, 0 ERRORES</div>
                      </v-alert>
                    </v-card-text>

                    {{/*Botones Cancelar y Levantar servicio*/}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>


                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>


              {{/* Boton Web Server */}}

              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="red lighten-1" dark width="100%" v-bind="attrs" v-on="on">
                    {{ TitleWeb }} {{/* Etiqueta de texto I18 (EN/ES) */}}
                  </v-btn>

                </template>


                <template v-slot:default="dialog"> {{/* Boton de estado Web server*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusWebServer }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <v-card-text>
                      <div class="text-center my-3">
                        <h3> Intentando establecer conexión </h3>
                        <v-progress-circular class="mt-2" indeterminate color="teal lighten-1"></v-progress-circular>
                      </div>
                    </v-card-text>

                    {{/*Botones Cancelar y Levantar Servidor*/}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>

                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>

              {{/* Boton Server X */}}
              <v-dialog transition="dialog-bottom-transition" width="80%">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn small color="yellow darken-3" dark width="100%" v-bind="attrs" v-on="on">
                    {{ TitleServerx }} {{/* Etiqueta de texto I18 (EN/ES) */}}
                  </v-btn>

                </template>

                <template v-slot:default="dialog"> {{/* Boton de estado Server*/}}
                  <v-card>
                    <v-toolbar color=#14AEB5 dark> {{ StatusWebServer }} </v-toolbar>

                    <v-spacer></v-spacer>

                    <v-card-text>
                      <v-alert outlined class="mt-8" color="yellow darken-2">
                        <div class="text-h6">
                          Servidor X Activo
                        </div>
                        <div>SERVIDOR X CONECTADO, 5 WARNINGS, 0 ERRORES</div>
                      </v-alert>
                    </v-card-text>

                    {{/*Botones Cancelar y Levantar Servidor */}}

                    <v-card-actions class="justify-end">
                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonCancelDashboard }}
                      </v-btn>

                      <v-btn color="green darken-1" text @click="dialog.value = false"> {{ ButtonUpService }}
                      </v-btn>

                    </v-card-actions>

                  </v-card>
                </template>
              </v-dialog>
            </v-col>

          </v-row>
        </v-card-text>
      </v-card>

    </v-row>



  </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import { internet } from '@/utils/Internet';
import axios from "axios";

@Component({
  name: 'AppDashboard'
})
export default class AppDashboard extends Vue {
  public TitleServices = this.$t("Main.TitleServices");
  public TitleDown = this.$t("Main.TitleDown");
  public TitleSeparation = this.$t("Main.TitleSeparation");
  public TitleProfiling = this.$t("Main.TitleProfiling");
  public TitleWeb = this.$t("Main.TitleWeb");
  public TitleServerx = this.$t("Main.TitleServerx");
  public Servicesup = this.$t("Main.Servicesup");
  public Servers = this.$t("Main.Servers");
  public StatusServiceSTT = this.$t("Main.StatusServiceSTT");
  public StatusVoiceSeparation = this.$t("Main.StatusVoiceSeparation");
  public StatusVoiceProfiling = this.$t("Main.StatusVoiceProfiling");
  public StatusServerSFTP = this.$t("Main.StatusServerSFTP");
  public StatusWebServer = this.$t("Main.StatusWebServer");
  public StatusServerX = this.$t("Main.StatusServerX");
  public ButtonCancelDashboard = this.$t("Main.ButtonCancelDashboard");
  public ButtonUpService = this.$t("Main.ButtonUpService");

}
</script>