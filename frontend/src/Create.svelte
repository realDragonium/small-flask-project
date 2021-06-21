<script>
    import { createEventDispatcher } from "svelte";
    import { post } from "axios";
    const dispatch = createEventDispatcher();

    let quizName = "Best quiz";

    $: notification = "";

    async function create() {
        post("/api/quiz", { name: quizName })
            .then((resp) => {
                console.log(resp);
                if (resp.data.status == "success") {
                    console.log("changed notification value!");
                    notification = "Quiz created!";
                    notificationTimer();
                }
            })
            .catch((err) => {
                console.log(err);
            });
    }

    function goBack() {
        dispatch("page", {
            text: "HOME",
        });
    }

    function notificationTimer() {
        setTimeout(() => {
            notification = "";
            console.log("changed notification back!");
        }, 4000);
    }
</script>

<article>
    <h2>Create here your quiz!</h2>
    {#if notification != ""}
        <p class="notification">{notification}</p>
    {/if}
    <input bind:value={quizName} type="text" />
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

    .notification {
        font-size: 1.5em;
        color: green;
        font-weight: 400;
        margin-bottom: -15px;
    }

    h2 {
        margin: 25px auto;
        font-size: 3em;
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
