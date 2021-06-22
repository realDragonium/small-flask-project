<script>
    import { createEventDispatcher } from "svelte";
    import { post } from "axios";
    const dispatch = createEventDispatcher();

    let defaultQuestion = {
        question: "Some default text",
        answer_options: [
            {
                text: "something",
                is_correct: false,
            },
            {
                text: "something2",
                is_correct: true,
            },
        ],
    };
    let defaultAnswerOption = {
        text: "something",
        is_correct: false,
    };

    let quizName = "Best quiz";
    let questions = [defaultQuestion];
    $: quizId = "";
    $: notification = "";

    async function create() {
        post("/api/quiz", { name: quizName })
            .then((resp) => {
                console.log(resp);
                if (resp.data.status == "success") {
                    notification = "Quiz created!";
                    notificationTimer();
                    quizId = resp.data.quiz.id;
                    addNewQuestion();
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
        }, 4000);
    }

    function addAnswerOption(event, question) {
        question.answer_options = {
            ...question.answer_options,
            defaultAnswerOption,
        };
    }

    function addNewQuestion() {
        questions = [...questions, defaultQuestion];
    }

    function saveQuestions() {
        let data = {
            quiz: {
                id: quizId,
            },
            questions,
        };
        post("/api/question", data)
            .then((resp) => {
                console.log(resp);
                if (resp.data.status == "success") {
                    notification = "Questions saved!";
                    notificationTimer();
                }
            })
            .catch((err) => {
                console.log(err);
            });
    }
</script>

<article class="creation">
    <h2>Create here your quiz!</h2>
    {#if notification != ""}
        <p class="notification">{notification}</p>
    {/if}
    <input bind:value={quizName} type="text" />
    <button class="back" on:click={goBack}>Go back</button>
    <button class="create" on:click={create}>Create!</button>
</article>

<article>
    <h3>Create a question for the quiz</h3>
    {#each questions as question}
        <h4>Question</h4>
        <section class="question">
            <textarea value={question.question} cols="30" rows="3" />
            <section class="answers">
                <h4>Answers</h4>
                {#each question.answer_options as answer_option}
                    <input type="text" value={answer_option.text} />
                    <button
                        on:click={(answer_option.is_correct =
                            !answer_option.is_correct)}
                    >
                        {answer_option.is_correct}
                    </button>
                {/each}
            </section>
            <button on:click={addAnswerOption(question)}>
                Add an answer option
            </button>
        </section>
    {/each}
</article>
<button on:click={addNewQuestion}>Add new Question</button>
<button on:click={saveQuestions}>Click to save!</button>

<style>
    article {
        text-align: center;
        padding: 1em;
        max-width: max(25%, 520px);
        margin: auto auto;
    }

    h2 {
        grid-column-end: span 2;
        margin: 25px auto;
        font-size: 3em;
    }

    .creation {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-gap: 15px 15px;
    }

    .notification {
        grid-column-end: span 2;
        font-size: 1.5em;
        color: green;
        font-weight: 400;
        margin-bottom: -15px;
    }

    input {
        grid-column-end: span 2;
        display: block;
        width: 100%;
        padding: 15px;
        margin: 5px auto;
    }

    .creation button {
        width: 100%;
        padding: 15px;
    }

    .create {
        background-color: rgb(49, 151, 2);
        color: white;
        font-weight: 400;
        border: none;
    }

    textarea {
        padding: 15px;
        width: 100%;
    }

    .question .answers {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        grid-gap: 10px 10px;
    }

    .answers h4 {
        grid-column-end: span 5;
    }
    .answers button {
        padding: 15px;
        margin: 5px auto;
        width: 80%;
    }
    .answers input {
        grid-column-end: span 4;
    }
</style>
