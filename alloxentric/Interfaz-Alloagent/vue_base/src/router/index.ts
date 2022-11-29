import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import MainBase from '../views/MainBase.vue'
import MainInicio from '../views/Inicio/MainInicio.vue'
import StatusClients from '../views/StatusClients.vue'
import MainClients from '../views/MainClients.vue'
import ReporteCargas from '../views/ReporteCargas.vue'


Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: MainBase,
    children: [
      {
        path: '/home/inicio',
        name: 'MainInicio',
        component: MainInicio
      },
      { /* Se agrega la ruta de CRUD Clientes */
        path: '/home/inicio/clients',
        name: 'MainClients',
        component: MainClients
      },
      { /* Se agrega la ruta de status Clientes */
        path: '/home/inicio/status',
        name: 'StatusClients',
        component: StatusClients
      },
      { /* Se agrega la ruta de status Clientes */
        path: '/home/inicio/report',
        name: 'ReporteCargas',
        component: ReporteCargas
      },
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
