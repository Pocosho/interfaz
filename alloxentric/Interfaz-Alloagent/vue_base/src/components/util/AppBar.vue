<template>
	<v-app-bar color="" app class="d-flex justify-end">
		<div class="text-center">
		</div>
		<template>
				<div> {{/* Boton de Multilenguaje EN/ES  */}}
				<v-avatar :size=35>
					<img  src="@/assets/global.png"/>
				</v-avatar>
				<select
					class="mx-2"
					v-model="$i18n.locale"
					@change="updateLanguage($event.target.value)"
					variant="info">mdi-chevron-down
					<option
						hide-details
						v-for="(o, i) in locales_array"
						:key="i"
						:value="o.value"
						:selected="o.value === locale_default"
				> {{ o.caption }}
				</option>
				</select>
				</div>
	
				<v-spacer></v-spacer>
				
				{{/* Boton de notificaciones  */}}

				<div class="flex-d justify-end mr-8">
					<ul>			
						<v-dialog
							transition="dialog-bottom-transition"
							max-width="600"
						>
						<template v-slot:activator="{ on, attrs }">
							<v-spacer></v-spacer>
							<v-btn
								class="mx-2"
								fab
								dark
								color= "teal lighten-1"
								v-bind="attrs"
								v-on="on"
								
							>	
								<v-icon dark>
									mdi-bell-badge
								</v-icon> </v-btn>
						</template>
	
						<template v-slot:default="dialog">
							<v-card>
								<v-toolbar
									color=#14AEB5
									dark
								> Suscribirse a eventos </v-toolbar>
								<v-card-text>
									<v-list-item-group>
										<v-list-item>
											<div class="pa-2 rounded-circle d-inline-block">
												<v-icon dark color=#14AEB5>
													mdi-alert
												</v-icon>
											</div>
											El servicio STT ha fallado
										</v-list-item>
	
										<v-list-item>
											<div class="pa-2 rounded-circle d-inline-block">
												<v-icon dark color=#14AEB5>
													mdi-cloud-check
												</v-icon>
											</div>
											Un servicio ha fallado
										</v-list-item>
	
										<v-list-item>
											<div class="pa-2 rounded-circle d-inline-block">
												<v-icon dark color=#14AEB5>
													mdi-alert
												</v-icon>
											</div>
											El servidor X se encuentra con problemas
										</v-list-item>
	
										<v-list-item>
											<div class="pa-2 rounded-circle d-inline-block">
												<v-icon dark color=#14AEB5>
													mdi-cloud-check
												</v-icon>
											</div>
											Un servicio ha fallado 
										</v-list-item>
	
	
									</v-list-item-group>
								</v-card-text>
	
								{{/*Boton cerrar*/}}
	
								<v-card-actions class="justify-end">
								<v-btn
									color = #16BF9B
									text
									@click="dialog.value = false"
								> Aceptar </v-btn>
								</v-card-actions>
	
							</v-card>
						</template>
						</v-dialog>
					</ul>
				</div>
					
				<v-spacer></v-spacer>
	
				<v-list>
					<v-list-item @click="listenLogout">
					<v-list-item-title>
						Cerrar Sesión
					</v-list-item-title>
					</v-list-item>
				</v-list>

			</template>
	</v-app-bar>
	</template>
	<script lang="ts">
		import { Component, Vue, Prop } from 'vue-property-decorator';
		import { LOCALES, Locales } from "@/locales/i18n";
		import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
		import MixinLogin from '@/mixing/MixinLogin.vue';
		import defaultLocale from "@/i18n";
		
		@Component({
			name: 'AppBar',
		})
		
		export default class AppBar extends MixinLogin {		
			public locales_array = LOCALES;
			public locale_default = defaultLocale;
			@Prop() readonly keycloak!: string
	
			public listenLogout() {
				//this.logout();
				//Util.showMessage('Hasta pronto', Icon.INFO);
				this.$router.push({
					name: 'Login',
				});
				//this.keycloak.logout();
			}
			public updateLanguage(lang: Locales) {
				console.log("cambiando idioma a ", lang);
				this.$emit('changeEvent', lang);
			}
	
	
		}
		
	
	</script>
	