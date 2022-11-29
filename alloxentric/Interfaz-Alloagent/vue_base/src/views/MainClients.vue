<template>
  <div class>
	<Data-Table />
  </div>
</template>
<script lang="ts">
	import { Component, Vue } from 'vue-property-decorator';
	import { internet } from '@/utils/Internet';
	import { AxiosResponse } from 'axios';
	import Util from '@/utils/Util';
	import DataTable from '@/components/util/DataTable.vue';
	@Component({
		name: 'MainClients',
		components: {
			DataTable
		}
	})
	export default class MainClients extends Vue {
    public isLoading = false;
	public message2 = this.$t("Main.message2");
    public message3 = this.$t("Main.message3");

	mounted(): void {
		this.getData();
	}

	private getData(): void {
			this.isLoading = true;
			const request_PruebaConexion = internet
				.newRequest()
				.get(
					`endpoint1`
				);
			Util.waitForPromises([
				request_PruebaConexion,
			])
				.then((responses) => {
					const response_1 = responses[0] as AxiosResponse;
					let message = this.message3 as string
					this.message3 = message+response_1.data
				})
				.catch(console.log)
				.finally(() => {
					this.isLoading = false;
				});
		}


		



	}
</script>