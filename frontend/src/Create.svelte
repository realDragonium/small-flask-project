<script>
    import { createEventDispatcher } from "svelte";
    import { post } from "axios";
    const dispatch = createEventDispatcher();

    let value = "Best quiz";

    async function create() {
        const testData = JSON.stringify({ name: "Best Test" });

        // fetch("/api/quiz", {
        //     method: "POST",
        //     body: JSON.stringify(data),
        // }).then((res) => {
        //     console.log("Request complete! response:", res);
        //     answer = JSON.parse(res.json());
        //     console.log(answer);
        // });
        // const res = await fetch("/api/quiz", {
        //     method: "POST",
        //     body: JSON.stringify({ name: "Best Test" }),
        // });

        post("/api/quiz", testData)
            .then((resp) => {
                console.log(resp);
            })
            .catch((err) => {
                console.log(err);
            });

        // const json = await res.json();
        // let result = JSON.stringify(json);
        // console.log(result);
        // dispatch("page", {
        // text: "CREATE",
        // });
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
