<template class="content-class">
  <v-container fluid>
    <AppDashboard/>
    <v-divider inset vertical></v-divider>
    <AppStatus/>

  </v-container>
</template>

<script lang="ts">
  
  import { Component, Vue } from 'vue-property-decorator';
	import { internet } from '@/utils/Internet';
	import { AxiosResponse } from 'axios';
	import Util from '@/utils/Util';

  

  import AppStatus from '../components/util/AppStatus.vue';
  import AppDashboard from '../components/util/AppDashboard.vue';
    @Component({

      name: 'util',
      components: {
        AppDashboard,
        AppStatus
      }
    })

    export default class AboutView extends Vue {
    public isLoading = false;
    public message2 = this.$t("Main.message2");
    public message3 = this.$t("Main.message3");
    public Clients = this.$t("Main.Clients");
    public papa = this.$t("Main.papa");

    mounted(): void {
      this.getData();
    }
  }

</script>