<script>
	import Home from "./Home.svelte";
	import Create from "./Create.svelte";

	$: current_page = "HOME";

	function changePage(event) {
		console.log("TESTING APP");
		console.log(event);
		current_page = event.detail.text;
	}
</script>

<main>
	{#if current_page == "HOME"}
		<Home on:page={changePage} />
	{:else if current_page == "CREATE"}
		<Create />
	{/if}
</main>

<style>
</style>
