<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let value = "Best quiz";

    function create() {
        let data = {
            name: value,
        };

        fetch("http://localhost:5000/api/quiz", {
            method: "POST",
            body: JSON.stringify(data),
        }).then((res) => {
            console.log("Request complete! response:", res);
        });

        dispatch("page", {
            text: "CREATE",
        });
    }

    function goBack() {
        dispatch("page", {
            text: "HOME",
        });
    }
</script>

<article>
    <h2>Create here your quiz!</h2>
    <input {value} type="text" />
    <section>
        <button class="back" on:click={goBack}>Go back</button>
        <button class="create" on:click={create}>Create!</button>
    </section>
</article>

<style>
    article {
        text-align: center;
        padding: 1em;
        max-width: max(25%, 520px);
        margin: auto auto;
    }

    h2 {
        margin: 25px auto;
    }

    input {
        display: block;
        width: 100%;
        padding: 15px;
        margin: 15px auto;
    }

    section {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-column-gap: 15px;
    }

    button {
        display: inline-block;
        width: 100%;
        padding: 15px;
    }

    .create {
        background-color: rgb(49, 151, 2);
        color: white;
        font-weight: 400;
        border: none;
    }
</style>
