<script>
    import { createEventDispatcher } from "svelte";
    import { get } from "axios";
    import QuizCard from "./component/QuizCard.svelte";
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

    $: quizzes = [
        {
            name: "Hello there",
            id: "1",
            questions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        },
        {
            name: "Hello there2",
            id: "2",
            questions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        },
        {
            name: "Hello there3",
            id: "3",
            questions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        },
        {
            name: "Hello there4",
            id: "4",
            questions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        },
    ];

    let offset = 0;
    let amount = 5;

    async function getQuizes() {
        let data = {
            amount,
            offset,
        };
        get("/api/quiz/all", data)
            .then((resp) => {
                console.log(resp);
                quizzes = resp.data.response;
                offset += amount;
            })
            .catch((err) => {
                console.log(err);
            });
    }
</script>

<svelte:head>
    <title>Quizzes</title>
</svelte:head>

<article>
    <button on:click={getQuizes}>
        Click to fetch new quizzes (if there are any)
    </button>
    <h2>Quizzes</h2>
    <QuizCard />
    {#each quizzes as quiz (quiz.id)}
        <QuizCard {quiz} />
    {/each}
</article>

<style>
    article {
        width: max(50%, 520px);
        display: grid;
    }
</style>
