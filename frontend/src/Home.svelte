<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    function create() {
        dispatch("page", {
            text: "CREATE",
        });
    }

    function view() {
        dispatch("page", {
            text: "VIEW",
        });
    }
</script>

<svelte:head>
    <title>Home page</title>
</svelte:head>

<main>
    <h1>Welcome to this website!</h1>
    <button on:click={view}>View quizzes</button>
    <button on:click={create}>Create quiz</button>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    button {
        margin: 1em;
        padding: 1.5em;
        font-size: 150%;
        background-color: #ffffff;
        border-radius: 5%;
        font-weight: 500;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
