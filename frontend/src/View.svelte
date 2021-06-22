<script>
    import { createEventDispatcher } from "svelte";
    import { get } from "axios";
    import QuizCard from "./component/QuizCard.svelte";
    const dispatch = createEventDispatcher();

    function home() {
        dispatch("page", {
            text: "HOME",
        });
    }

    function view() {
        dispatch("page", {
            text: "VIEW",
        });
    }

    let quizzes = [];

    setTimeout(() => {
        quizzes = [
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
        ];
    }, 1000);

    let offset = 0;
    let amount = 5;

    async function getQuizes() {
        get(`/api/quiz/all?offset=${offset}&amount=${amount}`)
            .then((resp) => {
                console.log(resp);
                quizzes = [...quizzes, ...resp.data];
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
    <button on:click={home}>Go back</button>
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
        margin: 0 auto;
    }
</style>
