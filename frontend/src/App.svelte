<script>
	import Home from "./Home.svelte";
	import Create from "./Create.svelte";
	import View from "./View.svelte";

	$: current_page = "HOME";

	function changePage(event) {
		current_page = event.detail.text;
	}
</script>

<main>
	{#if current_page == "HOME"}
		<Home on:page={changePage} />
	{:else if current_page == "CREATE"}
		<Create on:page={changePage} />
	{:else if current_page == "VIEW"}
		<View on:page={changePage} />
	{/if}
</main>

<style>
</style>
