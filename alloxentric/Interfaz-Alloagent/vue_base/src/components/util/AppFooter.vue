<template>
	<v-footer app bottom fixed padless>
		<v-container>
			<v-col class="text-center">
				{{ new Date().getFullYear() }} —
				<strong> Alloxentric  </strong>
			</v-col>
		</v-container>
	</v-footer>
</template>
<style>

</style>
<script lang="ts">
	import { Component, Vue } from 'vue-property-decorator';
	@Component({
		name: 'AppFooter',
	})
	export default class AppFooter extends Vue {

	}
</script>
